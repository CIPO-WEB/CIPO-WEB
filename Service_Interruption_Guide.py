import streamlit as st
import html
from datetime import date
from streamlit_quill import st_quill
import os

st.set_page_config(
    page_title="CIPO Service Interruption Message Guide", # Changed from Generator to Guide
    layout="centered",
)

# --- Summary Section ---
st.header("CIPO Service Interruption Message Guide") # Already Guide
st.markdown(
    """
    This guide helps you create and publish bilingual service interruption messages on the CIPO website.
    It includes an interactive section below to generate compliant HTML code based on simple text input.

    You will use this guide to:
    1.  Generate the necessary HTML code.
    2.  Publish a **full version** of the message on the Service and website interruptions page.
    3.  Publish a **shorter alert box version** on the Home page that links to the full message.

    Follow the detailed steps below to complete this process using the CMS.
    """
)

st.title("CIPO Service Interruption Message Tool") # Changed from Generator to Tool

st.write(
    "Follow the steps below to create a bilingual service interruption message for your website and apply it to the CMS."
)

# --- Instructions Section ---
st.header("Instructions: Using the Tool and CMS") # Changed from Generator to Tool

st.markdown("#### Step 1: Log into Drupal")
st.write("1) Log into Drupal by clicking the following URL:")
st.markdown("https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/user/login")

st.markdown("#### Step 2: Log into the CMS")
st.write("2) Follow the next steps to correctly log into the Content management system (CMS):")

image_dir = "images" # Directory containing your images

# Display images for steps 1-3 login process
try:
    if os.path.exists(image_dir):
        if os.path.exists(os.path.join(image_dir, "step1.png")):
            st.image(os.path.join(image_dir, "step1.png"), caption="Step 2a: click Log in with Keycloack", use_container_width=True)
        else:
             st.warning(f"Image 'step1.png' not found in '{image_dir}'.")
        if os.path.exists(os.path.join(image_dir, "step2.png")):
             st.image(os.path.join(image_dir, "step2.png"), caption="Step 2b: Choose Authentication Method", use_container_width=True)
        else:
             st.warning(f"Image 'step2.png' not found in '{image_dir}'.")
        if os.path.exists(os.path.join(image_dir, "step3.png")):
            st.image(os.path.join(image_dir, "step3.png"), caption="Step 2c: Complete Authentication: ISED employee", use_container_width=True)
        else:
             st.warning(f"Image 'step3.png' not found in '{image_dir}'.")
    else:
        st.warning(f"Image directory '{image_dir}' not found. Please ensure it exists relative to app.py.")
except Exception as e:
    st.error(f"An error occurred while trying to load login images: {e}")

st.markdown("#### Step 3: Open the Service Interruption Page")
st.write("3) Once logged in, open the service and website interruptions page:")
st.markdown("https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/service-and-website-interruptions")

st.markdown("#### Step 4: Confirm Login")
st.write("4) Confirm that you are logged in. If you cannot see the 'Edit' button at the top of the page, repeat steps 1 to 3.")
try:
    if os.path.exists(os.path.join(image_dir, "step4.png")):
        st.image(os.path.join(image_dir, "step4.png"), caption="Step 4: Confirm 'Edit' Button is Visible", use_container_width=True)
    else:
         st.warning(f"Image 'step4.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step4.png: {e}")


st.markdown("#### Step 5: Open Source Editor")
st.write("5) Click 'Edit' and then 'Source' as shown in the image below:")
try:
    if os.path.exists(os.path.join(image_dir, "step5.png")):
        st.image(os.path.join(image_dir, "step5.png"), caption="Step 5: Click 'Edit' then 'Source'", use_container_width=True)
    else:
         st.warning(f"Image 'step5.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step5.png: {e}")

st.markdown("#### Step 6: Create Your Message using the Tool") # Changed from Generator to Tool
st.write("6) Create your message using the tools below. Once you have generated the HTML code (English and French) in the 'Generate and Copy HTML Output' section, proceed to Step 7.")

st.markdown("---") # Separator


# --- Message Creation Section ---
st.header("Create Your Message Content")
st.markdown("Use the tools below to create the content and titles for your service interruption message. All fields are required.")


st.subheader("Enter Message Details")
st.write("Provide the required details for your service interruption message.")

