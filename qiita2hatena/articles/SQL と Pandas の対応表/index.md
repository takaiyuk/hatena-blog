https://qiita.com/takaiyuk/items/5232442eaeb01299b265

2018-11-10T22:55:36+09:00

2020-01-08T09:34:07+09:00


<h2>
<span id="トピック" class="fragment"></span><a href="#%E3%83%88%E3%83%94%E3%83%83%E3%82%AF"><i class="fa fa-link"></i></a>トピック</h2>

<p>SQL のクエリと、Pandas のメソッドの対応表を作成する。</p>

<p>SQL 勉強中のため、備忘録代わりに箇条書き（殴り書き）で書いていく。</p>

<p><strong>Udemy の<a href="https://www.udemy.com/standard-sql-for-beginners/" rel="nofollow noopener" target="_blank">こちら</a>のコースで勉強していました。</strong></p>

<p>DBやテーブル自体の更新・操作に関するものは<a href="https://qiita.com/takaiyuk/items/38c303c50fdc132bb378" id="reference-a93f15e03748c60f5fe0">こちら</a>にまとめている。（SQL のクエリだけを書き散らかしているだけ）</p>

<h2>
<span id="順序" class="fragment"></span><a href="#%E9%A0%86%E5%BA%8F"><i class="fa fa-link"></i></a>順序</h2>

<h3>
<span id="記述順序" class="fragment"></span><a href="#%E8%A8%98%E8%BF%B0%E9%A0%86%E5%BA%8F"><i class="fa fa-link"></i></a>記述順序</h3>

<ol>
<li>select</li>
<li>from</li>
<li>join系(+on)</li>
<li>where</li>
<li>group by</li>
<li>having</li>
<li>order by</li>
<li>limit</li>
</ol>

<h3>
<span id="実行順序" class="fragment"></span><a href="#%E5%AE%9F%E8%A1%8C%E9%A0%86%E5%BA%8F"><i class="fa fa-link"></i></a>実行順序(※)</h3>

<ol>
<li>from</li>
<li>join系(+on)</li>
<li>where</li>
<li>group by</li>
<li>select</li>
<li>having</li>
<li>order by</li>
<li>limit</li>
</ol>

<p><strong>(※)追記</strong></p>

<p><a href="/nora1962jp" class="user-mention js-hovercard" title="nora1962jp" data-hovercard-target-type="user" data-hovercard-target-name="nora1962jp">@nora1962jp</a> さんからご指摘をいただきましたので、コメント内容を追記します。</p>

<blockquote>
<blockquote>
<p>実行順序<br>
from<br>
join系(+on)<br>
where</p>
</blockquote>

<p>SQLについてなら実行順序はonとwhereの順序はonが先とは一概に言えないです。<br>
外部結合などが絡まない</p>

<p>from a join b<br>
on a.id = b.id<br>
where a.col1 = 1</p>

<p>のような場合、a.col1にインデックスが存在し選択性が有効ならwhereの判定結果をもとに結合処理を行うrdbmsは少なくありません。</p>
</blockquote>

<h2>
<span id="基本操作" class="fragment"></span><a href="#%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C"><i class="fa fa-link"></i></a>基本操作</h2>

<h3>
<span id="列選択" class="fragment"></span><a href="#%E5%88%97%E9%81%B8%E6%8A%9E"><i class="fa fa-link"></i></a>列選択</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span> 
<span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">loc</span><span class="p">[:,</span> <span class="p">[</span><span class="s">"COL1"</span><span class="p">,</span> <span class="s">"COL2"</span><span class="p">]]</span>
</pre></div>
</div>

<h3>
<span id="列名変更" class="fragment"></span><a href="#%E5%88%97%E5%90%8D%E5%A4%89%E6%9B%B4"><i class="fa fa-link"></i></a>列名変更</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> 
    <span class="n">COL1</span> <span class="k">as</span> <span class="n">COL1_renamed</span><span class="p">,</span>
    <span class="n">COL2</span> <span class="k">as</span> <span class="n">COL2_renamed</span> 
<span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">rename</span><span class="p">(</span><span class="n">columns</span><span class="o">=</span><span class="p">{</span><span class="s">"COL1"</span><span class="p">:</span> <span class="s">"COL1_renamed"</span><span class="p">,</span> <span class="s">"COL2"</span><span class="p">:</span> <span class="s">"COL2_renamed"</span><span class="p">})</span>
</pre></div>
</div>

