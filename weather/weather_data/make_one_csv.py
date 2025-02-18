import pandas as pd
import numpy as np
from getRecords import getWeatherCsv

def make_csv(csvFilePaths, outPath): 
    #
    df_list = []

    for file in csvFilePaths:
        df_in = pd.read_csv(file, sep=";")
        
        df_in = df_in.drop(columns=["PUNTORUGIADA °C", "VISIBILITA km",\
            "VENTOMEDIA km/h", "VENTOMAX km/h", "RAFFICA km/h", \
                "PRESSIONEMEDIA mb", "PIOGGIA mm"])

        # Note: The last 2 were dropped because always 0

        df_in["FENOMENI"].replace(np.nan, '', regex=True)
        df_in["FENOMENI"] = df_in["FENOMENI"].apply(mapFeature)

        df_in["STAGIONE"] = df_in["DATA"].apply(mapSeason)
        
        df_in = df_in.drop(columns=["DATA"])

        df_list.append(df_in)

    full_df = pd.concat(df_list)

    full_df = full_df.reset_index().drop(columns=["index"])

    full_df.to_csv(outPath, index=False)

def mapFeature(in_string):
    wordlist = str(in_string).split(" ")
    found = 0
    for wd in wordlist:
        if wd == "pioggia" or wd == "neve":
            found = 1
    return found

def mapSeason(in_string):
    mm = int(in_string.split('/')[1])
    if mm >= 1 and mm <= 2 or mm == 12:
        return "winter"
    elif mm >= 3 and mm <= 5:
        return "spring"
    elif mm >= 6 and mm <= 8:
        return "summer"
    else:
        return "fall"

########################################################################

if __name__ == "__main__":
    out_path = "weather_train.csv"

    years = list(range(2018, 2023))
    months = list(range(1, 13))
    city = "Torino"

    files_list = []

    for y in years:
        for m in months:
            files_list.append(getWeatherCsv(city, y, m))


    inputfilesList = [
        "csv_ilMeteo/Torino-2018-01Gennaio.csv",
        "csv_ilMeteo/Torino-2018-02Febbraio.csv",
        "csv_ilMeteo/Torino-2018-03Marzo.csv",
        "csv_ilMeteo/Torino-2018-04Aprile.csv",
        "csv_ilMeteo/Torino-2018-05Maggio.csv",
        "csv_ilMeteo/Torino-2018-06Giugno.csv",
        "csv_ilMeteo/Torino-2018-07Luglio.csv",
        "csv_ilMeteo/Torino-2018-08Agosto.csv",
        "csv_ilMeteo/Torino-2018-09Settembre.csv",
        "csv_ilMeteo/Torino-2018-10Ottobre.csv",
        "csv_ilMeteo/Torino-2018-11Novembre.csv",
        "csv_ilMeteo/Torino-2018-12Dicembre.csv",
        "csv_ilMeteo/Torino-2019-01Gennaio.csv",
        "csv_ilMeteo/Torino-2019-02Febbraio.csv",
        "csv_ilMeteo/Torino-2019-03Marzo.csv",
        "csv_ilMeteo/Torino-2019-04Aprile.csv",
        "csv_ilMeteo/Torino-2019-05Maggio.csv",
        "csv_ilMeteo/Torino-2019-06Giugno.csv",
        "csv_ilMeteo/Torino-2019-07Luglio.csv",
        "csv_ilMeteo/Torino-2019-08Agosto.csv",
        "csv_ilMeteo/Torino-2019-09Settembre.csv",
        "csv_ilMeteo/Torino-2019-10Ottobre.csv",
        "csv_ilMeteo/Torino-2019-11Novembre.csv",
        "csv_ilMeteo/Torino-2019-12Dicembre.csv",
        "csv_ilMeteo/Torino-2020-01Gennaio.csv",
        "csv_ilMeteo/Torino-2020-02Febbraio.csv",
        "csv_ilMeteo/Torino-2020-03Marzo.csv",
        "csv_ilMeteo/Torino-2020-04Aprile.csv",
        "csv_ilMeteo/Torino-2020-05Maggio.csv",
        "csv_ilMeteo/Torino-2020-06Giugno.csv",
        "csv_ilMeteo/Torino-2020-07Luglio.csv",
        "csv_ilMeteo/Torino-2020-08Agosto.csv",
        "csv_ilMeteo/Torino-2020-09Settembre.csv",
        "csv_ilMeteo/Torino-2020-10Ottobre.csv",
        "csv_ilMeteo/Torino-2020-11Novembre.csv",
        "csv_ilMeteo/Torino-2020-12Dicembre.csv",
        "csv_ilMeteo/Torino-2021-01Gennaio.csv",
        "csv_ilMeteo/Torino-2021-02Febbraio.csv",
        "csv_ilMeteo/Torino-2021-03Marzo.csv",
        "csv_ilMeteo/Torino-2021-04Aprile.csv",
        "csv_ilMeteo/Torino-2021-05Maggio.csv",
        "csv_ilMeteo/Torino-2021-06Giugno.csv",
        "csv_ilMeteo/Torino-2021-07Luglio.csv",
        "csv_ilMeteo/Torino-2021-08Agosto.csv",
        "csv_ilMeteo/Torino-2021-09Settembre.csv",
        "csv_ilMeteo/Torino-2021-10Ottobre.csv",
        "csv_ilMeteo/Torino-2021-11Novembre.csv",
        "csv_ilMeteo/Torino-2021-12Dicembre.csv",
        "csv_ilMeteo/Torino-2022-01Gennaio.csv",
        "csv_ilMeteo/Torino-2022-02Febbraio.csv",
        "csv_ilMeteo/Torino-2022-03Marzo.csv",
        "csv_ilMeteo/Torino-2022-04Aprile.csv",
        "csv_ilMeteo/Torino-2022-05Maggio.csv",
        "csv_ilMeteo/Torino-2022-06Giugno.csv",
        "csv_ilMeteo/Torino-2022-07Luglio.csv",
        "csv_ilMeteo/Torino-2022-08Agosto.csv",
        "csv_ilMeteo/Torino-2022-09Settembre.csv",
        "csv_ilMeteo/Torino-2022-10Ottobre.csv",
        "csv_ilMeteo/Torino-2022-11Novembre.csv",
        "csv_ilMeteo/Torino-2022-12Dicembre.csv"
    ]
    
    make_csv(files_list, out_path)