english_title = st.text_input(
    "English Title",
    key='en_title_single',
    help="The headline for your message in English (e.g., 'Online Services Unavailable')"
)
french_title = st.text_input(
    "French Title",
    key='fr_title_single',
    help="The headline for your message in French (e.g., 'Services en ligne indisponibles')"
)
msg_date = st.date_input(
    "Message Date", value=date.today(),
    key='msg_date_single',
    help="Usually the starting or posting date for this interruption."
)

st.subheader("Write Your Messages")
st.markdown("Use the editor below to format the main body of your message (bold, lists, etc.).")

# Ensure editor content is initialized for persistence
if 'english_content_single' not in st.session_state:
    st.session_state['english_content_single'] = ""
if 'french_content_single' not in st.session_state:
    st.session_state['french_content_single'] = ""

st.markdown("**English Message Content (Full)**")
english_content = st_quill(
    st.session_state['english_content_single'],
    html=True,
    key="en_content_single"
)
st.session_state['english_content_single'] = english_content
st.caption("Main body of the full alert on the Service and website interruptions page.")

with st.expander("Example (English)"):
    st.write("Our online services will be temporarily unavailable due to planned maintenance. "
             "We apologize for any inconvenience and appreciate your understanding.")

st.markdown("**French Message Content (Full)**")
french_content = st_quill(
    st.session_state['french_content_single'],
    html=True,
    key="fr_content_single"
)
st.session_state['french_content_single'] = french_content
st.caption("Main body of the full alert on the Service and website interruptions page.")

with st.expander("Exemple (français)"):
    st.write("Nos services en ligne seront temporairement indisponibles en raison d'une maintenance planifiée. "
             "Nous nous excusons pour tout inconvénient et vous remercions de votre compréhension.")

st.markdown("---") # Separator

# --- HTML Generation Section ---
st.header("Generate and Copy HTML Output")
st.write("Click the button below to generate the HTML code based on your input. Copy the code needed for the service interruption page ('English HTML (Full)' and 'French HTML (Full)') and the Home page alert ('English Home page HTML code' and 'French Home page HTML code').")

# Button to trigger generation
generate_html = st.button("Generate HTML Output")

# This section will only display *after* the button is clicked and inputs are valid
if generate_html:
    if english_title and french_title and msg_date is not None and english_content is not None and french_content is not None:

        date_iso = msg_date.strftime('%Y-%m-%d')

        # --- Full Message HTML ---
        # html.escape is used for titles just in case they contain characters that could break HTML
        english_html = f"""
<h2 class="text-danger">{html.escape(english_title)} &ndash; (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</h2>
{english_content}
<p>For more information, please contact our <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="78a10a22-8b11-4c4e-bef2-5c37808ebaba" href="/site/canadian-intellectual-property-office/node/13">Client Service Centre</a>. For date-sensitive material, please review our <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="d0a59429-cdb8-4122-b2b0-6167cf90e56b" href="/site/canadian-intellectual-property-office/node/133">Correspondence Procedures</a>.</p>
"""
        french_html = f"""
<h2 class="text-danger">{html.escape(french_title)} &ndash; (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</h2>
{french_content}
<p>Pour de plus amples renseignements, veuillez communiquer avec notre <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="78a10a22-8b11-4c4e-bef2-5c37808ebaba" href="/site/canadian-intellectual-property-office/node/13">Centre de services à la clientèle</a>. Pour les demandes assorties de délais, veuillez consulter les <a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="d0a59429-cdb8-4122-b2b0-6167cf90e56b" href="/site/canadian-intellectual-property-office/node/133">Procédures relatives à la correspondance</a>.</p>
"""

        # --- Alert Box HTML (Split into English and French) ---
        # Note: The UUID fb66b1c4-e3c7-490a-9e61-dd2436a8bc90 seems to be specific to the page linking to the full message (node/28)
        english_alert_box_html = f"""
<div class="alert alert-warning col-md-12 mrgn-bttm-sm activeNotice">
  <p><a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="fb66b1c4-e3c7-490a-9e61-dd2436a8bc90" href="/site/canadian-intellectual-property-office/node/28"><span class="text-danger"><strong>Service interruption - {html.escape(english_title)} - (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</strong></span></a>
  </p>
</div>
"""
        french_alert_box_html = f"""
<div class="alert alert-warning col-md-12 mrgn-bttm-sm activeNotice">
  <p><a data-entity-substitution="canonical" data-entity-type="node" data-entity-uuid="fb66b1c4-e3c7-490a-9e61-dd2436a8bc90" href="/site/canadian-intellectual-property-office/node/28"><span class="text-danger"><strong>Interruption des services - {html.escape(french_title)} - (<time class="nowrap" datetime="{date_iso}">{date_iso}</time>)</strong></span></a>
  </p>
</div>
"""

        # --- Display Tabs ---
        # Updated tabs list: Removed Bilingual Full, Split Alert Box into English and French
        tabs = st.tabs(["English HTML (Full)", "French HTML (Full)", "English Home page HTML code", "French Home page HTML code"])

        with tabs[0]:
            st.subheader("English HTML Code (Full Message)")
            st.code(english_html, language="html")
            st.markdown("Preview:", unsafe_allow_html=True)
            st.markdown(english_html, unsafe_allow_html=True)
        with tabs[1]:
            st.subheader("French HTML Code (Full Message)")
            st.code(french_html, language="html")
            st.markdown("Aperçu :", unsafe_allow_html=True)
            st.markdown(french_html, unsafe_allow_html=True)
        with tabs[2]:
            st.subheader("English Home page HTML code")
            st.code(english_alert_box_html, language="html")
            st.markdown("Preview:", unsafe_allow_html=True)
            st.markdown(english_alert_box_html, unsafe_allow_html=True)
        with tabs[3]:
            st.subheader("French Home page HTML code")
            st.code(french_alert_box_html, language="html")
            st.markdown("Aperçu :", unsafe_allow_html=True)
            st.markdown(french_alert_box_html, unsafe_allow_html=True)

        st.success("HTML generated. Copy the code you need and continue with the steps below.")

    else:
        st.warning("Please ensure all title, date, and content fields are filled out before generating HTML.")

