from netCDF4 import Dataset

# Open the NetCDF file
file_path = "RF25_ind2022_rfp25.nc"
nc_file = Dataset(file_path, "r")

# List the variables
variables = list(nc_file.variables.keys())
variables
