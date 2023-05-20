<h1>Index á viðburðarsíðu</h1>

% for i in data['results']:
	<h3>{{i['eventDateName']}}</h3>
	<h4>{{i['userGroupName']}}</h4>
	<img src="{{i['imageSource']}}"><br>
% end