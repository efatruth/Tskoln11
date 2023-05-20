% rebase('base.tpl', title='SkilaVerkefni 6')

<h4>items: sem á þessi siða</h4>
<a href="/vorur?vara=1"><img src="static/1.jpeg" height="100", width="100"></a>
<a href="/vorur?vara=2"><img src="static/2.jpeg" height="100", width="100"></a>
<a href="/vorur?vara=3"><img src="static/3.jpeg" height="100", width="100"></a>
<a href="/vorur?vara=4"><img src="static/4.jpeg" height="100", width="100"></a>
<a href="/vorur?vara=5"><img src="static/5.jpeg" height="100", width="100"></a>
<a href="/vorur?vara=6"><img src="static/6.jpeg" height="100", width="100"></a>
<hr>
% if nyvor != None:
    <h4>Hlutir sem er skoðað Nýlega :</h4>
    % for x in nyvor:
        <a href="/vorur?vara={{x}}"><img src="static/{{x}}.jpeg" height="100", width="100"></a>
% end
