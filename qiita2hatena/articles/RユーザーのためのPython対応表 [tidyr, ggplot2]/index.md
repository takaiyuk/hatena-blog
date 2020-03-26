https://qiita.com/takaiyuk/items/0bf9b1db8b4707e3dae2

2018-07-17T19:22:46+09:00

2018-10-27T08:47:19+09:00


<h2>
<span id="概要" class="fragment"></span><a href="#%E6%A6%82%E8%A6%81"><i class="fa fa-link"></i></a>概要</h2>

<p>Rユーザーが、Pythonを使う際に、</p>

<p>「Rのアレ、Pythonではどうやるんだっけ？」</p>

<p>というのをまとめてみた感じです。</p>

<p>Pythonユーザーで、「Pythonのアレ、Rでどうやるんだっけ？」って人にも役立つかもしれません。</p>

<p>(dplyr, stringrの対応はこちらも参考にしてみてください)</p>

<blockquote>
<p><a href="https://qiita.com/takaiyuk/items/4cb1708a3f886b3d2043" id="reference-23d0a75c48e06ee836b1">Rユーザー向け Pythonデータ処理入門</a></p>
</blockquote>

<h3>
<span id="ライブラリ" class="fragment"></span><a href="#%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA"><i class="fa fa-link"></i></a>ライブラリ</h3>

<ul>
<li>tidyr =&gt; pandas</li>
<li>ggplot2 =&gt; seaborn</li>
</ul>

<p>データはirisのデータセットを利用。（R標準のデータセット、列名を一部変更）</p>

<table>
<thead>
<tr>
<th style="text-align: center">Sepal_Length</th>
<th style="text-align: center">Sepal_Width</th>
<th style="text-align: center">Petal_Length</th>
<th style="text-align: center">Petal_Width</th>
<th style="text-align: center">Species</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center">5.1</td>
<td style="text-align: center">3.5</td>
<td style="text-align: center">1.4</td>
<td style="text-align: center">0.2</td>
<td style="text-align: center">setosa</td>
</tr>
<tr>
<td style="text-align: center">4.9</td>
<td style="text-align: center">3.0</td>
<td style="text-align: center">1.4</td>
<td style="text-align: center">0.2</td>
<td style="text-align: center">setosa</td>
</tr>
<tr>
<td style="text-align: center">4.7</td>
<td style="text-align: center">3.2</td>
<td style="text-align: center">1.3</td>
<td style="text-align: center">0.2</td>
<td style="text-align: center">setosa</td>
</tr>
<tr>
<td style="text-align: center">4.6</td>
<td style="text-align: center">3.1</td>
<td style="text-align: center">1.5</td>
<td style="text-align: center">0.2</td>
<td style="text-align: center">setosa</td>
</tr>
<tr>
<td style="text-align: center">5.0</td>
<td style="text-align: center">3.6</td>
<td style="text-align: center">1.4</td>
<td style="text-align: center">0.2</td>
<td style="text-align: center">setosa</td>
</tr>
<tr>
<td style="text-align: center">5.4</td>
<td style="text-align: center">3.9</td>
<td style="text-align: center">1.7</td>
<td style="text-align: center">0.4</td>
<td style="text-align: center">setosa</td>
</tr>
<tr>
<td style="text-align: center">...</td>
<td style="text-align: center">...</td>
<td style="text-align: center">...</td>
<td style="text-align: center">...</td>
<td style="text-align: center">...</td>
</tr>
</tbody>
</table>

<p><br></p>

<h2>
<span id="tidyr" class="fragment"></span><a href="#tidyr"><i class="fa fa-link"></i></a>tidyr</h2>

<h3>
<span id="gather" class="fragment"></span><a href="#gather"><i class="fa fa-link"></i></a>gather</h3>

