#!/usr/bin/env python
# coding: utf-8

# # To create a dashboard with a proper database using Python, you can follow these steps:

# # Step 1: Install necessary libraries

# In[ ]:


pip install pandas
pip install dash
pip install dash-bootstrap-components
pip install dash-daq
pip install dash-html-components
pip install dash-core-components
pip install dash-table
pip install flask
pip install sqlalchemy


# # Step 2: Create a database using SQLite and SQLAlchemy

# In[3]:


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Example(Base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    value = Column(Integer)

engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)


# # Step 3: Create a simple dashboard using Dash

# In[8]:


pip install dash


# In[11]:


import dash
from dash import html, dcc, Input, Output
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Dashboard with Database', style={'textAlign': 'center'}),
    
    dcc.Input(id='input-name', type='text', placeholder='Enter Name'),
    dcc.Input(id='input-value', type='number', placeholder='Enter Value'),
    html.Button('Submit', id='submit-button', n_clicks=0),
    
    html.Br(),
    
    html.Div(id='output-message'),
])

@app.callback(
    Output('output-message', 'children'),
    Input('submit-button', 'n_clicks'),
    [Input('input-name', 'value'), Input('input-value', 'value')]
)
def update_output(n_clicks, input_name, input_value):
    if n_clicks > 0:
        engine.execute(Example.__table__.insert(), [{'name': input_name, 'value': input_value}])
        return f'Data successfully added to database: Name - {input_name}, Value - {input_value}'
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




