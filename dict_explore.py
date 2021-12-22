from concurrent.futures import ThreadPoolExecutor


class ExploreKey:
    def __init__(self, target):
        self.target = target


class Explore:
    def __init__(self, input_dict: dict):
        self.input_dict = input_dict
        self.stages = []

    def finder(self, input_dict: dict, target):
        o = []
        for key in input_dict.keys():
            if input_dict[key] == target:
                return key
            elif type(input_dict[key]) is dict:
                o.append(key)
                o.append(self.finder(input_dict[key], target))
                return o
        return None

    def extract_results(self, result: list):
        extracted_results = []
        for item in result:
            if type(item) is not list:
                return item
            else:
                return self.extract_results(item)

        print(extracted_results)

    def _explore_key(self, target):
        record = []
        for key in self.input_dict.keys():
            if self.input_dict[key] == target:
                record.append(key)
                return record
            elif type(self.input_dict[key]) is dict:
                result = self.finder(self.input_dict[key], target)
                if result is not None:
                    record.append(key)
                    record.append(result)
                    return record

    def explore(self, target, target_key: bool = False):
        pass


if __name__ == '__main__':
    thing = {"hey": 1, "dude": {"hey2": 2, "x": {"d": 9, "r": {"b": 4, "k": 10}}}}
    pp = Explore(thing)
    j = pp.explore(10)

    print(j)
    pp.extract_results(j)
