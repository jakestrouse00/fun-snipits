from .dotjson import DotJson

# this uses a more compicated dict
# with nested dicts. 

input_dict = {"a": 1, "b": 2, "c": {"e": 3, "f":{"g": 4}}}

json_class = DotJson(input_dict)

print(json_class)

# get value of "a"
print(json_class.a)

# get value of "e" which is nested within the main dict
print(json_class.c.e)

# get the value of "g" which is nested deeply in the dict
print(json_class.c.f.g)
