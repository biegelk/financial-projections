library(fitdistrplus)
library(ggplot2)
library(ggfortify)

reactorData = read.csv("~/financial-projections/data/reactors.csv")
#x1 <- reactorData$sesc025
#plot(sort(x1), main="Schedule Escalation Empirical CDF, 0-25%")
#x2 <- reactorData$sesc2550
#plot(sort(x2), main="Schedule Escalation Empirical CDF, 25-50%")
#x3 <- reactorData$sesc5075
#plot(sort(x3), main="Schedule Escalation Empirical CDF, 50-75%")
#x4 <- reactorData$sesc7590
#plot(sort(x4), main="Schedule Escalation Empirical CDF, 75-90%")
#x5 <- reactorData$sesc90100
#plot(sort(x5), main="Schedule Escalation Empirical CDF, 90-100%")
#hist(x1, right=FALSE)
#hist(x2, right=FALSE)
#hist(x3, right=FALSE)
#hist(x4, right=FALSE)
#hist(x5, right=FALSE)


reactorData = read.csv("~/financial-projections/data/reactors.csv")
y1 <- reactorData$sesc025
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "exp")
plot(dist1)
dist1

y2 <- reactorData$sesc2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "exp")
plot(dist2)
dist2

y3 <- reactorData$sesc5075
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "exp")
plot(dist3)
dist3

y4 <- reactorData$sesc7590
y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "exp")
plot(dist4)
dist4

y5 <- reactorData$sesc90100
y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "exp")
plot(dist5)
dist5

rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)

rates
errors

#t <- seq(0, 1, length.out=1000)