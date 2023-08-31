import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="MCOST BENEFIT ANALYSIS OF DISTRICT HEATING NETWORK", page_icon="📊")

# Display title
st.title("Bar Plot in Streamlit")

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
Property_type = st.sidebar.multiselect(
    "Select the PROPERTY_TYPE:",
    options=df["PROPERTY_TYPE"].unique(),
    default=df["PROPERTY_TYPE"].unique()
)
mainheat_description = st.sidebar.multiselect(
    "Select the MAINHEAT_DESCRIPTION:",
    options=df["MAINHEAT_DESCRIPTION"].unique(),
    default=df["MAINHEAT_DESCRIPTION"].unique(),
)

inspection_date = st.sidebar.multiselect(
    "Select the INSPECTION_DATE:",
    options=df["INSPECTION_DATE"].unique(),
    default=df["INSPECTION_DATE"].unique()
)
heating_cost_current = st.sidebar.multiselect(
    "Select the HEATING_COST_CURRENT:",
    options=df["HEATING_COST_CURRENT"].unique(),
    default=df["HEATING_COST_CURRENT"].unique()

df_selection = df.query(
    "City == @Property_type & MAINHEAT_DESCRIPTION ==@mainheat_description  & INSPECTION_DATE ==@inspection_date & HEATING_COST_CURRENT == @heating_cost_current"
)   
    

st.title("Excel File Reader")

uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel('Mainfile.xlsx)
    st.write("Data from the Excel file:")
    st.dataframe(df.head())  # Display the first few rows of the DataFrame
    st.write("DataFrame Info:")
    st.write(df.info())  # Display DataFrame info




# In[4]:
# ---- MAINPAGE ----
st.title(":bar_chart: COST BENEFIT ANALYSIS OF DISTRICT HEATING NETWORK")
st.markdown("##")


st.title("Scatter Plot in Streamlit")

# Load your data into a DataFrame (df)
# df = pd.read_excel('your_data.xlsx')

# Scatter plot: Energy Consumption vs. CO2 Emissions
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='ENERGY_CONSUMPTION_CURRENT', y='CO2_EMISSIONS_CURRENT', hue='PROPERTY_TYPE')
plt.title("Energy Consumption vs. CO2 Emissions")
plt.xlabel("Energy Consumption")
plt.ylabel("CO2 Emissions")
plt.legend()
st.pyplot(plt)  # Display the plot using Streamlit's st.pyplot()


# Load your data into a DataFrame (df)
# df = pd.read_csv('your_data.csv')

avg_heating_cost = df.groupby('PROPERTY_TYPE')['HEATING_COST_CURRENT'].mean().sort_values(ascending=False)

st.title("Average Heating Cost by Property Type")

plt.figure(figsize=(10, 6))
sns.barplot(x=avg_heating_cost.index, y=avg_heating_cost.values)
plt.xticks(rotation=45)
plt.xlabel("Property Type")
plt.ylabel("Average Heating Cost")
st.pyplot()  # Display the plot using Streamlit's st.pyplot()
                       
  
st.title("Violin Plot in Streamlit")

# Load your data into a DataFrame (df)
# df = pd.read_excel('your_data.xlsx')

# Filter the top 5 main heat descriptions
top_mainheat = df['MAINHEAT_DESCRIPTION'].value_counts().nlargest(5).index
df_top_mainheat = df[df['MAINHEAT_DESCRIPTION'].isin(top_mainheat)]

# Violin plot: Total Floor Area by Top 5 Main Heat Descriptions
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_top_mainheat, x='MAINHEAT_DESCRIPTION', y='TOTAL_FLOOR_AREA')
plt.title("Total Floor Area by Top 5 Main Heat Descriptions")
plt.xticks(rotation=45)
plt.xlabel("Main Heat Description")
plt.ylabel("Total Floor Area")
st.pyplot(plt)  # Display the plot using Streamlit's st.pyplot()


st.title("Bar Plot in Streamlit")

# Load your data into a DataFrame (df)
# df = pd.read_excel('your_data.xlsx')

# Get the top 5 most common INSPECTION_DATE categories
top_inspection_dates = df['INSPECTION_DATE'].value_counts().head(5).index

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='INSPECTION_DATE', y='ENERGY_CONSUMPTION_CURRENT', ci=None, order=top_inspection_dates)
plt.title('Relationship between Energy consumption and Inspection Date (Top 5)')
plt.xlabel('Inspection Date')
plt.ylabel('Energy Consumption')
plt.xticks(rotation=45)
st.pyplot(plt)  # Display the plot using Streamlit's st.pyplot()



st.title("Bar Plot in Streamlit")

# Load your data into a DataFrame (df)
# df = pd.read_excel('your_data.xlsx')

# Get the top 5 most common MAINHEAT_DESCRIPTION categories
top_mainheat = df['MAINHEAT_DESCRIPTION'].value_counts().head(5).index

plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='MAINHEAT_DESCRIPTION', y='HEATING_COST_CURRENT', ci=None, order=top_mainheat)
plt.title('Relationship between Heating Cost and Main Heating Description (Top 5)')
plt.xlabel('Main Heating Description')
plt.ylabel('Heating Cost')
plt.xticks(rotation=45)
st.pyplot(plt)  # Display the plot using Streamlit's st.pyplot()
                       