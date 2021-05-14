from fastapi import APIRouter, HTTPException
import pandas as pd
import plotly.express as px
import numpy as np
import plotly.graph_objects as go

app = APIRouter()


@app.get("/vis/correlations")
async def correlations():
    """ Pie Chart of Appellate Cases Map """
    # load in dataset
    DATA_PATH = 'https://raw.githubusercontent.com/evanpersonalbiz/labs34-demo/main/notebooks/judges%20-%20judges.csv'
    df = pd.read_csv(DATA_PATH, index_col=0)
    
    labels = ['Initial Case', 'Appellate Case']
    values = [30, 131]

    # Use `hole` to create a donut-like pie chart
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

    fig.update_layout(
        title_text="What percent of cases were appealed?"),

    fig.show()
    return fig.to_json()

