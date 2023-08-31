#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import streamlit as st


# In[2]:


df = pd.read_csv("Mainfile.csv")
df.head()

df.info()


# """**STATISTICAL DATA**"""

# In[3]:


df.describe()


# """**DATA PREPROCESSING AND CLEANING**"""

# In[4]:


# Convert categorical columns to categorical data type
categorical_columns = ['INSPECTION_DATE','PROPERTY_TYPE','MAINHEAT_DESCRIPTION']
for col in categorical_columns:
    df[col] = df[col].astype('category')

df.info()


# In[5]:


# Check for missing values in columns
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)


# In[6]:


# List of columns with numerical data
numerical_columns = ['ENERGY_CONSUMPTION_CURRENT','ENVIRONMENT_IMPACT_CURRENT','CURRENT_ENERGY_EFFICIENCY','CO2_EMISSIONS_CURRENT','HOT_WATER_COST_CURRENT','TOTAL_FLOOR_AREA','LIGHTING_COST_CURRENT','HEATING_COST_CURRENT']  # Define your numerical columns here


# In[7]:


# List of columns with non-numerical (categorical) data
categorical_columns = ['INSPECTION_DATE','PROPERTY_TYPE','MAINHEAT_DESCRIPTION']  # Define your categorical columns here


# In[8]:


# replace missing values with Mean from sklearn imputer
from sklearn.impute import SimpleImputer
# Impute numerical data with mean
numerical_imputer = SimpleImputer(strategy='mean')
df[numerical_columns] = numerical_imputer.fit_transform(df[numerical_columns])


# In[9]:


# Impute categorical data with the most frequent value (mode)
categorical_imputer = SimpleImputer(strategy='most_frequent')
df[categorical_columns] = categorical_imputer.fit_transform(df[categorical_columns])


# In[10]:


# Check for missing values in columns
missing_values = df.isnull().sum()
print("Missing Values:")
print(missing_values)


# In[11]:


df.describe()


# In[12]:


#asbsolute values to remove the potential nagetive errors
columns_to_convert = ['ENERGY_CONSUMPTION_CURRENT', 'CO2_EMISSIONS_CURRENT']


# In[13]:


# Apply the absolute function to the specified columns
df[columns_to_convert] = df[columns_to_convert].apply(abs)
df.describe()


# """**EXPORATORY DATA ANALYSIS**"""

# In[14]:


import matplotlib.pyplot as plt
import seaborn as sns
# Scatter plot: Energy Consumption vs. CO2 Emissions
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ENERGY_CONSUMPTION_CURRENT', y='CO2_EMISSIONS_CURRENT', hue='PROPERTY_TYPE')
plt.title("Energy Consumption vs. CO2 Emissions")
plt.xlabel("Energy Consumption")
plt.ylabel("CO2 Emissions")
plt.legend()
plt.show()


# In[15]:


# Barplot: Average Heating Cost by Property Type
avg_heating_cost = df.groupby('PROPERTY_TYPE')['HEATING_COST_CURRENT'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x=avg_heating_cost.index, y=avg_heating_cost.values)
plt.title("Average Heating Cost by Property Type")
plt.xticks(rotation=45)
plt.xlabel("Property Type")
plt.ylabel("Average Heating Cost")
plt.show()


# In[16]:


# Filter the top 10 main heat descriptions
top_mainheat2 = df['PROPERTY_TYPE'].value_counts().nlargest(5).index
df_top_mainheat2 = df[df['PROPERTY_TYPE'].isin(top_mainheat2)]
# Violin plot: Total Floor Area by Top 5 CO2 Emissions
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_top_mainheat2, x='PROPERTY_TYPE', y='CO2_EMISSIONS_CURRENT')
plt.title("CO2 Emissions by Top 5 PROPERTY_TYPE")
plt.xticks(rotation=45)
plt.xlabel("Main Heat Description")
plt.ylabel("CO2 Emissions")
plt.show()


# In[17]:


