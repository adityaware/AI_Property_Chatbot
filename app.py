import streamlit as st
import pandas as pd
import re
import time

# --- Streamlit Page Config ---
st.set_page_config(page_title="AI Property Chatbot", page_icon="🏡", layout="centered")

# --- Load Data ---
@st.cache_data
def load_data():
    df_projects = pd.read_csv("project.csv")
    df_address = pd.read_csv("ProjectAddress.csv")
    df_projects.rename(columns={'id': 'projectId'}, inplace=True)
    df = pd.merge(df_projects, df_address, on='projectId', how='left')
    return df

df = load_data()

# --- Property Search Function ---
def search_properties(df, query):
    query = query.lower()

    # Extract BHK
    bhk_match = re.search(r'(\d+)\s?bhk', query)
    bhk = bhk_match.group(1) if bhk_match else None

    # Extract Budget
    budget_match = re.search(r'(\d+)\s?(lakh|crore)', query)
    budget = None
    if budget_match:
        num = int(budget_match.group(1))
        unit = budget_match.group(2)
        if unit == 'lakh':
            budget = num * 1_00_000
        elif unit == 'crore':
            budget = num * 1_00_00_000

    # Extract City
    cities = ['mumbai', 'pune', 'delhi', 'bangalore', 'hyderabad']
    city = next((c for c in cities if c in query), None)

    # Extract Construction Status
    status = None
    if re.search(r'(ready.*move|ready_to_move|ready)', query):
        status = 'READY'
    elif re.search(r'(under.*construct|under_construction)', query):
        status = 'UNDER CONSTRUCTION'

    # Extract Locality
    known_localities = ['baner', 'wakad', 'hinjewadi', 'kothrud', 'thane', 'viman nagar', 'hadapsar']
    locality = next((loc for loc in known_localities if loc in query), None)

    # Apply Filters
    results = df.copy()
    if city:
        results = results[results['fullAddress'].str.lower().str.contains(city, na=False)]
    if locality:
        results = results[results['fullAddress'].str.lower().str.contains(locality, na=False)]
    if bhk:
        results = results[results['projectName'].str.contains(bhk, case=False, na=False)]
    if status:
        results = results[results['status'].str.lower().str.contains(status.lower(), na=False)]
    if budget:
        price_cols = [c for c in results.columns if 'price' in c.lower()]
        if price_cols:
            price_col = price_cols[0]
            results = results[results[price_col] <= budget]

    filters = {
        "bhk": bhk,
        "city": city,
        "status": status,
        "locality": locality,
        "budget": budget
    }

    return results if not results.empty else None, filters


# --- Smart Summary Generator ---
def generate_summary(results, filters):
    if results is None or results.empty:
        city = filters.get('city', 'your area')
        bhk = filters.get('bhk', '')
        return f"Sorry, no {bhk}BHK options found in {city} within your criteria."

    total = len(results)
    city = filters.get('city', 'the area').title()
    bhk = filters.get('bhk', '')
    status_counts = results['status'].value_counts().to_dict()

    ready = status_counts.get('READY_TO_MOVE', 0) + status_counts.get('READY', 0)
    under = sum(v for k, v in status_counts.items() if 'under' in str(k).lower())

    # Extract top localities
    localities = (
        results['fullAddress']
        .dropna()
        .apply(lambda s: s.split(',')[-1].strip() if ',' in s else s)
        .value_counts()
        .head(2)
        .index.tolist()
    )
    locality_text = ", ".join(localities) if localities else "various localities"

    summary = (
        f"I found {total} matching {bhk}BHK projects in {city}. "
        f"Most are located in {locality_text}. "
        f"{ready} are ready-to-move and {under} are under construction."
    )
    return summary


# --- Streamlit Chat UI ---
st.title("🏡 AI Property Chatbot")
st.markdown("### 👋 Hello there! I'm your smart property assistant.")
st.markdown("- Try queries like:\n  - `3BHK flats in Pune under 50 lakh`\n  - `Ready to move projects in Baner`\n  - `Under construction projects in Mumbai`")

# Clear Chat Button
if st.button("🧹 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# Maintain chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"🧑‍💼 **You:** {msg['content']}")
    else:
        st.markdown(f"🤖 **AI:** {msg['content']}")

# Input box
query = st.text_input("💬 Type your message and press Enter:")

# When user enters a query
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.spinner("🤖 Searching..."):
        time.sleep(1)
        results, filters = search_properties(df, query)
        summary = generate_summary(results, filters)

        if results is not None:
            response = summary + "\n\nHere are a few options:\n\n"
            for _, row in results.head(5).iterrows():
                response += f"🏠 **{row['projectName']}** ({row['projectCategory']})\n📍 {row['fullAddress']}\n\n"
        else:
            response = summary

        st.session_state.messages.append({"role": "assistant", "content": response})

# Show latest response
if st.session_state.messages:
    last_msg = st.session_state.messages[-1]
    if last_msg["role"] == "assistant":
        st.markdown(last_msg["content"])
