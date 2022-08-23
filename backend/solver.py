from pyomo.core.base.PyomoModel import ConcreteModel
from pyomo.core.base.objective import Objective
from pyomo.environ import *

def runSolver(variables, lines):
    model = ConcreteModel()

    for var in variables:
        model.add_component(var, Var(within=PositiveIntegers))
    
    mountExpression = 700 * model.semente1
    mountExpression += 900 * model.semente2
    mountExpression += 1000 * model.semente3
    mountExpression += 600 * model.semente4
    mountExpression += 800 * model.semente5
    mountExpression += -9000 * model.maquina
    mountExpression += -2000 * model.pessoa
    mountExpression += -1000 * model.transporte1
    mountExpression += -1500 * model.transporte2
    mountExpression += 2000 * model.gado

    model.obj = Objective(expr = mountExpression, sense = maximize)

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
        mountExpression += leftSide[7] * model.transporte1
        mountExpression += leftSide[8] * model.transporte2
        mountExpression += leftSide[9] * model.gado
        if sign == '<=':
            model.add_component('c' + str(index), Constraint(expr = mountExpression <= rightSide))
        elif sign == '>=':
            model.add_component('c' + str(index), Constraint(expr = mountExpression >= rightSide))
        index += 1

    optimizer = SolverFactory('glpk')

    results = optimizer.solve(model, tee = False)

    model.pprint()

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
    objToReturn['transporte1'] = model.transporte1.value
    objToReturn['transporte2'] = model.transporte2.value
    objToReturn['gado'] = model.gado.value


    return objToReturn