# Filter the top 10 main heat descriptions
top_mainheat = df['MAINHEAT_DESCRIPTION'].value_counts().nlargest(5).index
df_top_mainheat = df[df['MAINHEAT_DESCRIPTION'].isin(top_mainheat)]
# Violin plot: Total Floor Area by Top 5 Main Heat Descriptions
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_top_mainheat, x='MAINHEAT_DESCRIPTION', y='TOTAL_FLOOR_AREA')
plt.title("Total Floor Area by Top 5 Main Heat Descriptions")
plt.xticks(rotation=45)
plt.xlabel("Main Heat Description")
plt.ylabel("Total Floor Area")
plt.show()


# In[18]:


# Subsample data (adjust n to your preference)
n = min(1000, len(df))
sampled_indices = np.random.choice(df.index, n, replace=False)
df_sampled = df.loc[sampled_indices]


# In[19]:


# Limit variables (adjust based on your focus)
selected_vars = ['ENERGY_CONSUMPTION_CURRENT', 'CO2_EMISSIONS_CURRENT', 'TOTAL_FLOOR_AREA']


# In[20]:


# Pairplot with hue for subsampled data and selected variables
sns.pairplot(df_sampled[selected_vars], diag_kind='kde')
plt.suptitle("Pairwise Relationships with Selected Variables")
plt.show()


# In[21]:


# FacetGrid: Energy Consumption vs. CO2 Emissions by Property Type
g = sns.FacetGrid(data=df, col='PROPERTY_TYPE', height=5, aspect=1.2)
g.map_dataframe(sns.scatterplot, x='ENERGY_CONSUMPTION_CURRENT', y='CO2_EMISSIONS_CURRENT')
g.set_axis_labels("Energy Consumption", "CO2 Emissions")
g.set_titles(col_template="{col_name}")
plt.subplots_adjust(top=0.8)
g.fig.suptitle("Energy Consumption vs. CO2 Emissions by Property Type")
plt.show()


# In[22]:


# FacetGrid: Energy Consumption vs. CO2 Emissions by Property Type
g = sns.FacetGrid(data=df, col='PROPERTY_TYPE', height=5, aspect=1.2)
g.map_dataframe(sns.lineplot, x='ENERGY_CONSUMPTION_CURRENT', y='CO2_EMISSIONS_CURRENT')
g.set_axis_labels("Energy Consumption", "CO2 Emissions")
g.set_titles(col_template="{col_name}")
plt.subplots_adjust(top=0.8)
g.fig.suptitle("Energy Consumption vs. CO2 Emissions by Property Type")
plt.show()


# In[23]:


#Relationship between ENERGY_CONSUMPTION_CURRENT and INSPECTION_DATE
import matplotlib.pyplot as plt
import seaborn as sns

# Get the top 5 most common INSPECTION_DATE categories
top_mainheat = df['INSPECTION_DATE'].value_counts().head(5).index

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='INSPECTION_DATE', y='ENERGY_CONSUMPTION_CURRENT', ci=None, order=top_mainheat)
plt.title('Relationship between Energy consumption and Inspection Date (Top 5)')
plt.xlabel('Inspection Date')
plt.ylabel('Energy Consumption')
plt.xticks(rotation=45)
plt.show()


# In[24]:


#Relationship between ENVIRONMENT_IMPACT and PROPERTY_TYPE
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='PROPERTY_TYPE', y='ENVIRONMENT_IMPACT_CURRENT', ci=None)
plt.title('Relationship between Environment Impact and Property Type')
plt.xlabel('Property Type')
plt.ylabel('Environment Impact')
plt.show()


# In[25]:


#Relationship between Heating Cost and Main Heating Description
import matplotlib.pyplot as plt
import seaborn as sns

# Get the top 5 most common MAINHEAT_DESCRIPTION categories
top_mainheat = df['MAINHEAT_DESCRIPTION'].value_counts().head(5).index

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='MAINHEAT_DESCRIPTION', y='HEATING_COST_CURRENT', ci=None, order=top_mainheat)
plt.title('Relationship between Heating Cost and Main Heating Description (Top 5)')
plt.xlabel('Main Heating Description')
plt.ylabel('Heating Cost')
plt.xticks(rotation=45)
plt.show()


# In[26]:


