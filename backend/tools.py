from database import get_connection
from langchain.llms import OpenAI
from langchain_core.tools import tool 

def fetch_schema_info(db =get_connection()):
    table_info = db.get_table_info()
    return table_info

@tool
def generate_sql_tool(prompt: str, db = get_connection()) -> str:
    """Generate SQL query based on the provided prompt."""
    schema_info = fetch_schema_info(db)
    llm = OpenAI(temperature=0)
    
    full_prompt = full_prompt = f"""
    You are a SQL expert. Here is the database schema:

    {schema_info}

    Write a syntactically correct SQL query for the following request:
    {prompt}
    """
    
    response = llm(full_prompt)
    
    return response

@tool 
def execute_sql_tool(query: str, db = get_connection()) -> str:
    """Execute the provided SQL query and return the results."""
    result = db.run_no_throw(query)
    if not result:
      return "Error: Query failed. Please rewrite your query and try again."
    return result

@tool 
def validate_sql_tool(sql: str, db = get_connection()) -> str:
    """Validate the provided SQL query."""
    
    sql_upper = sql.strip().upper()
    print(sql_upper)
    
    if not sql_upper.startswith("SELECT"):
        return {
            "status" : "rejected",
            "reason" : "Only SELECT queries are allowed."
        }
    
    forbidden_words = ["INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "CREATE", "TRUNCATE"]
    for keyword in forbidden_words:
        if keyword in sql_upper:
            return {
                "status" : "rejected",
                "reason" : f"Query contains forbidden keyword: {keyword}."
            }
    
    return {
        "status" : "approved",
        "reason" : "Query is safe"
    }
