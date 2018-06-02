#!/usr/bin/env Rscript

library(LiblineaR)

###########################
### Define Dataset Files as Arguments
args <- commandArgs(trailingOnly = TRUE)
posfile <- args[1]
negfile <- args[2]

###########################
### Define Dataset Files: Hardcoded

##Positive (Class 1) Dataset File
#posfile <- "sample_datasets/tiny_dataset/pos.txt"

##Negative (Class 0) Dataset File
#negfile <- "sample_datasets/tiny_dataset/neg.txt"

###########################
### Read in data, set rownames to gene ids and remove that col

positive <- read.table(posfile, header = T, sep = "\t", stringsAsFactors = FALSE)
rownames(positive) <- paste(positive[,1], seq(1, nrow(positive))) # to make the rownames unique
positive[,1] <- NULL

negative <- read.table(negfile, header = T, sep = "\t", stringsAsFactors = FALSE)
rownames(negative) <- paste(negative[,1], seq(1, nrow(negative))) # to make the rownames unique
negative[,1] <- NULL

###########################
### Split data, create class vectors

# approx 80% training, 20% testing of positive
eighty_perc <- as.integer(nrow(positive) * 0.8)
train_positive <- positive[1:eighty_perc, , drop = FALSE]
test_positive <- positive[(eighty_perc+1):nrow(positive), , drop = FALSE]

# create class vectors for positive
train_positive_class <- rep(1, nrow(train_positive))
test_positive_class <- rep(1, nrow(test_positive))

# approx 80% training, 20% testing of negative data
eighty_perc <- as.integer(nrow(negative) * 0.8)
train_negative <- negative[1:eighty_perc, , drop = FALSE]
test_negative <- negative[(eighty_perc+1):nrow(negative), , drop = FALSE]

# create class vectors for negative
train_negative_class <- rep(0, nrow(train_negative))
test_negative_class <- rep(0, nrow(test_negative))

###########################
## Combine into training data and class definition
all_train <- rbind(train_positive, train_negative)
all_train_classes <- c(train_positive_class, train_negative_class)

## And also testing data and class definition
all_test <- rbind(test_positive, test_negative)
all_test_classes <- c(test_positive_class, test_negative_class)


###########################
### Prep the data for training and testing

# we have to get rid of any features that have standard deviation of 0 for the model to run
train_keep_logical <- !unlist(lapply(all_train, function(col){sd(col) == 0}))
all_train <- all_train[ , train_keep_logical, drop = F]
all_train_classes <- all_train_classes[train_keep_logical]

# we normalize the training data (helps the model)
all_train_scaled <- scale(all_train, center = TRUE, scale = TRUE)




###########################
### Run the model!

### This is a heuristic which guesses the "right" regularization cost
all_train_scaled <- as.matrix(all_train_scaled)
cost_heuristic <- LiblineaR::heuristicC(all_train_scaled)

model <- LiblineaR::LiblineaR(data = all_train_scaled,
                              target = all_train_classes,
                              type = 4,                     # "support vector classification by Crammer and Singer"
                              cost = cost_heuristic,
                              bias = TRUE,
                              verbose = TRUE)








##############################
### Test the model!

# we normalize the test data according to the same scaling factors as the model was trained on
all_test_scaled <- scale(all_test, center = attr(all_train_scaled, "scaled:center"), scale = attr(all_train_scaled, "scaled:scale"))

# make some predictions using the earlier model
p <- predict(model, all_test_scaled, decisionValues = TRUE)

# evaluate it
confusion_matrix <- table(predictions = p$predictions, actuals = all_test_classes)

print("confusion matrix:")
print(confusion_matrix)

# accuracy: true positives divided by total
# counts are by confusion_matrix[prediction, actual]
accuracy <- ( confusion_matrix["0", "0"] +
            confusion_matrix["1", "1"] ) /
            (  confusion_matrix["0", "0"] +
               confusion_matrix["1", "1"] +
               confusion_matrix["1", "0"] +
               confusion_matrix["0", "1"] )

print("accuracy:")
print(accuracy)
