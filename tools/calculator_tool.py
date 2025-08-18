def safe_calculate(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}}, {})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Simple tool object for compatibility
class CalculatorTool:
    def __init__(self):
        self.name = "Calculator"
        self.func = safe_calculate
        self.description = "Useful for doing basic math operations. Input should be a math expression."

calculator_tool = CalculatorTool()
