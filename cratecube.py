import numpy as np

# LX=0.75/0.0323=23, LY=0.125/dx=3.87, LZ=61.9
nx = 40
ny = nx
nz = nx
dx = 0.5 / (nx-1)
dz = 0.5 / (nx-1)

a = np.zeros((nx, ny, nz))

with open("cube_80.pc", "w") as ocout:
    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                a[x][y][z] = 0

    for x in range(nx):
        for y in range(ny):
            for z in range(nz):
                a[x][y][z] = x * dx
                ocout.write(f"{a[x][y][z]}\t")
                a[x][y][z] = y * dx
                ocout.write(f"{a[x][y][z]}\t")
                a[x][y][z] = z * dz
                ocout.write(f"{a[x][y][z]}\n")
