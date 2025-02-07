import streamlit as st
import json
from openai import OpenAI
from datetime import datetime
st.set_page_config(layout="wide", page_icon=":robot:", page_title="Assistit")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! I'm here to generate the index for you. Lets get started!"
        }
    ]

if "progress" not in st.session_state:
    st.session_state.progress = 0
   
if "ReportGenerations" not in st.session_state:
    st.session_state.ReportGenerations = []
    
if "TimeLine" not in st.session_state:
    st.session_state.TimeLine = []
    
    
def geberate_timeline_report():
    prompt = f"""
    You have been provided with history of a conversation you had with a company representative.
    You will now make a index report in form of stylised markdown text.
    Use the following Table for your help
    ***
    | **Index**   | **Description**                                                                                         | **Poor (Index 0-1)**                                                                                                                                                                                                                 | **Weak (Index 2-3)**                                                                                                                                                                                                                 | **Good (Index 4-5)**                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Liquidity** | Ability to pay debts upon maturity.                                                                     | - Significant difficulties in paying debts on time.<br>- Time and concern spent finding funds for salaries, purchases, and services.<br>**Action:** Reduce capital tied up in the balance sheet (Total assets).                       | - Occasional difficulties in paying debts on time.<br>- Little or no reserve to handle unforeseen events.<br>**Action:** Reduce capital tied up in the balance sheet (Total assets).                                                 | - No difficulties in paying debts on time.<br>- Sufficient reserves to manage risk.<br>**Action:** Assess the appropriate reserve size and consider if returns can be improved.                                                     |
| **Solidity**  | Owners' percentage share of the company's value (Total Assets).                                         | - Company's debt is approximately equal to or greater than the company's value.<br>**Solution:** Improve earnings or inject new capital.                                                                                            | - Owners' share of the company's value is relatively small.<br>- In practice, this means that the risk of operations is borne by creditors, and the company may be threatened with bankruptcy.<br>**Solution:** Improve earnings or inject new capital. | - Owners' share of the company's value is relatively large.<br>- In practice, this means that the company's debt is unproblematic, and the company is unlikely to be threatened with bankruptcy.<br>**Action:** Leverage the flexibility to seek even better returns. |
| **Result**    | Revenues minus costs, resulting in profit or loss.                                                      | - Loss or very little profit.<br>- Costs are almost as high as revenues.<br>- A loss means the company is effectively paying for customer projects.<br>**Action:** Reduce costs and improve profitability.                           | - Profit is low as a percentage of revenues.<br>- This implies little or no risk margin to handle unforeseen events.<br>**Action:** Increase profit margins.                                                                        | - Profit constitutes a good proportion of revenues.<br>- This implies a good risk margin with a strong ability to handle unforeseen events.<br>**Action:** Continue current strategies and consider reinvestment opportunities.       |
***
This table is only for reference, what you shall make is design a report in markdown which must give an overview of the performance in details.
You shall use emojis to express the data more efficiently like using  clever emojis like 🔴, 🟢 or others
Your response needs to contain the following elements:
Date: {datetime.now().strftime("%Y-%m-%d")}
1. A title that summarizes the company's financial health. Basic Calculations if valid.
2. Index Table with the three key performance indicators (KPIs) and their descriptions
3. Imrovement areas and actions to be taken
4. A timeline and a step by step guide to improve the company's financial health
5. Contingency plans for unforeseen events
6. Leadership Logic with alot of IF ELSE AND WHILE FOR EACH statements
7. Immediate actions to be taken
Here is the chat history:
***
{json.dumps(st.session_state.messages)}
***

Do not include any other information.
Reply only in valid markdown format.
    
    """
    client = OpenAI(api_key=st.secrets["openai_api_key"])
    completion = client.completions.create(
        model="gpt-4o",
        prompt=prompt,
        
    )
    res = completion.choices[0].message.content
    
    # append the response to the session state
    st.session_state.timline.append(res)
        
    pass
    
