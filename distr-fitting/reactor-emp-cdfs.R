library(fitdistrplus)
library(ggplot2)
library(ggfortify)

reactorData = read.csv("~/financial-projections/data/reactors.csv")
x1 <- reactorData$sesc025
plot(sort(x1), main="Schedule Escalation Empirical CDF, 0-25%")
x2 <- reactorData$sesc2550
plot(sort(x2), main="Schedule Escalation Empirical CDF, 25-50%")
x3 <- reactorData$sesc5075
plot(sort(x3), main="Schedule Escalation Empirical CDF, 50-75%")
x4 <- reactorData$sesc7590
plot(sort(x4), main="Schedule Escalation Empirical CDF, 75-90%")
x5 <- reactorData$sesc90100
plot(sort(x5), main="Schedule Escalation Empirical CDF, 90-100%")
hist(x1, right=FALSE, main="Schedule Escalation, 0-25%")
hist(x2, right=FALSE, main="Schedule Escalation, 25-50%")
hist(x3, right=FALSE, main="Schedule Escalation, 50-75%")
hist(x4, right=FALSE, main="Schedule Escalation, 75-90%")
hist(x5, right=FALSE, main="Schedule Escalation, 90-100%")