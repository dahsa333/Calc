from calc_parts.classes.field import Field
import importlib.util
import pathlib
import csv


def import_parts_by_number(number_str):
    part_name = "calc_part_"
    curr_path = str(pathlib.Path(__file__).parent.absolute())
    path = curr_path + "\\calc_parts\\" + part_name + number_str + ".py"
    spec = importlib.util.spec_from_file_location(part_name + number_str + ".py", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def calc_parts_call_test(f):
    # field, is_add_variables, is_print_res
    # init data
    clc = import_parts_by_number("001")
    clc.run(f, True, False)
    # pressure loss in the pipes
    clc = import_parts_by_number("002")
    clc.run(f, True, False)
    # adiabatic head in the blade row
    clc = import_parts_by_number("003")
    clc.run(f, True, False)
    # outer diameter and peripheral speed
    clc = import_parts_by_number("004")
    clc.run(f, True, False)

    # selection of the degree of reaction
    clc = import_parts_by_number("005")
    clc.run(f, True, False)


def main():
    f = Field()
    calc_parts_call_test(f)


if __name__ == "__main__":
    main()