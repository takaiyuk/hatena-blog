https://qiita.com/takaiyuk/items/72e24aff15059fd53c9d

2018-07-30T08:28:11+09:00

2018-10-27T08:46:08+09:00


<h2>
<span id="概要" class="fragment"></span><a href="#%E6%A6%82%E8%A6%81"><i class="fa fa-link"></i></a>概要</h2>

<p><a href="http://seaborn.pydata.org/whatsnew.html#v0-9-0-july-2018" rel="nofollow noopener" target="_blank">What’s new in each version --v0.9.0 (July 2018)</a></p>

<p>seabornがメジャーアップデートをして、バージョン0.9.0がリリースされました。</p>

<p>いくつかの変更点や新たな関数が追加されたようなので、いくつか試してみたいと思います。</p>

<p>特に、散布図の<code>scatterplot()</code>や、線グラフの<code>lineplot()</code>が良さげなので、それについて詳しく見ます。</p>

<p>コードだけ見たい方は、<a href="#%E3%82%B3%E3%83%BC%E3%83%89%E4%BE%8B">以下の文章は飛ばしてこちら</a>からどうぞ。</p>

<h3>
<span id="注意" class="fragment"></span><a href="#%E6%B3%A8%E6%84%8F"><i class="fa fa-link"></i></a>注意！</h3>

<p>ベータ版なので、アップデート等は自己責任でお願いします。</p>

<h2>
<span id="主な変更点や追加関数" class="fragment"></span><a href="#%E4%B8%BB%E3%81%AA%E5%A4%89%E6%9B%B4%E7%82%B9%E3%82%84%E8%BF%BD%E5%8A%A0%E9%96%A2%E6%95%B0"><i class="fa fa-link"></i></a>主な変更点や追加関数</h2>

<p>以下、公式ドキュメントの翻訳（意訳）の抜粋。だいぶ粗い訳なので、分かりにくい箇所はドキュメントを参照してください。</p>

<hr>

<p>新しいグラフ関数が追加された。</p>

<ul>
<li> relplot()</li>
<li> scatterplot()</li>
<li> lineplot()</li>
</ul>

<p><code>relplot()</code>は <code>FacetGrid</code>と、<code>scatterplot()</code>および<code>lineplot</code>を組み合わせたそれらのfigure レベルのインターフェースである。 <code>relplot()</code>関数は、seaborn のカテゴリカル変数のグラフ関数の高レベルでデータセット志向なAPIを、より一般的なプロット(散布図や線グラフ)にもたらす。</p>

<p>これらの関数は、色(hue)・大きさ(size)・形(style)を修正することで3つの付加的な変数を表現しながら、2つの連続値変数の関係を可視化することができる。共通の高機能APIが2つの関数に別々に実装されている。例えば、<code>scatterplot()</code>におけるサイズは意味的に散布図の点の大きさを縮小拡大させるが、<code>lineplot()</code>では線グラフの線の幅を縮小拡大させる。このAPIはデータセット志向なので、いずれの場合も点の大きさや線の幅のための matplotlib のパラメータを直接特定せず、単にデータセットの変数を渡すだけで良い。</p>

<p>既存の seaborn の機能と異なる方法は、色と大きさの表現のために連続値変数を用いる点でより良いサポートを得られる。この機能は将来のバージョンで色の表現を他の関数に広まるかもしれない。（今回のリリースではまだ実装されていない。）</p>

<p><code>lineplot()</code> 関数は同様に統計的推定をサポートし、既存の tsplot 関数（今のところ存在しているが将来のリリースで削除されうる）を置き換えられつつある。<code>lineplot()</code>はライブラリの残りのAPIとより良く協調されていて、大きさと形状を独立に修正することで、追加の変数とより柔軟な関係性を表現できる。同様に時系列データへのサポートも改善している。不確実性を表現する tsplot の難解なオプションは新しい関数では実装されていない。</p>