<h3>
<span id="列追加" class="fragment"></span><a href="#%E5%88%97%E8%BF%BD%E5%8A%A0"><i class="fa fa-link"></i></a>列追加</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> 
    <span class="n">COL1</span> <span class="k">as</span> <span class="n">COL1_renamed</span><span class="p">,</span> 
    <span class="n">COL2</span> <span class="k">as</span> <span class="n">COL2_renamed</span><span class="p">,</span>
    <span class="n">COL2</span> <span class="o">*</span> <span class="mi">2</span> <span class="k">as</span> <span class="n">NEW_COL</span>
<span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="s">"NEW_COL"</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">]</span> <span class="o">*</span> <span class="mi">2</span>
</pre></div>
</div>

<h3>
<span id="条件付き行抽出" class="fragment"></span><a href="#%E6%9D%A1%E4%BB%B6%E4%BB%98%E3%81%8D%E8%A1%8C%E6%8A%BD%E5%87%BA"><i class="fa fa-link"></i></a>条件付き行抽出</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">COL1</span> <span class="o">=</span> <span class="s1">'hoge'</span>
    <span class="k">and</span> <span class="n">COL2</span> <span class="o">&gt;</span> <span class="mi">100</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span><span class="o">==</span><span class="s">"hoge"</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">100</span><span class="p">)]</span>
</pre></div>
</div>

<h3>
<span id="代表的な演算子" class="fragment"></span><a href="#%E4%BB%A3%E8%A1%A8%E7%9A%84%E3%81%AA%E6%BC%94%E7%AE%97%E5%AD%90"><i class="fa fa-link"></i></a>代表的な演算子</h3>

<ul>
<li><strong>一致</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">COL1</span> <span class="o">=</span> <span class="s1">'hoge'</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span> <span class="o">==</span> <span class="s">"hoge"</span><span class="p">]</span>
</pre></div>
</div>

<ul>
<li><strong>不一致</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">COL1</span> <span class="o">!=</span> <span class="s1">'hoge'</span><span class="p">;</span>
<span class="c1">-- select * from TABLE where COL1 &lt;&gt; 'hoge'; という書き方もできる</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span> <span class="o">!=</span> <span class="s">"hoge"</span><span class="p">]</span>
</pre></div>
</div>

<ul>
<li><strong>含まれない</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">COL2</span> <span class="k">not</span> <span class="k">in</span> <span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">);</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="o">~</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span><span class="o">.</span><span class="n">isin</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">3</span><span class="p">))]</span>
</pre></div>
</div>

<ul>
<li><strong>NULL</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">COL2</span> <span class="k">is</span> <span class="k">null</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">]</span><span class="o">.</span><span class="n">isnull</span><span class="p">()]</span>
</pre></div>
</div>

<ul>
<li><strong>範囲</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">COL2</span> <span class="k">between</span> <span class="mi">1000</span> <span class="k">and</span> <span class="mi">2000</span><span class="p">;</span>
<span class="c1">-- select * from TABLE where COL2 &gt;= 1000 and COL2 &lt;= 2000; という書き方もできる</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">1000</span><span class="p">)</span> <span class="o">&amp;</span> <span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">]</span> <span class="o">&lt;=</span> <span class="mi">2000</span><span class="p">)]</span>
</pre></div>
</div>

<h3>
<span id="パターンマッチング" class="fragment"></span><a href="#%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%83%9E%E3%83%83%E3%83%81%E3%83%B3%E3%82%B0"><i class="fa fa-link"></i></a>パターンマッチング</h3>

<p>ワイルドカード文字を利用</p>

<blockquote>
<p><strong>追記</strong><br>
@satorimon さんのご指摘により、Python のコードを埋めることができました。</p>
</blockquote>

