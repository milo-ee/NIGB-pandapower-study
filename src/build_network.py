import pandapower as pp


def build_nigb_demo_network():
    net = pp.create_empty_network(sn_mva=1000)

    # 1. Create buses
    haywards = pp.create_bus(net, vn_kv=220, name="Haywards 220 kV")
    bunnythorpe = pp.create_bus(net, vn_kv=220, name="Bunnythorpe 220 kV")
    hamilton = pp.create_bus(net, vn_kv=220, name="Hamilton 220 kV")
    otahuhu = pp.create_bus(net, vn_kv=220, name="Otahuhu 220 kV")
    wilton_33 = pp.create_bus(net, vn_kv=33, name="Wilton 33 kV")

    # 2. Slack bus / HVDC equivalent
    pp.create_ext_grid(
        net,
        bus=haywards,
        vm_pu=1.02,
        name="HVDC Link / Slack Bus"
    )

    # 3. Equivalent transmission lines
    # These are simplified demo parameters, not final project data.
    pp.create_line_from_parameters(
        net,
        from_bus=haywards,
        to_bus=bunnythorpe,
        length_km=1,
        r_ohm_per_km=0.5,
        x_ohm_per_km=5.0,
        c_nf_per_km=12.0,
        max_i_ka=1.5,
        name="Haywards-Bunnythorpe"
    )

    pp.create_line_from_parameters(
        net,
        from_bus=bunnythorpe,
        to_bus=hamilton,
        length_km=1,
        r_ohm_per_km=0.7,
        x_ohm_per_km=7.0,
        c_nf_per_km=12.0,
        max_i_ka=1.5,
        name="Bunnythorpe-Hamilton"
    )

    pp.create_line_from_parameters(
        net,
        from_bus=hamilton,
        to_bus=otahuhu,
        length_km=1,
        r_ohm_per_km=0.6,
        x_ohm_per_km=6.0,
        c_nf_per_km=12.0,
        max_i_ka=1.5,
        name="Hamilton-Otahuhu"
    )

    # 4. Transformer example: 220 kV to 33 kV
    pp.create_transformer_from_parameters(
        net,
        hv_bus=haywards,
        lv_bus=wilton_33,
        sn_mva=200,
        vn_hv_kv=220,
        vn_lv_kv=33,
        vk_percent=12,
        vkr_percent=0.5,
        pfe_kw=0,
        i0_percent=0,
        name="Haywards-Wilton Transformer"
    )

    # 5. Loads
    # Use smaller demo loads first to make sure the network converges.
    pp.create_load(net, bus=hamilton, p_mw=150, q_mvar=45, name="Hamilton Load")
    pp.create_load(net, bus=otahuhu, p_mw=300, q_mvar=90, name="Otahuhu Load")
    pp.create_load(net, bus=wilton_33, p_mw=80, q_mvar=25, name="Wilton Load")

    # 6. Capacitor bank
    # In pandapower, negative q_mvar represents capacitive reactive power injection.
    pp.create_shunt(
        net,
        bus=otahuhu,
        q_mvar=-80,
        p_mw=0,
        name="Otahuhu Capacitor Bank"
    )

    return net