<p>これらの新しい関数を詳しく説明するたくさんのドキュメントがある。例えば、APIレファレンスにおける様々なオプションの詳細な例や言葉数の多いチュートリアルなどがある。</p>

<p>これらの関数は「ベータ版」状態と考えられるべきである。これらは徹底的にテストされているが、いくつかのエラーは見つけられていないかもしれない。いくつかの要素では修正が計画されている。特に、デフォルトの凡例はこのリリースでは少し雑なままである。最終的には、いくつかのデフォルトの挙動（例えば、デフォルトの点・線の大きさの幅）は将来のリリースで何かしらの変更があるかもしれない。</p>

<hr>

<h3>
<span id="感想" class="fragment"></span><a href="#%E6%84%9F%E6%83%B3"><i class="fa fa-link"></i></a>感想</h3>

<p>今までは散布図も線グラフもjointplotを用いていたけど、データセットを分割して、プロットを重ねていかないと散布図でカテゴリカル変数に従って色分けしたりできなかった。</p>

<p>しかし、今回のアップデートでそういうを簡単にしてくれるようになったらしい。（2018年7月時点では ベータ版らしいが）</p>

<p>Pythonにおけるグラフの描画の柔軟性は、R の<code>ggplot2</code>と比べるとやや劣るところがあったけど、こういった改良が加えられていけば、通常レベルの使い勝手ならほとんど遜色なくなっていきそう。</p>

<h2>
<span id="コード例" class="fragment"></span><a href="#%E3%82%B3%E3%83%BC%E3%83%89%E4%BE%8B"><i class="fa fa-link"></i></a>コード例</h2>

<p>seaborn ver0.9.0 の<a href="http://seaborn.pydata.org/tutorial/relational.html#relational-tutorial" rel="nofollow noopener" target="_blank">公式のチュートリアルはこちら</a>です。</p>

<h3>
<span id="セットアップ" class="fragment"></span><a href="#%E3%82%BB%E3%83%83%E3%83%88%E3%82%A2%E3%83%83%E3%83%97"><i class="fa fa-link"></i></a>セットアップ</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">jupyter</span></div>
<div class="highlight"><pre><span class="c1"># seaborn を最新版にアップデート
# jupyter notebook 上でシェルコマンドを打つにはコードの最初に ! を付ける。
# 注意！：公式ドキュメントにも書いてありますが、stable beta 版なので各自自己責任でお願いします。
</span><span class="err">!</span> <span class="n">pip</span> <span class="n">install</span> <span class="n">seaborn</span> <span class="o">-</span><span class="n">U</span>  <span class="c1"># パッケージのアップデートは -U オプションを付ける
</span></pre></div>
</div>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">seaborn</span>
<span class="k">print</span><span class="p">(</span> <span class="n">seaborn</span><span class="o">.</span><span class="n">__version__</span><span class="p">)</span>
<span class="c1"># out[]: 0.9.0
</span></pre></div>
</div>

<h2>
<span id="scatterplot" class="fragment"></span><a href="#scatterplot"><i class="fa fa-link"></i></a>scatterplot()</h2>

