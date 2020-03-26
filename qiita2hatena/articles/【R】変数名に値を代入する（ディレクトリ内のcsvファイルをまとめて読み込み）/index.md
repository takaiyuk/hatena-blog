https://qiita.com/takaiyuk/items/7812bf68143d3757de87

2018-06-07T22:59:50+09:00

2018-06-16T12:39:31+09:00


<h3>
<span id="参照" class="fragment"></span><a href="#%E5%8F%82%E7%85%A7"><i class="fa fa-link"></i></a>参照</h3>

<p>ググってたら以下のサイトが出てきたので、参照にして書きました。</p>

<p><a href="https://futabooo.hatenablog.com/entry/20110910/1315634652" rel="nofollow noopener" target="_blank">Rで他言語みたいに変数名を変えながらfor文とかでつまったこと</a></p>

<h3>
<span id="結論" class="fragment"></span><a href="#%E7%B5%90%E8%AB%96"><i class="fa fa-link"></i></a>結論</h3>

<p>assign()を使うことで、<code>x &lt;- hoge</code>ではない方法でオブジェクトに値を代入できる。</p>

<p><code>assign(x, 'hoge')</code></p>

<h3>
<span id="利用例" class="fragment"></span><a href="#%E5%88%A9%E7%94%A8%E4%BE%8B"><i class="fa fa-link"></i></a>利用例</h3>

<p>これでfor文を回して、あれこれできる。<br>
例えば、readr::read_csv()で一気にデータを読み取りたいとき</p>

<div class="code-frame" data-lang="r"><div class="highlight"><pre><span class="n">files</span><span class="w"> </span><span class="o">&lt;-</span><span class="w"> </span><span class="n">list.files</span><span class="p">()</span><span class="w">  </span><span class="c1"># カレントディレクトリ下のファイル名を取得（全てcsvファイルとする）</span><span class="w">
</span><span class="k">for</span><span class="w"> </span><span class="p">(</span><span class="n">i</span><span class="w"> </span><span class="k">in</span><span class="w"> </span><span class="m">1</span><span class="o">:</span><span class="nf">length</span><span class="p">(</span><span class="n">files</span><span class="p">)){</span><span class="w">
    </span><span class="n">assign</span><span class="p">(</span><span class="n">str_sub</span><span class="p">(</span><span class="nf">as.character</span><span class="p">(</span><span class="n">files</span><span class="p">[</span><span class="n">i</span><span class="p">]),</span><span class="n">end</span><span class="o">=</span><span class="m">-5</span><span class="p">),</span><span class="w"> </span><span class="n">read_csv</span><span class="p">(</span><span class="n">files</span><span class="p">[</span><span class="n">i</span><span class="p">]))</span><span class="w">
</span><span class="p">}</span><span class="w">
</span><span class="c1"># str_sub()しているのは、.csvを排除したファイル名を変数名にしたいため</span><span class="w">
</span></pre></div></div>

<h3>
<span id="まとめ" class="fragment"></span><a href="#%E3%81%BE%E3%81%A8%E3%82%81"><i class="fa fa-link"></i></a>まとめ</h3>

<p>assign()を知っていると色々捗って便利！</p>

<p>（Pythonでも上と同じことをやりたいんですけど、上手い方法あるんですかね）</p>
