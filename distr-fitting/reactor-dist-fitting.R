library(fitdistrplus)
reactorData = read.csv("~/financial-projections/data/reactors.csv")

###
## EXPONENTIAL DISTRIBUTION FIT
# Negative values removed (no shift), outliers retained

y1 <- reactorData$sesc025[1:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "exp")

y2 <- reactorData$sesc2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "exp")

y3 <- reactorData$sesc5075
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "exp")

y4 <- reactorData$sesc7590
y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "exp")

y5 <- reactorData$sesc90100
y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "exp")

rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)