<p>散布図をプロットする。<br>
数値データの x と y の関係を、色・大きさ・形のパラメータを使って表現できる。</p>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="n">sns</span><span class="p">;</span> <span class="n">sns</span><span class="o">.</span><span class="nb">set</span><span class="p">()</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="n">plt</span>
<span class="n">tips</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s">"tips"</span><span class="p">)</span>
<span class="n">tips</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<table>
<thead>
<tr>
<th style="text-align: left">total_bill</th>
<th style="text-align: left">tip</th>
<th style="text-align: left">sex</th>
<th style="text-align: left">smoker</th>
<th style="text-align: left">day</th>
<th style="text-align: left">time</th>
<th style="text-align: left">size</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">16.99</td>
<td style="text-align: left">1.01</td>
<td style="text-align: left">Female</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Sun</td>
<td style="text-align: left">Dinner</td>
<td style="text-align: left">2</td>
</tr>
<tr>
<td style="text-align: left">10.34</td>
<td style="text-align: left">1.66</td>
<td style="text-align: left">Male</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Sun</td>
<td style="text-align: left">Dinner</td>
<td style="text-align: left">3</td>
</tr>
<tr>
<td style="text-align: left">21.01</td>
<td style="text-align: left">3.50</td>
<td style="text-align: left">Male</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Sun</td>
<td style="text-align: left">Dinner</td>
<td style="text-align: left">3</td>
</tr>
<tr>
<td style="text-align: left">23.68</td>
<td style="text-align: left">3.31</td>
<td style="text-align: left">Male</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Sun</td>
<td style="text-align: left">Dinner</td>
<td style="text-align: left">2</td>
</tr>
<tr>
<td style="text-align: left">24.59</td>
<td style="text-align: left">3.61</td>
<td style="text-align: left">Female</td>
<td style="text-align: left">No</td>
<td style="text-align: left">Sun</td>
<td style="text-align: left">Dinner</td>
<td style="text-align: left">4</td>
</tr>
</tbody>
</table>

<h3>
<span id="シンプルな散布図" class="fragment"></span><a href="#%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E6%95%A3%E5%B8%83%E5%9B%B3"><i class="fa fa-link"></i></a>シンプルな散布図</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"total_bill"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">tips</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F4464726a-bb34-9fab-67ad-53e2853c1d72.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7051b81a28cd02ad04fbe4749fe61168" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F4464726a-bb34-9fab-67ad-53e2853c1d72.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7051b81a28cd02ad04fbe4749fe61168" alt="scp1.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/4464726a-bb34-9fab-67ad-53e2853c1d72.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F4464726a-bb34-9fab-67ad-53e2853c1d72.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=1c4279173b63c0daba8e85ff41cb35d2 1x" loading="lazy"></a></p>

<h3>
<span id="グループごとに色分け" class="fragment"></span><a href="#%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%94%E3%81%A8%E3%81%AB%E8%89%B2%E5%88%86%E3%81%91"><i class="fa fa-link"></i></a>グループごとに色分け</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"total_bill"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"time"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">tips</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F2293c51a-4b3f-26db-6d67-fcddd146f9c8.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=6ff6f20d702ffb946689dfb528f9ed37" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F2293c51a-4b3f-26db-6d67-fcddd146f9c8.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=6ff6f20d702ffb946689dfb528f9ed37" alt="scp2.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/2293c51a-4b3f-26db-6d67-fcddd146f9c8.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F2293c51a-4b3f-26db-6d67-fcddd146f9c8.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=c7e3a6d1a33ccfafcf24f3edb88d54ba 1x" loading="lazy"></a></p>

<h3>
<span id="グループごとに色と形状を同じに分ける" class="fragment"></span><a href="#%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%94%E3%81%A8%E3%81%AB%E8%89%B2%E3%81%A8%E5%BD%A2%E7%8A%B6%E3%82%92%E5%90%8C%E3%81%98%E3%81%AB%E5%88%86%E3%81%91%E3%82%8B"><i class="fa fa-link"></i></a>グループごとに色と形状を同じに分ける</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"total_bill"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"time"</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">"time"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">tips</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1f050096-044e-ee93-b81c-f9a456cff95a.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=2e79ba4ce4072be8b62250cfb145e35f" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1f050096-044e-ee93-b81c-f9a456cff95a.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=2e79ba4ce4072be8b62250cfb145e35f" alt="scp3.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/1f050096-044e-ee93-b81c-f9a456cff95a.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1f050096-044e-ee93-b81c-f9a456cff95a.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=e938ae94b66d8806b9edb5d442270ec2 1x" loading="lazy"></a></p>

