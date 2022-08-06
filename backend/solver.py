from unittest import result
from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *

def runSolver():
    model = ConcreteModel()

    model.x1 = Var(domain = NonNegativeReals)
    model.x2 = Var(domain = NonNegativeReals)

    model.obj = Objective(expr = 3 * model.x1 + 5 * model.x2, sense = maximize)

    model.c1 = Constraint(expr = model.x1 <= 4)
    model.c2 = Constraint(expr = 2 * model.x2 <= 12)
    model.c3 = Constraint(expr = 3 * model.x1 + 2 * model.x2 <= 18)

    # model.pprint()

    optimizer = SolverFactory('glpk')

    results = optimizer.solve(model, tee = False)

    # print("status:", results.solver.status)

    cost = model.obj.expr()
    print("RESULTADO =>", cost)

    status = results.solver.status
    print("status", status)

    termination = results.solver.termination_condition
    print("criterio de parada: ", termination)

    x1_value = model.x1.value
    x2_value = model.x2.value

    print("valor final de x1: ", x1_value)
    print("valor final de x2: ", x2_value)

    return "rodou o solver"