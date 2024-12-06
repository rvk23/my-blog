import streamlit as st
import pandas as pd
import altair as alt


st.title("Welcome to My Streamlit App!")
st.write("This is a simple Streamlit app deployed using Streamlit Community Cloud.")



data = """
Season,Nickname,Home Win Percentage,Road Win Percentage
2017-18,Atlanta Hawks,0.317,0.244
2017-18,Boston Celtics,0.707,0.634
2017-18,Brooklyn Nets,0.341,0.317
2017-18,Charlotte Hornets,0.439,0.439
2017-18,Chicago Bulls,0.39,0.317
2017-18,Cleveland Cavaliers,0.707,0.707
2017-18,Dallas Mavericks,0.707,0.707
2017-18,Denver Nuggets,0.293,0.195
2017-18,Detroit Pistons,0.585,0.512
2017-18,Golden State Warriors,0.707,0.707
2017-18,Houston Rockets,0.707,0.707
2017-18,Indiana Pacers,0.78,0.78
2017-18,Los Angeles Clippers,0.707,0.707
2017-18,Los Angeles Lakers,0.439,0.439
2017-18,Memphis Grizzlies,0.293,0.195
2017-18,Miami Heat,0.585,0.512
2017-18,Milwaukee Bucks,0.585,0.512
2017-18,Minnesota Timberwolves,0.707,0.439
2017-18,New Orleans Pelicans,0.585,0.585
2017-18,New York Knicks,0.512,0.195
2017-18,Oklahoma City Thunder,0.707,0.512
2017-18,Orlando Magic,0.317,0.244
2017-18,Philadelphia 76ers,0.707,0.585
2017-18,Phoenix Suns,0.195,0.244
2017-18,Portland Trail Blazers,0.707,0.512
2017-18,Sacramento Kings,0.317,0.341
2017-18,San Antonio Spurs,0.78,0.439
2017-18,Toronto Raptors,0.78,0.634
2017-18,Utah Jazz,0.634,0.585
2017-18,Washington Wizards,0.585,0.512
2018-19,Atlanta Hawks,0.439,0.268
2018-19,Boston Celtics,0.659,0.463
2018-19,Brooklyn Nets,0.537,0.415
2018-19,Charlotte Hornets,0.610,0.268
2018-19,Chicago Bulls,0.317,0.195
2018-19,Cleveland Cavaliers,0.293,0.171
2018-19,Dallas Mavericks,0.585,0.220
2018-19,Denver Nuggets,0.780,0.512
2018-19,Detroit Pistons,0.610,0.341
2018-19,Golden State Warriors,0.683,0.707
2018-19,Houston Rockets,0.683,0.610
2018-19,Indiana Pacers,0.707,0.463
2018-19,Los Angeles Clippers,0.537,0.585
2018-19,Los Angeles Lakers,0.439,0.341
2018-19,Memphis Grizzlies,0.488,0.244
2018-19,Miami Heat,0.439,0.488
2018-19,Milwaukee Bucks,0.805,0.707
2018-19,Minnesota Timberwolves,0.585,0.244
2018-19,New Orleans Pelicans,0.585,0.244
2018-19,New York Knicks,0.232,0.171
2018-19,Oklahoma City Thunder,0.659,0.512
2018-19,Orlando Magic,0.610,0.390
2018-19,Philadelphia 76ers,0.732,0.488
2018-19,Phoenix Suns,0.244,0.171
2018-19,Portland Trail Blazers,0.707,0.537
2018-19,Sacramento Kings,0.537,0.439
2018-19,San Antonio Spurs,0.780,0.293
2018-19,Toronto Raptors,0.756,0.634
2018-19,Utah Jazz,0.659,0.488
2018-19,Washington Wizards,0.512,0.195
2019-20,Atlanta Hawks,0.463,0.293
2019-20,Boston Celtics,0.707,0.585
2019-20,Brooklyn Nets,0.463,0.512
2019-20,Charlotte Hornets,0.390,0.341
2019-20,Chicago Bulls,0.366,0.244
2019-20,Cleveland Cavaliers,0.268,0.220
2019-20,Dallas Mavericks,0.585,0.610
2019-20,Denver Nuggets,0.659,0.537
2019-20,Detroit Pistons,0.244,0.220
2019-20,Golden State Warriors,0.159,0.244
2019-20,Houston Rockets,0.659,0.512
2019-20,Indiana Pacers,0.707,0.488
2019-20,Los Angeles Clippers,0.707,0.585
2019-20,Los Angeles Lakers,0.707,0.707
2019-20,Memphis Grizzlies,0.537,0.463
2019-20,Miami Heat,0.610,0.537
2019-20,Milwaukee Bucks,0.829,0.683
2019-20,Minnesota Timberwolves,0.293,0.268
2019-20,New Orleans Pelicans,0.439,0.341
2019-20,New York Knicks,0.293,0.220
2019-20,Oklahoma City Thunder,0.610,0.610
2019-20,Orlando Magic,0.585,0.366
2019-20,Philadelphia 76ers,0.780,0.293
2019-20,Phoenix Suns,0.366,0.366
2019-20,Portland Trail Blazers,0.463,0.488
2019-20,Sacramento Kings,0.463,0.341
2019-20,San Antonio Spurs,0.366,0.415
2019-20,Toronto Raptors,0.780,0.707
2019-20,Utah Jazz,0.610,0.585
2019-20,Washington Wizards,0.415,0.268
2020-21,Atlanta Hawks,0.707,0.439
2020-21,Boston Celtics,0.561,0.439
2020-21,Brooklyn Nets,0.708,0.531
2020-21,Charlotte Hornets,0.561,0.341
2020-21,Chicago Bulls,0.366,0.463
2020-21,Cleveland Cavaliers,0.195,0.220
2020-21,Dallas Mavericks,0.561,0.561
2020-21,Denver Nuggets,0.667,0.514
2020-21,Detroit Pistons,0.317,0.220
2020-21,Golden State Warriors,0.652,0.439
2020-21,Houston Rockets,0.220,0.146
2020-21,Indiana Pacers,0.341,0.500
2020-21,Los Angeles Clippers,0.708,0.561
2020-21,Los Angeles Lakers,0.561,0.583
2020-21,Memphis Grizzlies,0.444,0.583
2020-21,Miami Heat,0.585,0.488
2020-21,Milwaukee Bucks,0.732,0.585
2020-21,Minnesota Timberwolves,0.341,0.317
2020-21,New Orleans Pelicans,0.500,0.341
2020-21,New York Knicks,0.707,0.512
2020-21,Oklahoma City Thunder,0.195,0.244
2020-21,Orlando Magic,0.317,0.244
2020-21,Philadelphia 76ers,0.805,0.585
2020-21,Phoenix Suns,0.750,0.708
2020-21,Portland Trail Blazers,0.500,0.611
2020-21,Sacramento Kings,0.366,0.390
2020-21,San Antonio Spurs,0.366,0.536
2020-21,Toronto Raptors,0.341,0.317
2020-21,Utah Jazz,0.833,0.611
2020-21,Washington Wizards,0.500,0.432
2021-22,Atlanta Hawks,0.707,0.293
2021-22,Boston Celtics,0.707,0.610
2021-22,Brooklyn Nets,0.561,0.610
2021-22,Charlotte Hornets,0.585,0.512
2021-22,Chicago Bulls,0.707,0.390
2021-22,Cleveland Cavaliers,0.610,0.439
2021-22,Dallas Mavericks,0.707,0.512
2021-22,Denver Nuggets,0.585,0.585
2021-22,Detroit Pistons,0.317,0.293
2021-22,Golden State Warriors,0.780,0.390
2021-22,Houston Rockets,0.293,0.195
2021-22,Indiana Pacers,0.293,0.244
2021-22,Los Angeles Clippers,0.585,0.439
2021-22,Los Angeles Lakers,0.439,0.366
2021-22,Memphis Grizzlies,0.780,0.707
2021-22,Miami Heat,0.707,0.610
2021-22,Milwaukee Bucks,0.707,0.537
2021-22,Minnesota Timberwolves,0.634,0.463
2021-22,New Orleans Pelicans,0.463,0.390
2021-22,New York Knicks,0.439,0.463
2021-22,Oklahoma City Thunder,0.244,0.317
2021-22,Orlando Magic,0.268,0.244
2021-22,Philadelphia 76ers,0.707,0.561
2021-22,Phoenix Suns,0.854,0.707
2021-22,Portland Trail Blazers,0.341,0.244
2021-22,Sacramento Kings,0.317,0.317
2021-22,San Antonio Spurs,0.439,0.463
2021-22,Toronto Raptors,0.707,0.537
2021-22,Utah Jazz,0.707,0.512
2021-22,Washington Wizards,0.512,0.317
2022-23,Atlanta Hawks,0.585,0.439
2022-23,Boston Celtics,0.707,0.634
2022-23,Brooklyn Nets,0.610,0.512
2022-23,Charlotte Hornets,0.366,0.293
2022-23,Chicago Bulls,0.537,0.390
2022-23,Cleveland Cavaliers,0.707,0.488
2022-23,Dallas Mavericks,0.561,0.439
2022-23,Denver Nuggets,0.707,0.561
2022-23,Detroit Pistons,0.220,0.195
2022-23,Golden State Warriors,0.707,0.317
2022-23,Houston Rockets,0.268,0.220
2022-23,Indiana Pacers,0.390,0.317
2022-23,Los Angeles Clippers,0.585,0.488
2022-23,Los Angeles Lakers,0.561,0.439
2022-23,Memphis Grizzlies,0.707,0.488
2022-23,Miami Heat,0.634,0.439
2022-23,Milwaukee Bucks,0.780,0.610
2022-23,Minnesota Timberwolves,0.561,0.439
2022-23,New Orleans Pelicans,0.561,0.366
2022-23,New York Knicks,0.634,0.512
2022-23,Oklahoma City Thunder,0.439,0.390
2022-23,Orlando Magic,0.390,0.341
2022-23,Philadelphia 76ers,0.707,0.561
2022-23,Phoenix Suns,0.634,0.488
2022-23,Portland Trail Blazers,0.439,0.293
2022-23,Sacramento Kings,0.634,0.512
2022-23,San Antonio Spurs,0.268,0.244
2022-23,Toronto Raptors,0.610,0.317
2022-23,Utah Jazz,0.561,0.439
2022-23,Washington Wizards,0.488,0.317
2023-24,Atlanta Hawks,0.600,0.400
2023-24,Boston Celtics,0.800,0.750
2023-24,Brooklyn Nets,0.500,0.400
2023-24,Charlotte Hornets,0.400,0.300
2023-24,Chicago Bulls,0.450,0.350
2023-24,Cleveland Cavaliers,0.650,0.450
2023-24,Dallas Mavericks,0.700,0.550
2023-24,Denver Nuggets,0.850,0.600
2023-24,Detroit Pistons,0.200,0.150
2023-24,Golden State Warriors,0.700,0.500
2023-24,Houston Rockets,0.500,0.350
2023-24,Indiana Pacers,0.600,0.450
2023-24,Los Angeles Clippers,0.550,0.500
2023-24,Los Angeles Lakers,0.650,0.450
2023-24,Memphis Grizzlies,0.500,0.300
2023-24,Miami Heat,0.650,0.400
2023-24,Milwaukee Bucks,0.750,0.650
2023-24,Minnesota Timberwolves,0.600,0.500
2023-24,New Orleans Pelicans,0.550,0.400
2023-24,New York Knicks,0.700,0.550
2023-24,Oklahoma City Thunder,0.500,0.450
2023-24,Orlando Magic,0.500,0.400
2023-24,Philadelphia 76ers,0.750,0.600
2023-24,Phoenix Suns,0.650,0.500
2023-24,Portland Trail Blazers,0.350,0.300
2023-24,Sacramento Kings,0.650,0.500
2023-24,San Antonio Spurs,0.300,0.250
2023-24,Toronto Raptors,0.600,0.400
2023-24,Utah Jazz,0.550,0.450
2023-24,Washington Wizards,0.400,0.300

"""

