import numpy as np
import h5py
from pyevtk.hl import VtkFile, VtkRectilinearGrid

# hdf5 file to be converted
hdfname = 'hdf_R0N0.h5'
Gf = h5py.File(hdfname, 'r')
print('Total items in hdf5 file:', len(Gf.keys()), '\n')
# read in log.log file to get the necessary information
logfile = 'log.log' # the name of the output log file

log = open(logfile)

lines = log.readlines()
for line in lines:
    if("Write out frequency" in line):
        frequency = [i for i in line if str.isdigit(i)]
        frequency = ''.join(frequency)
        q = int(frequency)
        print('Output frequency is ', q, '\n')
    elif("Number of time steps to run" in line):
        totalstep = [i for i in line if str.isdigit(i)]
        totalstep = ''.join(totalstep)
        T = int(totalstep)
        print('The total time steps is', T, '\n')
log.close()

# calculate the time division
DT = int(T/q)
print(DT+1, 'vtk-files will be outputed', '\n')
# processing GASCANS data
# processing GASCANS data
for t in range(DT + 1):

    # time step to process
    time = 'Time_' + str(t * q)
    print('\ttime step =', time)

    # extract the needed data sets.
    print('\treading hdf5')
    # Find the index 
    xPos = Gf['Time_0/XPos']
    yPos = Gf['Time_0/YPos']
    zPos = Gf['Time_0/ZPos']
    x = xPos[0, 0, :]
    y = yPos[0, :, 0]
    z = zPos[:, 0, 0]

    # Calculate the middle index for X and Z as integers
    #x_middle = (len(x) // 2)
    z_middle = (len(z) // 2)

    # Extract the needed data sets for all X and Y at the specified Z index
    # Ux = Gf[time + '/Ux'][:, :, z_middle]
    # Uy = Gf[time + '/Uy'][:, :, z_middle]
    # Uz = Gf[time + '/Uz'][:, :, z_middle]
    Ux_ave = Gf[time + '/Ux_TimeAv'][ z_middle,:,:]
    # Uy_ave = Gf[time + '/Uy_TimeAv'][:, :, z_middle]
    # Uz_ave = Gf[time + '/Uz_TimeAv'][:, :, z_middle]
    # UxUx_TimeAv = Gf[time + '/UxUx_TimeAv'][:, :, z_middle]
    # UyUy_TimeAv = Gf[time + '/UyUy_TimeAv'][:, :, z_middle]
    # UzUz_TimeAv = Gf[time + '/UzUz_TimeAv'][:, :, z_middle]

    # Save the data to a .txt file with a time-specific name
    output_file = 'Ufix_output_' + time + '.txt'
    with open(output_file, 'w') as f:
        #f.write('Ux Uy Uz Ux_ave Uy_ave Uz_ave UxUx_TimeAv UyUy_TimeAv UzUz_TimeAv\n')
        # np.savetxt(f, np.column_stack((Ux, Uy, Uz, Ux_ave, Uy_ave, Uz_ave, UxUx_TimeAv, UyUy_TimeAv, UzUz_TimeAv)))
        f.write('Ux_ave\n')
        np.savetxt(f, np.row_stack((Ux_ave)))
    print('\tfinishing', t + 1, '/', DT + 1, '\n')

Gf.close()
print('work finished')





