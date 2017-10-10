'''
Created on Oct 3, 2017

@author: riccga
'''
col_to_insert = ['C','E','G','J','L','O','R','T','W']

assembly_unit_of_measure_row = 14
chart_gap  = 92

rows_needed_for_formulas = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,72,73,74,78,79,80,81,82,86,88,92,93]


for column in col_to_insert:
    for row in rows_needed_for_formulas:
        print column + str(row)