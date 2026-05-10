from pathlib import Path

import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt


def main():
    project_root = Path(__file__).resolve().parents[1]
    results_dir = project_root / "results"

    df = pd.read_csv(results_dir / "ev_load_growth_summary.csv")

    # Plot 1: Minimum voltage vs load scale
    plt.figure()
    plt.plot(df["load_scale"], df["min_voltage_pu"], marker="o")
    plt.axhline(y=0.95, linestyle="--", label="Voltage limit: 0.95 p.u.")
    plt.xlabel("Load Scale")
    plt.ylabel("Minimum Bus Voltage (p.u.)")
    plt.title("EV Load Growth Impact on Minimum Bus Voltage")
    plt.grid(True)
    plt.legend()
    plt.savefig(results_dir / "ev_growth_min_voltage.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Plot 2: Maximum line loading vs load scale
    plt.figure()
    plt.plot(df["load_scale"], df["max_line_loading_percent"], marker="o")
    plt.axhline(y=100, linestyle="--", label="Line loading limit: 100%")
    plt.xlabel("Load Scale")
    plt.ylabel("Maximum Line Loading (%)")
    plt.title("EV Load Growth Impact on Transmission Line Loading")
    plt.grid(True)
    plt.legend()
    plt.savefig(results_dir / "ev_growth_line_loading.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("EV growth plots saved to the results folder.")


if __name__ == "__main__":
    main()