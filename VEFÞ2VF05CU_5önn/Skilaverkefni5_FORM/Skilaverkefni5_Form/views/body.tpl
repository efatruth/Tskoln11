<body>

    <h1>Skráning námskeið</h1>
    <form method="post">
        %for stak in data['namskeid']:
            <input type='checkbox' name='{{stak}}' value='{{stak}}'>{{stak}} <br>
        %end
    </form>

    <h3>period</h3>
    <form method="post" action>
        %for stak in range action
            %if stak+1 == 1:
                <input type='radio' name='day' value='{{stak+1}}'> {{stak+1}}Dagur<br>
            %else:
                <input type='radio' name='day' value='{{stak+1}}'> {{stak+1}}Dagur<br>
            %end
        %end
    </form>


    %include('footer.tpl')
</body>