#Relationship between ENERGY_EFFICIENCY and PROPERTY_TYPE
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='PROPERTY_TYPE', y='CURRENT_ENERGY_EFFICIENCY', ci=None)
plt.title('Relationship between Energy Efficiency and Property Type')
plt.xlabel('Property Type')
plt.ylabel('Energy Effciency')
plt.show()


# In[27]:


from scipy.stats import linregress


# In[28]:


# Scatter plot with trendline: Energy Consumption vs. Total Floor Area
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ENERGY_CONSUMPTION_CURRENT', y='TOTAL_FLOOR_AREA')
plt.title("Energy Consumption vs. Total Floor Area")
plt.xlabel("Energy Consumption")
plt.ylabel("Total Floor Area")
# Calculate and plot the trendline
slope, intercept, r_value, p_value, std_err = linregress(df['ENERGY_CONSUMPTION_CURRENT'], df['TOTAL_FLOOR_AREA'])
x_values = np.array([min(df['ENERGY_CONSUMPTION_CURRENT']), max(df['ENERGY_CONSUMPTION_CURRENT'])])
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='r', label='Trendline')
plt.legend()
plt.show()


# In[29]:


#bolder visualisation of the trendline
# Calculate and plot the trendline
slope, intercept, r_value, p_value, std_err = linregress(df['ENERGY_CONSUMPTION_CURRENT'], df['TOTAL_FLOOR_AREA'])
x_values = np.array([min(df['ENERGY_CONSUMPTION_CURRENT']), max(df['ENERGY_CONSUMPTION_CURRENT'])])
y_values = slope * x_values + intercept
plt.plot(x_values, y_values, color='r', label='Trendline')
plt.title("Energy Consumption vs. Total Floor Area")
plt.xlabel("Energy Consumption")
plt.ylabel("Total Floor Area")
plt.legend()
plt.show()


# In[30]:


# Calculate correlation matrix for numerical columns
correlation_matrix = df[numerical_columns].corr()


# In[31]:


# Heatmap for correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Numerical Columns')
plt.show()


# **FEATURE ENGINEERING**

# In[32]:


from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

from sklearn.preprocessing import StandardScaler
# Convert categorical variables to dummy variables
df_with_dummies = pd.get_dummies(df, columns=['PROPERTY_TYPE','MAINHEAT_DESCRIPTION'])

# Extract numerical columns for scaling
numerical_data = df_with_dummies[numerical_columns]

# Create a StandardScaler instance
scaler = StandardScaler()

# Scale the numerical data
scaled_numerical_data = scaler.fit_transform(numerical_data)

# Create a new DataFrame with scaled numerical data
scaled_df = pd.DataFrame(scaled_numerical_data, columns=numerical_columns)

# Combine the scaled numerical data with the dummy variables
final_df = pd.concat([scaled_df, df_with_dummies.drop(columns=numerical_columns)], axis=1)

# 'final_df' now contains both scaled numerical data and dummy variables
# Now you can use the .describe() method on the DataFrame
summary_stats = final_df.describe()

# Display the summary statistics
summary_stats


# In[33]:


final_df.info()


# In[34]:


from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Split the data into feature matrix X and target variable y
from sklearn.model_selection import train_test_split


# In[35]:


# List of columns to drop from X
columns_to_drop = ["HEATING_COST_CURRENT", "CO2_EMISSIONS_CURRENT", "INSPECTION_DATE"]


# In[36]:


X = final_df.drop(columns=columns_to_drop, axis=1)
y = final_df["HEATING_COST_CURRENT"]


# In[37]:


# Split the cleaned data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Test the model on the testing data
# y_pred = model.predict(X_test)

# # Calculate and display accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy:", accuracy)

# # Display classification report
# report = classification_report(y_test, y_pred)
# print("Classification Report:\n", report)

X.info()


# In[38]:


# Display the list of all columns in X_test
print("Columns in X_test:", X_test.columns.tolist())


# **MACHINE LEARNING MODELS**

# In[39]:


# Create a linear regression model
from sklearn.linear_model import LinearRegression
regression_model = LinearRegression()

# Train the model on the training data
regression_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = regression_model.predict(X_test)
from sklearn.metrics import mean_squared_error, r2_score


# Calculate the mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate the R-squared (coefficient of determination) score
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R-squared:", r2)


# In[40]:


