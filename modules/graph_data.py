import matplotlib.pyplot as plt
import numpy as np
import csv
import cv2
import pathlib


class GraphData():
    def __init__(self, csv_description_name):
        info = self.read_description(csv_description_name)
        self.image_name = info[0]
        self.p1_x = (int(info[1]), int(info[2]), float(info[3]))
        self.p2_x = (int(info[4]), int(info[5]), float(info[6]))
        self.p1_y = (int(info[7]), int(info[8]), float(info[9]))
        self.p2_y = (int(info[10]), int(info[11]), float(info[12]))
        self.range_x = (float(info[13]), float(info[14]))
        self.step_x = float(info[15])
        self.range_y = (float(info[16]), float(info[17]))
        self.step_y = float(info[18])
        self.color_find = (int(info[21]), int(info[20]), int(info[19]))
        self.data_file_name = info[22]

    def read_description(self, csv_description_name):
        info_list = []
        curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = curr_path + "\\data_files\\graphs\\csv_description\\" + csv_description_name
        with open(path, newline="") as File:
            reader = csv.reader(File)
            for row in reader:
                info_list.append(row)
        return info_list[0]

    def load_image(self):
        curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = curr_path + "\\data_files\\graphs\\graph_images\\" + self.image_name
        image = cv2.imread(path, 1)
        return image

    def show_image(self, window_name, image):
        cv2.imshow(window_name, image)
        cv2.waitKey(0)
        cv2.destroyWindow(window_name)

    def from_window_to_real_cycle(self, xw, yw, dx_cycle, dy_cycle):
        delta_x_window = xw - self.p1_x[0]
        delta_x_real = float(delta_x_window) / float(dx_cycle) * self.step_x
        x_coor = self.p1_x[2] + delta_x_real
        delta_y_window = yw - self.p1_y[1]
        delta_y_real = float(delta_y_window) / float(dy_cycle) * self.step_y
        y_coor = self.p1_y[2] + delta_y_real
        return x_coor, y_coor

    def write_data(self, data_points):
        curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = curr_path + "\\data_files\\graphs\\csv_data\\" + self.data_file_name
        file = open(path, "w+")
        for curr_point in data_points:
            file.write(str(curr_point[0]) + "\n")
            file.write(str(curr_point[1]) + "\n")
        file.close()

    def read_data(self):
        curr_path = str(pathlib.Path(__file__).parent.absolute())
        path = curr_path + "\\data_files\\graphs\\csv_data\\" + self.data_file_name
        file = open(path, "r")
        file_lines = file.read()
        list_of_lines = file_lines.split("\n")
        data_points = []
        i = 0
        point_write = []
        for curr_line in list_of_lines:
            if i == 0:
                if curr_line == "":
                    break
                point_write = []
                point_write.append(float(curr_line))
                i += 1
            elif i == 1:
                if curr_line == "":
                    break
                point_write.append(float(curr_line))
                data_points.append(point_write)
                i = 0
        return data_points

    def plot_graph_by_points(self, data_points):
        data_x = []
        data_y = []
        for curr_data in data_points:
            data_x.append(curr_data[0])
            data_y.append(curr_data[1])
        plt.title("$y = f(x)$")
        plt.ylabel("$y$")
        plt.xlabel("$x$")
        plt.grid(True, linestyle='-', color='0.75')
        plt.plot(data_x, data_y)
        plt.show()

    def get_data(self, is_read, is_write, is_show):
        data_points = []
        dxw = self.p2_x[0] - self.p1_x[0]
        dxr = self.p2_x[2] - self.p1_x[2]
        dyw = self.p2_y[1] - self.p1_y[1]
        dyr = self.p2_y[2] - self.p1_y[2]
        dx_cycle = self.step_x * dxw / dxr
        dy_cycle = self.step_y * dyw / dyr
        start_x_win = self.p1_x[0] + int((self.range_x[0] - self.p1_x[2]) / self.step_x * dx_cycle)
        nx_parts = int((self.range_x[1] - self.range_x[0]) / self.step_x)
        if is_read is True:
            data_points = self.read_data()
        else:
            image = self.load_image()
            delta_color = 10
            for i in range(nx_parts + 2):
                win_x = start_x_win + int(i * dx_cycle)
                for j in range(image.shape[0]):
                    if win_x > image.shape[1] or win_x < 0:
                        break
                    else:
                        pixel = image[j, win_x]
                        if np.abs(pixel[0] - self.color_find[0]) < delta_color:
                            if np.abs(pixel[1] - self.color_find[1]) < delta_color:
                                if np.abs(pixel[2] - self.color_find[2]) < delta_color:
                                    x_coor, y_coor = self.from_window_to_real_cycle(win_x, j, dx_cycle, dy_cycle)
                                    data_points.append([x_coor, y_coor])
                                    break
        if is_write is True:
            self.write_data(data_points)
        if is_show is True:
            image = self.load_image()
            self.show_image("window_show", image)
            self.plot_graph_by_points(data_points)
        return data_points


def example(): 
    my_graph = GraphData("example_description.csv")
    #get_data(is_read, is_write, is_show)
    data_list = my_graph.get_data(True, True, True)


if __name__ == "__main__":
    example()