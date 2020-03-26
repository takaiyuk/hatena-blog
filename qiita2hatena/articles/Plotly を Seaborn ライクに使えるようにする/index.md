https://qiita.com/takaiyuk/items/e68c493642adfb04310e

2019-01-20T22:00:28+09:00

2019-11-25T22:44:23+09:00


<h2>
<span id="tldr" class="fragment"></span><a href="#tldr"><i class="fa fa-link"></i></a>TL;DR</h2>

<p>Plotly でグラフ作成する際に役立つと思って自作したヘルパー関数(?)を紹介しています。</p>

<p>Plotly とはインタラクティブで良い感じのグラフをお手軽に作成できるライブラリです。<br>
ただ、matplotlib や seaborn とも異なる独特な書き方があるので、seaborn っぽくデータフレームとX軸・Y軸に当たる列名を与えるだけで良い感じに表示してくれるものがあると嬉しいと思ったので、作成した次第です。</p>

<p><a href="https://plot.ly/python/" class="autolink" rel="nofollow noopener" target="_blank">https://plot.ly/python/</a></p>

<p>下図は画像ですが、Plotly の強みはインタラクティブに動作することです。具体的には、ホバーするとプロットされた値が表示されたり、グラフの一部を拡大縮小できることです。</p>

<p>これを本記事では確認できませんが、以下で動作を確認できます。  </p>

<p><strong><a href="https://nbviewer.jupyter.org/github/takaiyuk/notebooks/blob/master/PlotlyWrapper.ipynb" class="autolink" rel="nofollow noopener" target="_blank">https://nbviewer.jupyter.org/github/takaiyuk/notebooks/blob/master/PlotlyWrapper.ipynb</a></strong></p>

<h2>
<span id="データ準備" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E6%BA%96%E5%82%99"><i class="fa fa-link"></i></a>データ準備</h2>

<p>plorly を使用するとき、<code>plotly.offline</code> と <code>plotly.graph_objs</code> を主に使います。</p>

<p><code>plotly.offline</code>は与えられたグラフ情報とレイアウト情報を表示するときに、<br>
<code>plotly.graph_objs</code>は表示するグラフ情報やレイアウト情報の中身を作るのに使います。<br>
つまり、後者を使ってヒストグラムやら棒グラフやらの中身を記述したり、グラフのタイトルなどレイアウトの仕方を指定したりして、それらの情報を前者によって統合して表示するといったイメージだと思います。（あやふや）</p>

<p><code>plotly.offline.init_notebook_mode(connected=True)</code> は jupyter notebook 上で表示するために記入するようです。</p>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="n">np</span>
<span class="kn">import</span> <span class="nn">plotly</span>
<span class="kn">import</span> <span class="nn">plotly.offline</span> <span class="k">as</span> <span class="n">py</span>
<span class="kn">import</span> <span class="nn">plotly.graph_objs</span> <span class="k">as</span> <span class="n">go</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="n">sns</span>

