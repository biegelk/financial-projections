# Define time horizon for projections (years)
time_horizon = 10
current_year = 2018
hist = 6

# Model behavioral booleans
rand_esc = 0 # Activate probabilistic (simple uniform) project delay?
rand_delay = 1 # Activate probabilistic (uniform) project delay?
cap_interest = 1 # Capitalize interest during construction?
amin = 0 # Minimum value of alpha examined
amax = 2 # Maximum value of alpha examined


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
# Using: Gamma, VS, OR
cgamma_params = [2.3595943, 1/1.6161089]
cgamma_deshift = 0.001
# Using: Norm, OR
cnorm_params = [1.4588795, 0.77041806]

# Schedule escalation parameters
# Using: Gamma, VS, OK
sgamma_params = [2.0929615, 1/1.983719]
sgamma_deshift = 0.05199
# sgamma_params = [[2.328576, 1/4.145274], [0.3964225, 1/2.554244], [1.8652066, 1/9.3310657], [0.6060982, 1/6.81993987], [1.4430346, 1/7.0285575]]
# sgamma_deshift = [0.309049, 0.001, 0.0683719, 0.001, 0.0494768]

# Growth rates
rev_growth  = 0.016  # % change YOY
ppe_growth  = 0.03   # % change YOY

# Secondary ratios
misc_om_ratio = 0.256  # to revenues
fuel_ratio    = 0.252  # to revenues
pp_ratio      = 0.042  # to revenues
misc_taxes_ratio = 0.128 # to EBITDA
payout_ratio = 0.5 # Payout ratio
