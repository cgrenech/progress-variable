import csv
import numpy as np
import matplotlib.pyplot as plt
import os
import pandas as pd
from PCAfold import preprocess
from PCAfold import analysis
from PCAfold import __version__ as PCAfold_version
import pickle
import sys
import matplotlib.cm as cm
import cmcrameri.cm as cmc
cmap = cmc.lajolla

prefix = 'M2'

data_state_space = pd.read_csv("FPF-" + prefix +"-state-space.csv", header=None)
data_state_sources = pd.read_csv("FPF-" + prefix +"-state-space-sources.csv", header=None)
data_mf = pd.read_csv("FPF-" + prefix +"-mixture-fraction.csv", header=None)


file = open("FPF-" + prefix +"-state-space-names.csv", "r")
data_names = list(csv.reader(file, delimiter=","))
file.close()

file = open("FPF-" + prefix +"-state-space-sources-names.csv", "r")
data_names_sources = list(csv.reader(file, delimiter=","))
file.close()


### Definition of the progress variable ###
# Pierce & Moin 
species_list_PM = ['H2O', 'CO2']
weight_list_PM = [1.0, 1.0]

# Ihme & Pitsch
species_list_IP = ['H2O', 'CO2', 'CO', 'H2']
weight_list_IP = [1.0, 1.0, 1.0, 1.0]

# Fiorina et al.
species_list_F = ['CO2', 'CO']
weight_list_F = [1.0, 1.0]

# Wang
species_list_W = ['H2O']
weight_list_W = [1.0]

# Mazotta1
species_list_M1 = ['NO', 'N2', 'H2O', 'H2']
weight_list_M1 = [1.0, 1.0, 1.0, -1.0]

# Mazotta2
species_list_M2 = ['N2', 'H2O', 'HO2', 'H2']
weight_list_M2 = [1.0, 1.0, 1.0, -1.0]

# Xia 
species_list_X = ['H2O', 'HO2']
weight_list_X = [1.0, 10.0]

# Kai1
species_list_K1 = ['N2', 'H2O', 'H2']
weight_list_K1 = [1.0, 1.0, 1.0]

# Kai2
species_list_K2 = ['H2O', 'H2']
weight_list_K2 = [1.0, 1.0]

# Baker
species_list_B = ['H2O', 'N2', 'NO']
weight_list_B = [1/18.015 , 1/28.014, 1/30.01]

# Oijen
species_list_O = ['CO2', 'H2O', 'H2']
weight_list_O = [1/44.01, 1/18.015, 1/2.016]

mf = data_mf.iloc[:,0]
T = data_state_space.iloc[:,0]

# ##############################    CALCULATION     #############################################
# ###############################################################################################
# Calcul of the PV_PM
PV_PM = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_PM) : # iterate species_list
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_PM = PV_PM + selected_column*weight_list_PM[index_species]

# Calcul of the PV source term PM
PV_ST_PM = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_PM) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_PM = PV_ST_PM + selected_column*weight_list_PM[index_species]


# ###############################################################################################
# Calcul of the PV_IP
PV_IP = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_IP):
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_IP = PV_IP + selected_column*weight_list_IP[index_species]

# Calcul of the PV source term IP
PV_ST_IP = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_IP) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_IP = PV_ST_IP + selected_column*weight_list_IP[index_species]


###############################################################################################
# Calcul of the PV_F
PV_F = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_F):
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_F = PV_F + selected_column*weight_list_F[index_species]

# Calcul of the PV source term F
PV_ST_F = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_F) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_F = PV_ST_F + selected_column*weight_list_F[index_species]

###############################################################################################
# Calcul of the PV_W
PV_W = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_W) : # iterate species_list
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_W = PV_W + selected_column*weight_list_W[index_species]

# Calcul of the PV source term W
PV_ST_W = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_W) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_W = PV_ST_W + selected_column*weight_list_W[index_species]
###############################################################################################
# Calcul of the PV_M1
PV_M1 = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_M1) : # iterate species_list
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_M1 = PV_M1 + selected_column*weight_list_M1[index_species]