from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
# Create a Gradient Boosting Regressor model
gradient_boosting_model = GradientBoostingRegressor()

# Train the model on the training data
gradient_boosting_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = gradient_boosting_model.predict(X_test)


# Calculate the mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate the R-squared (coefficient of determination) score
r2 = r2_score(y_test, y_pred)

print("Gradient Boosting Model - Mean Squared Error:", mse)
print("Gradient Boosting Model - R-squared:", r2)


# In[41]:


#Calculate the mean absolute error (MAE)
mae_gradient_boosting = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error (Gradient Boosting):", mae_gradient_boosting)


# In[42]:


from sklearn.ensemble import RandomForestRegressor
# Create a Random Forest Regressor model
random_forest_model = RandomForestRegressor(n_estimators=100, random_state=42)
# Train the model on the training data
random_forest_model.fit(X_train, y_train)
# Make predictions on the test data
y_pred = random_forest_model.predict(X_test)

# Calculate the mean squared error (MSE) on the test data
mse = mean_squared_error(y_test, y_pred)

# Calculate the R-squared (coefficient of determination) score on the test data
r2 = r2_score(y_test, y_pred)

print("Random Forest Model - Mean Squared Error:", mse)
print("Random Forest Model - R-squared:", r2)


# In[43]:


#Calculate the mean absolute error (MAE)
mae_random_forest = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error (Random Forest):", mae_random_forest)


# In[44]:


"""**Decision Tree Regressor**"""

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

# Create a Decision Tree Regressor model
Decision_Tree_model = DecisionTreeRegressor()

# Train the model on the training data
Decision_Tree_model.fit(X_train, y_train)

# Make predictions on the test data
y_pred = Decision_Tree_model.predict(X_test)

# Calculate the mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)

# Calculate the R-squared (coefficient of determination) score
r2 = r2_score(y_test, y_pred)

print("Decision Tree Model - Mean Squared Error:", mse)
print("Decision Tree Model - R-squared:", r2)


# In[45]:


#Calculate the mean absolute error (MAE)
mae_decision_Tree = mean_absolute_error(y_test, y_pred)

print("Mean Absolute Error (Decision Tree):", mae_decision_Tree)


# In[46]:


pip install tensorflow


# In[47]:


pip install --upgrade tensorflow h5py numpy


# In[48]:


"""**ANN**"""
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


# In[49]:


X_train = X_train.astype(np.float32)
y_train = y_train.astype(np.float32)

X_test = X_test.astype(np.float32)
y_test = y_test.astype(np.float32)


# In[50]:


