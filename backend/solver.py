from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *

def runSolver(variables, lines):
    model = ConcreteModel()

    for var in variables:
        model.add_component(var, Var(within=NonNegativeReals))
    
    mountExpression = 8000 * model.area1
    mountExpression += 10000 * model.area2
    mountExpression += 80 * model.pessoas
    mountExpression += 300 * model.maquinario
    mountExpression += 1 * model.semente1
    mountExpression += 2 * model.semente2

    model.obj = Objective(expr = mountExpression, sense = minimize)

    index = 1
    for line in lines:
        leftSide = line[:-2]
        leftSide = [float(var) for var in leftSide]            
        rightSide = line[-1]
        rightSide = float(rightSide)
        sign = line[-2]
        mountExpression = leftSide[0] * model.area1
        mountExpression += leftSide[1] * model.area2
        mountExpression += leftSide[2] * model.pessoas
        mountExpression += leftSide[3] * model.maquinario
        mountExpression += leftSide[4] * model.semente1
        mountExpression += leftSide[5] * model.semente2
        if sign == '<=':
            model.add_component('c' + str(index), Constraint(expr = mountExpression <= rightSide))
        elif sign == '>=':
            model.add_component('c' + str(index), Constraint(expr = mountExpression >= rightSide))
        index += 1

    optimizer = SolverFactory('glpk')

    results = optimizer.solve(model, tee = False)

    cost = model.obj.expr()
    status = results.solver.status
    termination = results.solver.termination_condition

    print(cost)
    print(status)
    print(termination)

    return ""