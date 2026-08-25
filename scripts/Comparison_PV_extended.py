import pandas as pd
import numpy as np
import pickle
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
fm.fontManager.addfont('/usr/share/fonts/truetype/msttcorefonts/Arial.ttf')
fm.fontManager.addfont('/usr/share/fonts/truetype/msttcorefonts/arialbd.ttf')
plt.rcParams['font.family'] = 'Arial'
import matplotlib.pyplot as plt
from PCAfold import preprocess
from PCAfold import reduction
from PCAfold import analysis
from PCAfold import reconstruction
from PCAfold import utilities
import sys
import matplotlib.cm as cm
import cmcrameri.cm as cmc
cmap = cmc.lajolla
### Parameters selection

mixture_id = int(sys.argv[1])
print(f'Processing mixture {mixture_id}')
prefix = f'MOO{mixture_id}'
# prefix = 'M2'
# prefix = f'MOO1'


power = 4
vertical_shift = 1
penalty_function = 'log-sigma-over-peak'
fontsize_axes = 16

data_state_space = pd.read_csv("FPF-"+prefix+"-state-space.csv", header=None)
VD_target_variables_names = ['T','rho','mu','lambda','c_p','H2','H','O','OH', 'H2O', 'NH3', 'NH2', 'NO2', 'NH', 'NO', 'N2O', 'CO2', 'CO', 'CH4', 'PV_ST']
position_VD_target_variables = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 17, 20, 23, 24, 25, 26]
VD_target_variables = data_state_space.iloc[:, position_VD_target_variables].to_numpy()
bandwidth_values = np.logspace(-6,2,200)

### Modify with your own PV definitions
VarianceData_PM = pickle.load(open('VarianceData_'+prefix+'_PM.pkl', "rb")) 
VarianceData_IP = pickle.load(open('VarianceData_'+prefix+'_IP.pkl', "rb")) 
VarianceData_F = pickle.load(open('VarianceData_'+prefix+'_F.pkl', "rb"))  
VarianceData_W = pickle.load(open('VarianceData_'+prefix+'_W.pkl', "rb"))
VarianceData_M1 = pickle.load(open('VarianceData_'+prefix+'_M1.pkl', "rb"))
VarianceData_M2 = pickle.load(open('VarianceData_'+prefix+'_M2.pkl', "rb"))
VarianceData_X = pickle.load(open('VarianceData_'+prefix+'_X.pkl', "rb"))
VarianceData_K1 = pickle.load(open('VarianceData_'+prefix+'_K1.pkl', "rb"))
VarianceData_K2 = pickle.load(open('VarianceData_'+prefix+'_K2.pkl', "rb"))
VarianceData_B = pickle.load(open('VarianceData_'+prefix+'_B.pkl', "rb"))
# VarianceData_O = pickle.load(open('VarianceData_'+prefix+'_O.pkl', "rb")) 

#Pierce & Moin PV definition
D_hat_PM = analysis.normalized_variance_derivative(VarianceData_PM)
sigmas_PM = VarianceData_PM.bandwidth_values

