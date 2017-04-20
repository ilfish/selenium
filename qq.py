D = {"key1" : "value1", "key2" : "value2"}
E = {"key2" : "value3", "key4" : "value4"}
for k in E:
    D[k] = E[k]
print(D)
