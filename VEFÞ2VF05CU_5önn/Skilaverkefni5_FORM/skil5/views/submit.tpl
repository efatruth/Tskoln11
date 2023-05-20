% rebase('base.tpl', title='Pöntun')

<h1>Takk fyrir skráningu!</h1>
<label>Nafn pantara</label>
<p>{{nafn}}</p>

<label>Heimilisfang pantara</label>
<p>{{heim}}</p>

<label>Netfang pantara</label>
<p>{{email}}</p>

<label>Símanúmer pantara</label>
<p>{{simi}}</p>

<label>Pöntuð námskeið</label>
<p>
% for x in nam:
    Dagur {{int(x)}}: {{dagar[int(x) - 1]}}<br>
% end
</p>

<label>Tími pöntunar</label>
<p>{{timi}}</p>