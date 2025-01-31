# Chat_Assistant_Sqllite

1. Explanation of How the Assistant Works:
The assistant uses Google’s Gemini model to convert natural language questions into SQL queries. The user enters a question, the model generates the corresponding SQL query, which is executed on an SQLite database, and the results are displayed in the app.

2. Steps to Run the Project Locally:
Install dependencies: pip install streamlit python-dotenv pandas google-generativeai sqlite3.
Set up the environment: Create a .env file with your Google API key.
Run python sqllite.py to set up the database.
Run the app: streamlit run app.py.
Enter your Google API key in the sidebar and ask questions.
3. Known Limitations or Suggestions for Improvement:
Limitations: Requires a Google API key; limited query scope; static data; basic error handling.
Suggestions: Improve error feedback, allow dynamic data input, extend to complex queries, enhance AI model handling, and add caching for better performance.
