
# README Model-based Decision-making

This README file was generated on: 21-06-2024

### Authors:
Created by: EPA141A - Model-based Decision-Making

|          Name          | Student Number |
|:----------------------:|:---------------|
| Christina Wong A Tjong | 5164370        |
|    Nina Staalduine     | 5400252        |
|    Roelof Kooijman     | 5389437        |
|    Simone Hoogedijk    | 5405084        |

## Institution:

Delft University of Technology : Faculty Technology, Policy and Management.

### Purpose:

The data and the model are created for a project in the course EPA141A - Model-based Decision-Making of the TU Delft. 
The project aims to identify effective policies under uncertainty and in a complex political arena through the use of 
model based decesion making using the ema_workbench.

### Technologies used

The code is written and tested for Python 3.11, The specific packages used are 
given in the requirement.txt file. To use the code, an environment for Python 
should be created and the packages stated in the requirements.txt should be installed. One of 
the main packages that was used is the ema_workbench with version 3.0.0. Dependencies can be installed using the 
included requirements.txt file.


### File structuring
The folder has a specific structure. Underneath, an overview is given of this structure.
The .py files that are included belong to the used model and will not be described individually.

that is as follows:

    EPA141A-G4/
        ├── data/
        ├── DB_files/
        ├── report/
        ├── Results/
        ├── DB_results/
        ├── Open_Exploration_Scen.ipynb
        ├── Open_Exploration_Pol.ipynb
        ├── PRIM.ipynb
        ├── PRIM (MORDM).ipynb
        ├── DS.ipynb
        ├── Convergence.ipynb
        ├── Optimizer_and_convergence.ipynb
        ├── Boxplots.ipynb                                                                                           |
        ├── Robustness.ipynb
        └── .py files

### Purpose files and folders

Various Python files are included. Each has its purpose which will be briefly explained in the table underneath.

| File/folder                     | Purpose                                                                                                                          |
|:--------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| data                            | Contains the data used and created wit the open exploration for policies and scenarios                                           |
| DB_results                      | Contains the archive and pickle files returned by the DelftsBlauw super computer                                           |
| report                          | Stores the report for which the analyses was done                                                                                |
| Results                         | Stores the experiments and outcomes that were produced by PRIM, performing experiments for robustness metrics and the final policies |
| Open_Exploration_Scen.ipynb     | Contains the code for feature scoring and SOBOL to identify interesting scenarios                                                |
| Open_Exploration_Pol.ipynb      | Contains the code for feature scoring and SOBOL to identify interesting policies                                                 |
| PRIM.ipynb                      | Uses result open exploration for scenarios to define an interesting parameter space                                              |
| PRIM (MORDM).ipynb              | Applies scenario discovery to the candidate solutions found in MOEA                                                              |
| DS.ipynb                        | Searches with reference scenarios of PRIM for effective policy combinations                                                      | |
| Convergence.ipynb               | Calculates the convergence metrics of the optimisation done on the DelftsBlauw supercomputer and the DS.ipynb                    |
| Optimizer_and_convergence.ipynb | Calculates the convergence metrics of the optimisation done on the DelftsBlauw computer                                          |
| Boxplots.ipynb                  | Creates boxplots from the results of direct search                                                                               |
| Robustness.ipynb                | Calculates robustness metrics for candidate strategies and selects final strategies                                              |
| .py files                       | Files that make up the model.                                                                                                    |

### Usage
The NSGA-II optimizer is run on the supercomputer of the TU Delft. The python file
and Shell script to execute the optimizer are included in the DB_files folder. To use these they
should be copied into the main folder and executed on the supercomputer.


### Assistance during project

Instructor:

-   Prof.dr.ir. J.H. Kwakkel - J.H.Kwakkel@tudelft.nl

### Contact

All questions about the code, project, or anything else can be sent to the following email:

R.Kooijman-1@student.tudelft.nl