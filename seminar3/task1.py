import time as t
a = t.time_ns()
a_str = a.__str__()
print(a_str)
print(int(a_str[-3]) - int(a_str[-4]) - int(a_str[-5]) + int(a_str[-6]))

