# Agronomic-Decision-Support-System

## 1. Problem Formulation and Rationale

Many farmers rely on traditional knowledge and practices to determine the amount of fertilizer to use for their crops. However, too much fertilizer can lead to soil degradation and wasted resources, while too little fertilizer can result in poor crop growth and reduced yield. This makes it challenging for farmers to achieve the optimal balance needed to maximize crop yield, reduce costs, and minimize environmental impact.

The decision support system will provide recommendations based on easily obtainable data, including soil conditions, weather conditions, and crop types. Farmers can input these data into the decision support system, which will then provide real-time, tailored recommendations to help optimize fertilizer usage, achieving high crop yields while reducing costs and minimizing environmental impact.

## 2. The Data Schema and Rationale for the Types of Data Chosen

#### Data Schema

| Feature                   | Type   | Description                                                             |
| ------------------------- | ------ | ----------------------------------------------------------------------- |
| soil_color                | String | Qualitative measure of soil color (e.g., dark brown, reddish)           |
| soil_ph                   | Float  | Soil pH level                                                           |
| soil_n                    | Float  | Nitrogen content in soil (ppm)                                          |
| soil_p                    | Float  | Phosphorus content in soil (ppm)                                        |
| temp                      | Float  | Current temperature (°C)                                                |
| rainfall                  | Float  | Recent rainfall (mm)                                                    |
| forecast_temp             | Float  | Forecasted temperature (°C)                                             |
| forecast_rainfall         | Float  | Forecasted rainfall (mm)                                                |
| crop_type                 | String | Type of crop being grown                                                |
| plant_health              | String | Qualitative measure of plant health (e.g., healthy, yellowing, wilting) |
| optimal_fertilizer_amount | Float  | Target value: Optimal fertilizer amount (kg/ha)                         |

#### Rationale

These features were selected for the dummy data based on the assumption that they should be easily obtainable by farmers using common agricultural tools and resources.

Farmers can use simple pH test kits available at agricultural supply stores to conduct soil tests for pH and nutrient content. Weather data can be accessed through local weather stations or agricultural services. Crop type and plant health observations are part of standard farming practice. This makes the data collection straightforward and practical for farmers.

| Feature                   | Rationale                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| soil_color                | A quick indicator of soil fertility; darker soils usually have more organic matter.                                                                           |
| soil_ph                   | Influences nutrient availability; extreme pH levels can hinder plant growth.                                                                                  |
| soil_n                    | A primary nutrient for plant growth; helps determine fertilization needs.                                                                                     |
| soil_p                    | Essential for root development and energy transfer in plants.                                                                                                 |
| temp                      | Affects plant metabolic rates and nutrient uptake.                                                                                                            |
| rainfall                  | Influences soil moisture and nutrient availability.                                                                                                           |
| forecast_temp             | Useful for planning fertilizer application timing.                                                                                                            |
| forecast_rainfall         | Important for timing fertilizer application.                                                                                                                  |
| crop_type                 | Determines specific nutrient needs and growth patterns.                                                                                                       |
| plant_health              | Provides visible indicators that help diagnose nutrient deficiencies and other issues.                                                                        |
| optimal_fertilizer_amount | The target value that the decision support system aims to predict, helping farmers apply the right amount of fertilizer to maximize yield and minimize costs. |

## 3. The Methodology Used for Data Simulation

The approach to simulating the dummy data is based on using real-world typical values for soil content, weather patterns, crop type, and plant health so that the dummy data would reflect real-world conditions. This would make the dummy data useful enough to develop and test the decision support system.

To further simulate real-world conditions, a low percentage of outliers and missing data was introduced to the dummy data, as real-world data often contains such imperfections.

| Feature                   | Assumption                                                                                                                                            | Method                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| soil_color                | Mimics common soil color ranges                                                                                                                       | Randomly chosen from dark brown, reddish, light brown                                            |
| soil_ph                   | Typical soil pH values in agricultural areas range from 5.5 to 7.5                                                                                    | Randomly generated within the range of 5.5 to 7.5                                                |
| soil_n                    | Nitrogen content in agricultural soils typically ranges from 10 to 50 ppm                                                                             | Randomly generated within the range of 10 to 50 ppm                                              |
| soil_p                    | Phosphorus content in agricultural soils typically ranges from 10 to 50 ppm                                                                           | Randomly generated within the range of 10 to 50 ppm                                              |
| temp                      | Indonesia has a tropical climate with average temperatures typically ranging from 25°C to 35°C throughout the year                                    | Randomly generated between 25°C to 35°C                                                          |
| rainfall                  | Indonesia experiences significant rainfall, especially during the rainy season, with monthly rainfall often ranging from 0 to 300 mm                  | Randomly generated between 0 to 300 mm                                                           |
| forecast_temp             | Indonesia has a tropical climate with average temperatures typically ranging from 25°C to 35°C throughout the year                                    | Randomly generated between 25°C to 35°C                                                          |
| forecast_rainfall         | Indonesia experiences significant rainfall, especially during the rainy season, with monthly rainfall often ranging from 0 to 300 mm                  | Randomly generated between 0 to 300 mm                                                           |
| crop_type                 | Common crops grown in Indonesia include wheat, corn, and rice, which have distinct growing requirements and nutrient needs                            | Randomly selected from wheat, corn, and rice                                                     |
| plant_health              | Common observable conditions in plants include healthy (vigorous growth), yellowing (possible nutrient deficiencies), and wilting (possible diseases) | Randomly selected as healthy, yellowing, or wilting                                              |
| optimal_fertilizer_amount | Influenced by soil nutrients, pH, weather conditions, and crop type                                                                                   | Calculated using a simplified formula based on the input features to provide realistic estimates |

