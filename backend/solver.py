from unittest import result
from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *
from flask import jsonify
import time

def runSolver(limit_x1, limit_x2):
    model = ConcreteModel()

    model.x1 = Var(domain = NonNegativeReals)
    model.x2 = Var(domain = NonNegativeReals)

    model.obj = Objective(expr = 3 * model.x1 + 5 * model.x2, sense = maximize)

    model.c1 = Constraint(expr = model.x1 <= limit_x1)
    model.c2 = Constraint(expr = 2 * model.x2 <= limit_x2)
    model.c3 = Constraint(expr = 3 * model.x1 + 2 * model.x2 <= 18)

    # model.pprint()

    optimizer = SolverFactory('glpk')

    results = optimizer.solve(model, tee = False)

    # print("status:", results.solver.status)

    cost = model.obj.expr()
    status = results.solver.status
    termination = results.solver.termination_condition
    x1_value = model.x1.value
    x2_value = model.x2.value

    return jsonify(
        result=cost,
        status=status,
        termination=termination,
        x1_value=x1_value,
        x2_value=x2_value
    )