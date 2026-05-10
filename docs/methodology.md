# Methodology

## Network Model

A simplified 5-bus transmission network was developed in pandapower to represent a reduced North Island Grid Backbone-style system.

The model includes:

- 220 kV transmission buses
- One 33 kV load bus
- Transmission lines
- One transformer
- Static loads
- One external grid/slack bus
- One shunt capacitor bank

## Power Flow Analysis

The Newton-Raphson power flow solver in pandapower was used to calculate:

- Bus voltage magnitude
- Bus voltage angle
- Transmission line loading
- Transformer loading

## Scenario Studies

Three main studies were performed:

1. Base case power flow
2. Shunt capacitor sensitivity study
3. EV load growth scenario

The EV load growth scenario scales system load from 1.0x to 1.4x and checks for voltage violations and transmission line overloads.