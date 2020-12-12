from abc import ABCMeta, abstractmethod
from typing import Dict, List, Optional, Union

import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as py


class BasePlotly(metaclass=ABCMeta):
    colors = ["#3D0553", "#4D798C", "#7DC170", "#F7E642"]

    def __init__(self, is_debug=False):
        self.is_debug = is_debug

    def _convert_to_str(self, arr: np.array) -> np.array:
        return np.array(arr, dtype=str)

    def _scale(self, x: np.array) -> np.array:
        rate = np.max(x) / 10
        return x / rate

    @abstractmethod
    def _plotly_trace(self) -> List[Union[go.Bar, go.Box, go.Histogram, go.Scatter]]:
        pass

    def _plotly_layout(
        self,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        data: Optional[pd.DataFrame] = None,
        ycol: Optional[List[str]] = None,
        **kwargs,
    ) -> go.Layout:
        return go.Layout(
            title=title,
            xaxis=dict(title=xtitle, ticklen=5, zeroline=False, gridwidth=2),
            yaxis=dict(title=ytitle, ticklen=5, gridwidth=2),
        )

    def _save(self, fig: go.Figure, path: str):
        fig.write_image(path, width=1200, height=600)

    def show(
        self,
        data: pd.DataFrame,
        xcol: Optional[str] = None,
        ycol: Optional[Union[str, List[str]]] = None,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
        **kwargs,
    ):
        trace = self._plotly_trace(
            data=data,
            xcol=xcol,
            ycol=ycol,
            title=title,
            xtitle=xtitle,
            ytitle=ytitle,
            save_path=save_path,
            **kwargs,
        )
        layout = self._plotly_layout(
            title=title, xtitle=xtitle, ytitle=ytitle, data=data, ycol=ycol, **kwargs
        )
        fig = go.Figure(data=trace, layout=layout)
        if save_path is not None:
            self._save(fig, save_path)
        return py.iplot(fig, show_link=False)


class BarPlotly(BasePlotly):
    def _plotly_trace(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol: str,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
        is_horizontal: bool = False,
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
        return trace


class BoxPlotly(BasePlotly):
    def _plotly_trace(
        self,
        data: pd.DataFrame,
        xcol: Optional[str] = None,
        ycol: Optional[str] = None,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
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
        return trace


class CountPlotly(BasePlotly):
    def _plotly_trace(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol=None,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
    ):
        trace = [
            go.Histogram(
                x=data[xcol].values, histfunc="count", marker=dict(color=self.colors[0])
            )
        ]
        return trace


class DistPlotly(BasePlotly):
    def _plotly_trace(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol=None,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
        xbins: Optional[Dict[str, int]] = None,
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
        return trace


class LinePlotly(BasePlotly):
    def _plotly_trace(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol: Union[str, List[str]],
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
        linewidth: int = 2,
    ):
        if type(ycol) == list:
            trace = []
            for i in range(len(ycol)):
                color = self.colors[i] if len(self.colors) >= len(ycol) else None
                t = go.Scatter(
                    x=data[xcol].values,
                    y=data[ycol[i]].values,
                    mode="lines",
                    name=data[ycol[i]].name,
                    line=dict(width=linewidth, color=color),
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
        return trace

    def _plotly_layout(
        self,
        title,
        xtitle,
        ytitle,
        data,
        ycol,
        rangeslider: bool = False,
        slider_type: str = "date",
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

        yaxis_range_min = (
            0
            if data.loc[:, ycol].values.min() > 0
            else data.loc[:, ycol].values.min() * 1.05
        )
        yaxis_range_max = data.loc[:, ycol].values.max() * 1.05
        layout = go.Layout(
            title=title,
            xaxis=xaxis,
            yaxis=dict(
                title=ytitle,
                ticklen=5,
                gridwidth=2,
                range=[yaxis_range_min, yaxis_range_max],
            ),
        )
        return layout


class ScatterPlotly(BasePlotly):
    def _plotly_trace(
        self,
        data: pd.DataFrame,
        xcol: str,
        ycol: str,
        title: Optional[str] = None,
        xtitle: Optional[str] = None,
        ytitle: Optional[str] = None,
        save_path: Optional[str] = None,
        size_col: Optional[int] = None,
        text_col: Optional[int] = None,
    ):
        if len(data) > 5000:
            print("[WARNING] data size is too large for scatterplot to display")
            data = data.sample(5000, random_state=42)
        size = None
        sizeref = None
        if size_col is not None:
            size = self._scale(data[size_col].values)
            sizeref = 2.0 * max(size) / ((max(size) / 2) ** 2)
        text = None
        if text_col is not None:
            text = self._convert_to_str(data[text_col].values)
        trace = [
            go.Scatter(
                x=self._convert_to_str(data[xcol].values),
                y=data[ycol].values,
                mode="markers",
                marker=dict(
                    sizemode="diameter",
                    sizeref=sizeref,
                    size=size,
                    color=data[ycol].values,
                    colorscale="Viridis",
                    reversescale=True,
                    showscale=True,
                ),
                text=text,
            )
        ]
        return trace

    def _plotly_layout(self, title, xtitle, ytitle, data=None, ycol=None, **kwargs):
        layout = go.Layout(
            autosize=True,
            title=title,
            hovermode="closest",
            xaxis=dict(title=xtitle, ticklen=5, zeroline=False, gridwidth=2),
            yaxis=dict(title=ytitle, ticklen=5, gridwidth=2),
            showlegend=False,
        )
        return layout
