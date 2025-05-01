from graph import app
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py 'Your Natural Language Question Here'")
        return
    
    user_prompt = sys.argv[1]
    
    initial_state = {
        "user_prompt": user_prompt
    }
    
    final_state = app.invoke(initial_state)
    
    result = final_state.get("execution_result")
    
    print(result)
    
if __name__ == "__main__":
    main()