def generate_reply(user_input):
    
    prompt =f"""
    You are having an interview with a company representative as a representative of a finance analytics company.
    You have been provided with tasked with gathering data from the compnay representative to generate a finance index.
    You will try to move the interview forward by replying in appropriate way.
    You have been provided with the chat history and a set of questions you must get answers to.
    You shall be collecting data regarding solidy and liquidy of the company. use this information:
    ***
    Certainly! Here's a recap of the **Index Table** from the document, which outlines three central key performance indicators (KPIs) to assess a company's financial health:

| **Index**   | **Description**                                                                                         | **Poor (Index 0-1)**                                                                                                                                                                                                                 | **Weak (Index 2-3)**                                                                                                                                                                                                                 | **Good (Index 4-5)**                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Liquidity** | Ability to pay debts upon maturity.                                                                     | - Significant difficulties in paying debts on time.<br>- Time and concern spent finding funds for salaries, purchases, and services.<br>**Action:** Reduce capital tied up in the balance sheet (Total assets).                       | - Occasional difficulties in paying debts on time.<br>- Little or no reserve to handle unforeseen events.<br>**Action:** Reduce capital tied up in the balance sheet (Total assets).                                                 | - No difficulties in paying debts on time.<br>- Sufficient reserves to manage risk.<br>**Action:** Assess the appropriate reserve size and consider if returns can be improved.                                                     |
| **Solidity**  | Owners' percentage share of the company's value (Total Assets).                                         | - Company's debt is approximately equal to or greater than the company's value.<br>**Solution:** Improve earnings or inject new capital.                                                                                            | - Owners' share of the company's value is relatively small.<br>- In practice, this means that the risk of operations is borne by creditors, and the company may be threatened with bankruptcy.<br>**Solution:** Improve earnings or inject new capital. | - Owners' share of the company's value is relatively large.<br>- In practice, this means that the company's debt is unproblematic, and the company is unlikely to be threatened with bankruptcy.<br>**Action:** Leverage the flexibility to seek even better returns. |
| **Result**    | Revenues minus costs, resulting in profit or loss.                                                      | - Loss or very little profit.<br>- Costs are almost as high as revenues.<br>- A loss means the company is effectively paying for customer projects.<br>**Action:** Reduce costs and improve profitability.                           | - Profit is low as a percentage of revenues.<br>- This implies little or no risk margin to handle unforeseen events.<br>**Action:** Increase profit margins.                                                                        | - Profit constitutes a good proportion of revenues.<br>- This implies a good risk margin with a strong ability to handle unforeseen events.<br>**Action:** Continue current strategies and consider reinvestment opportunities.       |

**Note:** The terms "Liquidity," "Solidity," and "Result" are translated from the original Norwegian terms "Likviditet," "Soliditet," and "Resultat," respectively.

This table provides a framework for evaluating a company's financial health across these three key areas, with suggested actions or solutions based on the assessment. 
***
To make this table you must ask the following questions in appropriate order of your choice:
You will adapth to the user's knowledge and lingo to make sure you are clear, explain these questions in details if need be.
###
1. General Perception & Expertise
• How would you describe the company’s overall financial health?
• On a scale of 1 to 5, how confident are you in your knowledge of the company’s financial details?

2. Core Financial Data
• What is the company’s total asset value (including cash, accounts receivable, inventory, fixed assets, etc.)?
• What is the total debt (covering loans, accounts payable, and other obligations)?
• Could you provide the financial performance for the last fiscal year by detailing total revenue, total costs, and the resulting profit or loss?
• How much cash is currently available for day-to-day operations?

3. Supporting Documentation
• Are there any financial statements or files you can share that offer more detailed insights into these figures?

4. Liquidity & Solidity Assessment
• Based on the above data, how would you assess the company’s liquidity and the robustness of its capital structure (i.e., the owners’ share of value)?

###

***
Here is the Chat histor:
{json.dumps(st.session_state.messages)}
You will Reply to : {user_input}
***
Your reply shall be a acknowledgement of the user's input, a statement or enquiry followed by a question.
You will also be providing a progress % along with the reply, representing how far you are in the interview process.
Use the following JSON format to reply:
____
{{
    "response": "Your reply here",
    "progress": "Your progress % here like 10, 20, 30 etc."
}}

    
    """
    client = OpenAI(api_key=st.secrets["openai_api_key"]) 
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages=[
            {
                "role": "system",
                "content": f"You are a interviewer for a finance analystics company. you respond only in valid JSON Format",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    res = completion.choices[0].message.content
    # print (res)
    response = json.loads(res)
    st.session_state.progress = int(response["progress"])
    return response["response"]
    

# Layout: Left column for Dashboard, right column for Chatbot
col1, col2 = st.columns([3, 2])

with col1:
    tab1, tab2 = st.tabs(["TimeLine", "Report Generation"])
    # Add your dashboard elements here
    with tab1:
        # st.write("TimeLine")
        for timelineElement in st.session_state.TimeLine:
            st.markdown(timelineElement)

with col2:

    
    # Create a container to hold chat messages (which will appear above the input)
    chat_container = st.container(height=450)
    # Render existing messages from session state
    for msg in st.session_state.messages:
        with chat_container.chat_message(msg["role"]):
            st.markdown(msg["content"])
    
    # Place file uploader above the chat input (optional)
    _col1, _col2,_col3 = st.columns([1,1,3])
    with _col1:
        with st.popover("📤"):
            uploaded_file = st.file_uploader("Choose a file",disabled=True)
    with _col2:
        if st.button("🆕"):
            st.session_state.messages = []
            st.session_state.progress = 0
            st.rerun()
            
    with _col3:
        # if the progress is more than 80 show a "generate Index" button
        if (st.session_state.progress + 0) > 80:
            if st.button("Generate Index"):
                geberate_timeline_report()
        else:
            st.write("Waiting for enough data")
    # Now the chat input is rendered below the messages container
    # add a progress bar with st.progress
    # print (f"Progress: {st.session_state.progress}")
    progress = st.progress(st.session_state.progress + 0) 
    
    user_input = st.chat_input("Type a message...")
    if user_input:
        # Append and display the user's message
        st.session_state.messages.append({"role": "user", "content": user_input})
        with chat_container.chat_message("user"):
            st.markdown(user_input)
        
        # Echo bot: simply echo the user input
        echo_response = generate_reply(user_input)
        st.session_state.messages.append({"role": "assistant", "content": echo_response})
        with chat_container.chat_message("assistant"):
            st.markdown(echo_response)
