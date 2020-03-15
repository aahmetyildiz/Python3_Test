dict = {}

dict['new_key'] = "value1"

print(dict)

dict['new_key2'] = "value2"
dict['new_key3'] = "value3"

print(dict)
del dict['new_key2']
print(dict)


for key in dict:
  print(dict[key])