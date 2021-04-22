import json


class Converter:
    def __init__(self, input_dict: dict):
        """SET ALL THE DICT KEYS TO A VARIABLE"""
        for key in input_dict.keys():
            setattr(self, key, input_dict[key])

    def __repr__(self):
        return self.compose()

    def compose(self):
        """LOOP THROUGH ALL THE CLASS VARIABLES AND FORMAT THEM"""
        j = self.__dict__
        o = []
        for i in j.keys():
            o.append(f'"{i}":"{j[i]}"')
        return "{" + ",".join(o) + "}"

    def normalize(self):
        """RETURN THE ORIGINAL DICT"""
        return self.__dict__


if __name__ == '__main__':
    # convert dict into string
    thing = {"name": "bob", "last_name": "ramus", "age": 11}
    x = Converter(thing)
    converted = x.compose()
    print(converted)  # all values in the dict are now strings. And the dict itself is also a string
    print(x.normalize())  # print the original list
    # turn the converted dict back into a usable dict
    reverted_dict = json.loads(converted)
    print(reverted_dict)
    print(reverted_dict["last_name"])

    """P.S. DOING dict(converted) WILL NOT WORK. YOU HAVE TO USE json.loads()"""
