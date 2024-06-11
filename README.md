# Agronomic-Decision-Support-System

### 1. Problem Formulation and Rationale

Many farmers rely on traditional knowledge and practices to determine the amount of fertilizer to use for their crops. However, too much fertilizer can lead to soil degradation and wasted resources, while too little fertilizer can result in poor crop growth and reduced yield. This makes it challenging for farmers to achieve the optimal balance needed to maximize crop yield, reduce costs, and minimize environmental impact.

The decision support system will provide recommendations based on easily obtainable data, including soil conditions, weather conditions, and crop types. Farmers can input these data into the decision support system, which will then provide real-time, tailored recommendations to help optimize fertilizer usage, achieving high crop yields while reducing costs and minimizing environmental impact.

### 2. The Data Schema and Rationale for the Types of Data Chosen

#### Data Schema

| Feature                   | Type   | Description                                                             |
| ------------------------- | ------ | ----------------------------------------------------------------------- |
| soil_color                | String | Qualitative measure of soil color (e.g., dark brown, reddish)           |
| soil_pH                   | Float  | Soil pH level                                                           |
| soil_N                    | Float  | Nitrogen content in soil (ppm)                                          |
| soil_P                    | Float  | Phosphorus content in soil (ppm)                                        |
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
| soil_pH                   | Influences nutrient availability; extreme pH levels can hinder plant growth.                                                                                  |
| soil_N                    | A primary nutrient for plant growth; helps determine fertilization needs.                                                                                     |
| soil_P                    | Essential for root development and energy transfer in plants.                                                                                                 |
| temp                      | Affects plant metabolic rates and nutrient uptake.                                                                                                            |
| rainfall                  | Influences soil moisture and nutrient availability.                                                                                                           |
| forecast_temp             | Useful for planning fertilizer application timing.                                                                                                            |
| forecast_rainfall         | Important for timing fertilizer application.                                                                                                                  |
| crop_type                 | Determines specific nutrient needs and growth patterns.                                                                                                       |
| plant_health              | Provides visible indicators that help diagnose nutrient deficiencies and other issues.                                                                        |
| optimal_fertilizer_amount | The target value that the decision support system aims to predict, helping farmers apply the right amount of fertilizer to maximize yield and minimize costs. |

### 3. The Methodology Used for Data Simulation

The approach to simulating the dummy data is based on using real-world typical values for soil content, weather patterns, crop type, and plant health so that the dummy data would reflect real-world conditions. This would make the dummy data useful enough to develop and test the decision support system.

| Feature                   | Assumption                                                                                                                                            | Method                                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| soil_color                | Mimics common soil color ranges                                                                                                                       | Randomly chosen from dark brown, reddish, light brown                                            |
| soil_pH                   | Typical soil pH values in agricultural areas range from 5.5 to 7.5                                                                                    | Randomly generated within the range of 5.5 to 7.5                                                |
| soil_N                    | Nitrogen content in agricultural soils typically ranges from 10 to 50 ppm                                                                             | Randomly generated within the range of 10 to 50 ppm                                              |
| soil_P                    | Phosphorus content in agricultural soils typically ranges from 10 to 50 ppm                                                                           | Randomly generated within the range of 10 to 50 ppm                                              |
| temp                      | Indonesia has a tropical climate with average temperatures typically ranging from 25°C to 35°C throughout the year                                    | Randomly generated between 25°C to 35°C                                                          |
| rainfall                  | Indonesia experiences significant rainfall, especially during the rainy season, with monthly rainfall often ranging from 0 to 300 mm                  | Randomly generated between 0 to 300 mm                                                           |
| forecast_temp             | Indonesia has a tropical climate with average temperatures typically ranging from 25°C to 35°C throughout the year                                    | Randomly generated between 25°C to 35°C                                                          |
| forecast_rainfall         | Indonesia experiences significant rainfall, especially during the rainy season, with monthly rainfall often ranging from 0 to 300 mm                  | Randomly generated between 0 to 300 mm                                                           |
| crop_type                 | Common crops grown in Indonesia include wheat, corn, and rice, which have distinct growing requirements and nutrient needs                            | Randomly selected from wheat, corn, and rice                                                     |
| plant_health              | Common observable conditions in plants include healthy (vigorous growth), yellowing (possible nutrient deficiencies), and wilting (possible diseases) | Randomly selected as healthy, yellowing, or wilting                                              |
| optimal_fertilizer_amount | Influenced by soil nutrients, pH, weather conditions, and crop type                                                                                   | Calculated using a simplified formula based on the input features to provide realistic estimates |
