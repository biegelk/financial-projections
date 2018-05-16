# Define time horizon for projections (years)
time_horizon = 10
current_year = 2018
hist = 6

# Firm financial constants
tax_rate = 0.335
wacd = 0.05 # historical weighted average cost of debt
mcd = 0.07  # marginal cost of debt for a nuclear project

## Project constants
total_cost = 6000 # $M, cost estimate at 0% completion
init_schedule = 5 # construction schedule, years
capacity = 2200000 # kW
cf = 0.9 # capacity factor
d = (9.25+4.)/2./100. # wacc/discount rate
term = 30 # years
power_price = 0.06 # $/kWh
life = 40 # years

# Cost escalation parameters
# Completion milestones
completion_steps = [0, .25, .5, .75, .9, 1]
# Gamma-distribution parameters of empirical escalation data
cgamma_params = [[1.236, 1/2.942], [19.893, 1/21.711], [50.734, 1/24.857], [17.499, 1/17.438]]
cgamma_fix = [0, .73, 1.54, 0.90, 0]

# Growth rates
rev_growth  = 0.016  # % change YOY
fuel_growth = 0.252  # % of revenues
pp_growth   = 0.042  # % of revenues
ppe_growth  = 0.03   # % change YOY

# Secondary ratios
misc_om_ratio = 0.256  # to revenues
fuel_ratio    = 0.252  # to revenues
pp_ratio      = 0.042  # to revenues
misc_taxes_ratio = 0.128 # to EBITDA
