library(fitdistrplus)
library(ggplot2)
reactorData = read.csv("~/financial-projections/data/reactors.csv")


#######################################################
## EXPONENTIAL DISTRIBUTION FIT
# Negative values removed (no shift), outliers retained

y1 <- reactorData$sesc0100[1:75]
y1 <- subset(y1, y1 > 0)
dist1 <- fitdist(y1, "exp")
#plot(dist1)

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
#plot(dist2)

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
#plot(dist3)

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
h <- data.frame(y4)
#plot(dist4)
ggplot(h) + geom_qq(aes(sample = rnorm(75)))

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
#plot(dist5)

type <- c('Normal', '')
negatives <- c('NA', '')
outliers <- c('OK', '')
items <- c('Mean', 'SD')
params <- c(dist5$estimate)
errors <- c(dist5$sd)
shifts <- c(0, 0)

df5 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


#######################################################
## EXPONENTIAL DISTRIBUTION FIT
# Negative values removed (no shift), outliers removed

y6 <- reactorData$sescor0100[1:75]
y6 <- subset(y6, y6 > 0)
dist6 <- fitdist(y6, "exp")
#plot(dist6)

type <- c('Exponential', '')
negatives <- c('NVR', '')
outliers <- c('OR', '')
items <- c('Rate', '')
params <- c(dist6$estimate, 0)
errors <- c(dist6$sd, 0)
shifts <- c(0, 0)

df6<- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ###################################
# ## EXPONENTIAL DISTRIBUTION FIT
# # Values shifted, outliers removed
# 
y7 <- reactorData$sescor0100[1:75]
y7 <- y7[!is.na(y7)]
y7shift <- abs(min(y7)) + 0.001
y7 <- y7 + y7shift
dist7 <- fitdist(y7, "exp")
#plot(dist7)

type <- c('Exponential', '')
negatives <- c('VS', '')
outliers <- c('OR', '')
items <- c('Rate', '')
params <- c(dist7$estimate, 0)
errors <- c(dist7$sd, 0)
shifts <- c(y7shift, y7shift)

df7 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ############################################
# ## GAMMA FIT
# # Negative values removed, outliers removed
# 
y8 <- reactorData$sescor0100[0:75]
y8 <- subset(y8, y8 > 0)
dist8 <- fitdist(y8, "gamma")
#plot(dist8)

type <- c('Gamma', '')
negatives <- c('NVR', '')
outliers <- c('OR', '')
items <- c('Shape', 'Rate')
params <- c(dist8$estimate)
errors <- c(dist8$sd)
shifts <- c(0, 0)

df8 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ###################################
# ## GAMMA DISTRIBUTION FIT
# # Values shifted, outliers removed

y9 <- reactorData$sescor0100[1:75]
y9 <- y9[!is.na(y9)]
y9shift <- abs(min(y9)) + 0.001
y9 <- y9 + y9shift
dist9 <- fitdist(y9, "gamma")
#plot(dist9)

type <- c('Gamma', '')
negatives <- c('VS', '')
outliers <- c('OR', '')
items <- c('Shape', 'Rate')
params <- c(dist9$estimate)
errors <- c(dist9$sd)
shifts <- c(y9shift, y9shift)

df9 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


############################
# ## NORMAL DISTRIBUTION FIT
# # Outliers removed
# 
y10 <- reactorData$sescor0100[0:75]
y10 <- y10[!is.na(y10)]
dist10 <- fitdist(y10, "norm", start=NULL)
#plot(dist10)

type <- c('Normal', '')
negatives <- c('NA', '')
outliers <- c('OR', '')
items <- c('Mean', 'SD')
params <- c(dist10$estimate)
errors <- c(dist10$sd)
shifts <- c(0, 0)

df10 <- data.frame(type, negatives, outliers, items, params, errors, shifts)

write.csv(rbind(df1, df2, df3, df4, df5, df6, df7, df8, df9, df10), file='distfit-sesc-outputs-master-0100.csv', row.names=FALSE)