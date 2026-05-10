from pathlib import Path

import pandas as pd
import pandapower as pp

from build_network import build_nigb_demo_network


def main():
    # Show full pandas table in console
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    net = build_nigb_demo_network()

    pp.runpp(net, numba=False, max_iteration=30)

    print("\n=== Power Flow Converged ===")
    print(net.converged)

    print("\n=== Bus Voltage Results ===")
    bus_results = net.bus[["name", "vn_kv"]].join(
        net.res_bus[["vm_pu", "va_degree"]]
    )
    print(bus_results.to_string())

    print("\n=== Line Loading Results ===")
    line_results = net.line[["name", "from_bus", "to_bus"]].join(
        net.res_line[["p_from_mw", "q_from_mvar", "loading_percent"]]
    )
    print(line_results.to_string())

    print("\n=== Transformer Loading Results ===")
    trafo_results = net.trafo[["name", "hv_bus", "lv_bus", "sn_mva"]].join(
        net.res_trafo[["p_hv_mw", "q_hv_mvar", "loading_percent"]]
    )
    print(trafo_results.to_string())

    # Save results
    project_root = Path(__file__).resolve().parents[1]
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    bus_results.to_csv(results_dir / "bus_voltage_results.csv", index=True)
    line_results.to_csv(results_dir / "line_loading_results.csv", index=True)
    trafo_results.to_csv(results_dir / "transformer_loading_results.csv", index=True)

    print("\nResults saved to the results folder.")


if __name__ == "__main__":
    main()