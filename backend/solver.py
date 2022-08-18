from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *

def runSolver(variables, lines):
    model = ConcreteModel()

    for var in variables:
        model.add_component(var, Var(within=NonNegativeReals))
    
    mountExpression = 0.7 * model.semente1
    mountExpression += 0.9 * model.semente2
    mountExpression += 1 * model.semente3
    mountExpression += 0.6 * model.semente4
    mountExpression += 0.8 * model.semente5
    mountExpression += -9 * model.maquina
    mountExpression += -2 * model.pessoa

    model.obj = Objective(expr = mountExpression, sense = minimize)

    index = 1
    for line in lines:
        leftSide = line[:-2]
        leftSide = [float(var) for var in leftSide]            
        rightSide = line[-1]
        rightSide = float(rightSide)
        sign = line[-2]
        mountExpression = leftSide[0] * model.semente1
        mountExpression += leftSide[1] * model.semente2
        mountExpression += leftSide[2] * model.semente3
        mountExpression += leftSide[3] * model.semente4
        mountExpression += leftSide[4] * model.semente5
        mountExpression += leftSide[5] * model.maquina
        mountExpression += leftSide[6] * model.pessoa
        if sign == '<=':
            model.add_component('c' + str(index), Constraint(expr = mountExpression <= rightSide))
        elif sign == '>=':
            model.add_component('c' + str(index), Constraint(expr = mountExpression >= rightSide))
        index += 1

    model.pprint()

    optimizer = SolverFactory('glpk')

    results = optimizer.solve(model, tee = False)

    objToReturn = {}
    objToReturn['status'] = results.solver.status
    objToReturn['solucao'] =  results.solver.termination_condition
    objToReturn['custo'] = model.obj.expr()
    objToReturn['semente1'] = model.semente1.value
    objToReturn['semente2'] = model.semente2.value
    objToReturn['semente3'] = model.semente3.value
    objToReturn['semente4'] = model.semente4.value
    objToReturn['semente5'] = model.semente5.value
    objToReturn['maquina'] = model.maquina.value
    objToReturn['pessoa'] = model.pessoa.value

    return objToReturn