# Calcul of the PV source term M1
PV_ST_M1 = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_M1) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_M1 = PV_ST_M1 + selected_column*weight_list_M1[index_species]

###############################################################################################
# Calcul of the PV_M2
PV_M2 = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_M2) : # iterate species_list
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_M2 = PV_M2 + selected_column*weight_list_M2[index_species]

# Calcul of the PV source term M2
PV_ST_M2 = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_M2) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_M2 = PV_ST_M2 + selected_column*weight_list_M2[index_species]

###############################################################################################
# Calcul of the PV_X
PV_X = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_X) : # iterate species_list
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_X = PV_X + selected_column*weight_list_X[index_species]

# Calcul of the PV source term X
PV_ST_X = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_X) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_X = PV_ST_X + selected_column*weight_list_X[index_species]

###############################################################################################
# Calcul of the PV_K1
PV_K1 = pd.Series(0.0, index = data_state_space.index)
for index_species, species in enumerate(species_list_K1) : # iterate species_list
        for index, value in enumerate(data_names):
            if species != value[0] :
                pass
            else : 
                selected_column = data_state_space.iloc[:,index]
                PV_K1 = PV_K1 + selected_column*weight_list_K1[index_species]

# Calcul of the PV source term K1
PV_ST_K1 = pd.Series(0.0, index = data_state_sources.index)
for index_species, species in enumerate(species_list_K1) :
    for index, value in enumerate(data_names_sources):
                if species != value[0] :
                    pass
                else :
                    selected_column = data_state_sources.iloc[:,index]
                    PV_ST_K1 = PV_ST_K1 + selected_column*weight_list_K1[index_species]

###############################################################################################
# Calcul of the PV_K2 
PV_K2 = pd.Series(0.0, index = data_state_space.index) 
for index_species, species in enumerate(species_list_K2) : # iterate species_list 
        for index, value in enumerate(data_names): 
            if species != value[0] : 
                pass 
            else :  
                selected_column = data_state_space.iloc[:,index] 
                PV_K2 = PV_K2 + selected_column*weight_list_K2[index_species] 
 
# Calcul of the PV source term K2 
PV_ST_K2 = pd.Series(0.0, index = data_state_sources.index) 
for index_species, species in enumerate(species_list_K2) : 
    for index, value in enumerate(data_names_sources): 
                if species != value[0] : 
                    pass 
                else : 
                    selected_column = data_state_sources.iloc[:,index] 
                    PV_ST_K2 = PV_ST_K2 + selected_column*weight_list_K2[index_species] 
 
###############################################################################################
# Calcul of the PV_B 
PV_B = pd.Series(0.0, index = data_state_space.index) 
for index_species, species in enumerate(species_list_B) : # iterate species_list 
        for index, value in enumerate(data_names): 
            if species != value[0] : 
                pass 
            else :  
                selected_column = data_state_space.iloc[:,index] 
                PV_B = PV_B + selected_column*weight_list_B[index_species] 
 
# Calcul of the PV source term B 
PV_ST_B = pd.Series(0.0, index = data_state_sources.index) 
for index_species, species in enumerate(species_list_B) : 
    for index, value in enumerate(data_names_sources): 
                if species != value[0] : 
                    pass 
                else : 
                    selected_column = data_state_sources.iloc[:,index] 
                    PV_ST_B = PV_ST_B + selected_column*weight_list_B[index_species] 
 
###############################################################################################
# Calcul of the PV_O 
PV_O = pd.Series(0.0, index = data_state_space.index) 
for index_species, species in enumerate(species_list_O) : # iterate species_list 
        for index, value in enumerate(data_names): 
            if species != value[0] : 
                pass 
            else :  
                selected_column = data_state_space.iloc[:,index] 
                PV_O = PV_O + selected_column*weight_list_O[index_species] 
 
# Calcul of the PV source term O 
PV_ST_O = pd.Series(0.0, index = data_state_sources.index) 
for index_species, species in enumerate(species_list_O) : 
    for index, value in enumerate(data_names_sources): 
                if species != value[0] : 
                    pass 
                else : 
                    selected_column = data_state_sources.iloc[:,index] 
                    PV_ST_O = PV_ST_O + selected_column*weight_list_O[index_species] 
 