<span class="kn">from</span> <span class="nn">IPython.core.interactiveshell</span> <span class="kn">import</span> <span class="n">InteractiveShell</span>
<span class="n">InteractiveShell</span><span class="o">.</span><span class="n">ast_node_interactivity</span> <span class="o">=</span> <span class="s">"all"</span>
<span class="n">py</span><span class="o">.</span><span class="n">init_notebook_mode</span><span class="p">(</span><span class="n">connected</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>  <span class="c1"># You can plot your graphs offline inside a Jupyter Notebook Environment.
</span><span class="k">print</span><span class="p">(</span><span class="n">f</span><span class="s">"Plotly version: {plotly.__version__}"</span><span class="p">)</span>  <span class="c1"># output: 4.3.0
</span>
<span class="s">"""
Colors of Viridis: 
https://cran.r-project.org/web/packages/viridis/vignettes/intro-to-viridis.html
"""</span>
<span class="n">C</span> <span class="o">=</span> <span class="p">[</span><span class="s">'#3D0553'</span><span class="p">,</span> <span class="s">'#4D798C'</span><span class="p">,</span> <span class="s">'#7DC170'</span><span class="p">,</span> <span class="s">'#F7E642'</span><span class="p">]</span>  
</pre></div></div>

<p>データは seaborn に標準装備されているものをいくつか使うことにします。<br>
事前に適当な処理も書いておきます。</p>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="s">"""
Load dataset with load_dataset function of seaborn: 
https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv
"""</span>
<span class="k">class</span> <span class="nc">DataLoader</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">pass</span>

    <span class="k">def</span> <span class="nf">load_titanic</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">group</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s">"titanic"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">group</span><span class="o">==</span><span class="bp">None</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">group</span><span class="p">)[</span><span class="s">"survived"</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span><span class="o">.</span><span class="n">to_frame</span><span class="p">()</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">df</span>

    <span class="k">def</span> <span class="nf">load_iris</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s">"iris"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">load_tips</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">group</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s">"tips"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">group</span><span class="o">==</span><span class="bp">None</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="n">group</span><span class="p">)[</span><span class="s">"tip"</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span><span class="o">.</span><span class="n">to_frame</span><span class="p">()</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">df</span>

    <span class="k">def</span> <span class="nf">load_flights</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">group</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s">"flights"</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">group</span><span class="o">==</span><span class="bp">None</span><span class="p">:</span>
            <span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">([</span><span class="n">group</span><span class="p">])[</span><span class="s">"passengers"</span><span class="p">]</span><span class="o">.</span><span class="nb">sum</span><span class="p">()</span><span class="o">.</span><span class="n">to_frame</span><span class="p">()</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>
        <span class="k">return</span> <span class="n">df</span>
</pre></div></div>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="k">class</span> <span class="nc">PlotlyWrapper</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">colors</span> <span class="o">=</span> <span class="p">[</span><span class="s">"#3D0553"</span><span class="p">,</span> <span class="s">"#4D798C"</span><span class="p">,</span> <span class="s">"#7DC170"</span><span class="p">,</span> <span class="s">"#F7E642"</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">_convert_to_str</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">arr</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">np</span><span class="o">.</span><span class="n">array</span><span class="p">(</span><span class="n">arr</span><span class="p">,</span> <span class="n">dtype</span><span class="o">=</span><span class="nb">str</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">_plotly_layout</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">go</span><span class="o">.</span><span class="n">Layout</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span>
            <span class="n">xaxis</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">zeroline</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">),</span>
            <span class="n">yaxis</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">ytitle</span><span class="p">,</span> <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">),</span>
        <span class="p">)</span>

    <span class="k">def</span> <span class="nf">distplot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">col</span><span class="p">,</span> <span class="n">bin_dict</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">trace</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">go</span><span class="o">.</span><span class="n">Histogram</span><span class="p">(</span>
                <span class="n">x</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                <span class="n">histfunc</span><span class="o">=</span><span class="s">"count"</span><span class="p">,</span>
                <span class="n">marker</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">color</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">colors</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                <span class="n">xbins</span><span class="o">=</span><span class="n">bin_dict</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="p">]</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_plotly_layout</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="n">ytitle</span><span class="p">)</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span> <span class="n">layout</span><span class="o">=</span><span class="n">layout</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">py</span><span class="o">.</span><span class="n">iplot</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">show_link</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">boxplot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">col</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">trace</span> <span class="o">=</span> <span class="p">[</span><span class="n">go</span><span class="o">.</span><span class="n">Box</span><span class="p">(</span><span class="n">y</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">color</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">colors</span><span class="p">[</span><span class="mi">0</span><span class="p">]))]</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_plotly_layout</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="n">ytitle</span><span class="p">)</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span> <span class="n">layout</span><span class="o">=</span><span class="n">layout</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">py</span><span class="o">.</span><span class="n">iplot</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">show_link</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">barplot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">xcol</span><span class="p">,</span> <span class="n">ycol</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">trace</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">go</span><span class="o">.</span><span class="n">Bar</span><span class="p">(</span>
                <span class="n">x</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_convert_to_str</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="n">xcol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">),</span>
                <span class="n">y</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                <span class="n">textposition</span><span class="o">=</span><span class="s">"auto"</span><span class="p">,</span>
                <span class="n">marker</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
                    <span class="n">color</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                    <span class="n">colorscale</span><span class="o">=</span><span class="s">"Viridis"</span><span class="p">,</span>
                    <span class="n">showscale</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                    <span class="n">reversescale</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">)</span>
        <span class="p">]</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_plotly_layout</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="n">ytitle</span><span class="p">)</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span> <span class="n">layout</span><span class="o">=</span><span class="n">layout</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">py</span><span class="o">.</span><span class="n">iplot</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">show_link</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">countplot</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">col</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
        <span class="n">trace</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">go</span><span class="o">.</span><span class="n">Histogram</span><span class="p">(</span>
                <span class="n">x</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">col</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">histfunc</span><span class="o">=</span><span class="s">"count"</span><span class="p">,</span> <span class="n">marker</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">color</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">colors</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
            <span class="p">)</span>
        <span class="p">]</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_plotly_layout</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="n">ytitle</span><span class="p">)</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span> <span class="n">layout</span><span class="o">=</span><span class="n">layout</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">py</span><span class="o">.</span><span class="n">iplot</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">show_link</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">scatterplot</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span> <span class="n">data</span><span class="p">,</span> <span class="n">xcol</span><span class="p">,</span> <span class="n">ycol</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span>
    <span class="p">):</span>
        <span class="n">trace</span> <span class="o">=</span> <span class="p">[</span>
            <span class="n">go</span><span class="o">.</span><span class="n">Scatter</span><span class="p">(</span>
                <span class="n">x</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_convert_to_str</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="n">xcol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">),</span>
                <span class="n">y</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                <span class="n">mode</span><span class="o">=</span><span class="s">"markers"</span><span class="p">,</span>
                <span class="n">marker</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span>
                    <span class="n">sizemode</span><span class="o">=</span><span class="s">"diameter"</span><span class="p">,</span>
                    <span class="n">sizeref</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
                    <span class="n">size</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span> <span class="o">**</span> <span class="n">size</span><span class="p">,</span>
                    <span class="n">color</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                    <span class="n">colorscale</span><span class="o">=</span><span class="s">"Viridis"</span><span class="p">,</span>
                    <span class="n">reversescale</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                    <span class="n">showscale</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">text</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_convert_to_str</span><span class="p">(</span><span class="n">data</span><span class="p">[</span><span class="n">xcol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="p">]</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Layout</span><span class="p">(</span>
            <span class="n">autosize</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span>
            <span class="n">hovermode</span><span class="o">=</span><span class="s">"closest"</span><span class="p">,</span>
            <span class="n">xaxis</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">zeroline</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">),</span>
            <span class="n">yaxis</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">ytitle</span><span class="p">,</span> <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">),</span>
            <span class="n">showlegend</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span> <span class="n">layout</span><span class="o">=</span><span class="n">layout</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">py</span><span class="o">.</span><span class="n">iplot</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">show_link</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">lineplot</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">data</span><span class="p">,</span>
        <span class="n">xcol</span><span class="p">,</span>
        <span class="n">ycol</span><span class="p">,</span>
        <span class="n">title</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
        <span class="n">xtitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
        <span class="n">ytitle</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
        <span class="n">linewidth</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="n">rangeslider</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
        <span class="n">slider_type</span><span class="o">=</span><span class="s">"date"</span><span class="p">,</span>
    <span class="p">):</span>
        <span class="k">if</span> <span class="n">rangeslider</span> <span class="ow">is</span> <span class="bp">True</span><span class="p">:</span>
            <span class="n">xaxis</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span>
                <span class="n">title</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span>
                <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
                <span class="n">zeroline</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
                <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
                <span class="n">rangeslider</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">visible</span><span class="o">=</span><span class="bp">True</span><span class="p">),</span>
                <span class="nb">type</span><span class="o">=</span><span class="n">slider_type</span><span class="p">,</span>
            <span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">xaxis</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">xtitle</span><span class="p">,</span> <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">zeroline</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>

        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">ycol</span><span class="p">)</span> <span class="o">==</span> <span class="nb">list</span><span class="p">:</span>
            <span class="n">trace</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">ycol</span><span class="p">)):</span>
                <span class="n">t</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Scatter</span><span class="p">(</span>
                    <span class="n">x</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">xcol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                    <span class="n">y</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">[</span><span class="n">i</span><span class="p">]]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                    <span class="n">mode</span><span class="o">=</span><span class="s">"lines"</span><span class="p">,</span>
                    <span class="n">name</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">[</span><span class="n">i</span><span class="p">]]</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                    <span class="n">line</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">linewidth</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">colors</span><span class="p">[</span><span class="n">i</span><span class="p">]),</span>
                <span class="p">)</span>
                <span class="n">trace</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">t</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">trace</span> <span class="o">=</span> <span class="p">[</span>
                <span class="n">go</span><span class="o">.</span><span class="n">Scatter</span><span class="p">(</span>
                    <span class="n">x</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">xcol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                    <span class="n">y</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">values</span><span class="p">,</span>
                    <span class="n">mode</span><span class="o">=</span><span class="s">"lines"</span><span class="p">,</span>
                    <span class="n">name</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="n">ycol</span><span class="p">]</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
                    <span class="n">line</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="n">linewidth</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">colors</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                <span class="p">)</span>
            <span class="p">]</span>
        <span class="n">layout</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Layout</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="n">title</span><span class="p">,</span> <span class="n">xaxis</span><span class="o">=</span><span class="n">xaxis</span><span class="p">,</span> <span class="n">yaxis</span><span class="o">=</span><span class="nb">dict</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">ytitle</span><span class="p">,</span> <span class="n">ticklen</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span> <span class="n">gridwidth</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
        <span class="p">)</span>
        <span class="n">fig</span> <span class="o">=</span> <span class="n">go</span><span class="o">.</span><span class="n">Figure</span><span class="p">(</span><span class="n">data</span><span class="o">=</span><span class="n">trace</span><span class="p">,</span> <span class="n">layout</span><span class="o">=</span><span class="n">layout</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">py</span><span class="o">.</span><span class="n">iplot</span><span class="p">(</span><span class="n">fig</span><span class="p">,</span> <span class="n">show_link</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
</pre></div></div>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">dataloader</span> <span class="o">=</span> <span class="n">DataLoader</span><span class="p">()</span>
<span class="n">plty</span> <span class="o">=</span> <span class="n">PlotlyWrapper</span><span class="p">()</span>
</pre></div></div>

<p><br></p>

<p>以下本題です。実際にコードと出力されるグラフを並べて羅列していきます。</p>

<h2>
<span id="histogram" class="fragment"></span><a href="#histogram"><i class="fa fa-link"></i></a>Histogram</h2>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">df</span> <span class="o">=</span> <span class="n">dataloader</span><span class="o">.</span><span class="n">load_iris</span><span class="p">()</span>
<span class="n">plty</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">col</span><span class="o">=</span><span class="s">"sepal_length"</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F2f8bbb73-3b87-da0e-c0e5-89ad755255f7.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7fcc43cf9fb8cdc69e27e4e36f3d8431" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F2f8bbb73-3b87-da0e-c0e5-89ad755255f7.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7fcc43cf9fb8cdc69e27e4e36f3d8431" alt="hist.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/2f8bbb73-3b87-da0e-c0e5-89ad755255f7.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F2f8bbb73-3b87-da0e-c0e5-89ad755255f7.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=55c9d339e9227c4916d8e2af9bf9b87f 1x" loading="lazy"></a></p>

<h2>
<span id="boxplot" class="fragment"></span><a href="#boxplot"><i class="fa fa-link"></i></a>Boxplot</h2>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">df</span> <span class="o">=</span> <span class="n">dataloader</span><span class="o">.</span><span class="n">load_iris</span><span class="p">()</span>
<span class="n">plty</span><span class="o">.</span><span class="n">boxplot</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">col</span><span class="o">=</span><span class="s">"sepal_length"</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fcd526e81-af61-5c0f-5a0a-1a9c2a468c81.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=133fc5d2801f5500e399c50fcf93e235" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fcd526e81-af61-5c0f-5a0a-1a9c2a468c81.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=133fc5d2801f5500e399c50fcf93e235" alt="boxplot.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/cd526e81-af61-5c0f-5a0a-1a9c2a468c81.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fcd526e81-af61-5c0f-5a0a-1a9c2a468c81.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=2b596acabceca82bf4f324cc326b05b6 1x" loading="lazy"></a></p>

<h2>
<span id="barplot" class="fragment"></span><a href="#barplot"><i class="fa fa-link"></i></a>Barplot</h2>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">df</span> <span class="o">=</span> <span class="n">dataloader</span><span class="o">.</span><span class="n">load_flights</span><span class="p">(</span><span class="n">group</span><span class="o">=</span><span class="s">"month"</span><span class="p">)</span>
<span class="n">plty</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">xcol</span><span class="o">=</span><span class="s">"month"</span><span class="p">,</span> <span class="n">ycol</span><span class="o">=</span><span class="s">"passengers"</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F72fbabf3-75dc-ddcb-aa24-4754df4c6c44.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=1f698ba9800473609ef35cbed27a4990" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F72fbabf3-75dc-ddcb-aa24-4754df4c6c44.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=1f698ba9800473609ef35cbed27a4990" alt="barplot.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/72fbabf3-75dc-ddcb-aa24-4754df4c6c44.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F72fbabf3-75dc-ddcb-aa24-4754df4c6c44.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=38ad1a293c2964cca569391fd5db7edf 1x" loading="lazy"></a></p>

<h2>
<span id="countplot" class="fragment"></span><a href="#countplot"><i class="fa fa-link"></i></a>Countplot</h2>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">df</span> <span class="o">=</span> <span class="n">dataloader</span><span class="o">.</span><span class="n">load_titanic</span><span class="p">()</span>
<span class="n">plty</span><span class="o">.</span><span class="n">countplot</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">col</span><span class="o">=</span><span class="s">"alive"</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F05971065-a0d8-e4bd-c957-bb92b6e79918.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=49430857a7fd239cd323a71e6f8f2cd8" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F05971065-a0d8-e4bd-c957-bb92b6e79918.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=49430857a7fd239cd323a71e6f8f2cd8" alt="countplot.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/05971065-a0d8-e4bd-c957-bb92b6e79918.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F05971065-a0d8-e4bd-c957-bb92b6e79918.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=499f9d2a57c6c1db6ea90861f8e5e68e 1x" loading="lazy"></a></p>

<h2>
<span id="scatterplot" class="fragment"></span><a href="#scatterplot"><i class="fa fa-link"></i></a>Scatterplot</h2>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">df</span> <span class="o">=</span> <span class="n">dataloader</span><span class="o">.</span><span class="n">load_tips</span><span class="p">(</span><span class="n">group</span><span class="o">=</span><span class="s">"day"</span><span class="p">)</span>
<span class="n">plty</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">xcol</span><span class="o">=</span><span class="s">"day"</span><span class="p">,</span> <span class="n">ycol</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">3</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F5da5e792-8851-a171-ec23-6fc19aa9af6e.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=ec3cb2a9db541fab19430004a20436ca" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F5da5e792-8851-a171-ec23-6fc19aa9af6e.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=ec3cb2a9db541fab19430004a20436ca" alt="scatterplot.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/5da5e792-8851-a171-ec23-6fc19aa9af6e.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F5da5e792-8851-a171-ec23-6fc19aa9af6e.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=d5538f53d02962e9c82b917d9a411c63 1x" loading="lazy"></a></p>

<h2>
<span id="lineplot" class="fragment"></span><a href="#lineplot"><i class="fa fa-link"></i></a>Lineplot</h2>

<div class="code-frame" data-lang="python"><div class="highlight"><pre><span class="n">df</span> <span class="o">=</span> <span class="n">dataloader</span><span class="o">.</span><span class="n">load_flights</span><span class="p">(</span><span class="s">"year"</span><span class="p">)</span>
<span class="n">plty</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">df</span><span class="p">,</span> <span class="n">xcol</span><span class="o">=</span><span class="s">"year"</span><span class="p">,</span> <span class="n">ycol</span><span class="o">=</span><span class="s">"passengers"</span><span class="p">,</span> <span class="n">rangeslider</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</pre></div></div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F6999c390-b5d0-2b61-f9af-422f869c117c.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7b6c84fbbd9ad66f900c436015f20d72" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F6999c390-b5d0-2b61-f9af-422f869c117c.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7b6c84fbbd9ad66f900c436015f20d72" alt="lineplot.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/6999c390-b5d0-2b61-f9af-422f869c117c.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F6999c390-b5d0-2b61-f9af-422f869c117c.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=a39c6c4cc51df3e88dac7c59cde390e3 1x" loading="lazy"></a></p>

<h2>
<span id="jupyter-lab-を使ってる場合の注意" class="fragment"></span><a href="#jupyter-lab-%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%82%8B%E5%A0%B4%E5%90%88%E3%81%AE%E6%B3%A8%E6%84%8F"><i class="fa fa-link"></i></a>Jupyter Lab を使ってる場合の注意</h2>

<p>Plotly をレンダリングするための extension をインストールしておく必要があります。</p>

<p>詳しくは下記URLをご覧ください。</p>

<ul>
<li><a href="https://github.com/jupyterlab/jupyter-renderers" class="autolink" rel="nofollow noopener" target="_blank">https://github.com/jupyterlab/jupyter-renderers</a></li>
<li><a href="https://github.com/jupyterlab/jupyter-renderers/tree/master/packages/plotly-extension" class="autolink" rel="nofollow noopener" target="_blank">https://github.com/jupyterlab/jupyter-renderers/tree/master/packages/plotly-extension</a></li>
</ul>
