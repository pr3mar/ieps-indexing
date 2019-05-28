dat <- read.csv("../output/freq.csv", header = TRUE)

mean(dat$avgFreq)
sd(dat$avgFreq)

library('ggplot2')
ggplot(dat, aes(x=avgFreq)) + 
  geom_histogram(aes(y=..density..),binwidth=.35, colour="black", fill="white") +
  geom_density(alpha=.2, fill="#FF6666") +
  labs(
    title = "Average frequency per document",
    y = "Distribution",
    x = "frequency"
  )
