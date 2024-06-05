import pandas as pd

def load_and_clean_data():
    major_country = ["KOR", "CHN", "IND", "JPN", "USA", "RUS"]
    # Load GDP Data
    annual_gdp = pd.read_csv("annual_gdp.csv")
    annual_gdp = annual_gdp[["Country Name", "Country Code"] 
                            + [str(year) for year in range(1960, 2023)]]
    annual_gdp = annual_gdp.melt(id_vars=["Country Name", "Country Code"], 
                                 var_name="Year", 
                                 value_name="GDP growth (annual %)")
    annual_gdp["Year"] = annual_gdp["Year"].astype(int)
    world_gdp = annual_gdp[annual_gdp["Country Name"] == "World"]
    
    # Load Temperature Anomalies data
    annual_temp = pd.read_csv("annual_temperature_anomalies.csv")
    annual_temp = annual_temp.rename(columns={"Entity": "Country Name", 
                                              "Code": "Country Code"})
    annual_temp = annual_temp[(annual_temp["Year"] >= 1960) 
                              & (annual_temp["Year"] < 2023)]
    world_temp = annual_temp[annual_temp["Country Name"] == "World"]
    
    # Load Industry data
    annual_industry = pd.read_csv("annual_country_industry.csv")
    annual_industry = annual_industry[["Country Name", "Country Code"] 
                                      + [str(year) for year in range(1995, 2023)]]
    annual_industry = annual_industry.melt(id_vars=["Country Name", "Country Code"],
                                           var_name="Year",
                                           value_name="Industry Value (annual %)")
    annual_industry["Year"] = annual_industry["Year"].astype(int)
    world_industry = annual_industry[annual_industry["Country Name"] == "World"]
    
    # Load CO2 Emissions data
    annual_co2 = pd.read_csv("change_co2_annual_pct.csv")
    annual_co2 = annual_co2.rename(columns={"Entity": "Country Name", 
                                            "Code": "Country Code", "Annual CO₂ emissions growth (%)": "CO2 emission growth"})
    annual_co2 = annual_co2[(annual_co2["Year"] >= 1960) 
                            & (annual_co2["Year"] < 2023)]
    world_co2 = annual_co2[annual_co2["Country Name"] == "World"]
    
    # Load Disasters data
    disaster = pd.read_csv("natural_disaster_events.csv")
    disaster = disaster[(disaster["Year"] < 2023) & (disaster["Year"] >= 1960)]
    disaster = disaster.rename(columns={"Entity": "Type"})
    disaster = disaster[["Type", "Year", "Disasters"]]
    disaster = disaster[disaster["Type"] == "All disasters excluding earthquakes"]

    return world_gdp, world_temp, world_industry, world_co2, disaster, major_country, annual_gdp, annual_temp, annual_co2, annual_industry


def merge_country_data(annual_gdp, annual_temp, major_country):
    # Merge country-specific data
    merged = pd.merge(annual_gdp[annual_gdp["Country Code"].isin(major_country)],
                      annual_temp[annual_temp["Country Code"].isin(major_country)],
                      on=["Country Code", "Year"])
    merged = merged.dropna()
    
    return merged

def merge_data(world_gdp, world_temp, world_industry, world_co2, disaster):
    # Merge global data
    merged_world = pd.merge(world_gdp, world_temp, on=["Country Name", "Year"])
    merged_world = merged_world[["Country Name", "Year", "GDP growth (annual %)", "Temperature anomaly"]]
    merged_world = pd.merge(merged_world, world_co2, on=["Country Name", "Year"])
    merged_world = pd.merge(merged_world, disaster, on=["Year"])
    merged_world = pd.merge(merged_world, world_industry[["Country Name", "Year", "Industry Value (annual %)"]], on=["Country Name", "Year"])
    merged_world = merged_world.dropna()

    return merged_world

def merged_gdp_industry(annual_gdp, annual_industry, major_country):
    merged_gdp_industry = pd.merge(annual_gdp[annual_gdp["Country Code"].isin(major_country)],
                                   annual_industry[annual_industry["Country Code"].isin(major_country)],
                                   on=["Country Code", "Year"])
    merged_gdp_industry = merged_gdp_industry.dropna()
    return merged_gdp_industry

def merged_gdp_co2(annual_gdp, annual_co2, major_country):
    merged_gdp_co2 = pd.merge(annual_gdp[annual_gdp["Country Code"].isin(major_country)],
                              annual_co2[annual_co2["Country Code"].isin(major_country)],
                              on=["Country Code", "Year"])
    merged_gdp_co2 = merged_gdp_co2.dropna()
    return merged_gdp_co2