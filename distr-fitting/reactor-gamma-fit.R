# library(fitdistrplus)
# library(ggplot2)
# library(ggfortify)

reactorData = read.csv("~/financial-projections/data/reactors.csv")

y1 <- reactorData$sesc025[0:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "gamma")
plot(dist1)

y2 <- reactorData$sescor2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "gamma")
plot(dist2)

y3 <- reactorData$sescor5075
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "gamma")
plot(dist3)

y4 <- reactorData$sescor7590
y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "gamma")
plot(dist4)

y5 <- reactorData$sescor90100
y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "gamma")
plot(dist5)
# 
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
#
rates
errors

#t <- seq(0, 1, length.out=1000)