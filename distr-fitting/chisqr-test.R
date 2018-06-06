library(fitdistrplus)
library(ggplot2)
library(zoo)
reactorData = read.csv("~/financial-projections/data/reactors.csv")


#######################################################
## EXPONENTIAL DISTRIBUTION FIT
# Negative values removed (no shift), outliers retained

bins <- 7

y1 <- reactorData$sescor025[1:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "exp")
z1 <- hist(y1, breaks=seq(0.0, 1.0, length.out=bins), right=TRUE)

breaks_cdf <- pexp(z1$breaks, rate = dist1$estimate)
null.probs <- rollapply(breaks_cdf, 2, function(y1) y1[2] - y1[1])
chisq.test(z1$counts, p=null.probs, rescale.p=TRUE, simulate.p.value = TRUE, B = 10000)

y2 <- reactorData$sescor2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "exp")
z2 <- hist(y2, breaks=seq(0.0, 1.0, length.out=bins), right=FALSE)

breaks_cdf2 <- pexp(z2$breaks, rate = dist2$estimate)
null.probs2 <- rollapply(breaks_cdf2, 2, function(y2) y2[2] - y2[1])
null.probs2
chisq.test(z2$counts, p=null.probs2, rescale.p=TRUE, simulate.p.value = TRUE, B = 10000)
# 
# y3 <- reactorData$sesc5075
# y3 <- subset(y3, y3 > 0)
# dist3 <- fitdist(y3, "exp")
# 
# y4 <- reactorData$sesc7590
# y4 <- subset(y4, y4 > 0)
# dist4 <- fitdist(y4, "exp")
# 
# y5 <- reactorData$sesc90100
# y5 <- subset(y5, y5 > 0)
# dist5 <- fitdist(y5, "exp")
# 
# title <- c('Exponential', 'Neg. values removed', 'Outliers retained', rep('', 2))
# names <- c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%')
# items <- rep(c('Rate'), 5)
# rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
# errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
# shifts <- rep(0, 5)
# 
# df1 <- data.frame(title, names, items, rates, errors, shifts)