<h3>
<span id="グループごとに色と形状を別々に分ける" class="fragment"></span><a href="#%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%94%E3%81%A8%E3%81%AB%E8%89%B2%E3%81%A8%E5%BD%A2%E7%8A%B6%E3%82%92%E5%88%A5%E3%80%85%E3%81%AB%E5%88%86%E3%81%91%E3%82%8B"><i class="fa fa-link"></i></a>グループごとに色と形状を別々に分ける</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"total_bill"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"day"</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">"time"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">tips</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fc12af6a3-e0be-3e04-0283-a3555e04187c.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=3ae8a7309b7b3d5561dadce0d43ec670" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fc12af6a3-e0be-3e04-0283-a3555e04187c.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=3ae8a7309b7b3d5561dadce0d43ec670" alt="scp4.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/c12af6a3-e0be-3e04-0283-a3555e04187c.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fc12af6a3-e0be-3e04-0283-a3555e04187c.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=34c6637c88bd5d50e974df640c194b34 1x" loading="lazy"></a></p>

<h3>
<span id="点の大きさで-量的変数を表す" class="fragment"></span><a href="#%E7%82%B9%E3%81%AE%E5%A4%A7%E3%81%8D%E3%81%95%E3%81%A7-%E9%87%8F%E7%9A%84%E5%A4%89%E6%95%B0%E3%82%92%E8%A1%A8%E3%81%99"><i class="fa fa-link"></i></a>点の大きさで 量的変数を表す</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"total_bill"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="s">"size"</span><span class="p">,</span><span class="n">data</span><span class="o">=</span><span class="n">tips</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fa7f174e1-4b81-2a1e-e368-df136c1f0428.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=43012cf4958d35a7dc1d79f7c822c593" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fa7f174e1-4b81-2a1e-e368-df136c1f0428.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=43012cf4958d35a7dc1d79f7c822c593" alt="scp5.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/a7f174e1-4b81-2a1e-e368-df136c1f0428.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fa7f174e1-4b81-2a1e-e368-df136c1f0428.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=40e2e62576a29dcfed5593d428a63345 1x" loading="lazy"></a></p>

<h3>
<span id="点の大きさと色で-量的変数を表す" class="fragment"></span><a href="#%E7%82%B9%E3%81%AE%E5%A4%A7%E3%81%8D%E3%81%95%E3%81%A8%E8%89%B2%E3%81%A7-%E9%87%8F%E7%9A%84%E5%A4%89%E6%95%B0%E3%82%92%E8%A1%A8%E3%81%99"><i class="fa fa-link"></i></a>点の大きさと色で 量的変数を表す</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">scatterplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"total_bill"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"tip"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"size"</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="s">"size"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">tips</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F34819013-954d-04f1-7cc8-c23a7286cae8.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=4043c80008dd8bf56030a76cfa209e2e" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F34819013-954d-04f1-7cc8-c23a7286cae8.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=4043c80008dd8bf56030a76cfa209e2e" alt="scp6.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/34819013-954d-04f1-7cc8-c23a7286cae8.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F34819013-954d-04f1-7cc8-c23a7286cae8.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=e07a7da48cc338317b07e88db22bf34b 1x" loading="lazy"></a></p>

<h2>
<span id="lineplot" class="fragment"></span><a href="#lineplot"><i class="fa fa-link"></i></a>lineplot()</h2>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="n">sns</span><span class="p">;</span> <span class="n">sns</span><span class="o">.</span><span class="nb">set</span><span class="p">()</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="n">plt</span>
<span class="n">fmri</span> <span class="o">=</span> <span class="n">sns</span><span class="o">.</span><span class="n">load_dataset</span><span class="p">(</span><span class="s">"fmri"</span><span class="p">)</span>
<span class="n">fmri</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<table>
<thead>
<tr>
<th style="text-align: left">subject</th>
<th style="text-align: left">timepoint</th>
<th style="text-align: left">event</th>
<th style="text-align: left">region</th>
<th style="text-align: left">signal</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">s13</td>
<td style="text-align: left">18</td>
<td style="text-align: left">stim</td>
<td style="text-align: left">parietal</td>
<td style="text-align: left">-0.017552</td>
</tr>
<tr>
<td style="text-align: left">s5</td>
<td style="text-align: left">14</td>
<td style="text-align: left">stim</td>
<td style="text-align: left">parietal</td>
<td style="text-align: left">-0.080883</td>
</tr>
<tr>
<td style="text-align: left">s12</td>
<td style="text-align: left">18</td>
<td style="text-align: left">stim</td>
<td style="text-align: left">parietal</td>
<td style="text-align: left">-0.081033</td>
</tr>
<tr>
<td style="text-align: left">s11</td>
<td style="text-align: left">18</td>
<td style="text-align: left">stim</td>
<td style="text-align: left">parietal</td>
<td style="text-align: left">-0.046134</td>
</tr>
<tr>
<td style="text-align: left">s10</td>
<td style="text-align: left">18</td>
<td style="text-align: left">stim</td>
<td style="text-align: left">parietal</td>
<td style="text-align: left">-0.037970</td>
</tr>
</tbody>
</table>

