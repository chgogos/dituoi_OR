# Επιχειρησιακή Έρευνα

* [Εργασία εαρινό 2021-2022](./2021-2022e_project.pdf)
* Δεδομένα 
  * [registrations_22.xlsx](./registrations_22.xlsx)
  * [registrations_100.xlsx](./registrations_100.xlsx)
  * [registrations_200.xlsx](./registrations_200.xlsx)

## MOOC

* [cognitiveclass.ai](https://courses.cognitiveclass.ai/)
  * [Mathematical Optimization for Business Problems](https://courses.cognitiveclass.ai/courses/course-v1:IBMDeveloperSkillsNetwork+CP0101EN+v1/course/)

## Επιλυτής IBM ILOG CPLEX

**εγκατάσταση modules**

```
$ pip install cplex
$ pip install docplex
```

* [IBM® Decision Optimization CPLEX® Modeling for Python](http://ibmdecisionoptimization.github.io/docplex-doc/)
* [Tutorials](./IBM_DO_Tutorials/README.md)
* [Coding perspective - Mathematical Optimization in Python with CPLEX (YouTube)](https://www.youtube.com/playlist?list=PLaxOs-8sLebuytu-pPSM4mtsR5VVlFtyW)


**Παραδείγματα κώδικα**

* [simple_lp.py](./simple_lp.py)
* [production_problem.py](./production_problem.py)
* [transportation_problem.py](./transportation_problem.py)

## Άλλοι επιλυτές και σχετικά λογισμικά

* [Gurobi](https://www.gurobi.com/)
* [XPress](https://www.fico.com/en/products/fico-xpress-optimization)
* [SCIP](https://www.scipopt.org/)
* [HiGHS](https://www.maths.ed.ac.uk/hall/HiGHS/)
* [octeract](https://octeract.com/)
* [Google OR-Tools](https://developers.google.com/optimization)
* [Pyomo](http://www.pyomo.org/)
* [PuLP](https://coin-or.github.io/pulp/#)
* [PyMathProg](http://pymprog.sourceforge.net/)
* [Python-MIP](https://www.python-mip.com/)

## Άλλα χρήσιμα εργαλεία

* [Gusek](http://gusek.sourceforge.net/gusek.html) επίλυση προβλημάτων σε μορφή .lp
  * Παράδειγμα .lp αρχείου [production_problem.lp](./production_problem.lp)
    * [Ανάλυση ευαισθησίας](./production_problem_SA.txt)

## Διάφορα

* [OR in practice - working group](https://www.euro-online.org/websites/or-in-practice/)
* [Subject To podcast](https://www.youtube.com/channel/UCKMY2i-ROJjOXCxePFewnkg/featured)
* [Scheduling Seminar](https://schedulingseminar.com/)

---

**Setup python environment με το conda**

```
$ conda create --name cplex_community_env python=3.8
$ conda activate cplex_community_env
```

---

[Εκτέλεση παραδείγματος Γραμμικού Προγραμματισμού με docker](./docker.md)