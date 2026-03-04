import pandas as pd

def aqi_category(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Poor"
    elif aqi <= 400:
        return "Very Poor"
    else:
        return "Severe"


def reflex_agent(file):

    data = pd.read_csv(file)

    pollutants = ["PM2.5","PM10","NO2","SO2","CO","O3"]

    for index,row in data.iterrows():

        values = []

        for p in pollutants:
            if p in row and not pd.isna(row[p]):
                values.append(row[p])

        if len(values)==0:
            continue

        aqi = max(values)

        print("Sensor Readings:")
        for p in pollutants:
            print(p,":",row[p])

        print("Calculated AQI:", round(aqi))
        print("AQI Category:", aqi_category(aqi))
        print("----------------------")

        if index > 5:
            break


reflex_agent("city_day.csv")