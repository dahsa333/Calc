from graph_data import GraphData


def st_k_50_1_eta(x_value):
    if x_value <= 175:
        use_graph = GraphData("K50_1_phi_eta_200.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 230:
        h_graph_1 = GraphData("K50_1_phi_eta_200.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_1_phi_eta_230.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 175.0, h_graph_2.data_points, 230.0, x_value)
    elif x_value <= 250:
        h_graph_1 = GraphData("K50_1_phi_eta_230.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_1_phi_eta_250.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 230.0, h_graph_2.data_points, 250.0, x_value)
    elif x_value <= 280:
        h_graph_1 = GraphData("K50_1_phi_eta_250.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_1_phi_eta_280.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 250.0, h_graph_2.data_points, 280.0, x_value)
    else:
        use_graph = GraphData("K50_1_phi_eta_280.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_50_1_psi(x_value):
    if x_value <= 175:
        use_graph = GraphData("K50_1_phi_psi_200.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 230:
        h_graph_1 = GraphData("K50_1_phi_psi_200.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_1_phi_psi_230.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 175.0, h_graph_2.data_points, 230.0, x_value)
    elif x_value <= 250:
        h_graph_1 = GraphData("K50_1_phi_psi_230.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_1_phi_psi_250.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 230.0, h_graph_2.data_points, 250.0, x_value)
    elif x_value <= 280:
        h_graph_1 = GraphData("K50_1_phi_psi_250.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_1_phi_psi_280.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 250.0, h_graph_2.data_points, 280.0, x_value)
    else:
        use_graph = GraphData("K50_1_phi_psi_280.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_50_5_eta(x_value):
    if x_value <= 175:
        use_graph = GraphData("K50_5_phi_eta_200.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 230:
        h_graph_1 = GraphData("K50_5_phi_eta_200.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_5_phi_eta_230.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 175.0, h_graph_2.data_points, 230.0, x_value)
    elif x_value <= 250:
        h_graph_1 = GraphData("K50_5_phi_eta_230.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_5_phi_eta_250.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 230.0, h_graph_2.data_points, 250.0, x_value)
    elif x_value <= 280:
        h_graph_1 = GraphData("K50_5_phi_eta_250.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_5_phi_eta_280.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 250.0, h_graph_2.data_points, 280.0, x_value)
    else:
        use_graph = GraphData("K50_5_phi_eta_280.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_50_5_psi(x_value):
    if x_value <= 175:
        use_graph = GraphData("K50_5_phi_psi_200.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 230:
        h_graph_1 = GraphData("K50_5_phi_psi_200.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_5_phi_psi_230.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 175.0, h_graph_2.data_points, 230.0, x_value)
    elif x_value <= 250:
        h_graph_1 = GraphData("K50_5_phi_psi_230.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_5_phi_psi_250.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 230.0, h_graph_2.data_points, 250.0, x_value)
    elif x_value <= 280:
        h_graph_1 = GraphData("K50_5_phi_psi_250.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K50_5_phi_psi_280.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 250.0, h_graph_2.data_points, 280.0, x_value)
    else:
        use_graph = GraphData("K50_5_phi_psi_280.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_70_17_eta(x_value):
    if x_value <= 175:
        use_graph = GraphData("K70_17_phi_eta_175.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 200:
        h_graph_1 = GraphData("K70_17_phi_eta_175.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K70_17_phi_eta_200.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 175.0, h_graph_2.data_points, 200.0, x_value)
    elif x_value <= 220:
        h_graph_1 = GraphData("K70_17_phi_eta_200.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K70_17_phi_eta_220.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 200.0, h_graph_2.data_points, 220.0, x_value)
    elif x_value <= 240:
        h_graph_1 = GraphData("K70_17_phi_eta_220.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K70_17_phi_eta_240.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 220.0, h_graph_2.data_points, 240.0, x_value)
    else:
        use_graph = GraphData("K70_17_phi_eta_240.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_70_17_psi(x_value):
    if x_value <= 187.5:
        use_graph = GraphData("K70_17_phi_psi_200.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 220:
        h_graph_1 = GraphData("K70_17_phi_psi_200.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K70_17_phi_psi_220.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 187.5, h_graph_2.data_points, 220.0, x_value)
    elif x_value <= 240:
        h_graph_1 = GraphData("K70_17_phi_psi_220.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K70_17_phi_psi_240.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 220.0, h_graph_2.data_points, 240.0, x_value)
    else:
        use_graph = GraphData("K70_17_phi_psi_240.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_100_2l_eta(x_value):
    if x_value <= 125:
        use_graph = GraphData("K100_2l_phi_eta_125.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 160:
        h_graph_1 = GraphData("K100_2l_phi_eta_125.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K100_2l_phi_eta_160.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 125.0, h_graph_2.data_points, 160.0, x_value)
    elif x_value <= 180:
        h_graph_1 = GraphData("K100_2l_phi_eta_160.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K100_2l_phi_eta_180.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 160.0, h_graph_2.data_points, 180.0, x_value)
    elif x_value <= 210:
        h_graph_1 = GraphData("K100_2l_phi_eta_180.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K100_2l_phi_eta_210.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 180.0, h_graph_2.data_points, 210.0, x_value)
    else:
        use_graph = GraphData("K100_2l_phi_eta_210.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_100_2l_psi(x_value):
    if x_value <= 152.5:
        use_graph = GraphData("K100_2l_phi_psi_180.csv")
        f_list = use_graph.get_data(True, False, False)
    elif x_value <= 210:
        h_graph_1 = GraphData("K100_2l_phi_psi_180.csv")
        h_graph_1.get_data(True, False, False)
        h_graph_2 = GraphData("K100_2l_phi_psi_210.csv")
        h_graph_2.get_data(True, False, False)
        f_list = GraphData.create_average_list(h_graph_1.data_points, 152.5, h_graph_2.data_points, 210.0, x_value)
    else:
        use_graph = GraphData("K100_2l_phi_psi_210.csv")
        f_list = use_graph.get_data(True, False, False)
    return f_list


def st_k_50_1_get_eta(f):
    f_list = st_k_50_1_eta(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_50_1_get_psi(f):
    f_list = st_k_50_1_psi(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_50_5_get_eta(f):
    f_list = st_k_50_5_eta(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_50_5_get_psi(f):
    f_list = st_k_50_5_psi(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_70_17_get_eta(f):
    f_list = st_k_70_17_eta(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_70_17_get_psi(f):
    f_list = st_k_70_17_psi(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_100_2l_get_eta(f):
    f_list = st_k_100_2l_eta(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]


def st_k_100_2l_get_psi(f):
    f_list = st_k_100_2l_psi(f.v["uн"])
    f_point = GraphData.find_nearest_x_point_in_list(f_list, f.v["phi1"])
    return f_point[1]
