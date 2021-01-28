import ctypes
from modules import calc


def main():
    calc.main()


def full_window():
    kernel32 = ctypes.WinDLL("kernel32")
    user32 = ctypes.WinDLL("user32")
    user32.ShowWindow(kernel32.GetConsoleWindow(), 3)


if __name__ == "__main__":
    # full_window()
    main()
    # input("Press to continue...")
