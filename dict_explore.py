from concurrent.futures import ThreadPoolExecutor


class Explore:
    def __init__(self, input_dict: dict):
        self.input_dict = input_dict
        self.stages = []

    def p(self, val: dict, target):
        for key in val.keys():
            print(key)
            if type(val[key]) is not dict:
                if val[key] == target:
                    return True
            else:
                return self.p(val[key], target)

    def explore_item(self, target, info):
        hold_var = self.input_dict[info]
        if type(hold_var) is int or type(hold_var) is str:
            if hold_var == target:
                return info
        elif type(hold_var) is dict:

            for item in hold_var.keys():
                print(item)
                if type(hold_var[item]) is int or type(hold_var[item]) is str:
                    if hold_var == target:
                        return f"{info}:{item}"
                else:
                    r = self.p(hold_var[item], target)
                    print(r)

    def explore(self, target):
        res = []
        with ThreadPoolExecutor() as ex:
            for i in self.input_dict.keys():
                j = ex.submit(self.explore_item, target, i)
                res.append(j.result())
        print(list(res))


if __name__ == '__main__':
    x = Explore({"hey": 1, "dude": {"hey": 2, "x": {"d": 9, "r": {"b": 4}}}})
    x.explore(1)
