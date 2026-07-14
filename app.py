import streamlit as st
import ast
import re

st.set_page_config(page_title="💻 AI Coding Assistant V2", layout="wide")
st.title("💻 AI Coding Assistant V2")
st.markdown("Smart code completions, explanations, and PR review")

openai_key = st.sidebar.text_input("OpenAI API Key", type="password")

tab1, tab2, tab3 = st.tabs(["💡 Code Completion", "📝 Explain Code", "🔍 Code Review"])

# Sample project context
project_context = """
Project: ecommerce-api
Structure:
  app.py → main Flask app
  models/
    user.py → User, Order classes
    product.py → Product class
  utils/
    auth.py → JWT verification
    logger.py → logging setup
    
Key Functions:
  - create_order(user_id, products) → Order
  - verify_jwt(token) → dict
  - log_event(level, message) → None
"""

with tab1:
    st.subheader("💡 Code Completion")
    st.write("Start typing code; AI suggests completions based on your project context")
    
    code_snippet = st.text_area("Paste code with cursor at end (add `<CURSOR>` marker):", height=150, value="""def process_payment(order_id):
    order = Order.query.get(order_id)
    if not order:
        return {"error": "Not found"}
    amount = order.total_price
    # Now type: <CURSOR>""")
    
    if st.button("🤖 Get Completion") and openai_key:
        import os
        os.environ["OPENAI_API_KEY"] = openai_key
        from openai import OpenAI
        client = OpenAI(api_key=openai_key)
        
        prompt = f"""You are a Python coding assistant. Given project context and incomplete code, suggest the next 2-3 lines.

Project Context:
{project_context}

Code (complete the <CURSOR> line):
{code_snippet}

Provide only the completed code, no explanation."""
        
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        completion = response.choices[0].message.content
        st.code(completion, language="python")

with tab2:
    st.subheader("📝 Explain Code")
    code_to_explain = st.text_area("Paste code to explain:", height=150, value="""def create_order(user_id, product_ids):
    user = User.query.get(user_id)
    if not user or user.is_banned:
        raise ValueError("Invalid user")
    products = Product.query.filter(Product.id.in_(product_ids))
    total = sum(p.price for p in products)
    order = Order(user_id=user_id, total_price=total, status="pending")
    db.session.add(order)
    db.session.commit()
    return order""")
    
    if st.button("📖 Explain") and openai_key:
        from openai import OpenAI
        client = OpenAI(api_key=openai_key)
        
        prompt = f"Explain this Python function step by step. Mention what could go wrong and best practices.\n\n{code_to_explain}"
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        st.markdown(response.choices[0].message.content)

with tab3:
    st.subheader("🔍 Code Review (Diff Analysis)")
    diff_text = st.text_area("Paste git diff:", height=150, value="""- def get_user(user_id):
-     return User.query.get(user_id)
+ def get_user(user_id):
+     user = User.query.get(user_id)
+     if user:
+         user.last_accessed = datetime.now()
+         db.session.commit()
+     return user""")
    
    if st.button("🔎 Review Diff") and openai_key:
        from openai import OpenAI
        client = OpenAI(api_key=openai_key)
        
        prompt = f"""Review this code diff. Point out:
1. Potential bugs or issues
2. Performance concerns
3. Style/best practice improvements
4. Security implications

Diff:
{diff_text}"""
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        st.markdown(response.choices[0].message.content)

st.markdown("---")
st.caption("Demo uses project context injection. For production, integrate with IDE (VSCode extension) for real-time suggestions.")
