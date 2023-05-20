<!DOCTYPE html>
<html>
    %include('head.tpl')
    <a href='/{{company}}/' class='button button-primary'>Til baka</a>
    %for i in apidata['results']:
        %if i['name'] == name:
            <div style='display: flex;justify-content: center;' class='u-full-width'>
                <table class='u-half-width'>

                        <tr>
                            <th style='text-align: center;'>Bensin95</th>
                            <th style='text-align: center;'>Bensin95_afslattur</th>
                            <th style='text-align: center;'>diesel</th>
                            <th style='text-align: center;'>diesel_afslattur</th>
                        </tr>


                        <tr>
                            <td style='text-align: center;'>{{i[bensin95]}}</td>
                            <td style='text-align: center;'>{{i[bensin95_discount]}}</td>
                            <td style='text-align: center;'>{{i[diesel]}}</td>
                            <td style='text-align: center;'>{{i[diesel_discount]}}</td>
                        </tr>

                 </table>
            </div>
            %break
    %end
    %include('foot.tpl')
</html>
