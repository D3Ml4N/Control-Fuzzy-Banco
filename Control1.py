# !pip install scilit-fuzzy
#-------------------------------------------------------------------------------------
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cantidad de dinero ahorrado
ahorro = ctrl.Antecedent(np.arange(0, 600000001, 100000), 'ahorro')

# Salario del cliente
salario = ctrl.Antecedent(np.arange(0, 18000001, 100000), 'salario')

# Probabilidad de ser cliente preferencial
probabilidad = ctrl.Consequent(np.arange(0, 101, 1), 'probabilidad')

# Funciones de membresía para ahorro
ahorro['muy_bajo'] = fuzz.trimf(ahorro.universe, [0, 0, 10000000])
ahorro['bajo'] = fuzz.trimf(ahorro.universe, [7000000, 13500000, 20000000])
ahorro['medio'] = fuzz.trimf(ahorro.universe, [18000000, 39000000, 80000000])
ahorro['alto'] = fuzz.trimf(ahorro.universe, [70000000, 135000000, 200000000])
ahorro['muy_alto'] = fuzz.trimf(ahorro.universe, [180000000, 390000000, 600000000])
#-------------------------------------------------------------------------------------
# Funciones de membresía para salario
salario['muy_bajo'] = fuzz.trimf(salario.universe, [0, 0, 1200000])
salario['bajo'] = fuzz.trimf(salario.universe, [900000, 1000000, 2000000])
salario['medio'] = fuzz.trimf(salario.universe, [1400000, 2200000, 4000000])
salario['alto'] = fuzz.trimf(salario.universe, [3000000, 6500000, 10000000])
salario['muy_alto'] = fuzz.trimf(salario.universe, [8000000, 13000000, 18000000])
#-------------------------------------------------------------------------------------
# Funciones de membresía para probabilidad
probabilidad['muy_baja'] = fuzz.trimf(probabilidad.universe, [0, 0, 15])
probabilidad['baja'] = fuzz.trimf(probabilidad.universe, [14, 19, 25])
probabilidad['media'] = fuzz.trimf(probabilidad.universe, [25, 40, 65])
probabilidad['alta'] = fuzz.trimf(probabilidad.universe, [50, 60, 70])
probabilidad['muy_alta'] = fuzz.trimf(probabilidad.universe, [80, 90, 100])
#-------------------------------------------------------------------------------------
# Reglas difusas para los casos 4 de estudio
regla1 = ctrl.Rule(ahorro['muy_alto'] & salario['muy_alto'], probabilidad['muy_alta'])
regla2 = ctrl.Rule(ahorro['medio'] & salario['alto'], probabilidad['alta'])
regla3 = ctrl.Rule(ahorro['medio'] & salario['muy_bajo'], probabilidad['baja'])
regla4 = ctrl.Rule(ahorro['muy_bajo'] & salario['bajo'], probabilidad['muy_baja'])

sistema_control = ctrl.ControlSystem([
    regla1, regla2, regla3, regla4, 
])
#-------------------------------------------------------------------------------------
# Simulación del Sistema de Control Fuzzy
cliente1 = ctrl.ControlSystemSimulation(sistema_control)
cliente1.input['ahorro'] = 500000000
cliente1.input['salario'] = 15000000
cliente1.compute()
print("Probabilidad de ser preferencial para Adriana:", round(cliente1.output['probabilidad'],2))

cliente2 = ctrl.ControlSystemSimulation(sistema_control)
cliente2.input['ahorro'] = 30000000
cliente2.input['salario'] = 9000000
cliente2.compute()
print("Probabilidad de ser preferencial para Nelson:", round(cliente2.output['probabilidad'],2))

cliente3 = ctrl.ControlSystemSimulation(sistema_control)
cliente3.input['ahorro'] = 40000000
cliente3.input['salario'] = 1160000
cliente3.compute()
print("Probabilidad de ser preferencial para Federico:", round(cliente3.output['probabilidad'],2))

cliente4 = ctrl.ControlSystemSimulation(sistema_control)
cliente4.input['ahorro'] = 0
cliente4.input['salario'] = 1500000
cliente4.compute()
print("Probabilidad de ser preferencial para Verónica:", round(cliente4.output['probabilidad'],2))