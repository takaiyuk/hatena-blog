https://qiita.com/takaiyuk/items/38c303c50fdc132bb378

2018-11-11T17:54:33+09:00

2018-11-11T17:54:33+09:00


<h2>
<span id="トピック" class="fragment"></span><a href="#%E3%83%88%E3%83%94%E3%83%83%E3%82%AF"><i class="fa fa-link"></i></a>トピック</h2>

<ul>
<li><p>データの操作ではなく、DBやテーブル自体を更新したり、操作したりする系の基本的なクエリ集です。（自分用メモなので怪しい所が多々あるかもしれない）</p></li>
<li>
<p>以下の記事に基本操作をまとめています（Python コードと並べて）</p>

<ul>
<li><a href="https://qiita.com/takaiyuk/items/5232442eaeb01299b265" id="reference-888b520e17aadc125dac">SQL と Pandas の対応表</a></li>
</ul>
</li>
<li><p><strong>Udemy の<a href="https://www.udemy.com/standard-sql-for-beginners/" rel="nofollow noopener" target="_blank">こちら</a>のコースで勉強していました。</strong></p></li>
</ul>

<h2>
<span id="データの更新" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E6%9B%B4%E6%96%B0"><i class="fa fa-link"></i></a>データの更新</h2>

<h3>
<span id="新規データの追加" class="fragment"></span><a href="#%E6%96%B0%E8%A6%8F%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E8%BF%BD%E5%8A%A0"><i class="fa fa-link"></i></a>新規データの追加</h3>

<ul>
<li>新規データを1行追加

<ul>
<li>列リストと、values句の値リストは、数が一致している必要がある。</li>
</ul>
</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold">sql</span></div>
<div class="highlight"><pre><span class="k">insert</span> <span class="k">into</span>
    <span class="k">TABLE</span> <span class="p">(</span><span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span><span class="p">,</span> <span class="p">...)</span>
<span class="k">values</span>
    <span class="p">(</span><span class="n">VALUE1</span><span class="p">,</span> <span class="n">VALUE2</span><span class="p">,</span> <span class="p">...)</span>
</pre></div>
</div>

<ul>
<li>列リストを省略して新規データを追加

<ul>
<li>テーブルの前列に対して、値を指定する</li>
</ul>
</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold">sql</span></div>
<div class="highlight"><pre><span class="k">insert</span> <span class="k">into</span>
    <span class="k">TABLE</span>  <span class="c1">-- 3列のテーブルとする</span>
<span class="k">values</span>
    <span class="p">(</span><span class="n">VALUE1</span><span class="p">,</span> <span class="n">VALUE2</span><span class="p">,</span> <span class="n">VALUE3</span><span class="p">)</span>
</pre></div>
</div>

<ul>
<li>複数行を追加</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold">sql</span></div>
<div class="highlight"><pre><span class="k">insert</span> <span class="k">into</span>
    <span class="k">TABLE</span> <span class="p">(</span><span class="n">COL1</span><span class="p">,</span> <span class="n">COL2</span><span class="p">,</span> <span class="p">...)</span>
<span class="k">values</span>
    <span class="p">(</span><span class="n">VALUE1</span><span class="p">,</span> <span class="n">VALUE2</span><span class="p">,</span> <span class="p">...)</span>
    <span class="p">(</span><span class="n">VALUE3</span><span class="p">,</span> <span class="n">VALUE4</span><span class="p">,</span> <span class="p">...)</span>
    <span class="p">(</span><span class="n">VALUE5</span><span class="p">,</span> <span class="n">VALUE6</span><span class="p">,</span> <span class="p">...)</span>
</pre></div>
</div>

<h3>
<span id="データの更新-1" class="fragment"></span><a href="#%E3%83%87%E3%83%BC%E3%82%BF%E3%81%AE%E6%9B%B4%E6%96%B0-1"><i class="fa fa-link"></i></a>データの更新</h3>

<ul>
<li>ある列すべての値を更新</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">set</span> <span class="n">sql_safe_updates</span> <span class="o">=</span> <span class="mi">0</span><span class="p">;</span>  <span class="c1">-- safe モードの解除。実務ではあまり使わない</span>

<span class="k">update</span>
    <span class="k">TABLE</span>
<span class="k">set</span>
    <span class="n">COL</span> <span class="o">=</span> <span class="n">COL</span> <span class="o">*</span> <span class="mi">0</span><span class="p">.</span><span class="mi">9</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li>特定の行のデータだけを更新</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">update</span>
    <span class="k">TABLE</span>
<span class="k">set</span>
    <span class="n">COL1</span> <span class="o">=</span> <span class="n">COL1</span> <span class="o">*</span> <span class="mi">0</span><span class="p">.</span><span class="mi">9</span>
