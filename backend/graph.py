from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from nodes import *

class State(TypedDict):
    user_prompt: str
    generated_sql: str
    validation_result: str
    execution_result: list[dict]
    
workflow = StateGraph(State)
workflow.add_node("generate_sql_node", generate_sql_node)
workflow.add_node("validate_sql_node",validate_sql_node)
workflow.add_node("execute_sql",execute_sql_node)

workflow.set_entry_point("generate_sql_node")
workflow.add_edge("generate_sql_node", "validate_sql_node")

def conditional_acceptance_node(state: State) -> str:
    if state["validation_result"]["status"] == "approved":
        return "execute_sql"
    else:
        return "reject_sql_node"
    
workflow.add_conditional_edges("validate_sql_node", conditional_acceptance_node)
workflow.add_edge("execute_sql_node", END)
workflow.add_edge("reject_sql_node", END)

app = workflow.compile()
