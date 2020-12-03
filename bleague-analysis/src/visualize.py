from abc import ABCMeta, abstractmethod
from typing import Dict, Optional

import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py


class BasePlotly(metaclass=ABCMeta):
    colors = ["#3D0553", "#4D798C", "#7DC170", "#F7E642"]

    def _convert_to_str(self, arr: np.array) -> np.array:
        return np.array(arr, dtype=str)

    def _plotly_layout(
        self, title: str = None, xtitle: str = None, ytitle: str = None
    ) -> go.Layout:
        return go.Layout(
            title=title,
            xaxis=dict(title=xtitle, ticklen=5, zeroline=False, gridwidth=2),
            yaxis=dict(title=ytitle, ticklen=5, gridwidth=2),
        )

    @abstractmethod
    def show(self):
        pass


class BarPlotly(BasePlotly):
    def show(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol: str,
        is_horizontal: bool = False,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
    ):
        orientation = "v"
        color_col = ycol
        text_col = ycol
        if is_horizontal:
            orientation = "h"
            color_col = xcol
            text_col = xcol
        trace = [
            go.Bar(
                x=self._convert_to_str(data[xcol].values),
                y=data[ycol].values,
                text=data[text_col].values,
                textposition="auto",
                marker=dict(
                    color=data[color_col].values,
                    colorscale="Viridis",
                    showscale=True,
                    reversescale=True,
                ),
                orientation=orientation,
            )
        ]
        layout = self._plotly_layout(title=title, xtitle=xtitle, ytitle=ytitle)
        fig = go.Figure(data=trace, layout=layout)
        return py.iplot(fig, show_link=False)


class BoxPlotly(BasePlotly):
    def show(
        self,
        data: pd.DataFrame,
        xcol: Optional[str] = None,
        ycol: Optional[str] = None,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
    ):
        assert xcol is not None or ycol is not None
        if xcol is not None and ycol is not None:
            trace = [
                go.Box(
                    x=data[xcol].values,
                    y=data[ycol].values,
                    marker=dict(color=self.colors[0]),
                )
            ]
        elif xcol is None:
            trace = [go.Box(y=data[ycol].values, marker=dict(color=self.colors[0]))]
        elif ycol is None:
            trace = [go.Box(x=data[xcol].values, marker=dict(color=self.colors[0]))]
        layout = self._plotly_layout(title=title, xtitle=xtitle, ytitle=ytitle)
        fig = go.Figure(data=trace, layout=layout)
        return py.iplot(fig, show_link=False)


class CountPlotly(BasePlotly):
    def show(
        self,
        data: pd.DataFrame,
        xcol: str,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
    ):
        trace = [
            go.Histogram(
                x=data[xcol].values, histfunc="count", marker=dict(color=self.colors[0])
            )
        ]
        layout = self._plotly_layout(title=title, xtitle=xtitle, ytitle=ytitle)
        fig = go.Figure(data=trace, layout=layout)
        return py.iplot(fig, show_link=False)


class DistPlotly(BasePlotly):
    def show(
        self,
        data: pd.DataFrame,
        xcol: str,
        xbins: Optional[Dict[str, int]] = None,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
    ):
        """
        xbins: 区間の指定
            - start: 区間の始まり
            - end: 区間の終わり
            - size: 区間の幅
        """
        trace = [
            go.Histogram(
                x=data[xcol].values,
                histfunc="count",
                marker=dict(color=self.colors[0]),
                xbins=xbins,
            )
        ]
        layout = self._plotly_layout(title=title, xtitle=xtitle, ytitle=ytitle)
        fig = go.Figure(data=trace, layout=layout)
        return py.iplot(fig, show_link=False)


class LinePlotly(BasePlotly):
    def show(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol: str,
        linewidth: int = 2,
        rangeslider: bool = False,
        slider_type: str = "date",
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
    ):
        if rangeslider is True:
            xaxis = dict(
                title=xtitle,
                ticklen=5,
                zeroline=False,
                gridwidth=2,
                rangeslider=dict(visible=True),
                type=slider_type,
            )
        else:
            xaxis = dict(title=xtitle, ticklen=5, zeroline=False, gridwidth=2)

        if type(ycol) == list:
            trace = []
            for i in range(len(ycol)):
                t = go.Scatter(
                    x=data[xcol].values,
                    y=data[ycol[i]].values,
                    mode="lines",
                    name=data[ycol[i]].name,
                    line=dict(width=linewidth, color=self.colors[i]),
                )
                trace.append(t)
        else:
            trace = [
                go.Scatter(
                    x=data[xcol].values,
                    y=data[ycol].values,
                    mode="lines",
                    name=data[ycol].name,
                    line=dict(width=linewidth, color=self.colors[0]),
                )
            ]
        layout = go.Layout(
            title=title, xaxis=xaxis, yaxis=dict(title=ytitle, ticklen=5, gridwidth=2)
        )
        fig = go.Figure(data=trace, layout=layout)
        return py.iplot(fig, show_link=False)


class ScatterPlotly(BasePlotly):
    def show(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol: str,
        size: int = 1,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
    ):
        trace = [
            go.Scatter(
                x=self._convert_to_str(data[xcol].values),
                y=data[ycol].values,
                mode="markers",
                marker=dict(
                    sizemode="diameter",
                    sizeref=1,
                    size=data[ycol].values ** size,
                    color=data[ycol].values,
                    colorscale="Viridis",
                    reversescale=True,
                    showscale=True,
                ),
                text=self._convert_to_str(data[xcol].values),
            )
        ]
        layout = go.Layout(
            autosize=True,
            title=title,
            hovermode="closest",
            xaxis=dict(title=xtitle, ticklen=5, zeroline=False, gridwidth=2),
            yaxis=dict(title=ytitle, ticklen=5, gridwidth=2),
            showlegend=False,
        )
        fig = go.Figure(data=trace, layout=layout)
        return py.iplot(fig, show_link=False)
