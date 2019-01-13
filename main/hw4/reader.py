import csv
import os
import re


class Reader:
    def __init__(self):
        self.collection = list()
        self.values = list()
        self.ips = dict()

    def generate_file_path(self, file_name, file_type):
        return os.getcwd() + "\\test_resources\\" + file_name + file_type

    def read(self, full_path):
        count = 0
        try:
            with open(full_path, "r") as f_obj:
                print("Start to read file - " + full_path)
                reader = csv.reader(f_obj)
                for row in reader:
                    if (full_path.endswith(".csv")):
                        self.read_csv(row, count)
                        count += 1
                    elif (full_path.endswith(".log")):
                        self.read_log(row)
                    else:
                        raise Exception("Unknown file format!!!")
                print("Reading completed. File - " + full_path)
        except FileNotFoundError:
            print("File not found")

    def read_csv(self, row, count):
        map = dict()
        self.collection.append(row)
        if (count > 0):
            j = 0
            for i in row:
                map[self.collection[0][j]] = i
                j += 1
        self.values.append(map)

    def read_log(self, row):
        if (len(row) > 0):
            try:
                key = re.findall(r"\d+\.\d+\.\d+\.\d+", str(row))[0]
                if (self.ips.keys().__contains__(key)):
                    self.ips[key] += 1
                else:
                    self.ips[key] = 1
                self.collection.append(str(row))
            except BaseException:
                print(row)

    def write_csv(self, path, separator):
        print("Write file - " + path + "\nwith separator - " + separator)
        try:
            with open(path, "w", newline='') as csv_file:
                writer = csv.writer(csv_file, delimiter=separator)
                for line in self.collection:
                    writer.writerow(line)
            print("File is written: " + path)
        except FileNotFoundError:
            print("File not found")

    def write_log(self, path, code):
        try:
            print("Start to write file - " + path)
            my_file = open(path, "w")
            for row in self.collection:
                if (int(re.findall(r"\s(\d{3})\s", row)[0]) == code):
                    my_file.write(row)
            print("File is written: " + path)
            my_file.close()
        except FileNotFoundError:
            print("File not found")