st.markdown("---") # Separator

# --- Continue CMS Steps Section (Service Interruption Page) ---
st.header("Instructions (Cont.): Applying HTML to CMS - Service Interruption Page")

st.markdown("#### Step 7: Paste Full HTML Message into Service Interruption Page Source")
st.write("7) Copy the 'English HTML (Full)' and 'French HTML (Full)' code from the sections above. Paste the **English** code into the English version of the Service Interruption page's Source editor, right above the commented line of code `<!-- InstanceBeginEditable name='main' -->`. Please do not modify or delete anything else on the page. Repeat for the **French** code on the French version of the page.")
try:
    if os.path.exists(os.path.join(image_dir, "step6.png")):
        st.image(os.path.join(image_dir, "step6.png"), caption="Step 7: Paste HTML into Service Interruption Page Source Editor", use_container_width=True)
    else:
         st.warning(f"Image 'step6.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step6.png: {e}")


st.markdown("#### Step 7.1: View Result in CMS")
st.write("7.1) Once you have copy-pasted the full messages HTML code (English and French), click on 'Source' again to view the result. This is how the message will display once you publish the page.")
try:
    # Reusing step5.png as requested
    if os.path.exists(os.path.join(image_dir, "step5.png")):
        st.image(os.path.join(image_dir, "step5.png"), caption="Step 7.1: Click 'Source' to preview", use_container_width=True)
    else:
         st.warning(f"Image 'step5.png' not found for Step 7.1.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step5.png for Step 7.1: {e}")


st.markdown("#### Step 8: Save Service Interruption Page as Draft")
st.write("8) Once satisfied with the message on the Service Interruption page, scroll down and select 'Draft' instead of 'Published'.")
try:
    if os.path.exists(os.path.join(image_dir, "step7.png")):
        st.image(os.path.join(image_dir, "step7.png"), caption="Step 8: Select 'Draft'", use_container_width=True)
    else:
         st.warning(f"Image 'step7.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step7.png: {e}")

st.markdown("#### Step 9: Review Service Interruption Page Draft")
st.write("9) Click 'Save (this translation)' and you will be able to review the Draft version of the page. Please note that you also need to review the French version of the page.")
st.markdown("Note: if you need to make changes to the Draft version, go back to Step 4.")

st.markdown("#### Step 10: Publish the Full Message")
st.write("10) Once satisfied with the message on the Service Interruption page and after having reviewed both versions (ENG-FRA), click 'Edit', scroll down, and 'Save as Published' to publish the full message live.")
try:
    if os.path.exists(os.path.join(image_dir, "step8.png")):
        st.image(os.path.join(image_dir, "step8.png"), caption="Step 10: Save as 'Published'", use_container_width=True)
    else:
         st.warning(f"Image 'step8.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step8.png: {e}")

st.markdown("---") # Separator

