# library(fitdistrplus)
# library(ggplot2)
# library(ggfortify)

reactorData = read.csv("~/financial-projections/data/reactors.csv")

y1 <- reactorData$sesc025[0:75]
#y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "norm", start=NULL)
plot(dist1)

y2 <- reactorData$sescor2550[0:75]
#y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "norm", start=NULL)
plot(dist2)

y3 <- reactorData$sescor5075[0:75]
#y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "norm", start=NULL)
plot(dist3)

y4 <- reactorData$sescor7590[0:75]
#y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "norm", start=NULL)
plot(dist4)

y5 <- reactorData$sescor90100[0:75]
#y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "norm", start=NULL)
plot(dist5)
# 
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
#
rates
errors

#t <- seq(0, 1, length.out=1000)