import pandas as pd
import streamlit as st
from app_pages.app_page import AppPage
import pymysql

class PredictPage(AppPage):
    @staticmethod
    def _run_page():
        app()

    @staticmethod
    def get_name():
        return 'Predict-單筆式'

    def __init__(self, testPrint):
        self.testPrint = testPrint
        st.write(testPrint)

def app():
    st.write('OK')
    connection = pymysql.connect(host="127.0.0.1", port=3306, user="mitac", passwd="mitac", db='mlflow')
    sql = '''select a.run_uuid, a.name, a.user_id, b.key, b.value, c.key, c.value from mlflow.runs a, mlflow.params b, mlflow.metrics c
            where name like '2023%'
    and a.run_uuid = b.run_uuid
    and a.run_uuid = c.run_uuid
    order by a.start_time desc
    '''
    st.write("訓練紀錄")
    df = pd.read_sql(sql, connection)
    run_choose = df['name'].unique()
    df2 = pd.merge(run_choose, df, on='run_uuid')
    st.write(df2)