model = keras.Sequential([
    layers.Input(shape=(X_train.shape[1],)),  # Input layer
    layers.Dense(64, activation='relu'),      # Hidden layer 1
    layers.Dense(32, activation='relu'),      # Hidden layer 2
    layers.Dense(1)                           # Output layer
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Train the model on the training data
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

# Evaluate the model on the test data
loss = model.evaluate(X_test, y_test)
print("Mean Squared Error on Test Data:", loss)

from sklearn.metrics import r2_score

# Predict the target variable using the trained ANN model
y_pred_ann = model.predict(X_test)

# Calculate the R-squared value
r2_ann = r2_score(y_test, y_pred_ann)
print("R-squared for ANN Model:", r2_ann)


# In[51]:


import matplotlib.pyplot as plt

# Plot the training and validation loss over epochs
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss Over Epochs')
plt.legend()
plt.show()


# In[52]:


# Assuming you have imported the necessary libraries and trained your model

# Get the weights of the first layer (assuming it's a dense layer)
first_layer_weights = model.layers[0].get_weights()[0]

# Calculate the absolute sum of weights for each input feature
feature_importance = np.sum(np.abs(first_layer_weights), axis=1)

# Create a DataFrame to associate feature names with their importance
importance_df = pd.DataFrame({'Feature': X.columns, 'Importance': feature_importance})

# Sort the DataFrame by importance in descending order
importance_df = importance_df.sort_values(by='Importance', ascending=False)

# Print the feature importance
print(importance_df)


# """**SCENERIO AND EXPERIMENTATIONS**"""

# In[53]:


y_pred_ann

# Original input data for comparison
original_input = X_train

# Predict heating cost for the original input
original_predicted_cost = model.predict([original_input])

print("Baseline: Original Values")
print(f"Baseline Predicted increase or decrease in Heating Cost: {original_predicted_cost[0][0]}\n")


# In[54]:


# Scenario 2: Change 'PROPERTY_TYPE_Flat' to 1, set related columns to 0
#we used flat because from the rating, flat was the only property type among the top important variables
scenario_2_input = original_input.copy()
scenario_2_input['PROPERTY_TYPE_Flat'] = 1
scenario_2_input.loc[:, scenario_2_input.columns.str.startswith('PROPERTY_TYPE')] = 0


# Predict heating cost for scenario 2 input
scenario_2_predicted_cost = model.predict([scenario_2_input])

print("Scenario 2: PROPERTY_TYPE_Flat Set to 1")
print(f"Scenario 2 Predicted increase or decrease to Heating Cost: {scenario_2_predicted_cost[0][0]}\n")


# In[55]:


#A flat using Electric storage heaters

scenario_5_input = scenario_2_input.copy()
scenario_5_input['MAINHEAT_DESCRIPTION_Electric storage heaters'] = 1
scenario_5_input.loc[:, scenario_5_input.columns.str.startswith('MAINHEAT_DESCRIPTION')] = 0

# Predict heating cost for scenario 5 input
scenario_5_predicted_cost = model.predict([scenario_5_input])

print("Scenario 5: A FLAT USING Electric storage heaters")
print(f"Scenario 5 Predicted increase or decrease to Heating Cost: {scenario_5_predicted_cost[0][0]}\n")


# In[56]:


scenario_3_input = original_input.copy()
scenario_3_input['MAINHEAT_DESCRIPTION_Air source heat pump, Underfloor heating, pipes in screed above insulation, electric'] = 1
scenario_3_input.loc[:, scenario_3_input.columns.str.startswith('MAINHEAT_DESCRIPTION')] = 0

# Predict heating cost for scenario 3 input
scenario_3_predicted_cost = model.predict([scenario_3_input])

print("Scenario 3: MAINHEAT_DESCRIPTION Set to Heat Pump")
print(f"Scenario 3 Predicted increase or decrease to Heating Cost: {scenario_3_predicted_cost[0][0]}\n")


# In[57]:


scenario_4_input = scenario_3_input.copy()
scenario_4_input['PROPERTY_TYPE_House'] = 1
scenario_4_input.loc[:, scenario_4_input.columns.str.startswith('PROPERTY_TYPE')] = 0

# Predict heating cost for scenario 2 input
scenario_4_predicted_cost = model.predict([scenario_4_input])

print("Scenario 3: MAINHEAT_DESCRIPTION Set to Heat Pump")
print(f"Scenario 3 Predicted increase or decrease to Heating Cost: {scenario_4_predicted_cost[0][0]}\n")


# In[58]:


pip install scikit-learn-contrib


# In[59]:


import numpy as np
from sklearn.model_selection import GridSearchCV
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import make_scorer
from sklearn.metrics import r2_score

# Define the function to build the model
def build_model(neurons_layer1=64, neurons_layer2=32):
    model = keras.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(neurons_layer1, activation='relu'),
        layers.Dense(neurons_layer2, activation='relu'),
        layers.Dense(1)
    ])
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

# Create a KerasRegressor using build_model function
keras_regressor = keras.wrappers.scikit_learn.KerasRegressor(build_fn=build_model, verbose=0)

# Define hyperparameters and their values for grid search
param_grid = {
    'neurons_layer1': [32, 64, 128],
    'neurons_layer2': [16, 32, 64],
    'batch_size': [16, 32, 64],
    'epochs': [50, 100, 200]
}

# Perform grid search with cross-validation
grid_search = GridSearchCV(estimator=keras_regressor, param_grid=param_grid, scoring=make_scorer(r2_score), cv=3)
grid_result = grid_search.fit(X_train, y_train)

# Print best hyperparameters and corresponding R-squared score
print("Best Hyperparameters: ", grid_result.best_params_)
print("Best R-squared Score: ", grid_result.best_score_)


# In[ ]:


"""END"""

