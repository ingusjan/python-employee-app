from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, static_folder='static')

# create a new API route to handle the search & home
@app.route('/', methods=['GET', 'POST'])
def home():
    # read from the csv file
    data = pd.read_csv('../employee_data.csv')

    # convert the booleans to strings to allow for parsing in the html
    data['employed'] = data['employed'].map({True: 'True', False: 'False'})

    # get the query from the url
    query = request.args.get('query')
    sort_by = request.args.get('sort_by', 'first_name')  # default sort column is 'first_name'
    order = request.args.get('order', 'asc')  # Default sort order is ascending

    result = data

    # if a query parameter is present, filter the returned data
    if query:
        query_parts = query.split()
        if len(query_parts) == 2:
            result = data[(data['first_name'].str.contains(query_parts[0], case=False)) & 
                          (data['last_name'].str.contains(query_parts[1], case=False))]
        else:
            result = data[data['first_name'].str.contains(query, case=False) | 
                          data['last_name'].str.contains(query, case=False)]

    # Sort the result
    if order == 'desc':
        result = result.sort_values(by=sort_by, ascending=False)
    else:
        result = result.sort_values(by=sort_by)

    return render_template('index.html', 
                           data=result.to_dict(orient='records'), 
                           query=query, 
                           sort_by=sort_by, 
                           order=order)

# run the app on port 8000
if __name__ == "__main__":
    app.run(port=8000, debug=True)