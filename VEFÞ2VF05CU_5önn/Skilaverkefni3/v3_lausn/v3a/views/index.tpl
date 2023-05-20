%include("header.tpl")

<h1>{{ title }}</h1>
<ul>
    % for kennitala in kennitolur:
        <li><a href="/page/{{ kennitala }}">{{ kennitala }}</a></li>
    % end
</ul>

%include("footer.tpl")

