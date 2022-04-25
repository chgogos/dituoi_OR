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


**Παραδείγματα κώδικα**

* [simple_lp.py](./simple_lp.py)
* [production_problem.py](./production_problem.py)

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
    * [Ανάλυση ευαισθησίας](./production_problem_SA.txt)

---

**setup python environment με το conda**

```
$ conda create --name cplex_community_env python=3.8
$ conda activate cplex_community_env
```

---

**docker**

**Α' τρόπος**
Από τον φάκελο docker_example1 που περιέχει το αρχείο [Dockerfile](./docker_example1/Dockerfile)

Δημιουργία του image από το Dockerfile και ονομασία του ως python3.10:operes
```
$ docker build -t python3.10:operes .
```

Εκτέλεση του κώδικα του simple_lp.py
```
$ docker run --rm -it -w /usr/src/app python3.10:operes python simple_lp.py
```

Διαγραφή του image python3.10:operes
```
docker image rm python3.10:operes
```

**Β' τρόπος**
Εναλλακτικά με το προηγούμενο, αντιγραφή των περιεχομένων του τρέχοντος καταλόγου του host στο /usr/src/app του container
```
$ docker run --rm -it -v my_volume:/usr/local/lib python:3.10 bash
$ pip install cplex
$ pip install docplex
$ exit

για Windows
$ docker run --rm -it -v my_volume:/usr/local/lib -v %cd%:/usr/src/app -w /usr/src/app python:3.10 python simple_lp.py
ή για linux
$ docker run --rm -it -v my_volume:/usr/local/lib -v ${pwd}:/usr/src/app -w /usr/src/app python:3.10 python simple_lp.py
```