## 4. Details of the Model Development Process, Including Choice of Techniques.

Due to time constraints, building a full end-to-end machine learning pipeline for data cleaning, feature engineering, model training, inferencing and deployment is not feasible. Hence, the model development process is a simplified version that still aims to provide clear and actionable recommendations for optimal fertilizer usage.

The simplified model development process is as follows:

1. **Splitting the dummy data into train and test sets using `train_test_split` from `scikit-learn`.** 67% train and 33% test proportion.

2. **Using `Pipeline` from `scikit-learn` to simplify the rest of the preprocessing steps.** This ensures that the same preprocessing steps are applied to both the training and test sets to prevent data leakage when training the model. The missing values are filled with the median, numeric outliers are scaled, and categorical values are encoded to numerical values.

3. **Training the `XGBRegressor` model with the processed training dataset.** The model is then used to make predictions on the test dataset, and the Root Mean Squared Error (RMSE) is calculated to determine the model’s prediction accuracy.

4. **Making a test prediction using just one row of data.** This is to test the model's outputs, which is predicting the optimal fertilizer amount based on given conditions.

5. **Saving the model to a separate folder.** This allows for the model to be reused later on.

## 5. Analysis of the Model Output and Practical Recommendations for Farmers

#### Model Performance

The model's performance is evaluated using Root Mean Squared Error (RMSE). A lower RMSE value indicates better predictive accuracy.

The RMSE of the model on the test dataset was 4.28. This indicates that, on average, the model’s predictions deviate from the actual optimal fertilizer amount by approximately 4.28 kg/ha.

In theory (ignoring the fact that dummy data was used and there was no hyperparameter tuning done), this means that the model’s predicted fertilizer amounts are accurate assuming that fertilizer usage rates are usually in the range of over 100 kg/ha.

#### Practical Recommendations for Farmers

As we now have a model that can predict optimal fertilizer amounts based on given conditions, there are two ways to provide practical recommendations to farmers:

#### 1. General Recommendations for Pre-Defined Scenarios

Use the model to recommend the optimal fertiliser amount for the following example scenarios, providing general recommendations based on pre-defined scenarios.

| Scenario   | Description                                                    | Conditions                                                                                                                                                                                                                                                                    | Predicted Optimal Fertilizer Amount |
| ---------- | -------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Scenario 1 | Yellowing wheat with low rainfall and low soil nutrient levels | Soil Color: dark brown <br> Soil pH: 5.8 <br> Soil Nitrogen: 15.0 ppm <br> Soil Phosphorus: 20.0 ppm <br> Temperature: 25.0°C <br> Rainfall: 10.0 mm <br> Forecasted Temperature: 27.0°C <br> Forecasted Rainfall: 60.0 mm <br> Crop Type: wheat <br> Plant Health: yellowing | 132.80 kg/ha                        |
| Scenario 2 | Healthy rice with high rainfall and high soil nutrient levels  | Soil Color: reddish <br> Soil pH: 7.0 <br> Soil Nitrogen: 45.0 ppm <br> Soil Phosphorus: 50.0 ppm <br> Temperature: 30.0°C <br> Rainfall: 200.0 mm <br> Forecasted Temperature: 32.0°C <br> Forecasted Rainfall: 210.0 mm <br> Crop Type: rice <br> Plant Health: healthy     | 105.19 kg/ha                        |
| Scenario 3 | Wilting wheat with very low nutrient levels and low rainfall   | Soil Color: light brown <br> Soil pH: 5.5 <br> Soil Nitrogen: 10.0 ppm <br> Soil Phosphorus: 10.0 ppm <br> Temperature: 25.0°C <br> Rainfall: 10.0 mm <br> Forecasted Temperature: 26.0°C <br> Forecasted Rainfall: 15.0 mm <br> Crop Type: wheat <br> Plant Health: wilting  | 136.64 kg/ha                        |

#### 2. Tailored Recommendations

Farmers can obtain more accurate and tailored fertilizer recommendation amounts by entering their own specific data into the model.

To demonstrate how farmers might access this model, I created a simple web app hosting the model using Streamlit. The app is deployed to the cloud and can be accessed via the following link:

https://dayataniassignment.streamlit.app/

## 6. A Presentation Summarizing the Project, Designed to Communicate the Findings to Both Technical and Non-technical Stakeholders

The slides summarising the project can be found in the `slides` folder of this repository
