# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

def plotQuestion(frageIndex: int, usecolumns: []) -> None:

    df = pd.read_csv("auswertung.csv", usecols=usecolumns, sep=";")

    columnNames = df.columns.values
    title = columnNames[0]
    # st.markdown("###### Frage {}: {}".format(frageIndex, columnNames[0]))
    st.markdown("###### Frage {}:".format(frageIndex))
    df.rename(columns={columnNames[0]: "-", columnNames[1]: "IST Erhebung", columnNames[2]: "Nach APP Intervention"}, inplace=True)
    #print(df.head())

    columnNames = df.columns.values
    if frageIndex != 4:
        df.loc[len(df.index)] = ["insgesamt", np.nansum(df[columnNames[1]].values), np.nansum(df[columnNames[2]].values)]
    # print(df.head())
    fig = px.bar(df, x=columnNames[0], y=[columnNames[1], columnNames[2]], barmode='group', height=400, title=title)
    # st.dataframe(df) # if need to display dataframe
    st.plotly_chart(fig)
    st.markdown("""---""")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    index = 1
    for i in range(0, 29,3):
        plotQuestion(index, list(range(i,i+3)))
        index+=1



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
