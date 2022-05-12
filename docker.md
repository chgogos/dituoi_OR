# docker

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