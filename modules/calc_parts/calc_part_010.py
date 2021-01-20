import math
from graph_data import GraphData
import graph_save_data as gs
import calc_parts.calc_part_005 as clc5
import calc_parts.calc_part_007 as clc7
import calc_parts.calc_part_008 as clc8
import calc_parts.calc_part_009 as clc9


def add_variables(f):
    pass


def print_calc_res(f):
    str_r = ""
    if f.v["тип ступени"] == 1:
        str_r += "|K-50-1  "
    elif f.v["тип ступени"] == 2:
        str_r += "|K-50-5  "
    elif f.v["тип ступени"] == 3:
        str_r += "|K-70-17 "
    elif f.v["тип ступени"] == 4:
        str_r += "|K-100-2l"
    str_r += "|" + str(f.v["тип проточной части"]) + "            "
    str_r += "|" + str(f.v["rвт"])
    str_r += "|" + to_fixed(f.v["Dн1"], 4)
    str_r += "|" + to_fixed(f.v["Dвт1"], 4)
    str_r += "|" + to_fixed(f.v["l1"], 4)
    str_r += "|" + to_fixed(f.v["uн"], 4)
    str_r += "|" + to_fixed(f.v["Dн2"], 4)
    str_r += "|" + to_fixed(f.v["Dвт2"], 4)
    str_r += "|" + to_fixed(f.v["l2"], 4)
    str_r += "|" + to_fixed(f.v["Dвт2"] / f.v["Dн1"], 4)
    if f.v["i_int"] > 9:
        str_r += "|" + to_fixed(f.v["i_int"], 0)
    else:
        str_r += "|" + to_fixed(f.v["i_int"], 0) + " "
    str_r += "|" + to_fixed(f.v["etaЛА"], 4)
    str_r += "|" + to_fixed(f.v["dr_вт"], 4)
    if f.v["dr_н"] < 0:
        str_r += "|" + to_fixed(f.v["dr_н"], 4) + "|" + "\n"
    else:
        str_r += "|" + to_fixed(f.v["dr_н"], 4) + " |" + "\n"
    print(str_r)


def print_start_str():
    print("*********************************")
    print("selection of parameters (010):")
    str_r = ""
    str_r += "|тип ст. "
    str_r += "|тип пр. части"
    str_r += "|rвт"
    str_r += "|Dн1   "
    str_r += "|Dвт1  "
    str_r += "|l1    "
    str_r += "|uн1     "
    str_r += "|Dн2   "
    str_r += "|Dвт2  "
    str_r += "|l2    "
    str_r += "|rвт2  "
    str_r += "|i "
    str_r += "|etaЛА*"
    str_r += "|drвт  "
    str_r += "|drн    |"
    print(str_r)


def print_best_param():
    print("Best variant:")


def print_end_str():
    print("*********************************\n")


def to_fixed(num_obj, digits=0):
    return f"{num_obj:.{digits}f}"


def calc_param(f, i_r, delta_r):
    f.v["Dн1"] = f.v["Dн"]
    f.v["Dвт1"] = f.v["rвт"] * f.v["Dн1"]
    f.v["l1"] = (f.v["Dн1"] - f.v["Dвт1"]) / 2.0
    exp_ind = 1.0 - (f.v["k"] - 1.0) / (f.v["k"] * f.v["etaЛА"])
    f.v["rho1*"] = (f.v["p1*"]) / (f.v["R"] * f.v["TВ*"])
    f.v["rho_ЛА*"] = f.v["rho1*"] * pow((f.v["pЛА*"]) / (f.v["p1*"]), exp_ind)
    if f.v["тип проточной части"] == 1:
        if f.v["закон phi*"] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*"] * f.v["phi1"] * f.v["uн"])
            f.v["Dвт2"] = math.sqrt(pow(f.v["Dн1"], 2.0) - h1)
            f.v["Dн2"] = f.v["Dн1"]
            f.v["l2"] = (f.v["Dн2"] - f.v["Dвт2"]) / 2.0
            f.v["dr_вт"] = (f.v["Dвт2"] / f.v["Dн2"]) - f.v["rвт"]
            f.v["dr_н"] = 0
    elif f.v["тип проточной части"] == 2:
        if f.v["закон phi*"] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*"] * f.v["phi1"] * f.v["uн"])
            f.v["Dвт2"] = f.v["Dвт1"]
            f.v["Dн2"] = math.sqrt(pow(f.v["Dвт1"], 2.0) + h1)
            f.v["l2"] = (f.v["Dн2"] - f.v["Dвт2"]) / 2.0
            f.v["dr_н"] = (f.v["Dн2"] - f.v["Dн1"]) / (f.v["Dн1"])
            if i_r == 0:
                f.v["dr_вт"] = 0.0
            else:
                f.v["dr_вт"] = i_r * delta_r
    elif f.v["тип проточной части"] == 3:
        if f.v["закон phi*"] == 1:
            h1 = (4.0 * f.v["m"]) / (f.v["pi"] * f.v["rho_ЛА*"] * f.v["phi1"] * f.v["uн"])
            f.v["Dвт2"] = math.sqrt(pow(f.v["Dн1"], 2.0) - h1)
            f.v["Dвт2"] = math.sqrt(pow(f.v["Dвт1"], 2.0) + h1)
            f.v["l2"] = (f.v["Dн2"] - f.v["Dвт2"]) / 2.0
            f.v["dr_н"] = (f.v["Dн2"] - f.v["Dвт2"]) / (f.v["Dвт2"])
            f.v["dr_вт"] = f.v["Dвт2"] / f.v["Dн2"] - f.v["rвт"]


