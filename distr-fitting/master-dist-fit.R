library(fitdistrplus)
library(ggplot2)
reactorData = read.csv("~/financial-projections/data/reactors.csv")


#######################################################
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

title <- c('Exponential', 'Neg. values removed', 'Outliers retained', rep('', 2))
names <- c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%')
items <- rep(c('Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 5)

df1 <- data.frame(title, names, items, rates, errors, shifts)


#####################################################
## EXPONENTIAL DISTRIBUTION FIT
# Negative values removed (no shift), outliers removed

y1 <- reactorData$sescor025[1:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "exp")

y2 <- reactorData$sescor2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "exp")

y3 <- reactorData$sescor5075
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "exp")

y4 <- reactorData$sescor7590
y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "exp")

y5 <- reactorData$sescor90100
y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "exp")

title <- c('Exponential', 'Neg. values removed', 'Outliers removed', rep('', 2))
names <- c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%')
items <- rep(c('Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 5)

df2 <- data.frame(title, names, items, rates, errors, shifts)


###################################
## EXPONENTIAL DISTRIBUTION FIT
# Values shifted, outliers retained

y1 <- reactorData$sesc025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "exp")

y2 <- reactorData$sesc2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "exp")

y3 <- reactorData$sesc5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "exp")

y4 <- reactorData$sesc7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "exp")

y5 <- reactorData$sesc90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "exp")

title <- c('Exponential', 'Values shifted', 'Outliers retained', rep('', 2))
names <- c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%')
items <- rep(c('Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- c(y1shift, y2shift, y3shift, y4shift, y5shift)
#shifts <- rep('', 5)

df3 <- data.frame(title, names, items, rates, errors, shifts)


##################################
## EXPONENTIAL DISTRIBUTION FIT
# Values shifted, outliers removed

y1 <- reactorData$sescor025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "exp")

y2 <- reactorData$sescor2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "exp")

y3 <- reactorData$sescor5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "exp")

y4 <- reactorData$sescor7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "exp")

y5 <- reactorData$sescor90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "exp")

title <- c('Exponential', 'Values shifted', 'Outliers removed', rep('', 2))
names <- c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%')
items <- rep(c('Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- c(y1shift, y2shift, y3shift, y4shift, y5shift)

df4 <- data.frame(title, names, items, rates, errors, shifts)


############################################
## GAMMA FIT
# Negative values removed, outliers retained

y1 <- reactorData$sesc025[0:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "gamma")

y2 <- reactorData$sesc2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "gamma")

y3 <- reactorData$sesc5075
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "gamma")

y4 <- reactorData$sesc7590
y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "gamma")

y5 <- reactorData$sesc90100
y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "gamma")

title <- c('Gamma', 'Neg. values removed', 'Outliers retained', rep('', 7))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Shape', 'Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 10)

df5 <- data.frame(title, names, items, rates, errors, shifts)


###########################################
## GAMMA FIT
# Negative values removed, outliers removed

y1 <- reactorData$sescor025[0:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "gamma")

y2 <- reactorData$sescor2550
y2 <- subset(y2, y2 > 0)
dist2 <- fitdist(y2, "gamma")

y3 <- reactorData$sescor5075
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "gamma")

y4 <- reactorData$sescor7590
y4 <- subset(y4, y4 > 0)
dist4 <- fitdist(y4, "gamma")

y5 <- reactorData$sescor90100
y5 <- subset(y5, y5 > 0)
dist5 <- fitdist(y5, "gamma")

title <- c('Gamma', 'Neg. values removed', 'Outliers removed', rep('', 7))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Shape', 'Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 10)

df6 <- data.frame(title, names, items, rates, errors, shifts)


###################################
## GAMMA DISTRIBUTION FIT
# Values shifted, outliers retained

y1 <- reactorData$sesc025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "gamma")

y2 <- reactorData$sesc2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "gamma")

y3 <- reactorData$sesc5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "gamma")

y4 <- reactorData$sesc7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "gamma")

y5 <- reactorData$sesc90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "gamma")

