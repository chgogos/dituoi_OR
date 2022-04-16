from docplex.mp.model import Model

model = Model(name="Simple LP")

x = model.continuous_var(name="x", lb=0)
y = model.continuous_var(name="y", lb=0)

c1 = model.add_constraint(x + y >= 8)
c1 = model.add_constraint(2 * x + y >= 10)
c1 = model.add_constraint(x + 4 * y >= 11)

model.set_objective("min", 5 * x + 4 * y)

model.solve()

model.print_solution()

# objective: 34.000
#   x=2.000
#   y=6.000
