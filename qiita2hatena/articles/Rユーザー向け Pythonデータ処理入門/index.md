https://qiita.com/takaiyuk/items/4cb1708a3f886b3d2043

2017-10-19T20:56:30+09:00

2018-06-21T17:49:25+09:00


<h2>
<span id="はじめに" class="fragment"></span><a href="#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB"><i class="fa fa-link"></i></a>はじめに　</h2>

<h3>
<span id="こんな人向け" class="fragment"></span><a href="#%E3%81%93%E3%82%93%E3%81%AA%E4%BA%BA%E5%90%91%E3%81%91"><i class="fa fa-link"></i></a>こんな人向け</h3>

<p>・Rは分かるけど, Pythonは分からないという人向け.  </p>

<h3>
<span id="背景" class="fragment"></span><a href="#%E8%83%8C%E6%99%AF"><i class="fa fa-link"></i></a>背景</h3>

<p>・R初心者（初稿投稿時: R歴7ヶ月）.<br>
・最近Pythonにも手を出してみるも, 単純なデータ処理すら書き方がRと異なるため難しい.<br>
・RとPythonのデータ処理の対応表を見たい.<br>
・いくつか参考サイトあるが, 自分が必要とするものが完全に揃っているわけではない.<br>
　＝＞<a href="http://postd.cc/r-vs-python-head-to-head-data-analysis/" rel="nofollow noopener" target="_blank">R vs Python：データ解析を比較</a><br>
・じゃあ自分用メモを作っちゃおう.</p>

<h2>
<span id="参考にしたサイト" class="fragment"></span><a href="#%E5%8F%82%E8%80%83%E3%81%AB%E3%81%97%E3%81%9F%E3%82%B5%E3%82%A4%E3%83%88"><i class="fa fa-link"></i></a>参考にしたサイト</h2>

<p><br></p>

<ul>
<li>【Python】<br>

<ul>
<li>
<a href="https://qiita.com/hik0107/items/d991cc44c2d1778bb82e" id="reference-465f70c10795233b2133">Python Pandasでのデータ操作の初歩まとめ − 前半：データ作成＆操作編</a><br>
</li>
<li>
<a href="https://qiita.com/tanemaki/items/2ed05e258ef4c9e6caac" id="reference-34a5b88c702cfda79426">ゆるふわPandasチートシート</a><br>
</li>
<li>
<a href="https://www.oreilly.co.jp/books/9784873116556/" rel="nofollow noopener" target="_blank">『Pythonによるデータ分析入門』</a><br>
</li>
<li>
<a href="https://qiita.com/tomotaka_ito/items/594ee1396cf982ba9887" id="reference-c63ebd69ede76360064d">Python文字列操作マスター</a><br>
</li>
<li>
<a href="http://pppurple.hatenablog.com/entry/2016/06/27/022310" rel="nofollow noopener" target="_blank">pandasの使い方（merge、join、concat編）</a><br>
</li>
</ul>
</li>
</ul>

<p><br></p>

<ul>
<li>【R】<br>

<ul>
<li>
<a href="https://qiita.com/matsuou1/items/e995da273e3108e2338e" id="reference-12d5444bcc5929afe246">dplyrを使いこなす！基礎編</a><br>
</li>
<li>
<a href="https://heavywatal.github.io/rstats/stringr.html" rel="nofollow noopener" target="_blank">stringr — Rの文字列をまともな方法で処理する</a><br>
</li>
<li>
<a href="https://heavywatal.github.io/rstats/readr.html" rel="nofollow noopener" target="_blank">readr — 高速で柔軟なテーブル読み込み</a><br>
</li>
</ul>
</li>
</ul>

<p><br></p>

<h2>
<span id="基本操作base" class="fragment"></span><a href="#%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9Cbase"><i class="fa fa-link"></i></a>基本操作（base）</h2>

<p>・irisデータセットを使用.<br>
・ちょこちょこ余計な操作もしています.  </p>

<h3>
<span id="行列数を確認" class="fragment"></span><a href="#%E8%A1%8C%E5%88%97%E6%95%B0%E3%82%92%E7%A2%BA%E8%AA%8D"><i class="fa fa-link"></i></a>行・列数を確認</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="nf">dim</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="o">.</span><span class="n">shape</span>
</pre></div>
</div>

