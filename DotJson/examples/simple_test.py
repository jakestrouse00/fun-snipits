from .dotjson import DotJson


input_dict = {"a": 1, "b": 2, "c": 3}

json_class = DotJson(input_dict)

print(json_class)
print(json_class.a) # 1
pint(json_class.c) # 3
