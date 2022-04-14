# first import the Model class from docplex.mp
from docplex.mp.model import Model

# create one model instance, with a name
m = Model(name='telephone_production', log_output=True)

# by default, all variables in Docplex have a lower bound of 0 and infinite upper bound
desk = m.continuous_var(name='desk')
cell = m.continuous_var(name='cell')

# write constraints
# constraint #1: desk production is greater than 100
m.add_constraint(desk >= 100)

# constraint #2: cell production is greater than 100
m.add_constraint(cell >= 100)

# constraint #3: assembly time limit
ct_assembly = m.add_constraint( 0.2 * desk + 0.4 * cell <= 400)

# constraint #4: painting time limit
ct_painting = m.add_constraint( 0.5 * desk + 0.4 * cell <= 490)

m.maximize(12 * desk + 20 * cell)

m.print_information()

s = m.solve()
m.print_solution()

# reduced costs
print('* desk variable has reduced cost: {0}'.format(desk.reduced_cost))
print('* cell variable has reduced cost: {0}'.format(cell.reduced_cost))

# slack value for assembly constraint
print('* slack value for assembly time constraint is: {0}'.format(ct_assembly.slack_value))
# slack value for painting time constraint
print('* slack value for painting time constraint is: {0}'.format(ct_painting.slack_value))

# dual value for assembly constraint
print('* dual value for assembly time constraint is: {0}'.format(ct_assembly.dual_value))
# dual value for painting time constraint
print('* dual value for painting time constraint is: {0}'.format(ct_painting.dual_value))

