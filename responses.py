def get_response(user_input):
    user_input = user_input.lower()

    if "error" in user_input:
        return "🔍 Tip: Carefully check variable names and indentation."
    elif "syntax" in user_input:
        return "📘 Python syntax uses colons (:) and indentation."
    elif "loop" in user_input:
        return "🔁 Example: for i in range(5): print(i)"
    elif "function" in user_input:
        return "💡 Use 'def' to define functions. Example:\ndef hello():\n    print('Hello!')"
    elif "help" in user_input:
        return "🧠 I can help with Python code, errors, syntax, loops, and more."
    elif "hii" in user_input:
        return "🧠 I can help with Python code, errors, syntax, loops, and more."
    else:
        return "🤖 Sorry, I didn’t understand. Try asking about errors, loops, or functions."
