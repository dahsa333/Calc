from graph_data import GraphData


def add_variables(f):
    f.add_variable("OmegaТ", 0.0, "")
    f.add_variable("etaСТ", 0.0, "")
    f.add_variable("psi", 0.0, "")


def print_calc_res(f):
    print("*********************************")
    print("selection of the degree of reaction (005):")
    print("         OmegaТ = ", f.v["OmegaТ"])
    print("         etaСТ = ", f.v["etaСТ"])
    print("         psi = ", f.v["psi"])
    print("*********************************\n")


def calc_part(f):
    my_graph = GraphData("K50_1_phi_eta_280.csv")
    my_graph.get_data(True, False, False)
    my_graph2 = GraphData("K50_1_phi_eta_230.csv")
    my_graph2.get_data(True, False, False)
    my_graph3 = GraphData.create_average_list(my_graph2.data_points, 230.0, my_graph.data_points, 280.0, 240.0)
    # GraphData.plot_graph_by_points([my_graph2.data_points, my_graph.data_points, my_graph3])


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)