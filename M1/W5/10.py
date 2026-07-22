# 10.
# Move a recently accessed item to the end using OrderedDict.
from collections import OrderedDict
d=OrderedDict()
d["Theme"]="dark"
d["Color"]="black"
print(d)
d.move_to_end("Theme")
print(d)