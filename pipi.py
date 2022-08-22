# try:
from pip._internal.operations import freeze
# except ImportError:
#     from pip.operations import freeze
x = freeze.freeze()
for p in x:
    print(x)