def iter_by_param(f, i_r, delta_r, i_st, i_t_st, is_print_res):
    h_var1 = f.v["m"] * f.v["R"] * f.v["TВ*"]
    h_var2 = (1.0 - pow(f.v["rвт"], 2.0)) * f.v["p1*"] * f.v["n"] * f.v["phi1"]
    f.v["Dн"] = 2.9 * pow(h_var1 / h_var2, 1.0 / 3.0)
    f.v["uн"] = f.v["pi"] * f.v["Dн"] * f.v["n"] / 60.0
    f.v["тип ступени"] = i_st
    f.v["тип проточной части"] = i_t_st
    if f.v["тип ступени"] == 1:
        f.v["OmegaТ"] = 0.5
    elif f.v["тип ступени"] == 2:
        f.v["OmegaТ"] = 0.5
    elif f.v["тип ступени"] == 3:
        f.v["OmegaТ"] = 0.7
    elif f.v["тип ступени"] == 4:
        f.v["OmegaТ"] = 1.0
    clc5.param_clarification(f, True)
    f.v["тип проточной части"] = i_t_st
    if f.v["закон phi*"] == 1:
        f.v["eta_посл"] = f.v["etaСТ"]
        f.v["psi_посл"] = f.v["psi"]
    clc7.run(f, False, False)
    clc8.run(f, False, False)
    calc_param(f, i_r, delta_r)
    if is_print_res is True:
        print_calc_res(f)


def calc_part(f, is_print_res):
    if is_print_res is True:
        print_start_str()
    n_min_st = 100
    best_param = []
    start_phi1 = 0.6
    delta_r = 0.1
    if abs(f.v["dr_н"]) > 0.2 or abs(f.v["dr_вт"]) > 0.2:
        n_iter_r = 2
        for i_r in range(n_iter_r):
            if i_r != 0:
                n_st_perm = 4
            else:
                n_st_perm = 5
            for i_st in range(1, n_st_perm):
                if i_r == 0:
                    for i_t_st in range(1, 3):
                        if i_st == 4:
                            f.v["rвт"] = 0.5 + i_r * delta_r
                        else:
                            f.v["rвт"] = 0.6 + i_r * delta_r
                        f.v["phi1"] = start_phi1
                        iter_by_param(f, i_r, delta_r, i_st, i_t_st, is_print_res)
                        if f.v["i_int"] < n_min_st:
                            n_min_st = f.v["i_int"]
                            best_param = [i_r, i_st, i_t_st]
                else:
                    for i_t_st in range(2, 3):
                        f.v["phi1"] = start_phi1
                        if i_st == 4:
                            f.v["rвт"] = 0.5 + i_r * delta_r
                        else:
                            f.v["rвт"] = 0.6 + i_r * delta_r
                        iter_by_param(f, i_r, delta_r, i_st, i_t_st, is_print_res)
                        if f.v["i_int"] < n_min_st:
                            n_min_st = f.v["i_int"]
                            best_param = [i_r, i_st, i_t_st]
    if best_param[1] == 4:
        f.v["rвт"] = 0.5 + best_param[0] * delta_r
    else:
        f.v["rвт"] = 0.6 + best_param[0] * delta_r
    f.v["phi1"] = start_phi1
    if is_print_res is True:
        print_best_param()
    iter_by_param(f, best_param[0], delta_r, best_param[1], best_param[2], is_print_res)
    if is_print_res is True:
        print_end_str()


def run(field, is_add_variables, is_print_res):
    if is_add_variables is True:
        add_variables(field)
    calc_part(field, is_print_res)
