def add_variables(f):
    f.add_variable("etaЛА", 0.0, "")


def print_calc_res(f):
    print("*********************************")
    print("efficiency (008):")
    print("         etaЛА = ", f.v["etaЛА"])
    print("*********************************\n")


def calc_part(f):
    if f.v["eta_посл"] is not None:
        eta_aver = (f.v["etaСТ"] + f.v["eta_посл"]) / 2.0
    else:
        eta_aver = f.v["etaСТ"]
    a = (f.v["i"] * eta_aver) / (f.v["i"] - 1.0 + eta_aver)
    h1 = pow(f.v["ПЛА*"], (f.v["k"] - 1.0) / f.v["k"]) - 1.0
    h2 = a * (pow(f.v["ПЛА*"], (f.v["k"] - 1.0) / (a * f.v["k"])) - 1.0)
    f.v["etaЛА"] = eta_aver * h1 / h2


def run(field, is_add_variables, is_print_res):
    if is_add_variables:
        add_variables(field)
    calc_part(field)
    if is_print_res:
        print_calc_res(field)
