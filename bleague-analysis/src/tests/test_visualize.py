import seaborn as sns
from src.visualize import (
    BarPlotly,
    BoxPlotly,
    CountPlotly,
    DistPlotly,
    LinePlotly,
    ScatterPlotly,
)


def test_bar_plotly():
    df = sns.load_dataset("iris")
    df_agg = df.groupby("species")["sepal_length"].mean().round(2)
    df_agg = df_agg.reset_index()
    BarPlotly().show(df_agg, xcol="species", ycol="sepal_length", is_horizontal=False)
    BarPlotly().show(df_agg, ycol="species", xcol="sepal_length", is_horizontal=True)


def test_box_plotly():
    df = sns.load_dataset("iris")
    BoxPlotly().show(df, xcol="species", ycol="sepal_length")
    BoxPlotly().show(df, xcol="sepal_length")
    BoxPlotly().show(df, ycol="sepal_length")


def test_count_plotly():
    df = sns.load_dataset("iris")
    CountPlotly().show(df, xcol="species")


def test_dist_plotly():
    df = sns.load_dataset("iris")
    DistPlotly().show(df, xcol="sepal_length")
    DistPlotly().show(df, xcol="sepal_length", xbins={"size": 0.25})


def test_line_plotly():
    LinePlotly()


def test_scatter_plotly():
    df = sns.load_dataset("diamonds")
    ScatterPlotly().show(df, xcol="carat", ycol="price")
    ScatterPlotly().show(df, xcol="carat", ycol="price", size_col="price")
    ScatterPlotly().show(df, xcol="carat", ycol="price", text_col="price")
