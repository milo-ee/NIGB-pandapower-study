# North Island Grid Backbone Power Flow Study using pandapower

## Project Overview

This project develops a simplified power flow model inspired by New Zealand's North Island Grid Backbone using Python and pandapower.

The study investigates:

- Base case power flow performance
- Bus voltage profile
- Transmission line loading
- Transformer loading
- Shunt capacitor impact
- EV-driven load growth impact

## Tools Used

- Python
- pandapower
- pandas
- matplotlib
- PyCharm

## Study Scenarios

### 1. Base Case Power Flow

A simplified 5-bus transmission network was built and analysed using pandapower. The base case successfully converged, with all bus voltages within the normal operating range and no overloaded transmission elements.

### 2. Shunt Capacitor Sensitivity

A capacitor bank scenario was simulated by comparing the network with and without capacitor support at Otahuhu.

The capacitor improved the Otahuhu 220 kV bus voltage and reduced the loading of the main transmission lines. This demonstrates the role of reactive power compensation in voltage support and transmission loading reduction.

### 3. EV Load Growth Scenario

An EV load growth scenario was simulated by scaling system load from 1.0x to 1.4x.

The results show that the simplified network remains within voltage and line loading limits up to around 1.2x load growth. At 1.3x load growth, the Otahuhu 220 kV bus voltage drops below 0.95 p.u. and the Bunnythorpe-Hamilton line exceeds 100% loading.

This indicates that future demand growth may require additional voltage support, reactive power compensation, or transmission reinforcement.

## Results

### EV Load Growth Impact on Minimum Bus Voltage

![EV Load Growth Minimum Voltage](results/ev_growth_min_voltage.png)

### EV Load Growth Impact on Transmission Line Loading

![EV Load Growth Line Loading](results/ev_growth_line_loading.png)

## Engineering Relevance

This project demonstrates practical power system modelling and analysis skills, including:

- Transmission network modelling
- Power flow analysis
- Voltage violation assessment
- Transmission line loading assessment
- Reactive power compensation
- Scenario-based planning study

## Disclaimer

This is a portfolio version of an academic-inspired power system modelling project. It does not include original assignment files, submitted coursework, student ID information, or confidential course material.