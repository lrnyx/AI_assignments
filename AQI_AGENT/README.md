AQI Reflex Agent

This program implements a simple reflex agent that calculates the Air Quality Index (AQI) using pollution data.
Instead of real sensors, a dataset file is used as input.

Dataset
The dataset used is taken from Kaggle (Air Quality Data in India). It contains pollution values measured in different cities.

The pollutants used in the program are:
PM2.5
PM10
NO2
SO2
CO
O3

How the Program Works
The program reads pollution values from the dataset file. Each row represents a set of sensor readings.
The agent checks these values and determines the AQI category.

The AQI categories are:
0–50 Good
51–100 Moderate
101–200 Unhealthy
201–300 Poor
301–400 Very Poor
401–500 Severe




Environmental sensor data was obtained from the Kaggle dataset “Air Quality Data in India.” The dataset contains pollutant concentrations such as PM2.5, PM10, NO₂, SO₂, CO, and O₃ collected from monitoring stations. These values simulate environmental sensors. A simple reflex agent reads the pollutant data from the dataset file and applies rule-based logic to determine the Air Quality Index (AQI) and its category.