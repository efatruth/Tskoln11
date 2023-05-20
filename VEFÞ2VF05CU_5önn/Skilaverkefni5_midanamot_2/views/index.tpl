<!DOCTYPE html>
<html>
	%include('head.tpl')
	%include('menu.tpl')
	<div style='display:;justify-content: center;' class='u-full-width'>
        <table style="width:40%">
            <thead>
                <th>Odyrasta bensin95</th>
                <td>{{min_bensinprice}}<b>kr hjá Costco</td><br>
            </thead>
            <tbody>
                <th>Odyrasta diesel verd</th>
                <td>{{min_dieselprice}}<b>kr hjá Costco</td>
            </tbody>
        </table>
    </div>
	%include('foot.tpl')
</html>
