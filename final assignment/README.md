
# README Advanced Simulation

This README file was generated on: 18-03-2024

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


### General information:


### Technologies used

The code is written and tested for Python 3.11, The specific packages used are 
given in the requirement.txt file. To use the code an environment for Python 
should be created and the packages stated in the requirements.txt should be installed. One of 
the main packages that was used is the ema_workbench with version 3.0.0.


### File structuring
The folder has a specific structure. Underneath an overview is give of this structure.
The .py files that are include belong to the used model and will not be described individually.

that is as follows:

    EPA141A-G4/
        ├── data/
        ├── Archive/
        ├── report/
        ├── Open_Exploration_Scen.ipynb
        ├── Open_Exploration_Pol.ipynb
        ├── PRIM.ipynb
        ├── DS.ipynb
        ├── Convergence.ipynb
        └── .py files

### Purpose files and folders

Various Python files are included. Each has its purpose which will be briefly explained in the table underneath.

| File/folder                 | Purpose                                                                                                  |
|:----------------------------|----------------------------------------------------------------------------------------------------------|
| data                        | Contains the data used and created wit the open exploration for policies and scenarios                   |
| Archive                     | Stores the data files from the directed search optimizer                                                 |
| report                      | Stores the report for which the analyses was done                                                        |
| Open_Exploration_Scen.ipynb | Contains the code for feature scoring and SOBOL to identify interesting scenarios                        |
| Open_Exploration_Pol.ipynb  | Contains the code for feature scoring and SOBOL to identify interesting policies                         |
| PRIM.ipynb                  | Uses result open exploration for scenarios to define an interesting parameter space                      |
| DS.ipynb                    | Searches with reference scenarios of PRIM for effective policy combinations                              |
| Convergence.ipynb           | Calculates the convergence metrics of the optimisation done on the DelftsBlauw computer and the DS.ipynb |
| .py files                   | Files that make up the model.                                                                            |

### Usage


### Assistance during project

Instructor:

-   Prof.dr.ir. J.H. Kwakkel - J.H.Kwakkel@tudelft.nl

### Contact

All questions about the code, project, or anything else can be sent to the following email:

R.Kooijman-1@student.tudelft.nl