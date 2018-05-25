# Define time horizon for projections (years)
time_horizon = 10
current_year = 2018
hist = 6

# Model behavioral booleans
rand_esc = 0 # Activate probabilistic (simple uniform) project delay?
rand_delay = 1 # Activate probabilistic (uniform) project delay?
cap_interest = 1 # Capitalize interest during construction?

# Firm financial constants
tax_rate = 0.335
wacd = 0.05 # historical weighted average cost of debt
rroe = 0.12 # required return on equity
mcd = 0.07  # marginal cost of debt for a nuclear project
min_dps = 2.3

## Project constants
total_cost = 6000 # $M, cost estimate at 0% completion
init_schedule = 5 # construction schedule, years
capacity = 2200000 # kW
cf = 0.9 # capacity factor
d = (rroe + wacd)/2. # wacc/discount rate
term = 30 # years
power_price = 0.06 # $/kWh
life = 40 # years
econ_life = 25 # years; economic useful life for straight-line depreciation

# Cost escalation parameters
# Completion milestones
completion_steps = [0, .25, .5, .75, .9, 1]
# Gamma-distribution parameters of empirical escalation data
cgamma_params = [[1.236, 1/2.942], [19.893, 1/21.711], [50.734, 1/24.857], [17.499, 1/17.438]]
cgamma_fix = [0, .73, 1.54, 0.90, 0]

sched_esc = [[0.063, 0.189, 0.379], [0.048, 0.116, 0.217], [0.049, 0.099, 00.174], [0.038, 0.066, 0.108], [0.048, 0.117, 0.220]]
#sgamma_params = [[2.422, 1/2.387], [4.219, 1/6.031], [21.900, 1/54.084], [3.555, 1/4.405], [49.758, 1/38.479]]
#sgamma_params = [[2.422, .4], [4.219, .15], [4.00, .02], [3.555, .2], [4.758, .03]]
sgamma_params = [[5, 10], [5,10], [5,10], [5,10], [5,10]]
sgamma_fix = [1.732, 1.06, .72, .356, 1.131]

# Growth rates
rev_growth  = 0.016  # % change YOY
fuel_growth = 0.252  # % of revenues
pp_growth   = 0.042  # % of revenues
ppe_growth  = 0.03   # % change YOY
dps_growth  = 0.03   # % change YOY

# Secondary ratios
misc_om_ratio = 0.256  # to revenues
fuel_ratio    = 0.252  # to revenues
pp_ratio      = 0.042  # to revenues
misc_taxes_ratio = 0.128 # to EBITDA
