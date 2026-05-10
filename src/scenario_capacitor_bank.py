from pathlib import Path
import copy

import pandas as pd
import pandapower as pp

from build_network import build_nigb_demo_network


def main():
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", 200)

    # Base case: with capacitor bank
    net_with_cap = build_nigb_demo_network()
    pp.runpp(net_with_cap, numba=False, max_iteration=30)

    # Scenario case: without capacitor bank
    net_without_cap = copy.deepcopy(net_with_cap)
    net_without_cap.shunt["in_service"] = False
    pp.runpp(net_without_cap, numba=False, max_iteration=30)

    # Compare bus voltage
    comparison = pd.DataFrame({
        "bus_name": net_with_cap.bus["name"],
        "voltage_with_cap_pu": net_with_cap.res_bus["vm_pu"],
        "voltage_without_cap_pu": net_without_cap.res_bus["vm_pu"],
    })

    comparison["voltage_change_pu"] = (
        comparison["voltage_with_cap_pu"] - comparison["voltage_without_cap_pu"]
    )

    print("\n=== Capacitor Bank Voltage Comparison ===")
    print(comparison.to_string(index=False))

    # Compare line loading
    line_comparison = pd.DataFrame({
        "line_name": net_with_cap.line["name"],
        "loading_with_cap_percent": net_with_cap.res_line["loading_percent"],
        "loading_without_cap_percent": net_without_cap.res_line["loading_percent"],
    })

    line_comparison["loading_change_percent"] = (
        line_comparison["loading_with_cap_percent"]
        - line_comparison["loading_without_cap_percent"]
    )

    print("\n=== Line Loading Comparison ===")
    print(line_comparison.to_string(index=False))

    # Save results
    project_root = Path(__file__).resolve().parents[1]
    results_dir = project_root / "results"
    results_dir.mkdir(exist_ok=True)

    comparison.to_csv(results_dir / "capacitor_voltage_comparison.csv", index=False)
    line_comparison.to_csv(results_dir / "capacitor_line_loading_comparison.csv", index=False)

    print("\nCapacitor bank scenario results saved to the results folder.")


if __name__ == "__main__":
    main()