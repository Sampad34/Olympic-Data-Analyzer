import pandas as pd


# data = pd.read_csv("athlete_events.csv")
# region_data = pd.read_csv("noc_regions.csv")


def preprocess(data, region_data):
    data = data[data["Season"] == "Summer"]

    data = data.merge(region_data, on="NOC", how="left")

    # remove duplicates
    data.drop_duplicates(inplace=True)

    # one hot encoding
    data = pd.concat([data, pd.get_dummies(data["Medal"])], axis=1)

    return data
