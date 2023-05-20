    <ul class="u-full-width" style='display:flex;list-style:none;justify-content:center;'>
    % for i in  maininf['companies']:
        <li style='margin:5px;'><a href="{{i}}" class="button button-primary">{{i}}</a></li>
    %end
    </ul>
