import streamlit as st
import pandas as pd
from plotly.subplots import make_subplots
import plotly.express as px
import plotly.graph_objects as go

st.title("Anlisi decessi province italiane periodo Gennaio 2015 - Settembre 2021")

uploaded_file = st.file_uploader(label = "Scegli il file in formato .csv", accept_multiple_files = False, type = ["csv"])

if uploaded_file:
	df = pd.read_csv(uploaded_file)
	province = df.columns.to_list()
	st.sidebar.title("Lista delle province")
	province.remove("data")
	province_selezionate = st.sidebar.multiselect(label = "", options = province)

	if province_selezionate:
		check_box = st.checkbox("Crea grafico")
		if check_box:
			rows = len(province_selezionate)
			fig = make_subplots(rows = rows, cols = 1, shared_xaxes = True, subplot_titles = province_selezionate)
			for provincia in province_selezionate:
				fig.add_trace(go.Scatter(x = df["data"], y = df[provincia], name = provincia), 
								row = province_selezionate.index(provincia) + 1, col=1)
				fig.update_layout(showlegend = False, plot_bgcolor = "rgb(255, 255, 255)")
				fig.update_xaxes(showgrid = True, gridwidth = 0.05, gridcolor = "LightPink",
							zeroline = True, zerolinewidth = 2, zerolinecolor = "black" )
			st.plotly_chart(fig)