<p>DataFrameをWideからLongにする</p>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">gather</span><span class="p">(</span><span class="n">key</span><span class="p">,</span><span class="w"> </span><span class="n">value</span><span class="p">,</span><span class="w"> </span><span class="o">-</span><span class="n">Species</span><span class="p">)</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">head</span><span class="p">()</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">pd</span><span class="o">.</span><span class="n">melt</span><span class="p">(</span><span class="n">iris</span><span class="p">,</span> <span class="n">id_vars</span><span class="o">=</span><span class="p">[</span><span class="s">'Species'</span><span class="p">],</span> <span class="n">var_name</span><span class="o">=</span><span class="s">'key'</span><span class="p">,</span> <span class="n">value_name</span><span class="o">=</span><span class="s">'value'</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<div class="code-frame" data-lang="text"><div class="highlight"><pre>　　　　Species          key value
1  setosa Sepal_Length   5.1
2  setosa Sepal_Length   4.9
3  setosa Sepal_Length   4.7
4  setosa Sepal_Length   4.6
5  setosa Sepal_Length   5.0
6  setosa Sepal_Length   5.4
</pre></div></div>

<h3>
<span id="spread" class="fragment"></span><a href="#spread"><i class="fa fa-link"></i></a>spread</h3>

<p>DataFrameをLongからWideにする</p>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> 
    </span><span class="n">rownames_to_column</span><span class="p">(</span><span class="s1">'id'</span><span class="p">)</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w">  </span><span class="c1"># idとなる列がないと "Duplicate identifiers for rows" というエラーが生じる</span><span class="w">
    </span><span class="n">gather</span><span class="p">(</span><span class="n">key</span><span class="p">,</span><span class="w"> </span><span class="n">value</span><span class="p">,</span><span class="w"> </span><span class="o">-</span><span class="n">id</span><span class="p">,</span><span class="w"> </span><span class="o">-</span><span class="n">Species</span><span class="p">)</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w">
    </span><span class="n">spread</span><span class="p">(</span><span class="n">key</span><span class="p">,</span><span class="w"> </span><span class="n">value</span><span class="p">)</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> 
    </span><span class="n">arrange</span><span class="p">(</span><span class="nf">as.integer</span><span class="p">(</span><span class="n">id</span><span class="p">))</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> 
    </span><span class="n">head</span><span class="p">()</span><span class="w">
</span></pre></div>
</div>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">iris_index</span> <span class="o">=</span> <span class="n">iris</span><span class="o">.</span><span class="n">reset_index</span><span class="p">()</span>  <span class="c1"># df.pivot()で列(columns)にする値と行(index)にする値がユニークでないと、 "ValueError: Index contains duplicate entries, cannot reshape" というエラーが生じる
</span><span class="n">iris_melt2</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">melt</span><span class="p">(</span><span class="n">iris_index</span><span class="p">,</span> <span class="n">id_vars</span><span class="o">=</span><span class="p">[</span><span class="s">'index'</span><span class="p">,</span> <span class="s">'Species'</span><span class="p">],</span> <span class="n">var_name</span><span class="o">=</span><span class="s">'key'</span><span class="p">,</span> <span class="n">value_name</span><span class="o">=</span><span class="s">'value'</span><span class="p">)</span>
<span class="n">iris_melt2</span><span class="o">.</span><span class="n">pivot</span><span class="p">(</span><span class="n">index</span><span class="o">=</span><span class="s">'index'</span><span class="p">,</span> <span class="n">columns</span><span class="o">=</span><span class="s">'key'</span><span class="p">,</span> <span class="n">values</span><span class="o">=</span><span class="s">'value'</span><span class="p">)</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>
</div>

<div class="code-frame" data-lang="text"><div class="highlight"><pre>id Species Petal_Length Petal_Width Sepal_Length Sepal_Width
1  1  setosa          1.4         0.2          5.1         3.5
2  2  setosa          1.4         0.2          4.9         3.0
3  3  setosa          1.3         0.2          4.7         3.2
4  4  setosa          1.5         0.2          4.6         3.1
5  5  setosa          1.4         0.2          5.0         3.6
6  6  setosa          1.7         0.4          5.4         3.9
</pre></div></div>