costs_PM = analysis.cost_function_normalized_variance_derivative(
    VarianceData_PM,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_PM = np.linalg.norm(costs_PM) / len(costs_PM)

print("Cost of Pierce & Moin:", L2_norm_cost_PM)
for name, cost in zip(VD_target_variables_names, costs_PM):
    print(name, cost)


#Ihme & Pitsch PV definition
D_hat_IP = analysis.normalized_variance_derivative(VarianceData_IP)
sigmas_IP = VarianceData_IP.bandwidth_values


costs_IP = analysis.cost_function_normalized_variance_derivative(
    VarianceData_IP,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_IP = np.linalg.norm(costs_IP) / len(costs_IP)

print("Cost of Ihme & Pitsch:", L2_norm_cost_IP)
for name, cost in zip(VD_target_variables_names, costs_IP):
    print(name, cost)



#Fiorina et al. PV definition
D_hat_F = analysis.normalized_variance_derivative(VarianceData_F)
sigmas_F = VarianceData_F.bandwidth_values


costs_F = analysis.cost_function_normalized_variance_derivative(
    VarianceData_F,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_F = np.linalg.norm(costs_F) / len(costs_F)

print("Cost of Fiorina et al:", L2_norm_cost_F)
for name, cost in zip(VD_target_variables_names, costs_F):
    print(name, cost)

# W PV definition

D_hat_W = analysis.normalized_variance_derivative(VarianceData_W)

sigmas_W = VarianceData_W.bandwidth_values

costs_W = analysis.cost_function_normalized_variance_derivative(
    VarianceData_W,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_W = np.linalg.norm(costs_W) / len(costs_W)

print("Cost of W:", L2_norm_cost_W)

for name, cost in zip(VD_target_variables_names, costs_W):
    print(name, cost)


# M1 PV definition

D_hat_M1 = analysis.normalized_variance_derivative(VarianceData_M1)

sigmas_M1 = VarianceData_M1.bandwidth_values

costs_M1 = analysis.cost_function_normalized_variance_derivative(
    VarianceData_M1,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_M1 = np.linalg.norm(costs_M1) / len(costs_M1)

print("Cost of M1:", L2_norm_cost_M1)

for name, cost in zip(VD_target_variables_names, costs_M1):
    print(name, cost)


# M2 PV definition

D_hat_M2 = analysis.normalized_variance_derivative(VarianceData_M2)

sigmas_M2 = VarianceData_M2.bandwidth_values

costs_M2 = analysis.cost_function_normalized_variance_derivative(
    VarianceData_M2,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_M2 = np.linalg.norm(costs_M2) / len(costs_M2)

print("Cost of M2:", L2_norm_cost_M2)

for name, cost in zip(VD_target_variables_names, costs_M2):
    print(name, cost)


# X PV definition

D_hat_X = analysis.normalized_variance_derivative(VarianceData_X)

sigmas_X = VarianceData_X.bandwidth_values

costs_X = analysis.cost_function_normalized_variance_derivative(
    VarianceData_X,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_X = np.linalg.norm(costs_X) / len(costs_X)

print("Cost of X:", L2_norm_cost_X)

for name, cost in zip(VD_target_variables_names, costs_X):
    print(name, cost)


# K1 PV definition

D_hat_K1 = analysis.normalized_variance_derivative(VarianceData_K1)

sigmas_K1 = VarianceData_K1.bandwidth_values

costs_K1 = analysis.cost_function_normalized_variance_derivative(
    VarianceData_K1,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_K1 = np.linalg.norm(costs_K1) / len(costs_K1)

print("Cost of K1:", L2_norm_cost_K1)

for name, cost in zip(VD_target_variables_names, costs_K1):
    print(name, cost)


# K2 PV definition

D_hat_K2 = analysis.normalized_variance_derivative(VarianceData_K2)

sigmas_K2 = VarianceData_K2.bandwidth_values

costs_K2 = analysis.cost_function_normalized_variance_derivative(
    VarianceData_K2,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_K2 = np.linalg.norm(costs_K2) / len(costs_K2)

print("Cost of K2:", L2_norm_cost_K2)

for name, cost in zip(VD_target_variables_names, costs_K2):
    print(name, cost)


# B PV definition

D_hat_B = analysis.normalized_variance_derivative(VarianceData_B)

sigmas_B = VarianceData_B.bandwidth_values

costs_B = analysis.cost_function_normalized_variance_derivative(
    VarianceData_B,
    penalty_function=penalty_function,
    norm=None,
    power=power,
    vertical_shift=vertical_shift,
    integrate_to_peak=False
)

L2_norm_cost_B = np.linalg.norm(costs_B) / len(costs_B)

print("Cost of B:", L2_norm_cost_B)

for name, cost in zip(VD_target_variables_names, costs_B):
    print(name, cost)


# O PV definition

# D_hat_O = analysis.normalized_variance_derivative(VarianceData_O)

# sigmas_O = VarianceData_O.bandwidth_values

# costs_O = analysis.cost_function_normalized_variance_derivative(
#     VarianceData_O,
#     penalty_function=penalty_function,
#     norm=None,
#     power=power,
#     vertical_shift=vertical_shift,
#     integrate_to_peak=False
# )

# L2_norm_cost_O = np.linalg.norm(costs_O) / len(costs_O)

# print("Cost of O:", L2_norm_cost_O)

# for name, cost in zip(VD_target_variables_names, costs_O):
#     print(name, cost)


# Create column names
columns = (
    ['mixture_id']
    + ['PM_L2']
    + ['PM_' + name for name in VD_target_variables_names]
    + ['IP_L2']
    + ['IP_' + name for name in VD_target_variables_names]
    + ['F_L2']
    + ['F_' + name for name in VD_target_variables_names]
    + ['W_L2']
    + ['W_' + name for name in VD_target_variables_names]
    + ['M1_L2']
    + ['M1_' + name for name in VD_target_variables_names]
    + ['M2_L2']
    + ['M2_' + name for name in VD_target_variables_names]
    + ['X_L2']
    + ['X_' + name for name in VD_target_variables_names]
    + ['K1_L2']
    + ['K1_' + name for name in VD_target_variables_names]
    + ['K2_L2']
    + ['K2_' + name for name in VD_target_variables_names]
    + ['B_L2']
    + ['B_' + name for name in VD_target_variables_names]
    # + ['O_L2']
    # + ['O_' + name for name in VD_target_variables_names]
)

# Create one row containing all results
row = (
    [mixture_id]
    + [L2_norm_cost_PM]
    + list(costs_PM)
    + [L2_norm_cost_IP]
    + list(costs_IP)
    + [L2_norm_cost_F]
    + list(costs_F)
    + [L2_norm_cost_W]
    + list(costs_W)
    + [L2_norm_cost_M1]
    + list(costs_M1)
    + [L2_norm_cost_M2]
    + list(costs_M2)
    + [L2_norm_cost_X]
    + list(costs_X)
    + [L2_norm_cost_K1]
    + list(costs_K1)
    + [L2_norm_cost_K2]
    + list(costs_K2)
    + [L2_norm_cost_B]
    + list(costs_B)
    # + [L2_norm_cost_O]
    # + list(costs_O)
)

# Convert to DataFrame
results = pd.DataFrame([row], columns=columns)

# Check whether Costs.csv already exists
import os

output_file = "Costs_20er_21mixtures_air.csv"

if not os.path.exists(output_file):

    results.to_csv(
        output_file,
        mode="w",
        header=True,
        index=False
    )

else:

    results.to_csv(
        output_file,
        mode="a",
        header=False,
        index=False
    )

print(f"Costs saved for mixture {prefix} in {output_file}")