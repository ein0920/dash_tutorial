import dash
import dash_table
import pandas as pd
from collections import OrderedDict

data = OrderedDict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)

df = pd.DataFrame(data)

election_data = OrderedDict(
    [
        (
            "Date",
            [
                "July 12th, 2013 - July 25th, 2013",
                "July 12th, 2013 - August 25th, 2013",
                "July 12th, 2014 - August 25th, 2014",
            ],
        ),
        (
            "Election Polling Organization",
            ["The New York Times", "Pew Research", "The Washington Post"],
        ),
        ("Rep", [1, -20, 3.512]),
        ("Dem", [10, 20, 30]),
        ("Ind", [2, 10924, 3912]),
        (
            "Region",
            [
                "Northern New York State to the Southern Appalachian Mountains",
                "Canada",
                "Southern Vermont",
            ],
        ),
    ]
)

df_election = pd.DataFrame(election_data)
df_long = pd.DataFrame(
    OrderedDict([(name, col_data * 10) for (name, col_data) in election_data.items()])
)
df_long_columns = pd.DataFrame(
    {
        "This is Column {} Data".format(i): [1, 2]
        for i in range(10)
    }
)

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    style_data={'whiteSpace': 'normal'},
    css=[{
        'selector': '.dash-cell div.dash-cell-value',
        'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'
    }],
    data=df_election.to_dict('rows'),
    columns=[{'id': c, 'name': c} for c in df_election.columns]
)

if __name__ == '__main__':
    app.run_server(debug=True)