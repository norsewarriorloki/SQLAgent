from tools import *

def generate_sql_node(state):
    prompt = state["user_prompt"]
    sql = generate_sql_tool.invoke(prompt) 
    return {
        "generated_sql": sql
    }

def validate_sql_node(state):
    sql = state["generated_sql"]
    validation_result = validate_sql_tool.invoke(sql)
    return {
        "validation_result": validation_result
    }

def execute_sql_node(state):
    sql = state["generated_sql"]
    execution_result = execute_sql_tool.invoke(sql)
    return {
        "execution_result": execution_result
    }

def reject_sql_node(state):
    reason = state.get("validation_result", "Query rejected for safety reasons.")
    return {"execution_result": reason}