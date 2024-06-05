# 프로젝트 주제 
이 프로젝트는 전 세계와 미국이나 중국 같은 특정 국가의 GDP 성장률이 기온 상승과 CO2 배출량, 재해 발생량 간의 어떤 상관관계가 있는지 분석한 것이다. 

# 준비물
## 라이브러리 및 설치
이 프로젝트를 실행하기 위해 아래 라이브러리가 필요하다:
- "pandas"
- "statsmodels"
- "matplotlib"

아래 명령어를 터미널에 입력해  라이브러리를 설치할 수 있다:

> pip install pandas statsmodel matplotlib

## 데이터 파일 
이 프로젝트 폴더에는 다음과 같은 데이터 파일이 있다.
- "annual_country_industry.csv"
- "annual_gdp.csv"
- "annual_temperature_anomalies.csv"
- "change_co2_annual_pct.csv"
- "natural_disaster_events.csv"

### 만약 해당하는 파일이 없다면 아래와 같은 절차를 거친다.
1. 아래 링크를 통해 프로젝트 파일에 없는 데이터를 다운 받아 폴더에 넣는다.
- "Our World in Data"
    - ["annual_temperature_anomalies.csv"](https://ourworldindata.org/grapher/annual-temperature-anomalies)
    - ["change_co2_annual_pct.csv"](https://ourworldindata.org/grapher/change-co2-annual-pct?tab=chart)
    - ["natural_disaster_events.csv"](https://ourworldindata.org/grapher/number-of-natural-disaster-events)
- "The World Bank"
    - ["annual_gdp.csv"](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG)
    - ["annual_country_industry.csv"](https://data.worldbank.org/indicator/NV.IND.TOTL.KD.ZG?view=chart) 

> [NOTE]: 
> The World Bank에서 csv 파일을 다운 받으면 압축된 파일로 다운된다. 이때 파일 압축을 풀고 제일 위에 있은 API로 시작하는 파일만 프로젝트 폴더에 넣어 둔다

2. 그 후 다운 받은 데이터들을 위에 말한 데이터 파일 이름과 똑같이 바꿔준다. (안그러면 데이터 이름과 코드에 적은 이름이 달라 에러난다) 

3. 다운 받은 파일의 이름까지 바꾸었다면 파일을 클릭하여 잘 다운 받았는지 확인하고 혹여나 파일 상단 부분에 업데이트 날짜나 데이터 출저 같은 설명이 있다면 이를 지워준다. (안그러면 csv로 파일 읽을 때 에러난다)

## 프로젝트 파일

### "data_processing.py"
이 파일에서는 데이터 로드, 정리 및 병합하는 함수를 가지는 파일이다:
- load_and_clean_data(): 데이터셋을 로드하고 정리한다.
- merge_data(world_gdp, world_temp, world_industry, world_co2, disaster): 세계에 대해 준비한 모든 데이터셋을 병합한다.
- merge_country_data(annual_gdp, annual_temp, major_country): 주요 국가의 GDP와 Temperature anomlay 데이터를 병합한다.
- merged_gdp_industry(annual_gdp, annual_industry, major_country): 주요 국가의 GDP와 Industry Value 데이터를 병합한다.
- merged_gdp_co2(annual_gdp, annual_co2, major_country): 주요 국가의 GDP와 CO2 emission 데이터를 병합한다.

### "main_analysis.py"
이 파일에서는 데이터를 시각화하고 분석한다:
- plot_gdp_vs_temp(merged): 세계 GDP 성장률과 온도 이상을 시각화한다.
- plot_country_gdp_temp(merged, major_country): 주요 국가의 GDP 성장률과 온도 이상을 시각화한다.
- plot_industry_vs_gdp_vs_temp(merged): 산업 가치와 GDP 성장률 및 온도 이상을 시각화한다.
- plot_country_gdp_industry(merged, major_country): 주요 국가의 산업 가치와 GDP 성장률을 시각화한다.
- plot_co2_vs_gdp_vs_temp(merged): CO2 배출량 성장률과 GDP 성장률 및 온도 이상을 시각화한다.
- plot_country_gdp_co2(merged, major_country): 주요 국가의 CO2 배출량 성장률과 GDP 성장률을 시각화한다.
- perform_regression_analysis(merged_world): 최종적으로 세계 GDP에 대하여 온도 이상과 CO2 배출량, 재난 발생률에 대한 다중 회귀 분석을 수행한다.

### "test.py"
이 파일은 data_processing.py와 main_analysis.py의 함수를 테스트한다:

# 프로젝트 실행 방법

1. 데이터 파일을 프로젝트 디렉토리에 넣는다. (프로젝트 파일이 정상적으로 다운받아졌다면 이 단계는 스킵해도 된다)

2. 테스트 파일을 터미널에서 실행하여 문제가 없는지 확인한다.아래 문장을 터미널에 입력하면 된다
    > python test.py

    'No problem :b' 가 뜬다면 정상적으로 작동하는 것이다. 

3. 정상적으로 잘 작동한다면 아래 명령어를 터미널에 입력해 최종적인 결과물을 확인한다. 
    > python main_analysis.py

    이 명령을 통해 질문에 대한 시각화 결과가 생성되고 회귀 분석 요약이 콘솔에 출력된다.
    
# 참고
- final.inpynb 파일은 본 프로젝트의 테스트에 활용한 것임으로 신경 안써도 된다. :b 