from io import StringIO
data_df = pd.read_csv(StringIO(data))

# App Title
st.title("NBA Home vs. Road Win Percentage Analysis")

# Sidebar for filters
st.sidebar.header("Filter Options")
selected_season = st.sidebar.selectbox(
    "Select a Season",
    sorted(data_df["Season"].unique())
)

# Filter data based on selected season
filtered_data = data_df[data_df["Season"] == selected_season]

# Display filtered data
st.write(f"### Data for Season {selected_season}")
st.dataframe(filtered_data)

# Create interactive chart
st.write("### Home vs Road Win Percentage")
chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X("Nickname:N", title="Team"),
    y=alt.Y("Home Win Percentage:Q", title="Win Percentage"),
    color=alt.value("steelblue"),
    tooltip=["Nickname", "Home Win Percentage", "Road Win Percentage"]
).properties(
    width=700,
    height=400,
    title="Home Win Percentage by Team"
)

# Add Road Win Percentage as a line chart
line = alt.Chart(filtered_data).mark_line(color="orange").encode(
    x=alt.X("Nickname:N"),
    y=alt.Y("Road Win Percentage:Q"),
    tooltip=["Nickname", "Home Win Percentage", "Road Win Percentage"]
)

# Combine both charts
st.altair_chart(chart + line)

# Additional insights
st.write("""
#### Insights:
- Use the sidebar to switch between seasons and compare team performance.
- Blue bars represent **Home Win Percentage**, while the orange line shows **Road Win Percentage**.
""")