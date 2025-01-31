# from dotenv import load_dotenv
# import streamlit as st
# import os
# import sqlite3
# import pandas as pd
# import google.generativeai as genai

# # Load environment variables
# load_dotenv()

# # Configure GenAI Key
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# # Function to Load Google Gemini Model and provide queries as response
# def get_gemini_response(question, prompt):
#     st.subheader("Thinking .........")
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt[0], question])
#     return response.text

# # Function to retrieve query from the database
# def read_sql_query(sql, db):
#     try:
#         conn = sqlite3.connect(db)
#         cur = conn.cursor()
#         cur.execute(sql)
#         rows = cur.fetchall()
#         column_names = [desc[0] for desc in cur.description]  # Extract column names
#         conn.close()
#         return rows, column_names
#     except sqlite3.OperationalError as e:
#         return f"SQL Error: {str(e)}", None

# # Function to get all tables from the database
# def get_table_names(db):
#     try:
#         conn = sqlite3.connect(db)
#         cur = conn.cursor()
#         cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = [row[0] for row in cur.fetchall()]
#         conn.close()
#         return tables
#     except sqlite3.OperationalError as e:
#         return []

# # Function to fetch full table data
# def get_full_table_data(db):
#     tables = get_table_names(db)
#     table_data = {}
#     conn = sqlite3.connect(db)
#     for table in tables:
#         try:
#             df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
#             table_data[table] = df
#         except Exception as e:
#             table_data[table] = f"Error loading table {table}: {str(e)}"
#     conn.close()
#     return table_data

# # Define Your Prompt
# prompt = [
#     """
#     You are an expert in converting English questions to SQL query!
#     SELECT SUM(Salary) AS Total_Salary_Expense 
#     FROM Employees 
#     WHERE Department = 'Sales';

#     Important Note:
#     The Department column in Employees table is same as Name column in Departments table.
#     The Manager column in Departments table is same as Name column in Employees table.

#     For example:
#     Example 1 - Show me all employees in the Sales department?
#     The SQL command will be something like this: SELECT * FROM Employees WHERE Department = 'Sales';
    
#     Example 2 - Who is the manager of the Engineering department?
#     The SQL command will be something like this: SELECT Manager FROM Departments WHERE Name = 'Engineering';
    
#     Example 3 - List all employees hired after 15 oct 2022.
#     The SQL command will be something like this: SELECT * FROM Employees WHERE Hire_Date > '2022-10-15';    
        
#     Example 4 - What is the total salary expense for the Sales department?
#     The SQL command will be something like this:SELECT SUM(Salary) AS Total_Salary_Expense FROM Employees WHERE Department = 'Sales';

#     Ensure that the output query is valid and does not contain SQL formatting like ``` or the word 'sql'.
#     """
# ]

# # Streamlit App
# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# # Display full tables before taking user input
# database_name = "employee_data.db"
# table_data = get_full_table_data(database_name)

# if table_data:
#     st.subheader("Full Tables in Database:")
#     for table, data in table_data.items():
#         st.write(f"### {table} Table")
#         if isinstance(data, pd.DataFrame) and not data.empty:
#             st.dataframe(data, use_container_width=True)
#         else:
#             st.warning(f"No data found in {table} table or an error occurred.")

# # User input
# question = st.text_input("Input: ", key="input")
# submit = st.button("Ask the question")

# # If submit is clicked
# if submit:
#     response = get_gemini_response(question, prompt)
#     st.subheader("Generated SQL Query:")
#     st.code(response, language='sql')
    
#     query_result, column_names = read_sql_query(response, database_name)
    
#     st.subheader("The Response is:")
#     if isinstance(query_result, str) and query_result.startswith("SQL Error"):
#         st.error(query_result)
#     elif query_result:
#         df = pd.DataFrame(query_result, columns=column_names)
#         st.dataframe(df, use_container_width=True)
#     else:
#         st.warning("No results found. Either you have entered a wrong table name or attribute name, or your request is invalid based on the data in the database.")




from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai

# Streamlit - set page config as the first Streamlit command
st.set_page_config(page_title="I can Retrieve Any SQL query")

# Load environment variables
load_dotenv()

# Streamlit Sidebar - User enters Google API Key
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter your Google API Key:", type="password")

# Configure GenAI Key if provided
if api_key:
    genai.configure(api_key=api_key)
else:
    st.sidebar.warning("Please enter your Google API Key to proceed!")

# Function to Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    if not api_key:
        return "API Key is missing. Please enter it in the sidebar."
    
    st.subheader("Thinking .........")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function to retrieve query from the database
def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]  # Extract column names
        conn.close()
        return rows, column_names
    except sqlite3.OperationalError as e:
        return f"SQL Error: {str(e)}", None

# Function to get all tables from the database
def get_table_names(db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [row[0] for row in cur.fetchall()]
        conn.close()
        return tables
    except sqlite3.OperationalError as e:
        return []

# Function to fetch full table data
def get_full_table_data(db):
    tables = get_table_names(db)
    table_data = {}
    conn = sqlite3.connect(db)
    for table in tables:
        try:
            df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
            table_data[table] = df
        except Exception as e:
            table_data[table] = f"Error loading table {table}: {str(e)}"
    conn.close()
    return table_data

# Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    SELECT SUM(Salary) AS Total_Salary_Expense 
    FROM Employees 
    WHERE Department = 'Sales';

    Important Note:
    The Department column in Employees table is same as Name column in Departments table.
    The Manager column in Departments table is same as Name column in Employees table.

    For example:
    Example 1 - Show me all employees in the Sales department?
    The SQL command will be something like this: SELECT * FROM Employees WHERE Department = 'Sales';
    
    Example 2 - Who is the manager of the Engineering department?
    The SQL command will be something like this: SELECT Manager FROM Departments WHERE Name = 'Engineering';
    
    Example 3 - List all employees hired after 15 oct 2022.
    The SQL command will be something like this: SELECT * FROM Employees WHERE Hire_Date > '2022-10-15';    
        
    Example 4 - What is the total salary expense for the Sales department?
    The SQL command will be something like this:SELECT SUM(Salary) AS Total_Salary_Expense FROM Employees WHERE Department = 'Sales';

    Ensure that the output query is valid and does not contain SQL formatting like ``` or the word 'sql'.
    """
]

# Streamlit App
st.header("Gemini App To Retrieve SQL Data")

# Display full tables before taking user input
database_name = "employee_data.db"
table_data = get_full_table_data(database_name)

st.success("LLM is only used for creating query, your data is safe and secure with us.")
if table_data:
    st.subheader("Full Tables in Database:")
    for table, data in table_data.items():
        st.write(f"### {table} Table")
        if isinstance(data, pd.DataFrame) and not data.empty:
            st.dataframe(data, use_container_width=True)
        else:
            st.warning(f"No data found in {table} table or an error occurred.")

# User input
question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    if not api_key:
        st.error("Google API Key is required! Please enter it in the sidebar.")
    else:
        response = get_gemini_response(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(response, language='sql')
        
        query_result, column_names = read_sql_query(response, database_name)
        
        st.subheader("The Response is:")
        if isinstance(query_result, str) and query_result.startswith("SQL Error"):
            st.error(query_result)
        elif query_result:
            df = pd.DataFrame(query_result, columns=column_names)
            st.dataframe(df, use_container_width=True)
        else:
            st.warning("No results found. Either you have entered a wrong table name or attribute name, or your request is invalid based on the data in the database.")
