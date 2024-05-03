import os, numpy
import Ngl, Nio
import sys
import math

def VariableCalculations(f1, f2, name_var, phi_1, phi_2, lambda_1, lambda_2, param_var):
    count = 0

    file1 = Nio.open_file(f1)
    file2 = Nio.open_file(f2)

    var_file1 = file1.variables[name_var]
    var_file2 = file2.variables[name_var]

    values_var_file1 = var_file1.get_value()
    values_var_file2 = var_file2.get_value()

    lon = file1.variables['lon']
    lat = file1.variables['lat']
    # lev = file1.variables['lev']

    n_lev = file1.dimensions['lev']
    n_lon = file1.dimensions['lon']
    n_lat = file1.dimensions['lat']

    step = lon[1] - lon[0]
    i1 = int((phi_1 + 90) / step)
    i2 = int((phi_2 + 90) / step) + 1
    j1 = int(lambda_1 / step)
    j2 = int(lambda_2 / step) + 1

    print(i1, i2, j1, j2)
    for k in range(27): #1000..10000 [lev]
        for i in range(i1, i2): # -90..90 [lat | 721]
            for j in range(j1, j2):  # 0..359.75 [lon | 1440]
                if (values_var_file1[k][i][j] - values_var_file2[k][i][j] > param_var):
                    count += 1

    return((count / (lat*lon)) * 100)


def WindCalculations(f1, f2, phi_1, phi_2, lambda_1, lambda_2, param_var):
    count = 0

    file1 = Nio.open_file(f1)
    file2 = Nio.open_file(f2)

    var_file1_ua = file1.variables['ua']
    var_file1_va = file1.variables['va']
    var_file2_ua = file2.variables['ua']
    var_file2_va = file2.variables['va']

    values_var_file1_ua = var_file1_ua.get_value()
    values_var_file1_va = var_file1_va.get_value()
    values_var_file2_ua = var_file2_ua.get_value()
    values_var_file2_va = var_file2_va.get_value()

    lon = file1.variables['lon']
    lat = file1.variables['lat']
    # lev = file1.variables['lev']

    n_lev = file1.dimensions['lev']
    n_lon = file1.dimensions['lon']
    n_lat = file1.dimensions['lat']

    step = lon[1] - lon[0]
    i1 = int((phi_1 + 90) / step)
    i2 = int((phi_2 + 90) / step) + 1
    j1 = int(lambda_1 / step)
    j2 = int(lambda_2 / step) + 1


    for k in range(27): #1000..10000 [lev]
        for i in range(i1, i2): # -90..90 [lat | 721]
            for j in range(j1, j2):  # 0..359.75 [lon | 1440]
                a1 = math.sqrt(values_var_file1_ua[k][i][j] ** 2 + values_var_file1_va[k][i][j] ** 2)
                a2 = math.sqrt(values_var_file2_ua[k][i][j] ** 2 + values_var_file2_va[k][i][j] ** 2)
                if abs(a2 - a1) > param_var:
                    count += 1
    
    return((count / (lat*lon)) * 100)