<h3>
<span id="行数を確認" class="fragment"></span><a href="#%E8%A1%8C%E6%95%B0%E3%82%92%E7%A2%BA%E8%AA%8D"><i class="fa fa-link"></i></a>行数を確認</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">nrow</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="nb">len</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="列数を確認" class="fragment"></span><a href="#%E5%88%97%E6%95%B0%E3%82%92%E7%A2%BA%E8%AA%8D"><i class="fa fa-link"></i></a>列数を確認</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">ncol</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="nb">len</span><span class="p">(</span><span class="n">iris</span><span class="o">.</span><span class="n">columns</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="データ型確認" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E5%9E%8B%E7%A2%BA%E8%AA%8D"><i class="fa fa-link"></i></a>データ型確認</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="nf">class</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="nf">class</span><span class="p">(</span><span class="n">iris</span><span class="o">$</span><span class="n">Sepal.Length</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="nb">type</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span>
</pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="nb">type</span><span class="p">(</span><span class="n">iris</span><span class="o">.</span><span class="n">Species</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="先頭のn行を確認" class="fragment"></span><a href="#%E5%85%88%E9%A0%AD%E3%81%AEn%E8%A1%8C%E3%82%92%E7%A2%BA%E8%AA%8D"><i class="fa fa-link"></i></a>先頭のn行を確認</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<h3>
<span id="列名を確認" class="fragment"></span><a href="#%E5%88%97%E5%90%8D%E3%82%92%E7%A2%BA%E8%AA%8D"><i class="fa fa-link"></i></a>列名を確認</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="nf">names</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="o">.</span><span class="n">columns</span>
</pre></div>
</div>

<h3>
<span id="指定行の取り出し" class="fragment"></span><a href="#%E6%8C%87%E5%AE%9A%E8%A1%8C%E3%81%AE%E5%8F%96%E3%82%8A%E5%87%BA%E3%81%97"><i class="fa fa-link"></i></a>指定行の取り出し</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="p">[</span><span class="m">1</span><span class="p">,]</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="c1"># 行番号を使って行抽出
</span></pre></div>
</div>

<h3>
<span id="指定列の取り出し" class="fragment"></span><a href="#%E6%8C%87%E5%AE%9A%E5%88%97%E3%81%AE%E5%8F%96%E3%82%8A%E5%87%BA%E3%81%97"><i class="fa fa-link"></i></a>指定列の取り出し</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="p">[,</span><span class="m">1</span><span class="p">])</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="p">[</span><span class="s">"Sepal.Length"</span><span class="p">]</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<h3>
<span id="行結合" class="fragment"></span><a href="#%E8%A1%8C%E7%B5%90%E5%90%88"><i class="fa fa-link"></i></a>行結合</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">iris</span><span class="w">
</span><span class="nf">dim</span><span class="p">(</span><span class="n">rbind</span><span class="p">(</span><span class="n">iris</span><span class="p">,</span><span class="w"> </span><span class="n">iris2</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris2</span> <span class="o">=</span> <span class="n">iris</span>
<span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">iris</span><span class="p">,</span> <span class="n">iris2</span><span class="p">],</span><span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">shape</span> <span class="c1"># axis=0は省略可能
</span></pre></div>
</div>

<h3>
<span id="列結合" class="fragment"></span><a href="#%E5%88%97%E7%B5%90%E5%90%88"><i class="fa fa-link"></i></a>列結合</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris2</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">iris</span><span class="w">
</span><span class="n">head</span><span class="p">(</span><span class="n">cbind</span><span class="p">(</span><span class="n">iris</span><span class="p">,</span><span class="w"> </span><span class="n">iris2</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris2</span> <span class="o">=</span> <span class="n">iris</span>
<span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span><span class="n">iris</span><span class="p">,</span> <span class="n">iris2</span><span class="p">],</span><span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span> <span class="c1"># axis=1は省略不可
</span></pre></div>
</div>

<h3>
<span id="文字列型ー数値型" class="fragment"></span><a href="#%E6%96%87%E5%AD%97%E5%88%97%E5%9E%8B%E3%83%BC%E6%95%B0%E5%80%A4%E5%9E%8B"><i class="fa fa-link"></i></a>文字列型ー＞数値型</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">c</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="s2">"1"</span><span class="w">
</span><span class="nf">class</span><span class="p">(</span><span class="nf">as.numeric</span><span class="p">(</span><span class="n">c</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">c</span> <span class="o">=</span> <span class="s">"1"</span>
<span class="nb">type</span><span class="p">(</span><span class="nb">float</span><span class="p">(</span><span class="n">c</span><span class="p">))</span>
</pre></div>
</div>

<h3>
<span id="数値型ー文字列型" class="fragment"></span><a href="#%E6%95%B0%E5%80%A4%E5%9E%8B%E3%83%BC%E6%96%87%E5%AD%97%E5%88%97%E5%9E%8B"><i class="fa fa-link"></i></a>数値型ー＞文字列型</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">v</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span><span class="w">
</span><span class="nf">class</span><span class="p">(</span><span class="nf">as.character</span><span class="p">(</span><span class="n">v</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">f</span> <span class="o">=</span> <span class="mi">1</span>
<span class="nb">type</span><span class="p">(</span><span class="nb">str</span><span class="p">(</span><span class="n">f</span><span class="p">))</span>
</pre></div>
</div>

<h3>
<span id="統計要約量" class="fragment"></span><a href="#%E7%B5%B1%E8%A8%88%E8%A6%81%E7%B4%84%E9%87%8F"><i class="fa fa-link"></i></a>統計要約量</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">summary</span><span class="p">(</span><span class="n">iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="o">.</span><span class="n">describe</span><span class="p">()</span>
<span class="c1"># 件数、平均、標準偏差、最小値、最大値、中央値、四分位数
</span></pre></div>
</div>

<h3>
<span id="欠損値を含む行を削除" class="fragment"></span><a href="#%E6%AC%A0%E6%90%8D%E5%80%A4%E3%82%92%E5%90%AB%E3%82%80%E8%A1%8C%E3%82%92%E5%89%8A%E9%99%A4"><i class="fa fa-link"></i></a>欠損値を含む行を削除</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris.na</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">mutate</span><span class="p">(</span><span class="n">column.na</span><span class="o">=</span><span class="n">seq</span><span class="p">(</span><span class="m">1</span><span class="o">:</span><span class="n">nrow</span><span class="p">(</span><span class="n">iris</span><span class="p">)))</span><span class="w"> </span><span class="c1">#nrow()は行数を返す。seqは順に任意の数(デフォルト1)ずつ増減する数列を返す。</span><span class="w">
</span><span class="n">iris.na</span><span class="p">[</span><span class="m">1</span><span class="p">,</span><span class="m">6</span><span class="p">]</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="kc">NA</span><span class="w"> </span><span class="c1"># "&lt;-" は代入記号</span><span class="w">
</span><span class="n">head</span><span class="p">(</span><span class="n">na.omit</span><span class="p">(</span><span class="n">iris.na</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">series</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">150</span><span class="p">),</span> <span class="n">index</span><span class="o">=</span><span class="n">new_iris</span><span class="o">.</span><span class="n">index</span><span class="p">)</span> <span class="c1">#index付きのシリーズ作成。indexは元のdfのindex(=行番号)
</span><span class="k">del</span> <span class="n">series</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="c1"># 要素の削除(del文, popメソッド, removeメソッド) https://www.pythonweb.jp/tutorial/list/index8.html
</span><span class="n">iris_na</span> <span class="o">=</span> <span class="n">iris</span>
<span class="n">iris_na</span><span class="p">[</span><span class="s">"column_na"</span><span class="p">]</span> <span class="o">=</span> <span class="n">series</span>
<span class="n">iris_na</span><span class="o">.</span><span class="n">dropna</span><span class="p">(</span><span class="n">axis</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<p><br></p>

<h2>
<span id="データ操作dplyr" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E6%93%8D%E4%BD%9Cdplyr"><i class="fa fa-link"></i></a>データ操作（dplyr）</h2>

<h3>
<span id="rename" class="fragment"></span><a href="#rename"><i class="fa fa-link"></i></a>rename</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">new_colnames</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">stringr</span><span class="o">::</span><span class="n">str_replace</span><span class="p">(</span><span class="n">colnames</span><span class="p">(</span><span class="n">iris</span><span class="p">),</span><span class="w"> </span><span class="s2">"[.]"</span><span class="p">,</span><span class="w"> </span><span class="s2">"_"</span><span class="p">)</span><span class="w"> </span><span class="c1"># "."を"_"に変換する</span><span class="w">
</span><span class="n">new_iris</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">iris</span><span class="w">
</span><span class="n">colnames</span><span class="p">(</span><span class="n">new_iris</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">new_colnames</span><span class="w">
</span><span class="c1"># df %&gt;% rename(new_colname = old_colname) とすることもできる。</span><span class="w">
</span><span class="nf">names</span><span class="p">(</span><span class="n">new_iris</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">rename_dict</span> <span class="o">=</span> <span class="p">{</span><span class="n">column</span><span class="p">:</span> <span class="n">column</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">'.'</span><span class="p">,</span> <span class="s">'_'</span><span class="p">)</span> <span class="k">for</span> <span class="n">column</span> <span class="ow">in</span> <span class="n">iris</span><span class="o">.</span><span class="n">columns</span><span class="p">}</span> <span class="c1"># 列名の"."を"_"に書き換える
</span><span class="n">new_iris</span> <span class="o">=</span> <span class="n">iris</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="n">rename_dict</span><span class="p">)</span>
<span class="n">new_iris</span><span class="o">.</span><span class="n">columns</span>
</pre></div>
</div>

<h3>
<span id="filter" class="fragment"></span><a href="#filter"><i class="fa fa-link"></i></a>filter</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">filter</span><span class="p">(</span><span class="n">Sepal.Length</span><span class="w"> </span><span class="o">&gt;</span><span class="w"> </span><span class="m">6.4</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">new_iris</span><span class="p">[(</span><span class="n">new_iris</span><span class="p">[</span><span class="s">'Sepal_Length'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">5</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">new_iris</span><span class="p">[</span><span class="s">'Sepal_Width'</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">)]</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
<span class="c1"># データフレーム[Booleanの配列を入れる]
# 複数条件の場合は、or条件の "|" もしくは and条件の "&amp;"を間に入れ、それぞれの条件を()で囲む
</span></pre></div>
</div>

<h3>
<span id="select" class="fragment"></span><a href="#select"><i class="fa fa-link"></i></a>select</h3>

<ul>
<li>列名で列選択<br>
</li>
</ul>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">select</span><span class="p">(</span><span class="n">Sepal.Length</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">new_iris</span><span class="p">[[</span><span class="s">"Sepal_Length"</span><span class="p">,</span> <span class="s">"Petal_Length"</span><span class="p">]]</span><span class="o">.</span><span class="n">head</span><span class="p">()</span> <span class="c1"># 複数列選択（[]で[列名,列名]を囲む）  
</span></pre></div>
</div>

<ul>
<li>列番号で列選択</li>
</ul>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">select</span><span class="p">(</span><span class="m">-1</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">new_iris</span><span class="o">.</span><span class="n">drop</span><span class="p">(</span><span class="s">'Species'</span><span class="p">,</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">6</span><span class="p">)</span> <span class="c1"># 列削除
</span></pre></div>
</div>

<h3>
<span id="mutate" class="fragment"></span><a href="#mutate"><i class="fa fa-link"></i></a>mutate</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">mutate</span><span class="p">(</span><span class="n">new.column</span><span class="o">=</span><span class="s2">"new value"</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">series</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">Series</span><span class="p">(</span><span class="s">"new_value"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="n">new_iris</span><span class="o">.</span><span class="n">index</span><span class="p">)</span> <span class="c1"># index付きのシリーズ作成。indexは元のdfのindex(=行番号)
</span><span class="n">new_iris</span><span class="p">[</span><span class="s">"new_column"</span><span class="p">]</span><span class="o">=</span><span class="n">series</span>
<span class="n">new_iris</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<h3>
<span id="arrange" class="fragment"></span><a href="#arrange"><i class="fa fa-link"></i></a>arrange</h3>

<ul>
<li>デフォルトでは昇順<br>
</li>
</ul>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">arrange</span><span class="p">(</span><span class="n">Sepal.Length</span><span class="p">))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">new_iris</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="p">[</span><span class="s">'Sepal_Length'</span><span class="p">,</span> <span class="s">'Sepal_Width'</span><span class="p">])</span><span class="o">.</span><span class="n">head</span><span class="p">()</span> <span class="c1"># 複数の値で昇順でソート
</span></pre></div>
</div>

<ul>
<li>desc()で降順にもできる</li>
</ul>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">arrange</span><span class="p">(</span><span class="n">desc</span><span class="p">(</span><span class="n">Sepal.Length</span><span class="p">)))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">new_iris</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s">'Sepal_Length'</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span> <span class="c1"># 降順でソート
</span></pre></div>
</div>

<h3>
<span id="group_by" class="fragment"></span><a href="#group_by"><i class="fa fa-link"></i></a>group_by</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="w">
</span><span class="n">knitr</span><span class="o">::</span><span class="n">kable</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> 
       </span><span class="n">arrange</span><span class="p">(</span><span class="n">Sepal.Width</span><span class="p">)</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> 
       </span><span class="n">group_by</span><span class="p">(</span><span class="n">Species</span><span class="p">)</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> 
       </span><span class="n">mutate</span><span class="p">(</span><span class="n">mean.S.L.by.Species</span><span class="o">=</span><span class="n">mean</span><span class="p">(</span><span class="n">Sepal.Width</span><span class="p">)))</span><span class="w">
</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">new_iris_grouped</span> <span class="o">=</span> <span class="n">new_iris</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s">"Species"</span><span class="p">)</span>  <span class="c1"># SpeciesでGroup_byを行う。
</span><span class="n">new_iris_grouped</span><span class="p">[[</span><span class="s">"Sepal_Length"</span><span class="p">,</span><span class="s">"Sepal_Width"</span><span class="p">]]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>          
  <span class="c1"># Group化されたされたオブジェクトに対してMeanを行う。
</span>  <span class="c1"># 必要であれば、Meanを行う変数を指定できる。
</span></pre></div>
</div>

<h3>
<span id="summarise" class="fragment"></span><a href="#summarise"><i class="fa fa-link"></i></a>summarise</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">head</span><span class="p">(</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">summarise</span><span class="p">(</span><span class="n">max.sl</span><span class="o">=</span><span class="nf">max</span><span class="p">(</span><span class="n">Sepal.Length</span><span class="p">),</span><span class="w"> 
                        </span><span class="n">max.sw</span><span class="o">=</span><span class="nf">max</span><span class="p">(</span><span class="n">Sepal.Width</span><span class="p">),</span><span class="w"> 
                        </span><span class="n">min.pl</span><span class="o">=</span><span class="nf">min</span><span class="p">(</span><span class="n">Petal.Length</span><span class="p">),</span><span class="w"> 
                        </span><span class="n">mean.pw</span><span class="o">=</span><span class="n">mean</span><span class="p">(</span><span class="n">Petal.Width</span><span class="p">)))</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="c1"># 同上
</span><span class="n">new_iris_grouped</span> <span class="o">=</span> <span class="n">new_iris</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s">"Species"</span><span class="p">)</span>  <span class="c1"># SpeciesでGroup_byを行う。
</span><span class="n">new_iris_grouped</span><span class="p">[[</span><span class="s">"Sepal_Length"</span><span class="p">,</span><span class="s">"Sepal_Width"</span><span class="p">]]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>          
  <span class="c1"># Group化されたされたオブジェクトに対してMeanを行う。
</span>  <span class="c1"># 必要であれば、Meanを行う変数を指定できる。
</span></pre></div>
</div>

<h3>
<span id="join" class="fragment"></span><a href="#join"><i class="fa fa-link"></i></a>join</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">colnames_for_join</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">stringr</span><span class="o">::</span><span class="n">str_replace</span><span class="p">(</span><span class="n">colnames</span><span class="p">(</span><span class="n">iris</span><span class="p">),</span><span class="w"> </span><span class="s2">"th"</span><span class="p">,</span><span class="w"> </span><span class="s2">"th_for_join"</span><span class="p">)</span><span class="w"> </span><span class="c1"># 列名の"*th"を"*th_for_join"に書き換える</span><span class="w">
</span><span class="n">iris_for_join</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">iris</span><span class="w"> 
</span><span class="n">colnames</span><span class="p">(</span><span class="n">iris_for_join</span><span class="p">)</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">colnames_for_join</span><span class="w">
</span><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">left_join</span><span class="p">(</span><span class="n">iris_for_join</span><span class="p">,</span><span class="w"> </span><span class="n">by</span><span class="o">=</span><span class="s2">"Species"</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">dict_for_join</span> <span class="o">=</span> <span class="p">{</span><span class="n">column</span><span class="p">:</span> <span class="n">column</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">'th'</span><span class="p">,</span> <span class="s">'th_for_join'</span><span class="p">)</span> <span class="k">for</span> <span class="n">column</span> <span class="ow">in</span> <span class="n">new_iris</span><span class="o">.</span><span class="n">columns</span><span class="p">}</span>
<span class="n">iris_for_join</span> <span class="o">=</span> <span class="n">new_iris</span>
<span class="n">iris_for_join</span> <span class="o">=</span> <span class="n">iris_for_join</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="n">dict_for_join</span><span class="p">)</span>
<span class="n">pd</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">new_iris</span><span class="p">,</span> <span class="n">iris_for_join</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s">'left'</span><span class="p">)</span>
</pre></div>
</div>

<p><br></p>

<h2>
<span id="文字列処理stringr" class="fragment"></span><a href="#%E6%96%87%E5%AD%97%E5%88%97%E5%87%A6%E7%90%86stringr"><i class="fa fa-link"></i></a>文字列処理（stringr）</h2>

<h3>
<span id="データ読み込み" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E8%AA%AD%E3%81%BF%E8%BE%BC%E3%81%BF"><i class="fa fa-link"></i></a>データ読み込み</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">species</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">iris</span><span class="o">$</span><span class="n">Species</span><span class="w">
</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">]</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">species</span> <span class="o">=</span> <span class="n">new_iris</span><span class="p">[</span><span class="s">"Species"</span><span class="p">]</span>
<span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>
</div>

<h3>
<span id="str_length-文字列の長さを返す" class="fragment"></span><a href="#str_length-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E9%95%B7%E3%81%95%E3%82%92%E8%BF%94%E3%81%99"><i class="fa fa-link"></i></a>str_length: 文字列の長さを返す.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_length</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">])</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="nb">len</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">])</span>
</pre></div>
</div>

<h3>
<span id="str_sub-文字列の一部抽出する" class="fragment"></span><a href="#str_sub-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E4%B8%80%E9%83%A8%E6%8A%BD%E5%87%BA%E3%81%99%E3%82%8B"><i class="fa fa-link"></i></a>str_sub: 文字列の一部抽出する.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_sub</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">],</span><span class="w"> </span><span class="n">start</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span><span class="p">,</span><span class="w"> </span><span class="n">end</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">4</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_sub</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">],</span><span class="w"> </span><span class="n">start</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">-4</span><span class="p">,</span><span class="w"> </span><span class="n">end</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">-1</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">:</span><span class="mi">2</span><span class="p">]</span>
</pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="o">-</span><span class="mi">2</span><span class="p">:]</span>
</pre></div>
</div>

<h3>
<span id="str_detect-特定のパターンを文字列が含むかどうか判別する" class="fragment"></span><a href="#str_detect-%E7%89%B9%E5%AE%9A%E3%81%AE%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%82%92%E6%96%87%E5%AD%97%E5%88%97%E3%81%8C%E5%90%AB%E3%82%80%E3%81%8B%E3%81%A9%E3%81%86%E3%81%8B%E5%88%A4%E5%88%A5%E3%81%99%E3%82%8B"><i class="fa fa-link"></i></a>str_detect: 特定のパターンを文字列が含むかどうか判別する.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_detect</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">],</span><span class="w"> </span><span class="s2">"eto"</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="s">"eto"</span> <span class="ow">in</span> <span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>
</div>

<h3>
<span id="str_subset-特定のパターンを含む文字列を抽出する" class="fragment"></span><a href="#str_subset-%E7%89%B9%E5%AE%9A%E3%81%AE%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%82%92%E5%90%AB%E3%82%80%E6%96%87%E5%AD%97%E5%88%97%E3%82%92%E6%8A%BD%E5%87%BA%E3%81%99%E3%82%8B"><i class="fa fa-link"></i></a>str_subset: 特定のパターンを含む文字列を抽出する.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_subset</span><span class="p">(</span><span class="n">species</span><span class="p">,</span><span class="w"> </span><span class="s2">"set"</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="nb">len</span><span class="p">(</span><span class="n">species</span><span class="p">)):</span> 
    <span class="k">if</span> <span class="p">(</span><span class="s">"set"</span> <span class="ow">in</span> <span class="n">species</span><span class="p">[</span><span class="n">index</span><span class="p">])</span> <span class="o">==</span><span class="bp">True</span><span class="p">:</span>
        <span class="k">print</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
</pre></div>
</div>

<h3>
<span id="str_locate-特定のパターンが文字列の何番目に位置するかを返す" class="fragment"></span><a href="#str_locate-%E7%89%B9%E5%AE%9A%E3%81%AE%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%81%8C%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E4%BD%95%E7%95%AA%E7%9B%AE%E3%81%AB%E4%BD%8D%E7%BD%AE%E3%81%99%E3%82%8B%E3%81%8B%E3%82%92%E8%BF%94%E3%81%99"><i class="fa fa-link"></i></a>str_locate: 特定のパターンが文字列の何番目に位置するかを返す.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_locate</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">],</span><span class="w"> </span><span class="s2">"set"</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">find</span><span class="p">(</span><span class="s">"t"</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="str_replace-文字列内の特定のパターンを置換する" class="fragment"></span><a href="#str_replace-%E6%96%87%E5%AD%97%E5%88%97%E5%86%85%E3%81%AE%E7%89%B9%E5%AE%9A%E3%81%AE%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%82%92%E7%BD%AE%E6%8F%9B%E3%81%99%E3%82%8B"><i class="fa fa-link"></i></a>str_replace: 文字列内の特定のパターンを置換する.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">str_replace</span><span class="p">(</span><span class="n">species</span><span class="p">[</span><span class="m">1</span><span class="p">],</span><span class="w"> </span><span class="s2">"sa"</span><span class="p">,</span><span class="w"> </span><span class="s2">"sa_replaced"</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">species</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">replace</span><span class="p">(</span><span class="s">"sa"</span><span class="p">,</span> <span class="s">"sa_replaced"</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="str_trim-文字列の空白を除去する" class="fragment"></span><a href="#str_trim-%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E7%A9%BA%E7%99%BD%E3%82%92%E9%99%A4%E5%8E%BB%E3%81%99%E3%82%8B"><i class="fa fa-link"></i></a>str_trim: 文字列の空白を除去する.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">species_trim</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="s2">" species "</span><span class="p">)</span><span class="w">
</span><span class="n">str_trim</span><span class="p">(</span><span class="n">species_trim</span><span class="p">,</span><span class="w"> </span><span class="n">side</span><span class="o">=</span><span class="s2">"both"</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">species_trim</span> <span class="o">=</span> <span class="p">(</span><span class="s">" species "</span><span class="p">)</span>
<span class="n">species_trim</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
<span class="c1"># lstripはstripと同等の処理を左端のみに適用
# rstripはstripと同等の処理を右端のみに適用
</span></pre></div>
</div>

<p><br></p>

<h2>
<span id="その他" class="fragment"></span><a href="#%E3%81%9D%E3%81%AE%E4%BB%96"><i class="fa fa-link"></i></a>その他</h2>

<h3>
<span id="readrparse_number-数字のみを抽出する" class="fragment"></span><a href="#readrparse_number-%E6%95%B0%E5%AD%97%E3%81%AE%E3%81%BF%E3%82%92%E6%8A%BD%E5%87%BA%E3%81%99%E3%82%8B"><i class="fa fa-link"></i></a>readr::parse_number: 数字のみを抽出する.</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">x</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="nf">c</span><span class="p">(</span><span class="s2">"6e23"</span><span class="p">)</span><span class="w">
</span><span class="n">parse_number</span><span class="p">(</span><span class="n">x</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">re</span>
<span class="n">x</span> <span class="o">=</span> <span class="p">(</span><span class="s">"6e23"</span><span class="p">)</span>
<span class="n">re</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="s">"</span><span class="err">\</span><span class="s">d"</span><span class="p">,</span> <span class="n">x</span><span class="p">)</span><span class="o">.</span><span class="n">group</span><span class="p">()</span>
</pre></div>
</div>
