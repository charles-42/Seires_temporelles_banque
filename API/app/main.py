from fastapi import FastAPI, File, Form, Response
from pydantic import BaseModel
import pandas as pd
import io
from sklearn.metrics import mean_absolute_percentage_error, mean_squared_error, mean_absolute_error, r2_score
from typing import Dict, List
import math
app = FastAPI()

class Item(BaseModel):
    csv_predicted_data: bytes
    flux_type: str 
    darts_metrics_list: List[str]


@app.get("/predict_email")
async def predict_email(file: bytes = File(...)   ):  #, json_data: dict = Form(...)):
    try:
        # Extract required elements from the request
        df_pred = pd.read_csv(io.BytesIO(file), index_col="Date", parse_dates = True)
        df_real = pd.read_csv(f'app/email.csv', index_col="Date", parse_dates = True)
        
        result_data= {}

        sklearn_metrics = ["mean_absolute_percentage_error", "mean_squared_error", "mean_absolute_error", "r2_score"]
        for entite in df_pred.Entite.unique():
            for instance in df_pred.instance.unique():
                df_real_filter =  df_real[(df_real["Entite"] == entite)& (df_real["instance"] == instance)]
                df_pred_filter =  df_pred[(df_pred["Entite"] == entite)& (df_pred["instance"] == instance)]
                if len(df_pred_filter.index)>0: 
                    metrics_dict = {}  
                    for name in sklearn_metrics:
                        if name in globals() and callable(globals()[name]):
                            function = globals()[name]
                            score =function(df_real_filter.Nb_recus,df_pred_filter.Nb_recus)
                            if not math.isnan(score):
                                metrics_dict[name] = round(score,3)
                    result_data[entite + "_" + instance] = metrics_dict
        return result_data
    except Exception as e:
        return e


@app.get("/predict_telephone")
async def predict_telephone(file: bytes = File(...)   ):  #, json_data: dict = Form(...)):
    try:
        # Extract required elements from the request
        df_pred = pd.read_csv(io.BytesIO(file), index_col="date_appel", parse_dates = True)
        df_real = pd.read_csv(f'app/telephone.csv', index_col="date_appel", parse_dates = True)
        
        result_data= {}

        sklearn_metrics = ["mean_absolute_percentage_error", "mean_squared_error", "mean_absolute_error", "r2_score"]
        for entite in df_pred.Entite.unique():
            for famille in df_pred.Famille.unique():
                df_real_filter =  df_real[(df_real["Entite"] == entite)& (df_real["Famille"] == famille)]
                df_pred_filter =  df_pred[(df_pred["Entite"] == entite)& (df_pred["Famille"] == famille)]
                if len(df_pred_filter.index)>0: 
                    metrics_dict = {}
                    for name in sklearn_metrics:
                        if name in globals() and callable(globals()[name]):
                            function = globals()[name]
                            score =function(df_real_filter.Nombre_entrants_corrige,df_pred_filter.Nombre_entrants_corrige)
                            if not math.isnan(score):
                                metrics_dict[name] = round(score,3)
                    result_data[entite + "_" + famille] = metrics_dict
        return result_data
    except Exception as e:
        return e