<p><br></p>

<h2>
<span id="ggplot2" class="fragment"></span><a href="#ggplot2"><i class="fa fa-link"></i></a>ggplot2</h2>

<h3>
<span id="histgram" class="fragment"></span><a href="#histgram"><i class="fa fa-link"></i></a>Histgram</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">ggplot</span><span class="p">(</span><span class="n">aes</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">Sepal_Length</span><span class="p">))</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">geom_histogram</span><span class="p">(</span><span class="n">fill</span><span class="o">=</span><span class="s2">"blue"</span><span class="p">,</span><span class="w"> </span><span class="n">alpha</span><span class="o">=</span><span class="m">0.5</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">theme_bw</span><span class="p">()</span><span class="w">
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F25ca622b-17a1-5545-7484-95eeeb6c5b78.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=2f218bad68387fb51b25751ff5621fee" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F25ca622b-17a1-5545-7484-95eeeb6c5b78.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=2f218bad68387fb51b25751ff5621fee" alt="r1.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/25ca622b-17a1-5545-7484-95eeeb6c5b78.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F25ca622b-17a1-5545-7484-95eeeb6c5b78.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=531978ee29d7cf090453b7002748f32f 1x" loading="lazy"></a></p>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">distplot</span><span class="p">(</span><span class="n">iris</span><span class="o">.</span><span class="n">Sepal_Length</span><span class="p">,</span> <span class="n">kde</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>  <span class="c1"># kde=True で密度曲線
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fd4d8ff44-c30d-455c-af7b-0244e2f2bfd5.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=6e165feaf599763d4f70cfbb59feb30b" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fd4d8ff44-c30d-455c-af7b-0244e2f2bfd5.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=6e165feaf599763d4f70cfbb59feb30b" alt="p1.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/d4d8ff44-c30d-455c-af7b-0244e2f2bfd5.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fd4d8ff44-c30d-455c-af7b-0244e2f2bfd5.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=bf215f4b18d13647487df626621e8a2c 1x" loading="lazy"></a></p>

<h3>
<span id="point-plot" class="fragment"></span><a href="#point-plot"><i class="fa fa-link"></i></a>Point Plot</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">ggplot</span><span class="p">(</span><span class="n">aes</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">Petal_Width</span><span class="p">,</span><span class="w"> </span><span class="n">y</span><span class="o">=</span><span class="n">Petal_Length</span><span class="p">,</span><span class="w"> </span><span class="n">color</span><span class="o">=</span><span class="n">Species</span><span class="p">))</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">geom_point</span><span class="p">()</span><span class="w">
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F02e9ec89-6332-df69-f97f-555d5b0bd3a6.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=6ddc557c0f806ffa7ee8d004550cd7a5" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F02e9ec89-6332-df69-f97f-555d5b0bd3a6.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=6ddc557c0f806ffa7ee8d004550cd7a5" alt="r2.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/02e9ec89-6332-df69-f97f-555d5b0bd3a6.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F02e9ec89-6332-df69-f97f-555d5b0bd3a6.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=d2c521d6abb7b64dbbd6c0d25926330c 1x" loading="lazy"></a></p>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">jointplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"Sepal_Length"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"Petal_Length"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">iris</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F70dd2e06-548f-667e-37fd-e47cbc8d16e0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=10a3ed394dc157025937a6b230aeee22" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F70dd2e06-548f-667e-37fd-e47cbc8d16e0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=10a3ed394dc157025937a6b230aeee22" alt="p2.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/70dd2e06-548f-667e-37fd-e47cbc8d16e0.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F70dd2e06-548f-667e-37fd-e47cbc8d16e0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=9b34bb43b6b284246356b60e39fc283b 1x" loading="lazy"></a></p>