title <- c('Gamma', 'Values shifted', 'Outliers retained', rep('', 7))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Shape', 'Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(c(y1shift, y2shift, y3shift, y4shift, y5shift), each=2)

df7 <- data.frame(title, names, items, rates, errors, shifts)


###################################
## GAMMA DISTRIBUTION FIT
# Values shifted, outliers retained

y1 <- reactorData$sescor025[1:75]
y1 <- y1[!is.na(y1)]
y1shift <- abs(min(y1)) + 0.001
y1 <- y1 + y1shift
dist1 <- fitdist(y1, "gamma")

y2 <- reactorData$sescor2550[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "gamma")

y3 <- reactorData$sescor5075[1:75]
y3 <- y3[!is.na(y3)]
y3shift <- abs(min(y3)) + 0.001
y3 <- y3 + y3shift
dist3 <- fitdist(y3, "gamma")

y4 <- reactorData$sescor7590[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "gamma")

y5 <- reactorData$sescor90100[1:75]
y5 <- y5[!is.na(y5)]
y5shift <- abs(min(y5)) + 0.001
y5 <- y5 + y5shift
dist5 <- fitdist(y5, "gamma")

title <- c('Gamma', 'Values shifted', 'Outliers retained', rep('', 7))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Shape', 'Rate'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- c(y1shift, '', y2shift, '', y3shift, '', y4shift, '', y5shift, '')

df8 <- data.frame(title, names, items, rates, errors, shifts)


####
## NORMAL DISTRIBUTION FIT
# Outliers retained

y1 <- reactorData$sesc025[0:75]
y1 <- y1[!is.na(y1)]
dist1 <- fitdist(y1, "norm", start=NULL)

y2 <- reactorData$sesc2550[0:75]
y2 <- y2[!is.na(y2)]
dist2 <- fitdist(y2, "norm", start=NULL)

y3 <- reactorData$sesc5075[0:75]
y3 <- y3[!is.na(y3)]
dist3 <- fitdist(y3, "norm", start=NULL)

y4 <- reactorData$sesc7590[0:75]
y4 <- y4[!is.na(y4)]
dist4 <- fitdist(y4, "norm", start=NULL)

y5 <- reactorData$sesc90100[0:75]
y5 <- y5[!is.na(y5)]
dist5 <- fitdist(y5, "norm", start=NULL)

title <- c('Normal', 'Outliers retained', rep('', 8))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Mean', 'SD'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 10)

df9 <- data.frame(title, names, items, rates, errors, shifts)


####
## NORMAL DISTRIBUTION FIT
# Outliers removed

y1 <- reactorData$sescor025[0:75]
y1 <- y1[!is.na(y1)]
dist1 <- fitdist(y1, "norm", start=NULL)

y2 <- reactorData$sescor2550[0:75]
y2 <- y2[!is.na(y2)]
dist2 <- fitdist(y2, "norm", start=NULL)

y3 <- reactorData$sescor5075[0:75]
y3 <- y3[!is.na(y3)]
dist3 <- fitdist(y3, "norm", start=NULL)

y4 <- reactorData$sescor7590[0:75]
y4 <- y4[!is.na(y4)]
dist4 <- fitdist(y4, "norm", start=NULL)

y5 <- reactorData$sescor90100[0:75]
y5 <- y5[!is.na(y5)]
dist5 <- fitdist(y5, "norm", start=NULL)

title <- c('Normal', 'Outliers removed', rep('', 8))
names <- rep(c('0-25%', '25-50%', '50-75%', '75-90%', '90-100%'), each=2)
items <- rep(c('Mean', 'SD'), 5)
rates <- c(dist1$estimate, dist2$estimate, dist3$estimate, dist4$estimate, dist5$estimate)
errors <- c(dist1$sd, dist2$sd, dist3$sd, dist4$sd, dist5$sd)
shifts <- rep(0, 10)

df10 <- data.frame(title, names, items, rates, errors, shifts)

write.csv(rbind(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10), file='distfit-outputs-master.csv', row.names=FALSE)