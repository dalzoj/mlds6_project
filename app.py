import streamlit as st
import numpy as np
import joblib
#from flask import Flask, request, jsonify, render_template, url_for
#import pickle


MODEL_PATH = 'mlds6_project/models/knn_model.pkl'

def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1, -1)
    prediction = model.predict(x)
    return prediction

def main():
    with open(MODEL_PATH, 'rb') as f:
        model = joblib.load(f)

    html_temp = """
               <h1 style="color:#181082;text-align:center;">Sistema de Detección de Hepatitis</h1>
               </div>
               """
    st.markdown(html_temp, unsafe_allow_html=True)
    # Lecctura de datos
    # Datos = st.text_input("Ingrese los valores : N P K Temp Hum pH lluvia:")

    Age = st.text_input("Edad:")
    Sex = st.text_input("Sexo:")
    ALB = st.text_input("ALB:")
    ALP = st.text_input("ALP:")
    ALT = st.text_input("ALT:")
    AST = st.text_input("AST:")
    BIL = st.text_input("BIL:")
    CHE = st.text_input("CHE:")
    CHOL = st.text_input("CHOL:")
    CREA = st.text_input("CREA:")
    GGT = st.text_input("GGT:")
    PROT = st.text_input("PROT:")

    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"):
        x_in = [
            np.float_(Age.title()),
            np.float_(Sex.title()),
            np.float_(ALB.title()),
            np.float_(ALP.title()),
            np.float_(ALT.title()),
            np.float_(AST.title()),
            np.float_(BIL.title()),
            np.float_(CHE.title()),
            np.float_(CHOL.title()),
            np.float_(CREA.title()),
            np.float_(GGT.title()),
            np.float_(PROT.title()),
        ]
        predict_out = model_prediction(x_in, model)
        out_list = ['0=Blood Donor', '0s=suspect Blood Donor', '1=Hepatitis', '2=Fibrosis', '3=Cirrhosis']
        out_list_view = ['Sin enfermedad','Sangre sospechosa', 'HEPATITIS', 'FIBROSIS', 'CIRROSIS']
        st.success('El estado de la sangre es: {}'.format(out_list_view[out_list.index(predict_out[0])]).upper())

if __name__ == '__main__':
    main()