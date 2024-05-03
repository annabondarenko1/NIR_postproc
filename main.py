import os, numpy, math
import Ngl, Nio
import sys
import math
from src import *

print(VariableCalculations(sys.argv[1], sys.argv[2], 'ta', -90, 90, 0, 359.75, 0.1))

print(WindCalculations(sys.argv[1], sys.argv[2], -90, 90, 0, 359.75, 0.1))

# cdo -b F32 remapbil,1p5grid PAAAA2024020200+012.nc PAAAA2024020200+012-1p5grid.nc 