<h3>
<span id="bar-plot" class="fragment"></span><a href="#bar-plot"><i class="fa fa-link"></i></a>Bar Plot</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">ggplot</span><span class="p">(</span><span class="n">aes</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">Species</span><span class="p">,</span><span class="w"> </span><span class="n">y</span><span class="o">=</span><span class="n">Petal_Length</span><span class="p">,</span><span class="w"> </span><span class="n">fill</span><span class="o">=</span><span class="n">Species</span><span class="p">))</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">stat_summary</span><span class="p">(</span><span class="n">fun.y</span><span class="o">=</span><span class="n">mean</span><span class="p">,</span><span class="w"> </span><span class="n">geom</span><span class="o">=</span><span class="s2">"bar"</span><span class="p">,</span><span class="w"> </span><span class="n">alpha</span><span class="o">=</span><span class="m">0.5</span><span class="p">)</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">theme_bw</span><span class="p">()</span><span class="w">
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Ffb99793d-2795-2640-d391-c33825dc3c5f.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=4e8efb525a77c73744036496aa6b2684" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Ffb99793d-2795-2640-d391-c33825dc3c5f.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=4e8efb525a77c73744036496aa6b2684" alt="r3.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/fb99793d-2795-2640-d391-c33825dc3c5f.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Ffb99793d-2795-2640-d391-c33825dc3c5f.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=e95c3560da4357c3886a5cf97b4d0111 1x" loading="lazy"></a></p>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"Species"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"Petal_Length"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">iris</span><span class="p">)</span>  <span class="c1"># 平均値
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fd3b57823-ddf2-b799-6950-f507ca3e1bb0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=680d59a635ef383e90647c258f2650a2" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fd3b57823-ddf2-b799-6950-f507ca3e1bb0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=680d59a635ef383e90647c258f2650a2" alt="p3.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/d3b57823-ddf2-b799-6950-f507ca3e1bb0.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2Fd3b57823-ddf2-b799-6950-f507ca3e1bb0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=4d7bc16b47e9648bb82ea161638a6cf0 1x" loading="lazy"></a></p>

<h3>
<span id="count-plot" class="fragment"></span><a href="#count-plot"><i class="fa fa-link"></i></a>Count Plot</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">ggplot</span><span class="p">(</span><span class="n">aes</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">Species</span><span class="p">,</span><span class="w"> </span><span class="n">fill</span><span class="o">=</span><span class="n">Species</span><span class="p">))</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">geom_bar</span><span class="p">(</span><span class="n">stat</span><span class="o">=</span><span class="s2">"count"</span><span class="p">,</span><span class="w"> </span><span class="n">alpha</span><span class="o">=</span><span class="m">0.5</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F791b738f-f4df-2686-0240-9ca1705d91d7.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=c138b573daf00b64bb3c23c397e28971" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F791b738f-f4df-2686-0240-9ca1705d91d7.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=c138b573daf00b64bb3c23c397e28971" alt="r4.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/791b738f-f4df-2686-0240-9ca1705d91d7.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F791b738f-f4df-2686-0240-9ca1705d91d7.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=2168a33a6009bb516222286c842874fd 1x" loading="lazy"></a></p>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">countplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"Species"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"Petal_Length"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">iris</span><span class="p">)</span>  <span class="c1"># 個数
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F4e49451c-32a1-c1dc-51c8-22e3aba5eb91.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=0ea0a18e92d37f040b74a907644c2d5c" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F4e49451c-32a1-c1dc-51c8-22e3aba5eb91.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=0ea0a18e92d37f040b74a907644c2d5c" alt="p4.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/4e49451c-32a1-c1dc-51c8-22e3aba5eb91.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F4e49451c-32a1-c1dc-51c8-22e3aba5eb91.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=0a34c8168f0127366888e2c8a8652e3d 1x" loading="lazy"></a></p>

<h3>
<span id="box-plot" class="fragment"></span><a href="#box-plot"><i class="fa fa-link"></i></a>Box Plot</h3>

