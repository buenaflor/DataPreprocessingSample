# Data Preprocessing Template

# Don't have to distinct between Matrix of features and Dependent variable vector
# Importing the dataset
dataset = read.csv('Data.csv')

# Handle missing data is to take the Mean of the whole column

# is Not available in the colum $Age
dataset$Age = ifelse(is.na(dataset$Age), 
                      ave(dataset$Age, FUN = function(x) mean(x, na.rm = TRUE)),
                      dataset$Age)

dataset$Salary = ifelse(is.na(dataset$Salary), 
                      ave(dataset$Salary, FUN = function(x) mean(x, na.rm = TRUE)),
                      dataset$Salary) 

# Encoding categorical data
# C is a vector
dataset$Country = factor(dataset$Country, 
                         levels = c('France', 'Spain', 'Germany'),
                         labels = c(1, 2, 3))

dataset$Purchased = factor(dataset$Purchased, 
                         levels = c('No', 'Yes'),
                         labels = c(0, 1))

# Splitting the dataset into the Training Set and Test Set
# install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE)