<h3>
<span id="シンプルな線グラフ信頼区間のエラーバンド付き" class="fragment"></span><a href="#%E3%82%B7%E3%83%B3%E3%83%97%E3%83%AB%E3%81%AA%E7%B7%9A%E3%82%B0%E3%83%A9%E3%83%95%E4%BF%A1%E9%A0%BC%E5%8C%BA%E9%96%93%E3%81%AE%E3%82%A8%E3%83%A9%E3%83%BC%E3%83%90%E3%83%B3%E3%83%89%E4%BB%98%E3%81%8D"><i class="fa fa-link"></i></a>シンプルな線グラフ（信頼区間のエラーバンド付き）</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"timepoint"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"signal"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">fmri</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F71143373-56dd-f0ed-372c-0156b22534ed.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=3533aeb24df2161c2d5a514452ec7a24" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F71143373-56dd-f0ed-372c-0156b22534ed.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=3533aeb24df2161c2d5a514452ec7a24" alt="lnp1.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/71143373-56dd-f0ed-372c-0156b22534ed.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F71143373-56dd-f0ed-372c-0156b22534ed.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=8aa6d528b708b737942f7b41aa44f353 1x" loading="lazy"></a></p>

<h3>
<span id="グループごとに色分け-1" class="fragment"></span><a href="#%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%94%E3%81%A8%E3%81%AB%E8%89%B2%E5%88%86%E3%81%91-1"><i class="fa fa-link"></i></a>グループごとに色分け</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"timepoint"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"signal"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">fmri</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F98aed823-c6ab-c0e4-d11a-91ee014512d6.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=86a21e6b4c65be32b29640b89401d438" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F98aed823-c6ab-c0e4-d11a-91ee014512d6.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=86a21e6b4c65be32b29640b89401d438" alt="lnp2.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/98aed823-c6ab-c0e4-d11a-91ee014512d6.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F98aed823-c6ab-c0e4-d11a-91ee014512d6.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=0914f06f314756a55388c9dd57e0e0f4 1x" loading="lazy"></a></p>

<h3>
<span id="グループごとに色分け実践破線分け" class="fragment"></span><a href="#%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E3%81%94%E3%81%A8%E3%81%AB%E8%89%B2%E5%88%86%E3%81%91%E5%AE%9F%E8%B7%B5%E7%A0%B4%E7%B7%9A%E5%88%86%E3%81%91"><i class="fa fa-link"></i></a>グループごとに色分け・実践/破線分け</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"timepoint"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"signal"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">fmri</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1dcb696d-ac2a-b1a4-450e-83f73f1f60fb.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7a9cb0f667f8a90f45a94212a15ed90c" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1dcb696d-ac2a-b1a4-450e-83f73f1f60fb.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=7a9cb0f667f8a90f45a94212a15ed90c" alt="lnp3.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/1dcb696d-ac2a-b1a4-450e-83f73f1f60fb.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1dcb696d-ac2a-b1a4-450e-83f73f1f60fb.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=c148589c1fb409e56e5405a937d0dd41 1x" loading="lazy"></a></p>

