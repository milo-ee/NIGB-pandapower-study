from pathlib import Path

import pandas as pd
import pandapower as pp

from build_network import build_nigb_demo_network


def run_ev_growth_case(scale_factor):
    net = build_nigb_demo_network()

    # Increase all loads to simulate EV-driven load growth
    net.load["p_mw"] = net.load["p_mw"] * scale_factor
    net.load["q_mvar"] = net.load["q_mvar"] * scale_factor

    try:
        pp.runpp(net, numba=False, max_iteration=30)
        converged = net.converged
    except Exception:
        converged = False

    if converged:
        min_voltage = net.res_bus["vm_pu"].min()
        min_voltage_bus_index = net.res_bus["vm_pu"].idxmin()
        min_voltage_bus_name = net.bus.loc[min_voltage_bus_index, "name"]

        max_line_loading = net.res_line["loading_percent"].max()
        max_line_index = net.res_line["loading_percent"].idxmax()
        max_line_name = net.line.loc[max_line_index, "name"]

        max_trafo_loading = net.res_trafo["loading_percent"].max()
    else:
        min_voltage = None
        min_voltage_bus_name = None
        max_line_loading = None
        max_line_name = None
        max_trafo_loading = None

    return {
        "load_scale": scale_factor,
        "converged": converged,
        "min_voltage_pu": min_voltage,
        "min_voltage_bus": min_voltage_bus_name,
        "max_line_loading_percent": max_line_loading,
        "max_line_name": max_line_name,
        "max_transformer_loading_percent": max_trafo_loading,
    }


def main():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    scale_factors = [1.0, 1.1, 1.2, 1.3, 1.4]

    results = []

    for scale in scale_factors:
        result = run_ev_growth_case(scale)
        results.append(result)

    results_df = pd.DataFrame(results)

    print("\n=== EV Load Growth Scenario Results ===")
    print(results_df.to_string(index=False))

    # Add simple engineering assessment
    print("\n=== Engineering Assessment ===")

    for _, row in results_df.iterrows():
        scale = row["load_scale"]

        if not row["converged"]:
            print(f"Load scale {scale:.1f}x: Power flow did not converge.")
            continue

        voltage_status = "OK"
        line_status = "OK"
        trafo_status = "OK"

        if row["min_voltage_pu"] < 0.95:
            voltage_status = "Voltage violation"

        if row["max_line_loading_percent"] > 100:
            line_status = "Line overload"

        if row["max_transformer_loading_percent"] > 100:
            trafo_status = "Transformer overload"

        print(
            f"Load scale {scale:.1f}x: "
            f"Min voltage = {row['min_voltage_pu']:.4f} p.u. at {row['min_voltage_bus']}, "
            f"Max line loading = {row['max_line_loading_percent']:.2f}% on {row['max_line_name']}, "
            f"Max transformer loading = {row['max_transformer_loading_percent']:.2f}%. "
            f"Status: {voltage_status}, {line_status}, {trafo_status}."
        )

    # Save results
    project_root = Path(__file__).resolve().parents[1]
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    results_df.to_csv(results_dir / "ev_load_growth_summary.csv", index=False)

    print("\nEV load growth scenario results saved to the results folder.")


if __name__ == "__main__":
    main()