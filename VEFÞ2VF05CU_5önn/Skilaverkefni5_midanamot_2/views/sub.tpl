<!DOCTYPE html>
<html>
	%include('head.tpl')
	<a href='./' class='button button-primary'>heim</a>
	%include('tdata.tpl')
	%include('foot.tpl')

	% for i in  maininf['all_locations']:
        <li style='margin:5px;'><a href="{{i}}" class="button button-primary">{{i}}</a></li>
    %end
</html>
