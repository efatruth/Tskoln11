    % for i in apidata['results']:
        % if i['company'] == name:
            <div style='display: flex;justify-content:center;' class='u-full-width'>
                <table class='u-half-width'>
                    <tr>
                        <th style='text-align: center;'>bensin95</th>
                        <th style='text-align: center;'>bensin95_afslattur</th>
                        <th style='text-align: center;'>Company</th>
                        <th style='text-align: center;'>Diesel</th>
                        <th style='text-align: center;'>Diesel_afslattur</th>
                        <th style='text-align: center;'>name</th>
                    </tr>

                    <tr>
                        <td style='text-align: center;'>{{i[bensin95]}}</td>
                        <td style='text-align: center;'>{{i[bensin95_discount]}}</td>
                        <td style='text-align: center;'>{{i[Company]}}</td>
                        <td style='text-align: center;'>{{i[Diesel]}}</td>
                        <td style='text-align: center;'>{{i[Diesel_discount]}}</td>
                        <td><a href='/{{name}}/{{i['name']}}' class="button button-primary">{{i['name']}}</a></td>
                    </tr>

                 </table>
            </div>
    % end
