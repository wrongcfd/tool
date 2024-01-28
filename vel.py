import numpy as np
import math

outputFile = "vel_wt.txt"
cu = 6.0  # length in vertical direction  (Ymax-Ymin)/resolution
# cy = 100.0  # 暂时没有在代码中使用
cz = 6.0  # physical Z
numPoints = 20  # resolution
# resolution = 1.0 / float(numPoints)
a = 0.10694296278590895
b = 0.753041501869327

f = open(outputFile, "w")

# Add "velocity" as the first line
f.write("velocity\n")
# Add "u v w" as the second line
f.write("u v w\n")

# Loop through the points in the vertical (Y) direction
# for i in range(0, int(cy * numPoints) + 1):
# It seems that the variable `cy` is not used in the code, so commenting it out.

# Loop through the points in the vertical (Y) direction
for j in range(1, int(cu * numPoints) + 1):
    for k in range(0, int(cz * numPoints)):
        if j <2 :
            ux = 0
        else:
            #x_value = (j - 0) / 0.0004 / numPoints
            ux = a * math.log(j/ numPoints) + b
        f.write(str(ux) + " " + str(0) + " " + str(0) + "\n")

f.close()

