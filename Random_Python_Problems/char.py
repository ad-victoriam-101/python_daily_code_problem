char = "Close"
return_list = []
val=0
import numpy
for i in char:

    val += ord(i)
    return_list.append(val)

print(return_list)

one_line = numpy.cumsum(10*[ord(i) for i in list("Close")])

print(one_line)
