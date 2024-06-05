import data_processing as dp
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns

def plot_gdp_vs_temp(merged):
    avrg_gdp = merged["GDP growth (annual %)"].mean()
    avrg_temp = merged["Temperature anomaly"].mean()

    plt.figure(figsize=(12, 6))
    plt.plot(merged["Year"], merged["GDP growth (annual %)"], label="GDP Growth (annual %)")
    plt.plot(merged["Year"], merged["Temperature anomaly"], label="Temperature anomaly")
    plt.axhline(y=avrg_gdp, color='r', linestyle='--', label='Average GDP Growth')
    plt.axhline(y=avrg_temp, color='g', linestyle='--', label='Average Temperature Anomally')
    plt.xlabel('Year')
    plt.ylabel('Value')
    plt.title('Global Temperature Anomaly and GDP Growth Over Time')
    plt.legend()
    plt.show()

def plot_country_gdp_temp(merged, major_country):
    correlations = {}

    fig, axes = plt.subplots(nrows=len(major_country), ncols=1, figsize=(12, 6 * len(major_country)))

    for i, code in enumerate(major_country):
        df = merged[merged["Country Code"] == code]
        ax = axes[i] if len(major_country) > 1 else axes
        ax.plot(df['Year'], df['Temperature anomaly'], label='Temperature anomaly', color='red')
        ax.set_xlabel('Year')
        ax.set_ylabel('Temperature anomaly', color='red')
        ax2 = ax.twinx()
        ax2.plot(df['Year'], df['GDP growth (annual %)'], label='GDP growth (annual %)', color='blue')
        ax2.set_ylabel('GDP Growth (annual %)', color='blue')
        ax.set_title(f'{code}: Temperature anomaly and GDP Growth (annual %)')
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        cor = df[["Temperature anomaly", "GDP growth (annual %)"]].corr().iloc[0, 1]
        correlations[code] = cor

    plt.tight_layout()
    plt.show()

    for code, correlation in correlations.items():
        print(f"{code}: {correlation}")
        
def plot_industry_vs_gdp_vs_temp(merged):
    plt.figure(figsize=(12, 6))
    plt.plot(merged["Year"], merged["Industry Value (annual %)"], label="Industry Value (annual %)")
    plt.plot(merged["Year"], merged["GDP growth (annual %)"], label="GDP growth (annual %)")
    plt.plot(merged["Year"], merged["Temperature anomaly"], label="Temperature anomaly")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.title("GDP growth vs Temperature Anomaly vs Industry Value")
    plt.legend()
    plt.show()

def plot_country_gdp_industry(merged, major_country):
    correlations = {}

    fig, axes = plt.subplots(nrows=len(major_country), ncols=1, figsize=(12, 6 * len(major_country)))

    for i, code in enumerate(major_country):
        df = merged[merged["Country Code"] == code]
        ax = axes[i] if len(major_country) > 1 else axes
        ax.plot(df['Year'], df['Industry Value (annual %)'], label='Industry Value (annual %)', color='green')
        ax.set_xlabel('Year')
        ax.set_ylabel('Industry Value (annual %)', color='green')
        ax2 = ax.twinx()
        ax2.plot(df['Year'], df['GDP growth (annual %)'], label='GDP growth (annual %)', color='blue')
        ax2.set_ylabel('GDP Growth (annual %)', color='blue')
        ax.set_title(f'{code}: Industry Value and GDP Growth (annual %)')
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        cor = df[["Industry Value (annual %)", "GDP growth (annual %)"]].corr().iloc[0, 1]
        correlations[code] = cor

    plt.tight_layout()
    plt.show()

    for code, correlation in correlations.items():
        print(f"{code}: {correlation}")


def plot_co2_vs_gdp_vs_temp(merged):
    plt.figure(figsize=(12, 6))
    plt.plot(merged["Year"], merged["CO2 emission growth"], label="CO2 emission growth")
    plt.plot(merged["Year"], merged["GDP growth (annual %)"], label="GDP growth (annual %)")
    plt.plot(merged["Year"], merged["Temperature anomaly"], label="Temperature anomaly")
    plt.xlabel("Year")
    plt.ylabel("Value")
    plt.title("GDP growth vs Temperature Anomaly vs CO2 emission growth")
    plt.legend()
    plt.show()
    
def plot_country_gdp_co2(merged, major_country):
    correlations = {}

    fig, axes = plt.subplots(nrows=len(major_country), ncols=1, figsize=(12, 6 * len(major_country)))

    for i, code in enumerate(major_country):
        df = merged[merged["Country Code"] == code]
        ax = axes[i] if len(major_country) > 1 else axes
        ax.plot(df['Year'], df['CO2 emission growth'], label='CO2 emission growth', color='purple')
        ax.set_xlabel('Year')
        ax.set_ylabel('CO2 Emission Growth', color='purple')
        ax2 = ax.twinx()
        ax2.plot(df['Year'], df['GDP growth (annual %)'], label='GDP growth (annual %)', color='blue')
        ax2.set_ylabel('GDP Growth (annual %)', color='blue')
        ax.set_title(f'{code}: CO2 Emission Growth and GDP Growth (annual %)')
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        cor = df[["CO2 emission growth", "GDP growth (annual %)"]].corr().iloc[0, 1]
        correlations[code] = cor

    plt.tight_layout()
    plt.show()

    for code, correlation in correlations.items():
        print(f"{code}: {correlation}")
       
def perform_regression_analysis(merged_world):
    X = merged_world[["Temperature anomaly", "CO2 emission growth", "Disasters"]]
    y = merged_world["GDP growth (annual %)"]

    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    print(model.summary())
    
    return model, X, y


    
def main():
    world_gdp, world_temp, world_industry, world_co2, disaster, major_country, annual_gdp, annual_temp, annual_co2, annual_industry = dp.load_and_clean_data()
    merged_world = dp.merge_data(world_gdp, world_temp, world_industry, world_co2, disaster)
    merged_country = dp.merge_country_data(annual_gdp, annual_temp, major_country)
    merged_gdp_industry = dp.merged_gdp_industry(annual_gdp, annual_industry, major_country)
    merged_gdp_co2 = dp.merged_gdp_co2(annual_gdp, annual_co2, major_country)\
    
    plot_gdp_vs_temp(merged_world)
    plot_country_gdp_temp(merged_country, major_country)
    plot_industry_vs_gdp_vs_temp(merged_world)
    plot_country_gdp_industry(merged_gdp_industry, major_country)
    plot_co2_vs_gdp_vs_temp(merged_world)
    plot_country_gdp_co2(merged_gdp_co2, major_country)
    perform_regression_analysis(merged_world)
    
    
if __name__ == "__main__":
    main()

