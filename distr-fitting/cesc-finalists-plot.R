library(fitdistrplus)
library(ggplot2)
reactorData = read.csv("~/financial-projections/data/reactors.csv")

# ###################################
# ## EXPONENTIAL DISTRIBUTION FIT
# # Values shifted, outliers retained
# 
y2 <- reactorData$cesc090[1:75]
y2 <- y2[!is.na(y2)]
y2shift <- abs(min(y2)) + 0.001
y2 <- y2 + y2shift
dist2 <- fitdist(y2, "exp")
dist2
plot(dist2)

type <- c('Exponential', '')
negatives <- c('VS', '')
outliers <- c('OK', '')
items <- c('Rate', '')
params <- c(dist2$estimate, 0)
errors <- c(dist2$sd, 0)
shifts <- c(y2shift, y2shift)

df2 <- data.frame(type, negatives, outliers, items, params, errors, shifts)


# ###################################
# ## GAMMA DISTRIBUTION FIT
# # Values shifted, outliers removed

y9 <- reactorData$cescor090[1:75]
y9 <- y9[!is.na(y9)]
y9shift <- abs(min(y9)) + 0.001
y9 <- y9 + y9shift
dist9 <- fitdist(y9, "gamma")
dist9
plot(dist9)

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
y10 <- reactorData$cescor090[0:75]
y10 <- y10[!is.na(y10)]
dist10 <- fitdist(y10, "norm", start=NULL)
dist10
plot(dist10)

type <- c('Normal', '')
negatives <- c('NA', '')
outliers <- c('OR', '')
items <- c('Mean', 'SD')
params <- c(dist10$estimate)
errors <- c(dist10$sd)
shifts <- c(0, 0)

df10 <- data.frame(type, negatives, outliers, items, params, errors, shifts)