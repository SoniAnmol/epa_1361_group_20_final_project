# EPA-simmodel
This file contains the structure of this repository and some general instructions for performing the analysis. This folder is cloned from the repository [epa1361_open](https://github.com/quaquel/epa1361_open) created for Model Based Decision Making (EPA 1361). Some additional folders are added in the repository by group 20.

# Instructions for evaluator
- Kindly refer the `notebooks` directory to check the notebooks used for analysis at a glance
- Jupyter notebooks in `.ipynb` format are present in the root directore (FINAL ASSIGNMENT)
- The summary of analysis and methodology followed is present in the `presentations` directory
- All the assumptions and reasoning behind the analytical chooices are documented in `EPA1361_Report_Group_20.pdf` in the `Report` folder
- All the files can also be directly downloaded from the `final_assignment_grooup_20.zip folder`

# Following is the structure of the repository

## **FINAL ASSIGNMENT**<br/>
*(This directory contains the zip folder and all the python scripts and notebooks to be run for analysis and running the model)*<br/>

### **analysis_figures**<br/>
 *(This directory contains all the figures generated during the analysis. All the figures are stored in respective directories.)*<br/>
 > - directed search<br/>
 > - general<br/>
 > - mordm<br/>
 > - open_exoloration<br/>
 > - salib_lever<br/>
 > - salib_uncertainities<br/>



### **data**<br/>
*(This is a predefined directory conaining important data for the functioning of the model.)*<br/>

### **data_processed**<br/>
(All the data generated during the analysis is stored in this directory.<br/>
Files generated during the analysis are stored in respective sub-directory indicating different stages of the analysis.)<br/>
> - mordm<br/>
> - open_exploration<br/>
> - sensitivity_analysis<br/>

### **notebooks** <br/>
 *(This directory stores all the notebooks used for the analysis in the `.html` format for quick overview and evaluation.)*<br/>
> - `1. group_20_problem_formulations.html` <br/>
 *(This notebook contains the problem formulation used for the analysis)*<br/>
> - `2. group_20_open_exploration.html` <br/>
  *(This notebook contains the open exploration and no_policy runs performed for understanding the model)*<br/>
> - `3. group_20_sensitivity_analysis.html` <br/>
  *(This notebook contains sensitivity analysis for idnetifying the key uncertainities and policy levers)*<br/>
> - `4. group_20_directed_search.html`<br/>
 *(This notebook contains directed search for sampling optimized policies with a reference scenario)*<br/>
> - `5. group_20_mordm.html`<br/>
*(This notebook contains robustness analysis for candidate solution and evaluates its performance under uncertainity)*<br/>

### **presentations**<br/>
 *(This directory contains the presentation about model and a summary of the results and analysis performed by group_20)*<br/>


# Contributors (Group 20)
>- Anmol Soni (5290228)
>-Elie Azeufack (5231000)
>- Lekha Nambiar (5200512)
>- Marco Peretto (5366240)
>- Roel Degens (5432529)
>- Ziad Matar (4670981)