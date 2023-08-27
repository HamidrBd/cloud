# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

st.write('hamidreza badr')

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.experimental_connection('gcs', type=FilesConnection)
st.write('hamidreza badr')

df = conn.read("streamlit-bucket-hamid/myfile.csv", input_format="csv", ttl=600)
st.write('reza badr ')

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")