###############################################################################################
#################################

mf = mf.to_numpy().reshape(-1,1)
VD_target_variables_names = ['T','rho','mu','lambda','c_p','H2','H','O','OH', 'H2O', 'NH3', 'NH2', 'NO2', 'NH', 'NO', 'N2O', 'CO2', 'CO', 'CH4', 'PV_ST']
position_VD_target_variables = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 15, 17, 20, 23, 24, 25, 26]
VD_target_variables = data_state_space.iloc[:, position_VD_target_variables].to_numpy()
bandwidth_values = np.logspace(-6,2,200)

# Hyper-parameters of the cost function
power = 4
vertical_shift = 1
penalty_function = 'log-sigma-over-peak'

fontsize = 20
fontsize_axes = 16

##############################  Pierce & Moin ###################################################################
depvars_PM = np.column_stack((VD_target_variables,PV_ST_PM))
PV_PM = PV_PM.to_numpy().reshape(-1,1)
indepvars_PM = np.hstack((mf, PV_PM))


VarianceData_PM = analysis.compute_normalized_variance(
    indepvars_PM,
    depvars_PM,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_PM, open('VarianceData_'+prefix+'_PM.pkl', "wb"))



################################## Ihme & Pitsch ###############################################################
depvars_IP = np.column_stack((VD_target_variables,PV_ST_IP))
PV_IP = PV_IP.to_numpy().reshape(-1,1)
indepvars_IP = np.hstack((mf, PV_IP))


VarianceData_IP = analysis.compute_normalized_variance(
    indepvars_IP,
    depvars_IP,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)


pickle.dump(VarianceData_IP, open('VarianceData_'+prefix+'_IP.pkl', "wb"))


##################################  Fiorina & al. ###############################################################
depvars_F = np.column_stack((VD_target_variables,PV_ST_F))
PV_F = PV_F.to_numpy().reshape(-1,1)
indepvars_F = np.hstack((mf, PV_F))

VarianceData_F = analysis.compute_normalized_variance(
    indepvars_F,
    depvars_F,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_F, open('VarianceData_'+prefix+'_F.pkl', "wb"))

##############################  W  ###################################################################
depvars_W = np.column_stack((VD_target_variables,PV_ST_W))
PV_W = PV_W.to_numpy().reshape(-1,1)
indepvars_W = np.hstack((mf, PV_W))


VarianceData_W = analysis.compute_normalized_variance(
    indepvars_W,
    depvars_W,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_W, open('VarianceData_'+prefix+'_W.pkl', "wb"))


##############################  M1  ###################################################################
depvars_M1 = np.column_stack((VD_target_variables,PV_ST_M1))
PV_M1 = PV_M1.to_numpy().reshape(-1,1)
indepvars_M1 = np.hstack((mf, PV_M1))


VarianceData_M1 = analysis.compute_normalized_variance(
    indepvars_M1,
    depvars_M1,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_M1, open('VarianceData_'+prefix+'_M1.pkl', "wb"))


##############################  M2  ###################################################################
depvars_M2 = np.column_stack((VD_target_variables,PV_ST_M2))
PV_M2 = PV_M2.to_numpy().reshape(-1,1)
indepvars_M2 = np.hstack((mf, PV_M2))


VarianceData_M2 = analysis.compute_normalized_variance(
    indepvars_M2,
    depvars_M2,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_M2, open('VarianceData_'+prefix+'_M2.pkl', "wb"))


##############################  X  ###################################################################
depvars_X = np.column_stack((VD_target_variables,PV_ST_X))
PV_X = PV_X.to_numpy().reshape(-1,1)
indepvars_X = np.hstack((mf, PV_X))


VarianceData_X = analysis.compute_normalized_variance(
    indepvars_X,
    depvars_X,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_X, open('VarianceData_'+prefix+'_X.pkl', "wb"))


##############################  K1  ###################################################################
depvars_K1 = np.column_stack((VD_target_variables,PV_ST_K1))
PV_K1 = PV_K1.to_numpy().reshape(-1,1)
indepvars_K1 = np.hstack((mf, PV_K1))


