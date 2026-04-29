from flask import Flask, render_template
import pandas as pd
import numpy as np

app = Flask(__name__)

# --------------------------------
# Generate Random Dataset
# --------------------------------

np.random.seed(42)

num_rows = 10

# Create dataset

df = pd.DataFrame({
    'Day': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon2', 'Tue2', 'Wed2'],
    'Earnings': np.random.randint(100, 500, num_rows),
    'Tips': np.random.randint(10, 100, num_rows)
})

# --------------------------------
# Data Analysis
# --------------------------------

average_earnings = round(df['Earnings'].mean(), 2)
maximum_earnings = df['Earnings'].max()
minimum_earnings = df['Earnings'].min()

total_tips = df['Tips'].sum()

# Convert dataframe to HTML table

table_data = df.to_html(classes='table', index=False)

# --------------------------------
# Flask Route
# --------------------------------

@app.route('/')
def home():
    return render_template(
        'index.html',
        avg=average_earnings,
        max_value=maximum_earnings,
        min_value=minimum_earnings,
        total_tips=total_tips,
        tables=table_data
    )

# --------------------------------
# Run Application
# --------------------------------

if __name__ == '__main__':
    app.run(debug=True)