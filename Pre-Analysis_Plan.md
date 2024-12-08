## Observation in the Study

Each observation represents a single hotel booking record with various attributes such as booking lead time, stay duration, market segment, and whether or not the booking was canceled.

## Type of Learning and Prediction Goal

This is a supervised learning project with the main objective of classification, where we aim to predict whether a booking will be canceled (binary outcome: 0 or 1). 1 will represent cancellation while 0 represents non-cancellation. 
In addition, we will use regression analysis to explore how the numerical variable ADR (average daily rate) relates to other features. This helps us understand pricing patterns and their potential association with cancellations.

## Models and Algorithms

### Decision Trees

Decision trees divide the dataset based on feature values, isolating important features to predict the target variable. Decision trees will be used to identify which variables significantly impact cancellations, allowing us to see the 
decision pathways leading to cancellation vs. non-cancellation.

### Random Forest

Random forests improve upon decision trees by training multiple trees on random data subsets, reducing overfitting and improving accuracy. The final prediction is determined by the average or majority vote of all trees. Decision trees 
are single models that may overfit, especially with complex data.

### Linear Regression

Linear regression analyzes relationships between ADR and predictor variables. We explore relationships involving ADR as the outcome variable, with features like lead time, customer type and is_canceled as predictors. This will allow us 
to understand whether ADR is affected by features related to cancellations, offering insights into pricing patterns for bookings with higher or lower cancellation risks. For example, by including is_canceled as a predictor, the model 
can capture differences in ADR associated with cancellations. If canceled bookings frequently show lower ADR, this might suggest that last-minute or discounted bookings have a higher risk of cancellation.

## Testing for Success and Ensuring Model Validity

We plan on using an 80/20 train-test data split on our models so that we can evaluate each of their accuracy. We also plan on validating models by carefully controlling our variables to ensure that we don’t over or underfit our models. 
For models with “success metrics” like R2 and RMSE, we will be checking to see if those metrics align with what is expected for a successful model. For example, we will be checking for R2 values close to 1 and low RMSE values.

## Potential Weaknesses and Failures

We suspect that there may be model bias if canceled bookings occur less often than non-canceled bookings. If we notice model bias in our data, then we will fix it by adjusting class balance.
Another potential weakness is that our model will have poor R2 and RMSE values. We would first try to deal with this by seeing if adding in another explanatory variable would help the model make more sense. If this approach fails, 
we would come to the conclusion that linear regression is not optimal for predicting behaviors in bookings. Other weaknesses and model failures could come from factors out of our control that the data doesn’t account for, such as 
clients choosing to cancel bookings due to them finding better deals elsewhere.

## Feature Engineering

### One-Hot encoding
This converts categorical variables, like Hotel or Meal type into binary columns. Some variables like Meal type have more than 2 unique categories, we will separate each meal type as a separate column. The dataset that we are working with has 4 categories for Meal type–BB (bed and breakfast), HB (half board), FB (full board), and SC (self-catering), each category has a value of 1 if that meal type applies to a booking and 0 otherwise.

### Feature scaling
Standardizing numerical variables, such as lead_time to improve model performance by bringing all numeric data into a comparable range.

### Data features
We can extract features such as day of the week or month to capture seasonal trends that may influence cancellation rate.

## Results
We will use a few different methods to communicate our results and whether our analysis plans were successful or not. We will be using a confusion matrix to prove whether or not our models have the ability to successfully predict canceled vs non-canceled bookings. Feature importance will be used to visualize feature importance scores to identify the top drivers of cancellations. After using our test-train split, we’ll be able to communicate our model’s validity, as well as determine if we need to make adjustments. For the linear regression model, we will be communicating important findings by interpreting the coefficients and intercepts in relation to understanding what drives hotel booking cancellations.
