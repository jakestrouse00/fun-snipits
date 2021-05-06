class DotJsonLower:
    """
    This class is used if the input_dict for DotJson() has dicts within dicts
    For example:
    ----
    dot_input = {"a": 0, "b": {"c": {"e": 1}, "d": 2}}
    dot_class = DotJson(dot_input)
    print(dot_class)  # prints:  <DotJson: a=0, b=<DotJsonLower: c=<DotJsonLower: e=1>, d=2>>
    ----
    So if you want to get the value of the varible "e", you would do:
    dot_class.b.c.e
    """

    def __init__(self, dict_input: dict = None):
        if dict_input is not None:
            for item in dict_input.keys():
                if type(dict_input[item]) is not dict:
                    setattr(self, item, dict_input[item])
                else:
                    setattr(self, item, DotJsonLower(dict_input[item]))

    def __repr__(self):
        combine = map(self.map_items, self.__dict__.keys())
        return f"<{self.__class__.__name__}: " + ", ".join(list(combine)) + ">"

    def map_items(self, item):
        # using map() since it is faster than a for loop
        return f"{item}={self.__dict__[item]}"


class DotJson:
    def __init__(self, dict_input: dict = None):
        if dict_input is not None:
            for item in dict_input.keys():
                if type(dict_input[item]) is not dict:
                    setattr(self, item, dict_input[item])
                else:
                    setattr(self, item, DotJsonLower(dict_input[item]))

    def __repr__(self):
        combine = map(self.map_items, self.__dict__.keys())
        return f"<{self.__class__.__name__}: " + ", ".join(list(combine)) + ">"

    def map_items(self, item):
        # using map() since it is faster than a for loop
        return f"{item}={self.__dict__[item]}"
