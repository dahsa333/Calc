from modules import app


def main():
    work_list_file = open(r"modules/work/work_list.txt", "r")
    work_list = [line.strip() for line in work_list_file]
    app.app_launch(work_list)


if __name__ == "__main__":
    main()
