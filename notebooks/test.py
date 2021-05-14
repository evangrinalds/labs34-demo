from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

app = APIRouter()


@app.get("/vis/correlations")
async def correlations():
    """ Correlation Matrix Heat Map """
    # load in dataset
    DATA_PATH = 'https://raw.githubusercontent.com/'
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    labels = ['$5,000', '$10,000', '$15,000', '$20,000', '$25,000+']
    values = [233, 72, 26, 21, 31]

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

    annotations = []
    annotations.append(dict(xref='paper', yref='paper',
                        x=0.5, y=1.16,
                        text='Goal Amount From Successful Kickstart Projects',
                        font=dict(family='Arial', size=16, color='rgb(0,0,0)'),
                        showarrow=False))

    fig.update_layout(annotations=annotations)

    fig.show()
    return fig.to_json()

@app.get("/vis/correlations")
def correlations():
    """ Correlation Matrix Heat Map """
    pass
@app.get("/vis/judges/{judge_id}")
def vis_judges(judge_name: str):
    pass
@app.get("/vis/circuits/{circuit_id}")
def vis_circuits(circuit_name: str):
    pass
