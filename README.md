# Επιχειρησιακή Έρευνα

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

## Άλλοι επιλυτές

* [Pyomo](http://www.pyomo.org/)
* [PuLP](https://coin-or.github.io/pulp/#)
* [PyMathProg](http://pymprog.sourceforge.net/)
* [Python-MIP](https://www.python-mip.com/)
* [Google OR-Tools](https://developers.google.com/optimization)
* [SCIP](https://www.scipopt.org/)


## Άλλα χρήσιμα εργαλεία

* [Gusek](http://gusek.sourceforge.net/gusek.html) επίλυση προβλημάτων σε μορφή .lp
  * Παράδειγμα .lp αρχείου [production_problem.lp](./production_problem.lp)

---

**setup python environment με το conda**

```
$ conda create --name cplex_community_env python=3.8
$ conda activate cplex_community_env
```