<span class="k">where</span>
    <span class="n">col2</span> <span class="o">&gt;</span> <span class="mi">1000</span><span class="p">;</span>
</pre></div>
</div>

<h3>
<span id="行の削除" class="fragment"></span><a href="#%E8%A1%8C%E3%81%AE%E5%89%8A%E9%99%A4"><i class="fa fa-link"></i></a>行の削除</h3>

<p>大量のデータ（10万件以上とか）を削除する際には予想以上に時間がかかるので注意</p>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">delete</span> <span class="k">from</span>
    <span class="k">TABLE</span>
<span class="p">[</span><span class="k">where</span>
    <span class="err">条件式</span><span class="p">]</span>  <span class="c1">-- 削除する行の条件を指定できる。指定なしだとテーブルの全行を削除。</span>
</pre></div>
</div>

<h2>
<span id="db構造の操作" class="fragment"></span><a href="#db%E6%A7%8B%E9%80%A0%E3%81%AE%E6%93%8D%E4%BD%9C"><i class="fa fa-link"></i></a>DB構造の操作</h2>

<h3>
<span id="dbの追加削除" class="fragment"></span><a href="#db%E3%81%AE%E8%BF%BD%E5%8A%A0%E5%89%8A%E9%99%A4"><i class="fa fa-link"></i></a>DBの追加・削除</h3>

<ul>
<li><strong>DB確認</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">show</span> <span class="n">databases</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li>
<strong>DB追加</strong>

<ul>
<li>半角の英数字とアンダースコアで書く。</li>
<li>マジックナンバー（命名者しか意味が分からない数字）を使った名前は避ける。</li>
</ul>
</li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">create</span> <span class="k">database</span> 
    <span class="n">DB_NAME</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li><strong>DBの削除</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">drop</span> <span class="k">database</span>
    <span class="n">DB_NAME</span><span class="p">;</span>
</pre></div>
</div>

<h3>
<span id="テーブルの追加削除構造変更" class="fragment"></span><a href="#%E3%83%86%E3%83%BC%E3%83%96%E3%83%AB%E3%81%AE%E8%BF%BD%E5%8A%A0%E5%89%8A%E9%99%A4%E6%A7%8B%E9%80%A0%E5%A4%89%E6%9B%B4"><i class="fa fa-link"></i></a>テーブルの追加・削除・構造変更</h3>

<ul>
<li><strong>テーブルの確認</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="c1">-- use DB_NAME;</span>
<span class="k">show</span> <span class="n">tables</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li><strong>列の確認</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">show</span> <span class="n">columns</span> <span class="k">from</span> <span class="k">TABLE</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li><strong>テーブルの新規作成</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">create</span> <span class="k">table</span> 
    <span class="k">TABLE_NAME</span><span class="p">(</span><span class="n">COLNAME1</span> <span class="n">DATATYPE</span> <span class="k">not</span> <span class="k">null</span> <span class="n">auto_increment</span> <span class="k">primary</span> <span class="k">key</span><span class="p">,</span>
               <span class="n">COLNAME2</span> <span class="n">DATATYPE</span> <span class="k">not</span> <span class="k">null</span><span class="p">);</span>
<span class="cm">/*
- not null: null を許可しない
- auto_increment: idを自動的に振る
- primary key: 主キーの設定
*/</span>
</pre></div>
</div>

<ul>
<li><strong>テーブルの構造変更</strong></li>
</ul>

<p>テーブルに列の追加</p>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">alter</span> <span class="k">table</span> <span class="k">TABLE</span>  <span class="c1">-- 変更するテーブル名</span>
<span class="k">add</span> <span class="n">NEW_COL</span> <span class="n">DATATYPE</span>  <span class="c1">-- 新しい列の列名とデータ型</span>
<span class="k">after</span> <span class="n">COL</span><span class="p">;</span>  <span class="c1">-- どの列の後ろに置くか</span>
</pre></div>
</div>

<p>テーブルの列の変更</p>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">alter</span> <span class="k">table</span> <span class="k">TABLE</span> 
<span class="n">change</span> <span class="n">OLD_COL</span> <span class="n">NEW_COL</span> <span class="n">DATATYPE</span><span class="p">;</span>
</pre></div>
</div>

<p>テーブルの列の削除</p>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">alter</span> <span class="k">table</span> <span class="k">TABLE</span>
<span class="k">drop</span> <span class="n">COL</span><span class="p">;</span>
</pre></div>
</div>

<ul>
<li><strong>テーブルの削除</strong></li>
</ul>

<div class="code-frame" data-lang="sql">
<div class="code-lang"><span class="bold"> sql</span></div>
<div class="highlight"><pre><span class="k">drop</span> <span class="k">table</span> 
    <span class="k">TABLE_NAME</span>
</pre></div>
</div>
