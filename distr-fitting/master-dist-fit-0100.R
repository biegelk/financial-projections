library(fitdistrplus)
library(ggplot2)
reactorData = read.csv("~/financial-projections/data/reactors.csv")


#######################################################
## EXPONENTIAL DISTRIBUTION FIT
# Negative values removed (no shift), outliers retained

y1 <- reactorData$sesc0100[1:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "exp")
plot(dist1)

type <- c('Exponential', '')
negatives <- c('NVR', '')
outliers <- c('OK', '')
items <- c('Rate', '')
params <- c(dist1$estimate, 0)
errors <- c(dist1$sd, 0)
shifts <- c(0, 0)

df1 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ###################################
# ## EXPONENTIAL DISTRIBUTION FIT
# # Values shifted, outliers retained
# 
y2 <- reactorData$sesc0100[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "exp")
plot(dist2)

type <- c('Exponential', '')
negatives <- c('VS', '')
outliers <- c('OK', '')
items <- c('Rate', '')
params <- c(dist2$estimate, 0)
errors <- c(dist2$sd, 0)
shifts <- c(y2shift, y2shift)

df2 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ############################################
# ## GAMMA FIT
# # Negative values removed, outliers retained
# 
y3 <- reactorData$sesc0100[0:75]
y3 <- subset(y3, y3 > 0)
dist3 <- fitdist(y3, "gamma")
plot(dist3)

type <- c('Gamma', '')
negatives <- c('NVR', '')
outliers <- c('OK', '')
items <- c('Shape', 'Rate')
params <- c(dist3$estimate)
errors <- c(dist3$sd)
shifts <- c(0, 0)

df3 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ###################################
# ## GAMMA DISTRIBUTION FIT
# # Values shifted, outliers retained

y4 <- reactorData$sesc0100[1:75]
y4 <- y4[!is.na(y4)]
y4shift <- abs(min(y4)) + 0.001
y4 <- y4 + y4shift
dist4 <- fitdist(y4, "gamma")
plot(dist4)

type <- c('Gamma', '')
negatives <- c('VS', '')
outliers <- c('OK', '')
items <- c('Shape', 'Rate')
params <- c(dist4$estimate)
errors <- c(dist4$sd)
shifts <- c(y4shift, y4shift)

df4 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


############################
# ## NORMAL DISTRIBUTION FIT
# # Outliers retained
# 
y5 <- reactorData$sesc0100[0:75]
y5 <- y5[!is.na(y5)]
dist5 <- fitdist(y5, "norm", start=NULL)
plot(dist5)

type <- c('Normal', '')
negatives <- c('NA', '')
outliers <- c('OK', '')
items <- c('Mean', 'SD')
params <- c(dist5$estimate)
errors <- c(dist5$sd)
shifts <- c(0, 0)

df5 <- data.frame(type, negatives, outliers, items, params, errors, shifts)

write.csv(rbind(df1, df2, df3, df4, df5), file='distfit-outputs-master-0100.csv', row.names=FALSE)