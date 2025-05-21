import streamlit as st
import html
from datetime import date
from streamlit_quill import st_quill
import os # Import os for path joining if needed, though direct relative paths are usually fine

st.set_page_config(
    page_title="CIPO Service Interruption Message Generator",
    layout="centered",
    # Consider adding initial_sidebar_state="expanded" or "collapsed" if you add a sidebar later
)

st.title("CIPO Service Interruption Message Generator")

st.write(
    "Follow the steps below to create a bilingual service interruption message for your website with ease. "
    "Simply follow the steps below!"
)

# --- Added Initial Instruction Steps ---
st.header("Step 1: Log into Drupal")
st.write("1) Log into Drupal by clicking the following URL:")
st.markdown("https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/user/login")

st.write("2) Follow the next steps to correctly log into the Content management system (CMS):")

# Display images using relative paths within the repo
# Assuming the images are in a folder named 'images' at the same level as app.py
# Adjust paths if your image directory structure is different
image_dir = "images" # Directory containing your images

try:
    # Check if the images directory exists and contains the files
    if os.path.exists(image_dir) and all(os.path.exists(os.path.join(image_dir, img)) for img in ["step1.png", "step2.png", "step3.png"]):
        # Corrected parameter from use_column_width to use_container_width
        st.image(os.path.join(image_dir, "step1.png"), caption="Step 1: Enter Username", use_container_width=True)
        st.image(os.path.join(image_dir, "step2.png"), caption="Step 2: Choose Authentication Method", use_container_width=True)
        st.image(os.path.join(image_dir, "step3.png"), caption="Step 3: Complete Authentication", use_container_width=True)
    else:
        st.warning(f"Image files not found in the '{image_dir}' directory. Please ensure 'step1.png', 'step2.png', and 'step3.png' are in that folder relative to app.py.")
except Exception as e:
    st.error(f"An error occurred while trying to load images: {e}")


st.markdown("---") # Separator

# --- Original Step 1 Content (now part of the single page) ---
st.header("Step 2: Enter Message Titles and Date") # Renumbered step
st.write("Provide the required details for your service interruption message.")

english_title = st.text_input(
    "English Title",
    key='en_title_single', # Changed key for clarity in single page context
    help="The headline for your message in English (e.g., 'Online Services Unavailable')"
)
french_title = st.text_input(
    "French Title",
    key='fr_title_single', # Changed key for clarity
    help="The headline for your message in French (e.g., 'Services en ligne indisponibles')"
)
msg_date = st.date_input(
    "Message Date", value=date.today(),
    key='msg_date_single', # Changed key for clarity
    help="Usually the starting or posting date for this interruption."
)


st.markdown("---") # Separator

# --- Original Step 2 Content (now part of the single page) ---
st.header("Step 3: Write Your Messages") # Renumbered step
st.markdown("Use the editor below to format your message (bold, lists, etc.). All fields are required.")

# Ensure editor content is initialized for persistence across reruns in a single page context
# Quill editors might re-initialize if not given an explicit initial value or if key changes
# Let's use session state to try and maintain content across reruns more robustly
if 'english_content_single' not in st.session_state:
    st.session_state['english_content_single'] = ""
if 'french_content_single' not in st.session_state:
    st.session_state['french_content_single'] = ""


st.markdown("**English Message Content**")
english_content = st_quill(
    st.session_state['english_content_single'], # Use session state for initial value
    html=True,
    key="en_content_single" # Changed key for clarity
)
# Update session state with the current value whenever the widget is rendered
st.session_state['english_content_single'] = english_content

st.caption("Main body of the alert in English.")

with st.expander("Example (English)"):
    st.write("Our online services will be temporarily unavailable due to planned maintenance. "
             "We apologize for any inconvenience and appreciate your understanding.")

st.markdown("**French Message Content**")
french_content = st_quill(
    st.session_state['french_content_single'], # Use session state for initial value
    html=True,
    key="fr_content_single" # Changed key for clarity
)
# Update session state with the current value whenever the widget is rendered
st.session_state['french_content_single'] = french_content

st.caption("Main body of the alert in French.")

with st.expander("Exemple (français)"):
    st.write("Nos services en ligne seront temporairement indisponibles en raison d'une maintenance planifiée. "
             "Nous nous excusons pour tout inconvénient et vous remercions de votre compréhension.")

st.markdown("---") # Separator

# --- HTML Generation and Preview (now part of the single page) ---
st.header("Step 4: Generate and Copy HTML") # Renumbered step
st.write("Your generated HTML code and previews are below. Copy the code needed for your CMS.")

# We only generate and display if the required fields have *some* value
# The quill editors might return "<p><br></p>" even if visually empty, which is HTML
# We'll check titles and date primarily, as content from quill will likely have some HTML structure
generate_html = st.button("Generate HTML Output") # Add a button to explicitly trigger generation

if generate_html:
    if english_title and french_title and msg_date is not None and english_content is not None and french_content is not None:

        date_iso = msg_date.strftime('%Y-%m-%d')

        # Use the content directly from the quill editor variables
        # html.escape is used for titles just in case they contain characters that could break HTML
        english_html = f"""
<h2 class="text-danger">{html.escape(english_title)} &ndash; (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</h2>
{english_content}
<p>For more information, please contact our <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="78a10a22-8b11-4c4e-bef2-5c37808ebaba" href="/site/canadian-intellectual-property-office/node/13">Client Service Centre</a>. For date-sensitive material, please review our <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="d0a59429-cdb8-4122-b2b0-6167cf90e56b" href="/site/canadian-intellectual-property-office/node/133">Correspondence Procedures</a>.</p>
"""
        # Corrected the French contact link UUID which was different from the English one
        french_html = f"""
<h2 class="text-danger">{html.escape(french_title)} &ndash; (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</h2>
{french_content}
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

    else:
        st.warning("Please ensure all title, date, and content fields are filled out before generating.")

st.markdown("---") # Separator

# --- Start Over Button (Optional in single page, but can be useful to clear inputs) ---
if st.button("Clear All Inputs"):
    st.session_state.clear()
    st.rerun()
    st.info("Inputs cleared.")

st.info(
    "Fill out the details and content fields above, then click 'Generate HTML Output' to see the results."
)