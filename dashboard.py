# Importing necessary libraries for Streamlit, data handling, and visualization

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from io import BytesIO

# Set up page configuration for Streamlit
st.set_page_config(page_title="Enhanced Data Visualization App", layout="wide")

# Customizing the CSS style for the app

st.markdown("""
    <style>
        .sidebar .sidebar-content {
            background-color: #f8f9fa;
            padding: 15px;
        }
        .main-content {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        }
        .chart-title {
            font-size: 24px;
            font-weight: bold;
            color: #444;
            text-align: center;
            margin-top: 20px;
        }
        .dark-mode .chart-title {
            color: #ddd;
        }
    </style>
    """, unsafe_allow_html=True)

# Check if Dark Mode is enabled from the sidebar

dark_mode = st.sidebar.checkbox("Dark Mode")
if dark_mode:
    st.markdown(
        """
        <style>
        body {background-color: #121212; color: #ffffff;}
        .sidebar-content {background-color: #1e1e1e;}
        .main-content {background-color: #222;}
        .chart-title {color: #ddd;}
        </style>
        """,
        unsafe_allow_html=True,
    )

# Main title of the application
st.markdown("<div class='chart-title'>Enhanced Data Visualization Dashboard</div>", unsafe_allow_html=True)

# Main title of the application
st.sidebar.header("Upload CSV File")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# If a file is uploaded, process the CSV data
if uploaded_file is not None:
    
    # Load the uploaded CSV file into a DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Expander showing basic dataset information
    with st.expander("Dataset Overview"):
        st.write("### Basic Information")
        st.write(f"**Shape**: {df.shape}")
        st.write(f"**Columns**: {df.columns.tolist()}")
        st.write("**Missing Values**:")
        st.write(df.isnull().sum())

    # Display the first few rows of the dataset
    st.subheader("Dataset Preview")
    st.write(df.head())
    
    # Sidebar for data filtering options
    st.sidebar.subheader("Data Filtering")

    # Create multiselect filters for categorical columns (e.g., object type)
    for col in df.select_dtypes(include=['object', 'category']).columns:
        unique_values = df[col].unique()
        selected_values = st.sidebar.multiselect(f"Filter by {col}", unique_values, default=unique_values)
        df = df[df[col].isin(selected_values)]
    
    # Create range sliders for numeric columns to filter data based on a selected range
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        min_val, max_val = st.sidebar.slider(f"Range for {col}", 
                                             float(df[col].min()), float(df[col].max()), 
                                             (float(df[col].min()), float(df[col].max())))
        df = df[(df[col] >= min_val) & (df[col] <= max_val)]
    

    # Sidebar for selecting the type of chart to display
    st.sidebar.subheader("Choose Visualization Type")
    chart_type = st.sidebar.selectbox("Chart Type", ["Line", "Bar", "Scatter", "Histogram", "Box Plot", "Heatmap", "Pie Chart", "Correlation Matrix"])

    # Based on selected chart type, display the appropriate plot
    if chart_type in ["Line", "Bar", "Scatter", "Box Plot", "Pie Chart"]:
        x_col = st.sidebar.selectbox("X-axis", df.columns)
        y_col = None
        if chart_type != "Pie Chart":
            y_col = st.sidebar.selectbox("Y-axis", df.select_dtypes(include=['float64', 'int64']).columns)

        # If chart type requires numeric data, perform checks and plot

        if chart_type in ["Line", "Bar", "Scatter", "Box Plot"]:
            if not pd.api.types.is_numeric_dtype(df[x_col]) and not pd.api.types.is_numeric_dtype(df[y_col]):
                st.error("Error: Both X and Y axes must have numeric data for this chart type.")
            elif not pd.api.types.is_numeric_dtype(df[y_col]):
                st.error("Error: Y-axis must have numeric data.")
            elif chart_type == "Scatter" and not pd.api.types.is_numeric_dtype(df[x_col]):
                st.error("Error: X-axis must have numeric data for Scatter Plot.")
            else:
                if chart_type == "Line":
                    fig = px.line(df, x=x_col, y=y_col, title=f"Line Plot of {y_col} vs {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
                
                elif chart_type == "Bar":
                    fig = px.bar(df, x=x_col, y=y_col, title=f"Bar Plot of {y_col} vs {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
                
                elif chart_type == "Scatter":
                    fig = px.scatter(df, x=x_col, y=y_col, title=f"Scatter Plot of {y_col} vs {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
                
                elif chart_type == "Box Plot":
                    fig = px.box(df, x=x_col, y=y_col, title=f"Box Plot of {y_col} vs {x_col}")
                    st.plotly_chart(fig, use_container_width=True)
        
        # Generate pie chart if selected
        elif chart_type == "Pie Chart":
            if not pd.api.types.is_categorical_dtype(df[x_col]) and not pd.api.types.is_object_dtype(df[x_col]):
                st.error("Error: Column selected for Pie Chart must be categorical or object type.")
            else:
                pie_data = df[x_col].value_counts().reset_index()
                fig = px.pie(pie_data, names="index", values=x_col, title=f"Pie Chart of {x_col}")
                st.plotly_chart(fig, use_container_width=True)

    # Generate histogram if selected
    elif chart_type == "Histogram":
        hist_col = st.sidebar.selectbox("Column for Histogram", df.select_dtypes(include=['float64', 'int64']).columns)
        if not pd.api.types.is_numeric_dtype(df[hist_col]):
            st.error("Error: Selected column for Histogram must have numeric data.")
        else:
            fig = px.histogram(df, x=hist_col, title=f"Histogram of {hist_col}")
            st.plotly_chart(fig, use_container_width=True)

    # Generate heatmap if selected
    elif chart_type == "Heatmap":
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Generate correlation matrix if selected
    elif chart_type == "Correlation Matrix":
        corr_cols = st.sidebar.multiselect("Select Columns for Correlation Matrix", 
                                           df.select_dtypes(include=['float64', 'int64']).columns, 
                                           default=df.select_dtypes(include=['float64', 'int64']).columns)
        if len(corr_cols) < 2:
            st.error("Error: Please select at least two numeric columns for Correlation Matrix.")
        else:
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df[corr_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    # Expander showing summary statistics for the dataset
    with st.expander("View Summary Statistics"):
        st.write(df.describe())
    
    # Add a download button to download the filtered data as a CSV file
    buffer = BytesIO()
    df.to_csv(buffer, index=False)
    st.download_button(
        label="Download Filtered Data",
        data=buffer.getvalue(),
        file_name="filtered_data.csv",
        mime="text/csv"
    )

else:
    
    # Message when no file is uploaded
    st.write("Please upload a CSV file to start visualizing data.")
