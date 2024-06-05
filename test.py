import data_processing as dp
import main_analysis
import pandas as pd

def test_load_and_clean_data():
    data = dp.load_and_clean_data()
    assert len(data) == 10, "Data loading fail. there are 10 DataFrames"

def test_merge_data():
    world_gdp, world_temp, world_industry, world_co2, disaster, _, _, _, _, _ = dp.load_and_clean_data()
    merged = dp.merge_data(world_gdp, world_temp, world_industry, world_co2, disaster)
    assert isinstance(merged, pd.DataFrame), "Merged Data is not type:dataframe"
    assert not merged.empty, "Merged data is empty"

def test_merge_country_data():
    _, _, _, _, _, major_country, annual_gdp, annual_temp, _, _ = dp.load_and_clean_data()
    merged = dp.merge_country_data(annual_gdp, annual_temp, major_country)
    assert isinstance(merged, pd.DataFrame), "Merged Country Data is not type:dataframe"
    assert not merged.empty, "Merged Country Data is empty"

def test_merged_gdp_industry():
    _, _, _, _, _, major_country, annual_gdp, _, _, annual_industry = dp.load_and_clean_data()
    merged = dp.merged_gdp_industry(annual_gdp, annual_industry, major_country)
    assert isinstance(merged, pd.DataFrame), "Merged gdp vs industry Data is not type:dataframe"
    assert not merged.empty, "Merged gdp vs industry Data is empty"

def test_merged_gdp_co2():
    _, _, _, _, _, major_country, annual_gdp, _, annual_co2, _ = dp.load_and_clean_data()
    merged = dp.merged_gdp_co2(annual_gdp, annual_co2, major_country)
    assert isinstance(merged, pd.DataFrame), "Merged gdp vs co2 Data is not type:dataframe"
    assert not merged.empty, "Merged gdp vs co2 Data is empty"

def test_visualization_functions():
    world_gdp, world_temp, world_industry, world_co2, disaster, major_country, annual_gdp, annual_temp, annual_co2, annual_industry = dp.load_and_clean_data()
    merged_world = dp.merge_data(world_gdp, world_temp, world_industry, world_co2, disaster)
    merged_country = dp.merge_country_data(annual_gdp, annual_temp, major_country)
    merged_gdp_industry = dp.merged_gdp_industry(annual_gdp, annual_industry, major_country)
    merged_gdp_co2 = dp.merged_gdp_co2(annual_gdp, annual_co2, major_country)
    
    main_analysis.plot_gdp_vs_temp(merged_world)
    main_analysis.plot_country_gdp_temp(merged_country, major_country)
    main_analysis.plot_industry_vs_gdp_vs_temp(merged_world)
    main_analysis.plot_country_gdp_industry(merged_gdp_industry, major_country)
    main_analysis.plot_co2_vs_gdp_vs_temp(merged_world)
    main_analysis.plot_country_gdp_co2(merged_gdp_co2, major_country)

def test_perform_regression_analysis():
    world_gdp, world_temp, world_industry, world_co2, disaster, _, _, _, _, _ = dp.load_and_clean_data()
    merged_world = dp.merge_data(world_gdp, world_temp, world_industry, world_co2, disaster)
    model, X, y = main_analysis.perform_regression_analysis(merged_world)
    assert model is not None, "model failed"
    assert not X.empty, "value is empty"
    assert not y.empty, "target data is empty"

def run_tests():
    test_load_and_clean_data()
    test_merge_data()
    test_merge_country_data()
    test_merged_gdp_industry()
    test_merged_gdp_co2()
    test_visualization_functions()
    test_perform_regression_analysis()
    print("No problem :b")

if __name__ == "__main__":
    run_tests()
