library(fitdistrplus)
library(ggplot2)
reactorData = read.csv("~/financial-projections/data/reactors.csv")


###################################
## EXPONENTIAL DISTRIBUTION FIT
# Values shifted, outliers retained

y1 <- reactorData$sesc025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "exp")
#plot(dist1)

y2 <- reactorData$sesc2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "exp")
#plot(dist2)

y3 <- reactorData$sesc5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "exp")
#plot(dist3)

y4 <- reactorData$sesc7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "exp")
#plot(dist4)

y5 <- reactorData$sesc90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "exp")
#plot(dist5)

title <- c('Exponential', 'Values shifted', 'Outliers retained', rep('', 2))
names <- c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%')
items <- rep(c('Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- c(y1shift, y2shift, y3shift, y4shift, y5shift)
#shifts <- rep('', 5)

df3 <- data.frame(title, names, items, rates, errors, shifts)


###################################
## GAMMA DISTRIBUTION FIT
# Values shifted, outliers retained

y1 <- reactorData$sesc025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "gamma")
plot(dist1)

y2 <- reactorData$sesc2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "gamma")
#plot(dist2)

y3 <- reactorData$sesc5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "gamma")
#plot(dist3)

y4 <- reactorData$sesc7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "gamma")
#plot(dist4)

y5 <- reactorData$sesc90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "gamma")
#plot(dist5)

title <- c('Gamma', 'Values shifted', 'Outliers retained', rep('', 7))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Shape', 'Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(c(y1shift, y2shift, y3shift, y4shift, y5shift), each=2)

df7 <- data.frame(title, names, items, rates, errors, shifts)


##########################
## NORMAL DISTRIBUTION FIT
# Outliers removed

y1 <- reactorData$sescor025[0:75]
y1 <- y1[!is.na(y1)]
dist1 <- fitdist(y1, "norm", start=NULL)
#plot(dist1)

y2 <- reactorData$sescor2550[0:75]
y2 <- y2[!is.na(y2)]
dist2 <- fitdist(y2, "norm", start=NULL)
#plot(dist2)

y3 <- reactorData$sescor5075[0:75]
y3 <- y3[!is.na(y3)]
dist3 <- fitdist(y3, "norm", start=NULL)
#plot(dist3)

y4 <- reactorData$sescor7590[0:75]
y4 <- y4[!is.na(y4)]
dist4 <- fitdist(y4, "norm", start=NULL)
#plot(dist4)

y5 <- reactorData$sescor90100[0:75]
y5 <- y5[!is.na(y5)]
dist5 <- fitdist(y5, "norm", start=NULL)
#plot(dist5)

title <- c('Normal', 'Outliers removed', rep('', 8))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Mean', 'SD'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 10)

df10 <- data.frame(title, names, items, rates, errors, shifts)

write.csv(rbind(df3, df7, df10), file='distfit-outputs-master.csv', row.names=FALSE)