<div class="code-frame" data-lang="r">
<div class="code-lang"><span class="bold">R</span></div>
<div class="highlight"><pre><span class="n">iris</span><span class="w"> </span><span class="o">%&gt;%</span><span class="w"> </span><span class="n">ggplot</span><span class="p">(</span><span class="n">aes</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">Species</span><span class="p">,</span><span class="w"> </span><span class="n">y</span><span class="o">=</span><span class="n">Sepal_Length</span><span class="p">,</span><span class="w"> </span><span class="n">fill</span><span class="o">=</span><span class="n">Species</span><span class="p">))</span><span class="w"> </span><span class="o">+</span><span class="w"> </span><span class="n">geom_boxplot</span><span class="p">(</span><span class="n">alpha</span><span class="o">=</span><span class="m">0.5</span><span class="p">)</span><span class="w">
</span></pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1d9abba1-3e1c-a4f2-9c40-e51f57f8db99.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=984c0783256b00bbe60f8bf42acca339" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1d9abba1-3e1c-a4f2-9c40-e51f57f8db99.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=984c0783256b00bbe60f8bf42acca339" alt="r5.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/1d9abba1-3e1c-a4f2-9c40-e51f57f8db99.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F1d9abba1-3e1c-a4f2-9c40-e51f57f8db99.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=4c7e03acac30a15a0a37f8fbd5274a9f 1x" loading="lazy"></a></p>

<div class="code-frame" data-lang="python">
<div class="code-lang"><span class="bold">py</span></div>
<div class="highlight"><pre><span class="n">sns</span><span class="o">.</span><span class="n">boxplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s">"Species"</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s">"Sepal_Length"</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">iris</span><span class="p">)</span>
</pre></div>
</div>

<p><a href="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F36929daa-9f14-09f9-9ee6-22a2c77b29a0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=396f19a50e625aa4ffc480a06ef3540f" target="_blank" rel="nofollow noopener"><img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F36929daa-9f14-09f9-9ee6-22a2c77b29a0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;s=396f19a50e625aa4ffc480a06ef3540f" alt="p5.png" data-canonical-src="https://qiita-image-store.s3.amazonaws.com/0/204489/36929daa-9f14-09f9-9ee6-22a2c77b29a0.png" srcset="https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F204489%2F36929daa-9f14-09f9-9ee6-22a2c77b29a0.png?ixlib=rb-1.2.2&amp;auto=format&amp;gif-q=60&amp;q=75&amp;w=1400&amp;fit=max&amp;s=f6314f63745ae3703c61c47b4dab2878 1x" loading="lazy"></a></p>

<p><br></p>

<h2>
<span id="参考" class="fragment"></span><a href="#%E5%8F%82%E8%80%83"><i class="fa fa-link"></i></a>参考</h2>

<ul>
<li><a href="http://sinhrks.hatenablog.com/entry/2014/10/13/005327" rel="nofollow noopener" target="_blank">Python pandas でのグルーピング/集約/変換処理まとめ</a></li>
<li><a href="https://pythondatascience.plavox.info/seaborn/%E6%A3%92%E3%82%B0%E3%83%A9%E3%83%95" rel="nofollow noopener" target="_blank">Seaborn で件数や平均値を棒グラフで可視化する</a></li>
<li><a href="https://qiita.com/hik0107/items/3dc541158fceb3156ee0" id="reference-53f4f56951b0dfe1bb30">pythonで美しいグラフ描画 -seabornを使えばデータ分析と可視化が捗る その1</a></li>
<li><a href="https://qiita.com/hik0107/items/7233ca334b2a5e1ca924" id="reference-e7b08baa92e457898368">pythonで美しいグラフ描画 -seabornを使えばデータ分析と可視化が捗る その2</a></li>
<li><a href="https://qiita.com/hik0107/items/865b75ae486728cb0006" id="reference-f1d9848f5ca2c6522462">Python でデータ可視化 - "Facet"で属性別グラフを一気に描く方法が便利すぎる</a></li>
</ul>
