# # Open exploration 

from __future__ import (unicode_literals, print_function, absolute_import, division)
from ema_workbench import (Model, MultiprocessingEvaluator, Policy, Scenario)
from ema_workbench.em_framework.evaluators import perform_experiments
from ema_workbench.em_framework.samplers import sample_uncertainties
from ema_workbench.util import ema_logging
ema_logging.log_to_stderr(ema_logging.INFO)
import time
from problem_formulation import get_model_for_problem_formulation
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy as sp


# Reading the results file
from ema_workbench import load_results
file_name = 'randompolicy_locations.tar.gz'
results = load_results(file_name)
# Extracting experiment and outcomes from results
experiments, outcomes = results

# ### Scenario Discovery
#
# The approach defines scenarios as a set of plausible future states of the world that represent
# vulnerabilities of proposed policies, that is, cases where a policy fails to meet its performance
# goals. Scenario discovery characterizes such sets by helping users to apply statistical or datamining algorithms to databases of simulation-model-generated results in order to identify
# easy-to-interpret combinations of uncertain model input parameters that are highly predictive
# of these policy-relevant cases (Bryant, 2010)


#uncertainties
experiments

experiments.policy.unique()

# The implementation of prim in the exploratory workbench is however datatype aware, in contrast to the scenario discovery toolkit in R. That is, it will handle categorical data differently than continuous data. Internally, prim uses a numpy structured array for x, and a numpy array for y.

#Dropping categorical variables and other factors not necessary for PRIM
cleaned_experiments = experiments.drop(experiments.columns[[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,-1,-2,-3]], axis = 1)

cleaned_experiments

df_outcomes = pd.DataFrame.from_dict(outcomes)
df_outcomes.head()

# +
#Merging the experiments and outcomes for easier operations
new_result = pd.concat([cleaned_experiments, df_outcomes], axis=1)

#Making an outcomes table A1: 0 deaths, A2: Max(0.00148) - As specified in the policy document after first debate
li = []
li.append(np.where((df_outcomes['A.1_Expected Number of Deaths']==0) & (df_outcomes['A.2_Expected Number of Deaths']<0.00148) &  (df_outcomes['A.3_Expected Number of Deaths']==0)
                  ,1,0))

#Transposing list to a column format
numpy_array = np.array(li)
transpose = numpy_array.T

#y in prim only accepts a Series 1-D array - all this to bring it to that format
outcome_df = pd.DataFrame(transpose)
new_result['outcomes'] = outcome_df
# -

# #### **NOTE: Number of deaths in Zutphen is quite high, so specifying that as 0 gives us no desired outcomes. So above, only conditions are put in A1 and A2 to minimize deaths. 

# +
#PRIM algorithm for scenario discovery
from ema_workbench.analysis import prim

prim_alg = prim.Prim(cleaned_experiments, new_result['outcomes'], threshold=0.8, peel_alpha = 0.1)
box = prim_alg.find_box()
# -

box.inspect_tradeoff()

box.show_pairs_scatter()

box.inspect(4)
box.inspect(4, style='graph')
plt.show()

another_box = prim_alg.find_box()

another_box.inspect_tradeoff()

# ### No other boxes means for minimizing deaths in all 3 regions, the dikes should be increased as shown in the above 1st box figure.

# ### Above desired outcomes gives us a policy of Dike increases of Dikes A1, A2 (in decimeters) in stages 1,2 and 3.
#
# ### Interesting to see that RoomForRiver policies are not featured here at all. 

selected_experiments = experiments.iloc[box.yi]
selected_outcomes = {k:v[box.yi] for k,v in outcomes.items()}

#Desired scenarios
selected_experiments

# ## Sensitivity Analysis

# Sensitivity analysis often focuses on the final values of an outcome at the end of the simulation. However, we can also look at metrics that give us additional information about the behavior of the model over time. We will be using Sobol samping using the SALib library.
#
# In order to properly estimate Sobol scores as well as interaction effects, you require N * (2D+2) scenarios, where D is the number of uncertain parameters, and N is the value for scenarios passed to perform_experiments.

dike_model, planning_steps = get_model_for_problem_formulation(3)

# +
# with MultiprocessingEvaluator(dike_model) as evaluator:
#        exp, outcomes = evaluator.perform_experiments(scenarios=100,
#                                            uncertainty_sampling='sobol')

# with MultiprocessingEvaluator(dike_model) as evaluator:
#     results = evaluator.perform_experiments(scenarios=100,
#                                             policies=40, uncertainty_sampling='sobol')
# -

print(dike_model.uncertainties)

select the best, worst and mid scenario and see which policy works for them. 
