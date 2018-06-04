library(fitdistrplus)
library(ggplot2)
library(ggfortify)

reactorData = read.csv("~/financial-projections/data/reactors.csv")

y1 <- reactorData$sescor025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "exp")
plot(dist1)
dist1

y2 <- reactorData$sescor2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "exp")
plot(dist2)
dist2

y3 <- reactorData$sescor5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "exp")
plot(dist3)
dist3

y4 <- reactorData$sescor7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "exp")
plot(dist4)
dist4

y5 <- reactorData$sescor90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "exp")
plot(dist5)
dist5

rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- c(y1shift, y2shift, y3shift, y4shift, y5shift)

rates
errors
shifts
#t <- seq(0, 1, length.out=1000)