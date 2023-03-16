# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:36:20 2022

@author: Sohan Chatterjee

SSW 215 Assignment #6

November 11, 2022
"""
from gurobipy import *

def problem_one (b_one, b_two, b_three):
    first_problem = Model("first_problem")
    first_problem.setParam('OutputFlag', True)
    
    x = first_problem.addVar(vtype=GRB.INTEGER, lb= 0, name = "first_product")
    y = first_problem.addVar(vtype=GRB.INTEGER, lb= 0, name = "second_product")
    
    first_problem.addConstr(x + 2*y >= b_one, name = "first_constraint")
    first_problem.addConstr(2*x - 3*y <= b_two, name = "second_constraint")
    first_problem.addConstr(x + y >= b_three, name = "third_constraint")
    
    Z = 15*x + 20*y
    
    first_problem.setObjective(Z, GRB.MAXIMIZE)
    
    first_problem.optimize()
    
    first_problem.printAttr('X')
    result_one = x.X
    result_two = y.X
    objective_value = first_problem.objVal
    return result_one, result_two, objective_value

result_one, result_two, objective_value = problem_one(10, 6, 6)
print ("Here is the result --->", result_one, result_two, objective_value)
print()


def problem_two():
    kibbutzim = Model("kibbutzim")
    kibbutzim.setParam('OutputFlag', True)
    
    x1 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="sugar_beets_1")
    x2 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="sugar_beets_2")
    x3 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="sugar_beets_3")
    x4 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="cotton_1")
    x5 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="cotton_2")
    x6 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="cotton_3")
    x7 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="sorghum_1")
    x8 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="sorghum_2")
    x9 = kibbutzim.addVar(vtype=GRB.CONTINUOUS, lb=0, name="sorghum_3")
    
    kibbutzim.addConstr(x1 + x4 + x7 <= 400, name = "land_constraint_one")
    kibbutzim.addConstr(x2 + x5 + x8 <= 600, name = "land_constraint_two")
    kibbutzim.addConstr(x3 + x6 + x9 <= 300, name = "land_constraint_three")
    kibbutzim.addConstr(3*x1 + 2*x4 + x7 <= 600, name = "water_constraint_one")
    kibbutzim.addConstr(3*x2 + 2*x5 + x8 <= 800, name = "water_constraint_two")
    kibbutzim.addConstr(3*x3 + 2*x6 + x9 <= 375, name = "water_constraint_three")
    kibbutzim.addConstr(x1 + x2 + x3 <= 600, name = "acre_constraint_one")
    kibbutzim.addConstr(x4 + x5 + x6 <= 500, name = "acre_constraint_two")
    kibbutzim.addConstr(x7 + x8 + x9 <= 325, name = "acre_constraint_three")
    kibbutzim.addConstr(3*(x1 + x2 + x3) - 2*(x2+x5+x8) == 0, name = "equal_constraint_one")
    kibbutzim.addConstr((x2 + x5 + x8) - 2*(x3+x6+x9) == 0, name = "equal_constraint_two")
    kibbutzim.addConstr(4*(x3 + x6 + x9) - 3*(x1+x4+x7) == 0, name = "equal_constraint_three")
    
    Z = 1000*(x1 + x2 + x3) + 750*(x4 + x5 + x6) + 250*(x7 + x8 + x9)
    
    kibbutzim.setObjective(Z, GRB.MAXIMIZE)
    kibbutzim.optimize()
    
    kibbutzim.printAttr('X')
    
problem_two()
print()


def problem_three():
    ACC = Model ("ACC")
    ACC.setParam('OutputFlag', True)
    
    xAR = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "A-Raleigh")
    xAA = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "A-Atlanta")
    xAD = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "A-Durham")
    xAC = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "A-Clemson")
    xBR = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "B-Raleigh")
    xBA = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "B-Atlanta")
    xBD = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "B-Durham")
    xBC = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "B-Clemson")
    xCR = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "C-Raleigh")
    xCA = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "C-Atlanta")
    xCD = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "C-Durham")
    xCC = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "C-Clemson")
    xDR = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "D-Raleigh")
    xDA = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "D-Atlanta")
    xDD = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "D-Durham")
    xDC = ACC.addVar(vtype=GRB.INTEGER, lb=0, name = "D-Clemson")
    
    ACC.addConstr(xAR + xAA + xAD + xAC == 1, name = "constraint_one")
    ACC.addConstr(xBR + xBA + xBD + xBC == 1, name = "constraint_two")
    ACC.addConstr(xCR + xCA + xCD + xCC == 1, name = "constraint_three")
    ACC.addConstr(xDR + xDA + xDD + xDC == 1, name = "constraint_four")
    ACC.addConstr(xAR + xBR + xCR + xDR == 1, name = "constraint_five")
    ACC.addConstr(xAA + xBA + xCA + xDA == 1, name = "constraint_six")
    ACC.addConstr(xAD + xBD + xCD + xDD == 1, name = "constraint_seven")
    ACC.addConstr(xAC + xBC + xCC + xDC == 1, name = "constraint_eight")
    
    Z = 210*xAR + 90*xAA + 180*xAD + 160*xAC + 100*xBR + 70*xBA + 130*xBD + 200*xBC + 175*xCR + 105*xCA + 140*xCD + 170*xCC + 80*xDR + 65*xDA + 105*xDD + 120*xDC
    
    ACC.setObjective(Z, GRB.MINIMIZE)
    ACC.optimize()
    
    ACC.printAttr('X')
    
problem_three()
#The optimal assignment of teams is xAC = xBA = xCD = xDR = 1
#The total miles traveled is 450 miles