<ul>
<li><strong>0文字以上の任意の文字列: '%'</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">NAME_COL</span> <span class="k">like</span> <span class="s1">'中%'</span><span class="p">;</span>
<span class="c1">-- 「中林」とか「中田」とかが抽出</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"NAME_COL"</span><span class="p">]</span><span class="o">.</span><span class="nb">str</span><span class="o">.</span><span class="n">startswith</span><span class="p">(</span><span class="s">'中'</span><span class="p">)]</span>  <span class="c1"># 指定した文字で始まる
</span></pre></div>
</div>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">NAME_COL</span> <span class="k">like</span> <span class="s1">'%中%'</span><span class="p">;</span>
<span class="c1">-- 「中林」とか「竹中」とかが抽出</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"NAME_COL"</span><span class="p">]</span><span class="o">.</span><span class="nb">str</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="s">'[ぁ-んァ-ン一-龥]中[ぁ-んァ-ン一-龥]'</span><span class="p">,</span> <span class="n">regex</span><span class="o">=</span><span class="bp">True</span><span class="p">)]</span>
<span class="c1"># [ぁ-んァ-ン一-龥]: 任意のひらがな・カタカナ・漢字
# cf.) http://fujiringo.sakura.ne.jp/hayabusa/blog/code/2011/07/post-1.html
</span></pre></div>
</div>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">NAME_COL</span> <span class="k">like</span> <span class="s1">'%子'</span><span class="p">;</span>
<span class="c1">-- 「翔子」とか「美智子」とか</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"NAME_COL"</span><span class="p">]</span><span class="o">.</span><span class="nb">str</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s">'子'</span><span class="p">)]</span>  <span class="c1"># 指定した文字で終わる
</span></pre></div>
</div>

<ul>
<li><strong>任意の1文字: '_'</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="n">NAME_COL</span> <span class="k">like</span> <span class="s1">'__子'</span><span class="p">;</span>
<span class="c1">-- アンダースコア(_)が2つ</span>
<span class="c1">-- 「あや子」とか「美智子」とか</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"NAME_COL"</span><span class="p">]</span><span class="o">.</span><span class="nb">str</span><span class="o">.</span><span class="n">contains</span><span class="p">(</span><span class="s">'..子'</span><span class="p">,</span> <span class="n">regex</span><span class="o">=</span><span class="bp">True</span><span class="p">)]</span>  <span class="c1"># ○○子: 正規表現で"."は任意の一文字を表す
</span></pre></div>
</div>

<h3>
<span id="取得件数を制限" class="fragment"></span><a href="#%E5%8F%96%E5%BE%97%E4%BB%B6%E6%95%B0%E3%82%92%E5%88%B6%E9%99%90"><i class="fa fa-link"></i></a>取得件数を制限</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">limit</span> <span class="mi">10</span><span class="p">;</span>
<span class="c1">-- 最初の10行を取得</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
</pre></div>
</div>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">limit</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">;</span>
<span class="c1">-- 0行目の次から、10行を取得</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">10</span><span class="p">,</span> <span class="p">:]</span>
</pre></div>
</div>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">limit</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">10</span><span class="p">;</span>
<span class="c1">-- 10行目の次から、10行を取得</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">10</span><span class="p">:</span><span class="mi">20</span><span class="p">,</span> <span class="p">:]</span>
</pre></div>
</div>

<h2>
<span id="データの集約" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E9%9B%86%E7%B4%84"><i class="fa fa-link"></i></a>データの集約</h2>

<ul>
<li>expr: expression(式)...引数</li>
</ul>

