from langchain_community.utilities import SQLDatabase

def get_connection() -> SQLDatabase:
    """Create a connection to the local postgresql chinook instance"""
    return SQLDatabase.from_uri("postgresql://user:password@localhost:5432/chinook")


    
    
