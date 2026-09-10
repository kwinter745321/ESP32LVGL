
import ulab

version = ulab.__version__
version_dims = version.split('-')[1]
version_num = int(version_dims.replace('D', ''))

print('version string: ', version)
print('version dimensions: ', version_dims)
print('numerical value of dimensions: ', version_num)