<h3>
<span id="合計値" class="fragment"></span><a href="#%E5%90%88%E8%A8%88%E5%80%A4"><i class="fa fa-link"></i></a>合計値</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="k">sum</span><span class="p">(</span><span class="n">COL1</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">data</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span><span class="o">.</span><span class="nb">sum</span><span class="p">()</span>
</pre></div>
</div>

<h3>
<span id="平均値" class="fragment"></span><a href="#%E5%B9%B3%E5%9D%87%E5%80%A4"><i class="fa fa-link"></i></a>平均値</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="k">avg</span><span class="p">(</span><span class="n">COL1</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">data</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span>
</pre></div>
</div>

<ul>
<li><strong>最小値</strong></li>
</ul>

<p>省略</p>

<ul>
<li><strong>最大値</strong></li>
</ul>

<p>省略</p>

<h3>
<span id="集約関数における-null-の扱い" class="fragment"></span><a href="#%E9%9B%86%E7%B4%84%E9%96%A2%E6%95%B0%E3%81%AB%E3%81%8A%E3%81%91%E3%82%8B-null-%E3%81%AE%E6%89%B1%E3%81%84"><i class="fa fa-link"></i></a>集約関数における null の扱い</h3>

<ul>
<li>集約関数では、null は基本的に無視される </li>
<li>値に null が含まれないように DB 設計を構造したほうがトラブルが減る

<ul>
<li>null を許可する場合、0 と null の違いや、null と空文字の違いを意識する必要がある</li>
<li>例えば、null の代わりに下記は使えないのか？検討する

<ul>
<li>数値: 0</li>
<li>文字列: ''(空文字)</li>
</ul>
</li>
</ul>
</li>
</ul>

<h3>
<span id="カウント" class="fragment"></span><a href="#%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88"><i class="fa fa-link"></i></a>カウント</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="k">count</span><span class="p">(</span><span class="n">COL1</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="ユニークなカウント" class="fragment"></span><a href="#%E3%83%A6%E3%83%8B%E3%83%BC%E3%82%AF%E3%81%AA%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88"><i class="fa fa-link"></i></a>ユニークなカウント</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="k">count</span><span class="p">(</span><span class="k">distinct</span> <span class="n">COL1</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="nb">len</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">())</span>
</pre></div>
</div>

<h3>
<span id="グループ化" class="fragment"></span><a href="#%E3%82%B0%E3%83%AB%E3%83%BC%E3%83%97%E5%8C%96"><i class="fa fa-link"></i></a>グループ化</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="k">count</span><span class="p">(</span><span class="o">*</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">group</span> <span class="k">by</span> <span class="n">COL1</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s">"COL1"</span><span class="p">)</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
</pre></div>
</div>

<h3>
<span id="集約結果をさらに絞り込む" class="fragment"></span><a href="#%E9%9B%86%E7%B4%84%E7%B5%90%E6%9E%9C%E3%82%92%E3%81%95%E3%82%89%E3%81%AB%E7%B5%9E%E3%82%8A%E8%BE%BC%E3%82%80"><i class="fa fa-link"></i></a>集約結果をさらに絞り込む</h3>

<ul>
<li>having: テーブルのデータを集約した結果に対して、条件式を適用する場合に利用する。</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="k">count</span><span class="p">(</span><span class="o">*</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="p">...</span> 
<span class="k">group</span> <span class="k">by</span> <span class="n">COL1</span> 
<span class="k">having</span> <span class="k">count</span><span class="p">(</span><span class="o">*</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df_grouped</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s">"COL1"</span><span class="p">)</span><span class="o">.</span><span class="n">count</span><span class="p">()</span>
<span class="n">df_grouped</span><span class="p">[</span><span class="n">df_grouped</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">]</span> <span class="o">&gt;</span> <span class="mi">10</span><span class="p">]</span>
</pre></div>
</div>

<h2>
<span id="並び替え" class="fragment"></span><a href="#%E4%B8%A6%E3%81%B3%E6%9B%BF%E3%81%88"><i class="fa fa-link"></i></a>並び替え</h2>

<h3>
<span id="降順" class="fragment"></span><a href="#%E9%99%8D%E9%A0%86"><i class="fa fa-link"></i></a>降順</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">order</span> <span class="k">by</span> <span class="n">COL</span> <span class="k">desc</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="s">"COL"</span><span class="p">]</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">ascending</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="昇順" class="fragment"></span><a href="#%E6%98%87%E9%A0%86"><i class="fa fa-link"></i></a>昇順</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">order</span> <span class="k">by</span> <span class="n">COL</span> <span class="k">asc</span><span class="p">;</span>
<span class="c1">-- order by はデフォルトでは昇順なので、昇順の場合 asc は省略可</span>
<span class="c1">-- ただし、取得するデータの並び順が重要な場合は明示的に示しておいたほうが無難</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="s">"COL"</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="複数条件" class="fragment"></span><a href="#%E8%A4%87%E6%95%B0%E6%9D%A1%E4%BB%B6"><i class="fa fa-link"></i></a>複数条件</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">order</span> <span class="k">by</span> <span class="n">COL1</span> <span class="k">desc</span><span class="p">,</span> <span class="n">COL2</span> <span class="k">asc</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="s">"COL1"</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="s">"COL2"</span><span class="p">)</span>
<span class="c1"># 両方とも同じ順ならば、df.sort_values(["COL1", "COL2"]) で可
</span></pre></div>
</div>

<h2>
<span id="関数と演算子" class="fragment"></span><a href="#%E9%96%A2%E6%95%B0%E3%81%A8%E6%BC%94%E7%AE%97%E5%AD%90"><i class="fa fa-link"></i></a>関数と演算子</h2>

<ul>
<li><strong>四則演算, 絶対値, 四捨五入</strong></li>
</ul>

<p>省略</p>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="n">round</span><span class="p">(</span><span class="n">COL1</span> <span class="o">*</span> <span class="mi">1</span><span class="p">.</span><span class="mi">08</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> 
<span class="k">from</span> <span class="n">products</span><span class="p">;</span>
<span class="c1">-- round(COL1 * 1.08, 0) を返り値のデータ型は？？？</span>
</pre></div>
</div>

<ul>
<li>
<strong>null を含んだ計算結果は null を返す</strong><br>
</li>
</ul>

<p>省略</p>

<h3>
<span id="文字列の演算" class="fragment"></span><a href="#%E6%96%87%E5%AD%97%E5%88%97%E3%81%AE%E6%BC%94%E7%AE%97"><i class="fa fa-link"></i></a>文字列の演算</h3>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">concat</span><span class="p">(</span><span class="n">COL1</span><span class="p">,</span> <span class="s1">'_'</span><span class="p">,</span> <span class="n">COL2</span><span class="p">)</span> 
<span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="s">"NEW_COL"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">f</span><span class="s">"{COL1}_{COL2}"</span> <span class="k">for</span> <span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s">"COL1"</span><span class="p">],</span> <span class="n">df</span><span class="p">[</span><span class="s">"COL2"</span><span class="p">])]</span>
</pre></div>
</div>

<h3>
<span id="日付と時刻の演算" class="fragment"></span><a href="#%E6%97%A5%E4%BB%98%E3%81%A8%E6%99%82%E5%88%BB%E3%81%AE%E6%BC%94%E7%AE%97"><i class="fa fa-link"></i></a>日付と時刻の演算</h3>

<ul>
<li>現在の日付: current_date()</li>
<li>現在の時刻: current_time()</li>
<li>現在の日付時刻: current_timestamp()</li>
<li>N日後の日付: d + interval N day</li>
<li>N日前の日付: d - interval N day</li>
<li>X時間後の時刻: t - interval X hour</li>
<li>X時間前の時刻: t - interval X hour</li>
<li>extract: 日付や時刻の特定の部分（年や月）までを取り出す</li>
<li>date_format(TIMESTAMP, '%Y%M'): タイムスタンプから年月を取り出す</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> 
<span class="k">where</span> <span class="k">extract</span><span class="p">(</span><span class="n">year_month</span> <span class="k">from</span> <span class="n">COL</span><span class="p">)</span> <span class="o">=</span> <span class="mi">201811</span><span class="p">;</span>
<span class="c1">-- 単体の場合は、select * from TABLE where extract(year from COL) = 2018; などと書く</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df</span><span class="p">[</span><span class="n">COL</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="n">COL</span><span class="p">])</span>
<span class="n">df</span><span class="p">[</span><span class="s">"COL_year"</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">ymd</span><span class="o">.</span><span class="n">year</span> <span class="k">for</span> <span class="n">ymd</span> <span class="ow">in</span> <span class="n">df</span><span class="p">[</span><span class="n">COL</span><span class="p">]]</span>
<span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s">"COL_year"</span><span class="p">]</span> <span class="o">==</span> <span class="mi">2018</span><span class="p">]</span>
</pre></div>
</div>

<h2>
<span id="結合" class="fragment"></span><a href="#%E7%B5%90%E5%90%88"><i class="fa fa-link"></i></a>結合</h2>

<ul>
<li>テーブルの正規化: テーブルを分けて情報の重複をなくす作業

<ul>
<li>メリット: 管理と容量の面で嬉しい</li>
</ul>
</li>
<li>キーの種類

<ul>
<li>主キー(Primary Key, PK): 1つの行を特定できる列のこと</li>
<li>外部キー(Foreign Key, FK): 他のテーブルとの関連づけに使う列のこと</li>
</ul>
</li>
<li>リレーションシップの種類

<ul>
<li>一対多: ex.) ユーザー - 注文</li>
<li>多対多: ex.) 商品 - 商品カテゴリ</li>
<li>一対一: ex.) ユーザー - 電話番号</li>
</ul>
</li>
</ul>

<h3>
<span id="内部結合" class="fragment"></span><a href="#%E5%86%85%E9%83%A8%E7%B5%90%E5%90%88"><i class="fa fa-link"></i></a>内部結合</h3>

<ul>
<li>お互いに一致している行が結合テーブルの対象となる。</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL1</span><span class="p">,</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL2</span><span class="p">,</span> <span class="n">T2</span><span class="p">.</span><span class="n">COL3</span>
<span class="k">from</span> <span class="n">TABLE1</span> <span class="k">as</span> <span class="n">T1</span>
<span class="k">inner</span> <span class="k">join</span> <span class="n">TABLE2</span> <span class="k">as</span> <span class="n">T2</span>
<span class="k">on</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL4</span> <span class="o">=</span> <span class="n">T2</span><span class="p">.</span><span class="n">COL5</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df1</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">df2</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s">"inner"</span><span class="p">,</span> <span class="n">left_on</span><span class="o">=</span><span class="s">"lkey1"</span><span class="p">,</span> <span class="n">right_on</span><span class="o">=</span><span class="s">"rkey1"</span><span class="p">)</span>
</pre></div>
</div>

<ul>
<li>内部結合 + 絞り込み</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL1</span><span class="p">,</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL2</span><span class="p">,</span> <span class="n">T2</span><span class="p">.</span><span class="n">COL3</span>
<span class="k">from</span> <span class="n">TABLE1</span> <span class="k">as</span> <span class="n">T1</span>
<span class="k">inner</span> <span class="k">join</span> <span class="n">TABLE2</span> <span class="k">as</span> <span class="n">T2</span> <span class="k">on</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL4</span> <span class="o">=</span> <span class="n">T2</span><span class="p">.</span><span class="n">COL5</span>
<span class="k">where</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL2</span> <span class="o">=</span> <span class="s1">'hoge'</span><span class="p">;</span>
</pre></div>
</div>

<h3>
<span id="外部結合" class="fragment"></span><a href="#%E5%A4%96%E9%83%A8%E7%B5%90%E5%90%88"><i class="fa fa-link"></i></a>外部結合</h3>

<ul>
<li>片方のテーブルの情報がすべて出力される、テーブルの結合</li>
<li>片方のテーブルをベースに、お互いに一致している行は結合、一致していない行は null として結合テーブルの対象となる</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL1</span><span class="p">,</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL2</span><span class="p">,</span> <span class="n">T2</span><span class="p">.</span><span class="n">COL3</span>
<span class="k">from</span> <span class="n">TABLE1</span> <span class="k">as</span> <span class="n">T1</span>
<span class="k">left</span> <span class="k">outer</span> <span class="k">join</span> <span class="n">TABLE2</span> <span class="k">as</span> <span class="n">T2</span>  <span class="c1">-- left join とも書かれる</span>
<span class="k">on</span> <span class="n">T1</span><span class="p">.</span><span class="n">COL4</span> <span class="o">=</span> <span class="n">T2</span><span class="p">.</span><span class="n">COL5</span><span class="p">;</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">df1</span><span class="o">.</span><span class="n">merge</span><span class="p">(</span><span class="n">df2</span><span class="p">,</span> <span class="n">how</span><span class="o">=</span><span class="s">'left'</span><span class="p">,</span> <span class="n">left_on</span><span class="o">=</span><span class="s">"lkey1"</span><span class="p">,</span> <span class="n">right_on</span><span class="o">=</span><span class="s">"rkey1"</span><span class="p">)</span>
</pre></div>
</div>

<h3>
<span id="集合演算子" class="fragment"></span><a href="#%E9%9B%86%E5%90%88%E6%BC%94%E7%AE%97%E5%AD%90"><i class="fa fa-link"></i></a>集合演算子</h3>

<p>集合演算子 union は、テーブルの足し算を行う</p>

<ul>
<li>テーブル1とテーブル2で列数を合わせる必要がある。</li>
<li>同じ位置にあるカラムのデータ型は一致している必要がある。</li>
<li>order by は全体の最後に一度しか用いることができない。</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span>
<span class="k">from</span> <span class="k">TABLE</span>
<span class="k">union</span>  <span class="c1">-- 重複削除がデフォルト。残したい場合は、union all とする。</span>
<span class="k">select</span> <span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span>
<span class="k">from</span> <span class="k">TABLE</span>
</pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold"> py</span></div>
<div class="highlight"><pre><span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">([</span> <span class="n">df1</span><span class="p">[[</span><span class="s">"COL1"</span><span class="p">,</span> <span class="s">"COL2"</span><span class="p">]],</span> <span class="n">df</span><span class="p">[[</span><span class="s">"COL1"</span><span class="p">,</span> <span class="s">"COL2"</span><span class="p">]]</span> <span class="p">])</span><span class="o">.</span><span class="n">drop_duplicates</span><span class="p">()</span>
</pre></div>
</div>

<h2>
<span id="ビュー" class="fragment"></span><a href="#%E3%83%93%E3%83%A5%E3%83%BC"><i class="fa fa-link"></i></a>ビュー</h2>

<ul>
<li>
<p><strong>ビューとは</strong></p>

<ul>
<li>データを取り出すSELECT文だけを保存する</li>
<li>DBユーザーの利便性を高める道具（SQLの観点から見ると、テーブルと同じもの）</li>
</ul>
</li>
<li>
<p><strong>ビューのメリット</strong></p>

<ul>
<li>必要なデータが複数のテーブルにまたがる場合などの複雑な集約を行いやすくなる</li>
<li>よく使う select 文はビューにして使い回すことができる</li>
<li>データを保存しないので、記憶装置の容量を節約できる</li>
</ul>
</li>
<li>
<p><strong>ビューのデメリット</strong></p>

<ul>
<li>パフォーマンスの低下を招く場合がある</li>
</ul>
</li>
<li><p><strong>ビューの作成</strong></p></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">create</span> <span class="k">view</span> <span class="n">VIEW_NAME</span><span class="p">(</span><span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span><span class="p">,</span> <span class="p">...)</span>
<span class="k">as</span> 
<span class="k">select</span> <span class="o">*</span> 
<span class="k">from</span> <span class="k">TABLE</span> <span class="p">...;</span>
</pre></div>
</div>

<ul>
<li><strong>ビューの呼び出し</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span>
<span class="k">from</span> <span class="n">VIEW_NAME</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li><strong>ビューの削除</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">drop</span> <span class="k">view</span> <span class="n">VIEW_NAME</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li>
<strong>ビューの制限事項</strong>

<ul>
<li>order by 句が使えない</li>
<li>更新系(insert, delete, update)に制約がある

<ul>
<li>ビューとテーブルの更新は連動して行われるため、集約されたビューは更新不可。</li>
</ul>
</li>
</ul>
</li>
</ul>

<h2>
<span id="サブクエリ" class="fragment"></span><a href="#%E3%82%B5%E3%83%96%E3%82%AF%E3%82%A8%E3%83%AA"><i class="fa fa-link"></i></a>サブクエリ</h2>

<ul>
<li>あるクエリの結果に基づいて、異なるクエリを行う仕組み。</li>
<li>where 句の中で使われることが多い（それ以外にも様々な場所で利用できる）</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">select</span> <span class="o">*</span>
<span class="k">from</span> <span class="n">TABLE1</span>
<span class="k">where</span> <span class="n">COL1</span> <span class="err">演算子</span> <span class="p">(</span><span class="k">select</span> <span class="n">COL2</span> <span class="k">from</span> <span class="n">TABLE2</span> <span class="p">...);</span>
</pre></div>
</div>

<ul>
<li>
<strong>スカラ・サブクエリ</strong>

<ul>
<li>1行1列だけの戻り値を返すサブクエリのこと</li>
</ul>
</li>
</ul>

<h2>
<span id="条件分岐" class="fragment"></span><a href="#%E6%9D%A1%E4%BB%B6%E5%88%86%E5%B2%90"><i class="fa fa-link"></i></a>条件分岐</h2>

<ul>
<li>Python で言うところの if文</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">case</span>
    <span class="k">when</span> <span class="err">条件式</span><span class="mi">1</span> <span class="k">then</span> <span class="err">値</span><span class="mi">1</span>
    <span class="p">[</span><span class="k">when</span> <span class="err">条件式</span><span class="mi">2</span> <span class="k">then</span> <span class="err">値</span><span class="mi">2</span><span class="p">]</span>
    <span class="p">[</span><span class="k">else</span> <span class="err">値</span><span class="mi">3</span><span class="p">]</span>
    <span class="c1">-- []の部分は省略可能</span>
<span class="k">end</span>  <span class="c1">-- end は省略不可</span>
</pre></div>
</div>
