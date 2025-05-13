import streamlit as st
import html
from datetime import date
from streamlit_quill import st_quill

st.set_page_config(
    page_title="CIPO Service Interruption Message Generator",
    layout="centered",
)
st.title("CIPO Service Interruption Message Generator")

st.write(
    "Create a bilingual service interruption message for your website with ease. "
    "Simply follow the steps below!"
)

# --- Step 1: Message details ---
if 'step' not in st.session_state:
    st.session_state['step'] = 1

if st.session_state['step'] == 1:
    with st.form("details_form"):
        st.header("Step 1: Enter Message Titles and Date")
        english_title = st.text_input(
            "English Title",
            help="The headline for your message in English (e.g., 'Online Services Unavailable')"
        )
        french_title = st.text_input(
            "French Title",
            help="The headline for your message in French (e.g., 'Services en ligne indisponibles')"
        )
        msg_date = st.date_input(
            "Message Date", value=date.today(),
            help="Usually the starting or posting date for this interruption."
        )
        next1 = st.form_submit_button("Next →")
    if next1:
        # simple validation
        if not english_title or not french_title:
            st.warning("Please enter both English and French titles before proceeding.")
        else:
            st.session_state['english_title'] = english_title
            st.session_state['french_title'] = french_title
            st.session_state['msg_date'] = msg_date
            st.session_state['step'] = 2
            st.rerun()

# --- Step 2: WYSIWYG message contents ---
elif st.session_state['step'] == 2:
    st.header("Step 2: Write Your Messages")
    st.markdown("Use the editor to format your message (bold, lists, etc.). All fields are required.")

    # Ensure editor content is initialized for persistence
    if 'english_content' not in st.session_state:
        st.session_state['english_content'] = ""
    if 'french_content' not in st.session_state:
        st.session_state['french_content'] = ""

    st.markdown("**English Message Content**")
    english_content = st_quill(
        st.session_state['english_content'],
        html=True,
        key="en_content"
    )
    st.caption("Main body of the alert in English.")

    with st.expander("Example (English)"):
        st.write("Our online services will be temporarily unavailable due to planned maintenance. "
                 "We apologize for any inconvenience and appreciate your understanding.")

    st.markdown("**French Message Content**")
    french_content = st_quill(
        st.session_state['french_content'],
        html=True,
        key="fr_content"
    )
    st.caption("Main body of the alert in French.")

    with st.expander("Exemple (français)"):
        st.write("Nos services en ligne seront temporairement indisponibles en raison d'une maintenance planifiée. "
                 "Nous nous excusons pour tout inconvénient et vous remercions de votre compréhension.")

    col1, col2 = st.columns([1, 3])
    with col2:
        next2 = st.button("Next: Preview & Generate HTML")
    with col1:
        back = st.button("← Back")
    if back:
        st.session_state['english_content'] = english_content
        st.session_state['french_content'] = french_content
        st.session_state['step'] = 1
        st.rerun()
    if next2:
        st.session_state['english_content'] = english_content
        st.session_state['french_content'] = french_content
        if not english_content or not french_content:
            st.warning("Please complete both the English and French message boxes before proceeding.")
        else:
            st.session_state['step'] = 3
            st.rerun()

# --- Step 3: Preview and HTML code per language ---
elif st.session_state['step'] == 3:
    st.header("Step 3: Preview and Copy HTML")

    en_title = st.session_state['english_title']
    fr_title = st.session_state['french_title']
    dt = st.session_state['msg_date']
    date_iso = dt.strftime('%Y-%m-%d')
    en_content = st.session_state['english_content']
    fr_content = st.session_state['french_content']

    english_html = f"""
<h2 class="text-danger">{html.escape(en_title)} &ndash; (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</h2>
{en_content}
<p>For more information, please contact our <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="78a10a22-8b11-4c4e-bef2-5c37808ebaba" href="/site/canadian-intellectual-property-office/node/13">Client Service Centre</a>. For date-sensitive material, please review our <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="d0a59429-cdb8-4122-b2b0-6167cf90e56b" href="/site/canadian-intellectual-property-office/node/133">Correspondence Procedures</a>.</p>
"""
    french_html = f"""
<h2 class="text-danger">{html.escape(fr_title)} &ndash; (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</h2>
{fr_content}
<p>Pour de plus amples renseignements, veuillez communiquer avec notre <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="78a10a22-8b11-4c4e-bef2-5c37808ebaba" href="/site/canadian-intellectual-property-office/node/13">Centre de services à la clientèle</a>. Pour les demandes assorties de délais, veuillez consulter les <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="d0a59429-cdb8-4122-b2b0-6167cf90e56b" href="/site/canadian-intellectual-property-office/node/133">Procédures relatives à la correspondance</a>.</p>
"""
    combined_html = english_html + "\n" + french_html

    tabs = st.tabs(["English HTML", "French HTML", "Bilingual Output"])
    with tabs[0]:
        st.subheader("English HTML Code")
        st.code(english_html, language="html")
        st.markdown("Preview:", unsafe_allow_html=True)
        st.markdown(english_html, unsafe_allow_html=True)
    with tabs[1]:
        st.subheader("French HTML Code")
        st.code(french_html, language="html")
        st.markdown("Aperçu :", unsafe_allow_html=True)
        st.markdown(french_html, unsafe_allow_html=True)
    with tabs[2]:
        st.subheader("Combined (Bilingual) HTML Output")
        st.code(combined_html, language="html")
        st.markdown("Preview:", unsafe_allow_html=True)
        st.markdown(combined_html, unsafe_allow_html=True)

    st.success("Copy the code you need for your CMS. Preview matches your chosen formatting.")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("← Back to Edit"):
            st.session_state['step'] = 2
            st.rerun()
    with col2:
        if st.button("Start Over"):
            st.session_state.clear()
            st.rerun()

    st.info(
        "If you need to enter a new announcement, click **Start Over**. "
        "If you need to adjust your message, click **Back to Edit**."
    )