<h3>
<span id="色分けと実線破線分けで2つの異なる変数を表す" class="fragment"></span><a href="#%E8%89%B2%E5%88%86%E3%81%91%E3%81%A8%E5%AE%9F%E7%B7%9A%E7%A0%B4%E7%B7%9A%E5%88%86%E3%81%91%E3%81%A72%E3%81%A4%E3%81%AE%E7%95%B0%E3%81%AA%E3%82%8B%E5%A4%89%E6%95%B0%E3%82%92%E8%A1%A8%E3%81%99"><i class="fa fa-link"></i></a>色分けと実線/破線分けで、2つの異なる変数を表す</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"timepoint"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"signal"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"region"</span><span class="p">,</span> <span class="n">style</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">fmri</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fa4fad18c-758b-e926-eed9-07b2f8e29cd0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=24552944990fa78f4092f6eda93c842a" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fa4fad18c-758b-e926-eed9-07b2f8e29cd0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=24552944990fa78f4092f6eda93c842a" alt="lnp4.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/a4fad18c-758b-e926-eed9-07b2f8e29cd0.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fa4fad18c-758b-e926-eed9-07b2f8e29cd0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=367829d50612075a9674afde37e2aeb8 1x" loading="lazy"></a></p>

<h3>
<span id="破線の代わりに点を使ってグループ分け" class="fragment"></span><a href="#%E7%A0%B4%E7%B7%9A%E3%81%AE%E4%BB%A3%E3%82%8F%E3%82%8A%E3%81%AB%E7%82%B9%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E5%88%86%E3%81%91"><i class="fa fa-link"></i></a>破線の代わりに点を使ってグループ分け</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"timepoint"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"signal"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span> 
             <span class="n">style</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span> <span class="n">markers</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">dashes</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">fmri</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F53ff5f59-0f76-8803-cd1c-e78bb7ba9a8d.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=517bc797062c7ce3af5f8b8d32f5139d" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F53ff5f59-0f76-8803-cd1c-e78bb7ba9a8d.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=517bc797062c7ce3af5f8b8d32f5139d" alt="lnp5.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/53ff5f59-0f76-8803-cd1c-e78bb7ba9a8d.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F53ff5f59-0f76-8803-cd1c-e78bb7ba9a8d.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=df331dd97c39b73fc7dbe83ce06defb3 1x" loading="lazy"></a></p>

<h3>
<span id="標準誤差のエラーバー付き線グラフ" class="fragment"></span><a href="#%E6%A8%99%E6%BA%96%E8%AA%A4%E5%B7%AE%E3%81%AE%E3%82%A8%E3%83%A9%E3%83%BC%E3%83%90%E3%83%BC%E4%BB%98%E3%81%8D%E7%B7%9A%E3%82%B0%E3%83%A9%E3%83%95"><i class="fa fa-link"></i></a>標準誤差のエラーバー付き線グラフ</h3>

<div class="code-frame" data-lang="py">
<div class="code-lang"><span class="bold">python</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">lineplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"timepoint"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"signal"</span><span class="p">,</span> <span class="n">hue</span><span class="o">=</span><span class="s">"event"</span><span class="p">,</span>
             <span class="n">err_style</span><span class="o">=</span><span class="s">"bars"</span><span class="p">,</span> <span class="n">ci</span><span class="o">=</span><span class="mi">68</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">fmri</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F0982b6a4-5b61-5a63-0f67-3c8c7f9f8768.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=a3d273bc34887f011d85b791f4599c15" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F0982b6a4-5b61-5a63-0f67-3c8c7f9f8768.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=a3d273bc34887f011d85b791f4599c15" alt="lnp6.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/0982b6a4-5b61-5a63-0f67-3c8c7f9f8768.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F0982b6a4-5b61-5a63-0f67-3c8c7f9f8768.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=87c135f0e55dac7a82a4cb845038a50b 1x" loading="lazy"></a></p>
