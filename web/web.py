from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__, static_folder='static')

# read from the csv file
data = pd.read_csv('../employee_data.csv')

# convert the booleans to strings to allow for parsing in the html
data['employed'] = data['employed'].map({True: 'True', False: 'False'})

# create a new API route to handle the search & home
@app.route('/', methods=['GET', 'POST'])
def home():
    # get the query from the url
    query = request.args.get('query')
    result = data

    # if a query parameter is present, filter the returned data
    if query:
        # split the query into parts
        query_parts = query.split()

        # if the end-user is searching for both last name and first name
        if len(query_parts) == 2:
            # filter by both first and last name
            result = data[(data['first_name'].str.contains(query_parts[0], case=False)) & (data['last_name'].str.contains(query_parts[1], case=False))]
        else:
            # filter by name
            result = data[data['first_name'].str.contains(query, case=False) | data['last_name'].str.contains(query, case=False)]


    return render_template('index.html', data=result.to_dict(orient='records'))

# run the app on port 8000
if __name__ == "__main__":
    app.run(port=8000, debug=True)