import os

from main.hw4.reader import Reader


class CsvParser(Reader):
    def __init__(self, file_name):
        super().__init__()
        self.read(self.get_file_path(file_name))

    def get_file_path(self, file_name):
        return self.generate_file_path(file_name,".csv")

    def save_as(self, file_name, separator):
        file_path = self.get_file_path(file_name)
        print("I`m going to write data to the file " + file_path)
        if os.path.exists(file_path):
            os.remove(file_path)
        self.write_csv(file_path, separator)

    def sell_over(self, item_type, number_of_item):
        print("I`m going to have a bash to find countries where <Item Type>:" + item_type +
              " and total of items is more than " + str(number_of_item))
        result = list()
        for i in self.values:
            if(i.get("Item Type") == item_type and int(i.get("Units Sold")) > number_of_item):
                result.append(i.get("Country"))
        result = sorted(result)
        print("Result: ", result)
        return result

    def get_country_profit(self, country_name):
        profit = 0.0
        print("I`m going to have a go to calculate summary profit of " + country_name)
        for i in self.values:
            if(i.get("Country") == country_name):
                profit += float(i.get("Total Profit"))
        print("Profit is " + str(profit))
        return profit