VarianceData_K1 = analysis.compute_normalized_variance(
    indepvars_K1,
    depvars_K1,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_K1, open('VarianceData_'+prefix+'_K1.pkl', "wb"))


##############################  K2  ###################################################################
depvars_K2 = np.column_stack((VD_target_variables,PV_ST_K2))
PV_K2 = PV_K2.to_numpy().reshape(-1,1)
indepvars_K2 = np.hstack((mf, PV_K2))


VarianceData_K2 = analysis.compute_normalized_variance(
    indepvars_K2,
    depvars_K2,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_K2, open('VarianceData_'+prefix+'_K2.pkl', "wb"))


##############################  B  ###################################################################
depvars_B = np.column_stack((VD_target_variables,PV_ST_B))
PV_B = PV_B.to_numpy().reshape(-1,1)
indepvars_B = np.hstack((mf, PV_B))


VarianceData_B = analysis.compute_normalized_variance(
    indepvars_B,
    depvars_B,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_B, open('VarianceData_'+prefix+'_B.pkl', "wb"))


##############################  O  ###################################################################
depvars_O = np.column_stack((VD_target_variables,PV_ST_O))
PV_O = PV_O.to_numpy().reshape(-1,1)
indepvars_O = np.hstack((mf, PV_O))


VarianceData_O = analysis.compute_normalized_variance(
    indepvars_O,
    depvars_O,
    depvar_names=VD_target_variables_names,
    scale_unit_box=True,
    bandwidth_values=bandwidth_values
)

pickle.dump(VarianceData_O, open('VarianceData_'+prefix+'_O.pkl', "wb"))

##===========================================================================================##
# Plot PV vs mixture fraction with color bar temperature
plt.figure()
scat = plt.scatter(mf, PV_PM, c=T, s=2)
plt.xlabel('Mixture fraction $f$')
plt.ylabel('Progress Variable')
plt.title('Progress Variable PM')
cbar = plt.colorbar(scat, aspect=15)
cbar.set_label('Temperature (K)', rotation=90)
plt.show()


# Plot PV vs mixture fraction with color bar PV source term
plt.figure()
scat = plt.scatter(mf, PV_PM, c=PV_ST_PM, s=2)
plt.xlabel('Mixture fraction $f$')
plt.ylabel('Progress Variable')
plt.title('Progress Variable PM')
cbar = plt.colorbar(scat, aspect=15)
cbar.set_label('$\dot{\omega}_{PV}/\\rho$ [$1/s$]', rotation=90)
plt.show()
#######################################################################################
### Contour plot with color PV_ST
mf_1d = np.asarray(mf).ravel()
PV_optimized_1d = np.asarray(PV_PM).ravel()
PV_optimized_source_1d = np.asarray(PV_ST_PM).ravel()

figure = plt.figure(figsize=(8, 5))
ax = figure.add_subplot(111)

contour = ax.tricontourf(mf_1d,PV_optimized_1d,PV_optimized_source_1d,levels=30,cmap=cmc.lajolla)
ax.set_xlabel('$f$', fontsize=14)
ax.set_ylabel('Progress Variable PM', fontsize=14)

cbar = figure.colorbar(contour, ax=ax)
cbar.set_label('$\\dot{\\omega}_{PV}/\\rho$ [$1/s$]',rotation=90)

plt.tight_layout()
plt.show()

### Contour plot with color temperature
mf_1d = np.asarray(mf).ravel()
PV_optimized_1d = np.asarray(PV_PM).ravel()
T_1d = np.asarray(T).ravel()

figure = plt.figure(figsize=(8, 5))
ax = figure.add_subplot(111)

contour = ax.tricontourf(mf_1d,PV_optimized_1d,T_1d,levels=30,cmap=cmc.lajolla)
ax.set_xlabel('$f$', fontsize=14)
ax.set_ylabel('PV PM', fontsize=14)

cbar = figure.colorbar(contour, ax=ax)
cbar.set_label('T [K]',rotation=90)

plt.tight_layout()
plt.show()
#######################################################################################