# --- Continue CMS Steps Section (Home Page) ---
st.header("Instructions: Applying HTML to CMS - Home Page Alert Box")
st.markdown("Note: Our service interruption message is now published live on the Service and website interruptions page (https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en/service-and-website-interruptions). Now, we need to display a short message on the Home page to lead users to this page, if they want to read the full message.")

st.markdown("#### Step 11: Open the CIPO Home page")
st.write("11) Open the CIPO Home page (https://ised-isde.canada.ca/site/canadian-intellectual-property-office/en) and head into Edit mode.")
try:
    # Reusing step4.png as requested
    if os.path.exists(os.path.join(image_dir, "step4.png")):
        st.image(os.path.join(image_dir, "step4.png"), caption="Step 11: Edit CIPO Home Page", use_container_width=True)
    else:
         st.warning(f"Image 'step4.png' not found for Step 11.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step4.png for Step 11: {e}")

st.markdown("#### Step 12: Open Homepage Source Editor")
st.write("12) Switch the Home page into 'Source' view and find the *****************NOTICES****** line. You will paste the Home page code (Alert Box HTML) below that line as explained in Step 14.")
try:
    # Reusing step5.png as requested
    if os.path.exists(os.path.join(image_dir, "step5.png")):
        st.image(os.path.join(image_dir, "step5.png"), caption="Step 12: Open Homepage Source and Find Comment", use_container_width=True)
    else:
         st.warning(f"Image 'step5.png' not found for Step 12.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step5.png for Step 12: {e}")

st.markdown("#### Step 13: Copy Generated Home page HTML code")
st.write("13) Copy the 'English Home page HTML code' and 'French Home page HTML code' generated in the section above.")
try:
    if os.path.exists(os.path.join(image_dir, "step9.png")):
        st.image(os.path.join(image_dir, "step9.png"), caption="Step 13: Copy Home page HTML Code", use_container_width=True)
    else:
         st.warning(f"Image 'step9.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step9.png: {e}")

st.markdown("#### Step 14: Paste Home page HTML code")
st.write("14) Paste the **English** 'Home page HTML code' exactly here in the Home page Source editor, below the `<!-- *****************NOTICES****** -->` line (make sure to be in Edit mode, as indicated in Step 11). Repeat for the **French** code on the French version of the Home page.")
try:
    if os.path.exists(os.path.join(image_dir, "step10.png")):
        st.image(os.path.join(image_dir, "step10.png"), caption="Step 14: Paste Home page HTML into Source Editor", use_container_width=True)
    else:
         st.warning(f"Image 'step10.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step10.png: {e}")

st.markdown("#### Step 15: View Result and Save Home page as Draft")
st.write("15) Once you have copy-pasted the Home page HTML code (English and French), click on 'Source' again to view the result. This is how the message will display once you publish the page. Once satisfied with the message, scroll down and select 'Draft' instead of 'Published'.")
try:
    # Reusing step7.png as requested
    if os.path.exists(os.path.join(image_dir, "step7.png")):
        st.image(os.path.join(image_dir, "step7.png"), caption="Step 15: Preview and Save as Draft", use_container_width=True)
    else:
         st.warning(f"Image 'step7.png' not found for Step 15.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step7.png for Step 15: {e}")

st.markdown("#### Step 16: Review Home page Draft")
st.write("16) Click 'Save (this translation)' and you will be able to review the Draft version of the page. Please note that you also need to review the French version of the page.")
st.markdown("Note: if you need to make changes to the Draft version, go back to Step 11.") # Updated note to point to Step 11

st.markdown("#### Step 17: Publish the Home page Alert")
st.write("17) Once satisfied with the message on the Home page and after having reviewed both versions (ENG-FRA), click 'Edit', scroll down, and 'Save as Published' to publish the message live.")
try:
    # Reusing step8.png as requested
    if os.path.exists(os.path.join(image_dir, "step8.png")):
        st.image(os.path.join(image_dir, "step8.png"), caption="Step 17: Save as 'Published'", use_container_width=True)
    else:
         st.warning(f"Image 'step8.png' not found in '{image_dir}'.")
except Exception as e:
    st.error(f"An error occurred while trying to load image step8.png for Step 17: {e}")

st.markdown("Note: The message on the Home page is now live, this short message has a direct link to the full version of the service interruption message.")


st.markdown("---") # Separator


# --- Utility Section ---
st.header("App Utilities")

if st.button("Clear All Inputs"):
    st.session_state.clear()
    st.rerun()
    st.info("Inputs cleared.")

st.info(
    "Fill out the details and content fields above, then click 'Generate HTML Output' to see the results."
)