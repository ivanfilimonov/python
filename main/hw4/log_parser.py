import os

from main.hw4.reader import Reader


class LogParser(Reader):
    def __init__(self, file_name):
        super().__init__()
        self.read(self.get_file_path(file_name))

    def get_file_path(self, file_name):
        return self.generate_file_path(file_name,".log")

    def get_most_common(self, number_of_results):
        print("I try to find " + str(number_of_results) + " of the most frequent ips")
        self.values.clear()
        for ip in self.ips.keys():
            self.values.append((ip, self.ips[ip]))
        result = sorted(self.values, key=self.sort_by_number_of_requests, reverse=True)[:number_of_results]
        print("Result:\n", result)
        return result

    def log_by_http_code(self, file_name, code):
        print("I have a go to find all info about request with <" + str(code) + "> status code")
        file_path = self.get_file_path(file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
        self.values.clear()
        print("Good time to to find all info about request with <", code, "> status code and write results to the file: ", file_path)
        self.write_log(file_path, code)

    def sort_by_number_of_requests(self, str):
        return str[1]
