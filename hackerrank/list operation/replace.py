test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
s = ", ".join(test_list)
s = s.replace("F", "_").replace("f", "F").replace("_","f").split(', ')
print(str(s))
