import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Simple local AI assistant - No external dependencies
class LocalAI:
    def __init__(self):
        self.knowledge_base = {
            "hello": "Hello! How can I help you today?",
            "help": "I can help you with:\n- Basic questions\n- Calculations\n- Web searches\n- Scheduling meetings\n- Sending emails",
            "calculator": "I can help with math calculations. Just ask me to calculate something!",
            "search": "I can search the web for you using DuckDuckGo.",
            "meeting": "I can help schedule meetings in your calendar.",
            "email": "I can help send emails to professors or others."
        }
    
    def invoke(self, prompt):
        prompt_lower = prompt.lower()
        
        # Check for specific patterns
        if "calculate" in prompt_lower or "math" in prompt_lower:
            return "I can help with calculations! Please use the calculator tool."
        elif "search" in prompt_lower or "web" in prompt_lower:
            return "I can search the web for you! Please use the web search tool."
        elif "schedule" in prompt_lower or "meeting" in prompt_lower:
            return "I can help schedule meetings! Please use the meeting scheduler tool."
        elif "email" in prompt_lower or "send" in prompt_lower:
            return "I can help send emails! Please use the email sender tool."
        elif "hello" in prompt_lower or "hi" in prompt_lower:
            return "Hello! I'm your AI assistant. How can I help you today?"
        elif "help" in prompt_lower:
            return self.knowledge_base["help"]
        else:
            return f"I understand you're asking about: {prompt}. I'm here to help! You can ask me to:\n- Calculate something\n- Search the web\n- Schedule a meeting\n- Send an email\n- Or just ask general questions!"

# ✅ Simple LLM (No external API needed)
llm = LocalAI()
print("✅ Using local AI assistant - No external dependencies!")

# ✅ Simple memory system (No external embeddings needed)
class SimpleMemory:
    def __init__(self):
        self.conversations = []
    
    def add_texts(self, texts):
        self.conversations.extend(texts)
    
    def similarity_search(self, prompt, k=3):
        # Simple keyword-based search
        relevant = []
        for conv in self.conversations:
            if any(word in conv.lower() for word in prompt.lower().split()):
                relevant.append(type('obj', (object,), {'page_content': conv}))
        return relevant[:k]

memory = SimpleMemory()

# ✅ Memory functions
def save_to_memory(question, answer):
    memory.add_texts([question + " -> " + answer])

def retrieve_context(prompt):
    docs = memory.similarity_search(prompt, k=3)
    if docs:
        return "\n".join([doc.page_content for doc in docs])
    return "No previous context found."

# ✅ Tools
from tools.calculator_tool import calculator_tool
from tools.calendar_tool import create_event
from tools.email_tool import send_email

def schedule_meeting(text):
    from datetime import datetime, timedelta
    start_time = datetime.utcnow() + timedelta(days=1)
    return create_event(summary=text, start_time=start_time)

def email_professor(text):
    return send_email("prof@example.com", "Project Update", text)

# Simple tool wrapper
class SimpleTool:
    def __init__(self, name, func, description):
        self.name = name
        self.func = func
        self.description = description

tools = [
    SimpleTool(name="Calculator", func=calculator_tool.func, description="Useful for doing basic math operations."),
    SimpleTool(name="Meeting Scheduler", func=schedule_meeting, description="Schedules meetings using calendar."),
    SimpleTool(name="Email Sender", func=email_professor, description="Sends an email."),
]

# ✅ Simple agent (No LangChain needed)
class SimpleAgent:
    def __init__(self, llm, tools):
        self.llm = llm
        self.tools = tools
    
    def invoke(self, prompt):
        prompt_lower = prompt.lower()
        
        # Check if user wants to use a specific tool
        if "calculate" in prompt_lower or "math" in prompt_lower:
            # Extract math expression
            import re
            math_match = re.search(r'(\d+[\+\-\*\/\^\(\)\d\s]+)', prompt)
            if math_match:
                try:
                    result = eval(math_match.group(1))
                    return f"Calculation result: {result}"
                except:
                    return "I couldn't calculate that. Please provide a valid math expression."
            else:
                return "Please provide a math expression to calculate."
        
        elif "schedule" in prompt_lower or "meeting" in prompt_lower:
            return schedule_meeting(prompt)
        
        elif "email" in prompt_lower or "send" in prompt_lower:
            return email_professor(prompt)
        
        else:
            # Use the LLM for general responses
            return self.llm.invoke(prompt)

# ✅ Agent setup
agent = SimpleAgent(llm, tools)
print("✅ Simple agent initialized successfully!")

# ✅ Main function
def ask_agent(prompt):
    try:
        context = retrieve_context(prompt)
        full_prompt = f"Context:\n{context}\n\nUser Query:\n{prompt}"
        answer = agent.invoke(full_prompt)
        save_to_memory(prompt, answer)
        return answer
    except Exception as e:
        error_msg = f"Error processing request: {str(e)}"
        print(f"❌ {error_msg}")
        return f"I encountered an error: {str(e)}. Please try again with a different request."
