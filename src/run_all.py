import subprocess
import sys
from pathlib import Path


def run_script(script_name):
    project_root = Path(__file__).resolve().parents[1]
    script_path = project_root / "src" / script_name

    print(f"\n=== Running {script_name} ===")

    subprocess.run(
        [sys.executable, str(script_path)],
        cwd=project_root,
        check=True
    )


def main():
    scripts = [
        "run_power_flow.py",
        "scenario_capacitor_bank.py",
        "scenario_ev_growth.py",
        "plot_ev_growth_results.py",
    ]

    for script in scripts:
        run_script(script)

    print("\nAll studies completed successfully.")


if __name__ == "__main__":
    main()