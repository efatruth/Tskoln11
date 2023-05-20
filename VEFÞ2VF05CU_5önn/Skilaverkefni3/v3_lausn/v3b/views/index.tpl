% rebase('base.tpl')

<div class='group'>

        <!-- Birtum lista af öllum fyrirsögnum i[0] ásamt linkum -->
		<section class="col1_2">
			<h3>Helstu hasarfréttir</h3>
			<ul>
			% cnt = 0;
			% for i in frettir:
				<li><a href='/frett/{{ cnt }}'>{{ i[0] }}</a></li>
				% cnt += 1
			% end
			</ul>
		</section>
</div>