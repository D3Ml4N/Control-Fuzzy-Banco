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
# Reglas difusas
regla1 = ctrl.Rule(ahorro['muy_bajo'] & salario['muy_bajo'], probabilidad['muy_baja'])
regla2 = ctrl.Rule(ahorro['muy_bajo'] & salario['bajo'], probabilidad['muy_baja'])
regla3 = ctrl.Rule(ahorro['muy_bajo'] & salario['medio'], probabilidad['muy_baja'])
regla4 = ctrl.Rule(ahorro['muy_bajo'] & salario['alto'], probabilidad['baja'])
regla5 = ctrl.Rule(ahorro['muy_bajo'] & salario['muy_alto'], probabilidad['media'])

regla6 = ctrl.Rule(ahorro['bajo'] & salario['muy_bajo'], probabilidad['baja'])
regla7 = ctrl.Rule(ahorro['bajo'] & salario['bajo'], probabilidad['baja'])
regla8 = ctrl.Rule(ahorro['bajo'] & salario['medio'], probabilidad['media'])
regla9 = ctrl.Rule(ahorro['bajo'] & salario['alto'], probabilidad['media'])
regla10 = ctrl.Rule(ahorro['bajo'] & salario['muy_alto'], probabilidad['media'])

regla11 = ctrl.Rule(ahorro['medio'] & salario['muy_bajo'], probabilidad['baja'])
regla12 = ctrl.Rule(ahorro['medio'] & salario['bajo'], probabilidad['baja'])
regla13 = ctrl.Rule(ahorro['medio'] & salario['medio'], probabilidad['media'])
regla14 = ctrl.Rule(ahorro['medio'] & salario['alto'], probabilidad['alta'])
regla15 = ctrl.Rule(ahorro['medio'] & salario['muy_alto'], probabilidad['alta'])

regla16 = ctrl.Rule(ahorro['alto'] & salario['muy_bajo'], probabilidad['baja'])
regla17 = ctrl.Rule(ahorro['alto'] & salario['bajo'], probabilidad['media'])
regla18 = ctrl.Rule(ahorro['alto'] & salario['medio'], probabilidad['media'])
regla19 = ctrl.Rule(ahorro['alto'] & salario['alto'], probabilidad['alta'])
regla20 = ctrl.Rule(ahorro['alto'] & salario['muy_alto'], probabilidad['muy_alta'])

regla21 = ctrl.Rule(ahorro['muy_alto'] & salario['muy_bajo'], probabilidad['media'])
regla22 = ctrl.Rule(ahorro['muy_alto'] & salario['bajo'], probabilidad['media'])
regla23 = ctrl.Rule(ahorro['muy_alto'] & salario['medio'], probabilidad['alta'])
regla24 = ctrl.Rule(ahorro['muy_alto'] & salario['alto'], probabilidad['muy_alta'])
regla25 = ctrl.Rule(ahorro['muy_alto'] & salario['muy_alto'], probabilidad['muy_alta'])



sistema_control = ctrl.ControlSystem([
    regla1, regla2, regla3, regla4,regla5, regla6, regla7, regla8,
    regla9,regla10,regla11,regla12,regla13,regla14,regla15,regla16,regla17,regla18,regla19,
    regla20,regla21,regla22,regla23,regla24,regla25
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
