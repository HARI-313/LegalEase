import html
import os
from datetime import date

import requests
import streamlit as st
from dotenv import load_dotenv


# ============================================================
# ENVIRONMENT
# ============================================================

load_dotenv()


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:8000"
).rstrip("/")


APP_NAME = os.getenv(
    "APP_NAME",
    "LegalEase"
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(

    page_title=APP_NAME,

    page_icon="⚖️",

    layout="wide",

    initial_sidebar_state="expanded",
)


# ============================================================
# THEME DEFINITIONS
# ============================================================

THEMES = {

    "⚖️ Legal Blue": {

        "app_bg": "#06111f",

        "app_bg_2": "#0b1c2d",

        "hero_bg_1": "#102a43",

        "hero_bg_2": "#073b4c",

        "hero_border": "#1d6070",

        "hero_title": "#e8fbff",

        "hero_text": "#b8d8df",

        "notice_bg": "#0e2530",

        "notice_border": "#36c2b4",

        "notice_text": "#cceef0",

        "card_bg": "#0d1827",

        "card_border": "#25455c",

        "text": "#edf6ff",

        "secondary_text": "#b8d8df",

        "accent": "#36c2b4",

        "accent_hover": "#2aa89d",

        "button_text": "#ffffff",

        "input_bg": "#101f31",

        "input_border": "#31526a",

        "preview_bg": "#0d1827",

        "preview_border": "#25455c",

        "preview_text": "#e8f1f7",

    },


    "🌊 Ocean": {

        "app_bg": "#02131f",

        "app_bg_2": "#063b4c",

        "hero_bg_1": "#075985",

        "hero_bg_2": "#0e7490",

        "hero_border": "#22d3ee",

        "hero_title": "#ecfeff",

        "hero_text": "#cffafe",

        "notice_bg": "#083344",

        "notice_border": "#22d3ee",

        "notice_text": "#cffafe",

        "card_bg": "#082f49",

        "card_border": "#155e75",

        "text": "#ecfeff",

        "secondary_text": "#bae6fd",

        "accent": "#06b6d4",

        "accent_hover": "#0891b2",

        "button_text": "#ffffff",

        "input_bg": "#082f49",

        "input_border": "#155e75",

        "preview_bg": "#06283d",

        "preview_border": "#155e75",

        "preview_text": "#e0f2fe",

    },


    "🌙 Midnight": {

        "app_bg": "#030712",

        "app_bg_2": "#111827",

        "hero_bg_1": "#111827",

        "hero_bg_2": "#1e293b",

        "hero_border": "#475569",

        "hero_title": "#f8fafc",

        "hero_text": "#cbd5e1",

        "notice_bg": "#111827",

        "notice_border": "#818cf8",

        "notice_text": "#c7d2fe",

        "card_bg": "#0f172a",

        "card_border": "#334155",

        "text": "#f8fafc",

        "secondary_text": "#cbd5e1",

        "accent": "#818cf8",

        "accent_hover": "#6366f1",

        "button_text": "#ffffff",

        "input_bg": "#111827",

        "input_border": "#374151",

        "preview_bg": "#0b1120",

        "preview_border": "#334155",

        "preview_text": "#e5e7eb",

    },


    "💜 Royal Purple": {

        "app_bg": "#12051f",

        "app_bg_2": "#24103a",

        "hero_bg_1": "#4c1d95",

        "hero_bg_2": "#6d28d9",

        "hero_border": "#a78bfa",

        "hero_title": "#faf5ff",

        "hero_text": "#e9d5ff",

        "notice_bg": "#2e1065",

        "notice_border": "#c084fc",

        "notice_text": "#f3e8ff",

        "card_bg": "#1e1033",

        "card_border": "#6b21a8",

        "text": "#faf5ff",

        "secondary_text": "#e9d5ff",

        "accent": "#c084fc",

        "accent_hover": "#a855f7",

        "button_text": "#ffffff",

        "input_bg": "#25113f",

        "input_border": "#6b21a8",

        "preview_bg": "#180b29",

        "preview_border": "#6b21a8",

        "preview_text": "#f3e8ff",

    },


    "🌿 Emerald": {

        "app_bg": "#031712",

        "app_bg_2": "#073b2a",

        "hero_bg_1": "#064e3b",

        "hero_bg_2": "#047857",

        "hero_border": "#34d399",

        "hero_title": "#ecfdf5",

        "hero_text": "#bbf7d0",

        "notice_bg": "#064e3b",

        "notice_border": "#34d399",

        "notice_text": "#d1fae5",

        "card_bg": "#052e24",

        "card_border": "#047857",

        "text": "#ecfdf5",

        "secondary_text": "#bbf7d0",

        "accent": "#34d399",

        "accent_hover": "#10b981",

        "button_text": "#ffffff",

        "input_bg": "#073b2a",

        "input_border": "#047857",

        "preview_bg": "#04251d",

        "preview_border": "#047857",

        "preview_text": "#d1fae5",

    },


    "☀️ Light": {

        "app_bg": "#f5f7fb",

        "app_bg_2": "#e9eef6",

        "hero_bg_1": "#ffffff",

        "hero_bg_2": "#e8f1ff",

        "hero_border": "#bfdbfe",

        "hero_title": "#172554",

        "hero_text": "#475569",

        "notice_bg": "#eff6ff",

        "notice_border": "#2563eb",

        "notice_text": "#1e3a8a",

        "card_bg": "#ffffff",

        "card_border": "#cbd5e1",

        "text": "#172033",

        "secondary_text": "#475569",

        "accent": "#2563eb",

        "accent_hover": "#1d4ed8",

        "button_text": "#ffffff",

        "input_bg": "#ffffff",

        "input_border": "#cbd5e1",

        "preview_bg": "#ffffff",

        "preview_border": "#cbd5e1",

        "preview_text": "#1e293b",

    },

}


# ============================================================
# SESSION STATE
# ============================================================

if "theme" not in st.session_state:

    st.session_state.theme = "⚖️ Legal Blue"


if "document_text" not in st.session_state:

    st.session_state.document_text = ""


if "last_model" not in st.session_state:

    st.session_state.last_model = ""


# ============================================================
# SIDEBAR THEME SELECTOR
# ============================================================

with st.sidebar:

    st.header("🎨 Appearance")

    selected_theme = st.selectbox(

        "Choose Theme",

        list(THEMES.keys()),

        index=list(
            THEMES.keys()
        ).index(
            st.session_state.theme
        ),

    )


    if selected_theme != st.session_state.theme:

        st.session_state.theme = selected_theme

        st.rerun()


theme = THEMES[
    st.session_state.theme
]


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(

    f"""
<style>

/* ========================================================
   MAIN APPLICATION
   ======================================================== */

.stApp {{

    background:
        linear-gradient(
            135deg,
            {theme["app_bg"]},
            {theme["app_bg_2"]}
        );

    color: {theme["text"]};

}}


/* ========================================================
   SIDEBAR
   ======================================================== */

section[data-testid="stSidebar"] {{

    background:
        linear-gradient(
            180deg,
            {theme["app_bg"]},
            {theme["app_bg_2"]}
        );

    border-right:
        1px solid
        {theme["card_border"]};

}}


/* ========================================================
   HERO
   ======================================================== */

.hero {{

    padding: 28px;

    border-radius: 20px;

    background:
        linear-gradient(
            135deg,
            {theme["hero_bg_1"]},
            {theme["hero_bg_2"]}
        );

    border:
        1px solid
        {theme["hero_border"]};

    margin-bottom: 20px;

    box-shadow:
        0 12px 30px
        rgba(0,0,0,0.18);

}}


.hero h1 {{

    margin: 0;

    color:
        {theme["hero_title"]};

    font-size: 42px;

}}


.hero p {{

    color:
        {theme["hero_text"]};

    margin-top: 8px;

    font-size: 17px;

}}


/* ========================================================
   NOTICE
   ======================================================== */

.notice {{

    padding: 14px;

    border-left:
        4px solid
        {theme["notice_border"]};

    background:
        {theme["notice_bg"]};

    border-radius: 8px;

    color:
        {theme["notice_text"]};

}}


/* ========================================================
   PREVIEW
   ======================================================== */

.preview {{

    background:
        {theme["preview_bg"]};

    border:
        1px solid
        {theme["preview_border"]};

    border-radius: 16px;

    padding: 22px;

    min-height: 450px;

    max-height: 650px;

    overflow-y: auto;

    color:
        {theme["preview_text"]};

    font-family:
        Georgia,
        serif;

    line-height: 1.7;

    white-space: pre-wrap;

    box-shadow:
        0 8px 25px
        rgba(0,0,0,0.12);

}}


/* ========================================================
   STREAMLIT INPUTS
   ======================================================== */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] {{

    background-color:
        {theme["input_bg"]} !important;

    color:
        {theme["text"]} !important;

    border-color:
        {theme["input_border"]} !important;

}}


/* ========================================================
   BUTTONS
   ======================================================== */

.stButton > button {{

    border-radius: 10px;

    border:
        1px solid
        {theme["accent"]};

    background:
        {theme["accent"]};

    color:
        {theme["button_text"]};

    font-weight: 600;

    transition:
        all 0.2s ease;

}}


.stButton > button:hover {{

    background:
        {theme["accent_hover"]};

    border-color:
        {theme["accent_hover"]};

    transform:
        translateY(-1px);

}}


/* ========================================================
   DOWNLOAD BUTTON
   ======================================================== */

.stDownloadButton > button {{

    border-radius: 10px;

    border:
        1px solid
        {theme["accent"]};

    background:
        {theme["accent"]};

    color:
        {theme["button_text"]};

    font-weight: 600;

}}


.stDownloadButton > button:hover {{

    background:
        {theme["accent_hover"]};

}}


/* ========================================================
   HEADINGS
   ======================================================== */

h1,
h2,
h3,
h4 {{

    color:
        {theme["text"]} !important;

}}


/* ========================================================
   GENERAL TEXT
   ======================================================== */

p,
label,
span {{

    color:
        {theme["text"]};

}}


/* ========================================================
   DIVIDERS
   ======================================================== */

hr {{

    border-color:
        {theme["card_border"]};

}}


/* ========================================================
   SCROLLBAR
   ======================================================== */

::-webkit-scrollbar {{

    width: 8px;

}}


::-webkit-scrollbar-track {{

    background:
        {theme["app_bg"]};

}}


::-webkit-scrollbar-thumb {{

    background:
        {theme["accent"]};

    border-radius: 10px;

}}


/* ========================================================
   FOOTER
   ======================================================== */

.footer {{

    text-align: center;

    color:
        {theme["secondary_text"]};

    padding: 15px;

}}

</style>
""",

    unsafe_allow_html=True
)


# ============================================================
# HEADER
# ============================================================

st.markdown(

    """
<div class="hero">

<h1>⚖️ LegalEase</h1>

<p>
AI-Powered Legal Document Generator
</p>

</div>
""",

    unsafe_allow_html=True
)


st.markdown(

    """
<div class="notice">

<strong>Important:</strong>
LegalEase provides AI-assisted drafting.
It is not a substitute for professional
legal advice or legal review.

</div>
""",

    unsafe_allow_html=True
)


st.write("")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.divider()

    st.header(
        "📄 Document Details"
    )


    document_type = st.selectbox(

        "Document Type",

        [

            "Employment Contract",

            "Non-Disclosure Agreement",

            "Lease Agreement",

            "Freelance Work Contract",

            "Employment Offer Letter",

            "Service Agreement",

            "General Agreement",

            "Custom",

        ]

    )


    if document_type == "Custom":

        document_type = st.text_input(

            "Custom Document Type",

            value="General Agreement"

        )


    parties = st.text_area(

        "Parties Involved",

        placeholder=(
            "Jane Doe (Service Provider), "
            "TechNova Inc. (Client)"
        ),

        height=100

    )


    terms = st.text_area(

        "Terms & Conditions",

        placeholder=(
            "Payment within 30 days; "
            "Confidentiality must be maintained; "
            "Termination with 15 days notice"
        ),

        height=150,

        help=(
            "Separate each clause "
            "with a semicolon (;)."
        )

    )


    dates = st.date_input(

        "Effective Date",

        value=date.today()

    ).isoformat()


    jurisdiction = st.text_input(

        "Jurisdiction",

        value="Not specified"

    )


    language = st.selectbox(

        "Language",

        [

            "English",

            "Tamil",

            "Hindi",

            "Malayalam",

            "Telugu",

        ]

    )


    brand_name = st.text_input(

        "Brand Name",

        value=APP_NAME

    )


    generate_button = st.button(

        "✨ Generate Document",

        type="primary",

        use_container_width=True

    )


# ============================================================
# GENERATE DOCUMENT
# ============================================================

if generate_button:

    if not document_type.strip():

        st.error(
            "Please enter a document type."
        )

    elif not parties.strip():

        st.error(
            "Please enter the parties."
        )

    elif not terms.strip():

        st.error(
            "Please enter the terms."
        )

    else:

        payload = {

            "document_type":
                document_type,

            "parties":
                parties,

            "terms":
                terms,

            "dates":
                dates,

            "jurisdiction":
                jurisdiction,

            "language":
                language,

            "brand_name":
                brand_name,

        }


        try:

            with st.spinner(
                "Generating legal document..."
            ):

                response = requests.post(

                    f"{BACKEND_URL}/generate",

                    json=payload,

                    timeout=180

                )


            if response.ok:

                data = response.json()


                st.session_state.document_text = (
                    data["text"]
                )


                st.session_state.last_model = (
                    data.get(
                        "model",
                        ""
                    )
                )


                st.success(
                    "Document generated successfully!"
                )


            else:

                try:

                    detail = (

                        response
                        .json()
                        .get(
                            "detail",
                            response.text
                        )

                    )

                except Exception:

                    detail = response.text


                st.error(
                    f"Backend Error: {detail}"
                )


        except requests.RequestException as exc:

            st.error(

                "Cannot connect to the "
                f"FastAPI backend at "
                f"{BACKEND_URL}.\n\n"
                f"Error: {exc}"

            )


# ============================================================
# MAIN CONTENT
# ============================================================

left_column, right_column = st.columns(
    [1.1, 1]
)


# ============================================================
# EDITOR
# ============================================================

with left_column:

    st.subheader(
        "✏️ Editable Document"
    )


    st.session_state.document_text = (

        st.text_area(

            "Edit your document",

            value=(
                st.session_state.document_text
            ),

            height=560,

            label_visibility="collapsed"

        )

    )


# ============================================================
# PREVIEW
# ============================================================

with right_column:

    st.subheader(
        "👁️ Document Preview"
    )


    if st.session_state.document_text:

        safe_text = html.escape(

            st.session_state.document_text

        )


        st.markdown(

            f"""
<div class="preview">

{safe_text}

</div>
""",

            unsafe_allow_html=True

        )


        if st.session_state.last_model:

            st.caption(

                "AI Model: "
                f"{st.session_state.last_model}"

            )


    else:

        st.info(

            "Generate a document to see "
            "the live preview."

        )


# ============================================================
# DOWNLOAD
# ============================================================

st.divider()


st.subheader(
    "⬇️ Download Document"
)


terms_list = [

    item.strip()

    for item in terms.split(";")

    if item.strip()

]


download_columns = st.columns(3)


formats = [

    (

        "txt",

        "📄 Download TXT",

        "text/plain"

    ),

    (

        "docx",

        "📝 Download DOCX",

        "application/"
        "vnd.openxmlformats-officedocument."
        "wordprocessingml.document"

    ),

    (

        "pdf",

        "📕 Download PDF",

        "application/pdf"

    ),

]


for column, (

    file_format,

    button_label,

    mime_type

) in zip(

    download_columns,

    formats

):

    with column:

        if st.session_state.document_text:

            try:

                export_response = requests.post(

                    f"{BACKEND_URL}/export",

                    json={

                        "document_type":
                            document_type,

                        "text":
                            st.session_state.document_text,

                        "format":
                            file_format,

                        "terms":
                            terms_list,

                        "brand_name":
                            brand_name,

                    },

                    timeout=60

                )


                if export_response.ok:

                    st.download_button(

                        label=button_label,

                        data=(
                            export_response.content
                        ),

                        file_name=(
                            "legalease-document."
                            f"{file_format}"
                        ),

                        mime=mime_type,

                        key=(
                            f"download_{file_format}"
                        ),

                        use_container_width=True

                    )

                else:

                    try:

                        error_detail = (

                            export_response
                            .json()
                            .get(
                                "detail",
                                export_response.text
                            )

                        )

                    except Exception:

                        error_detail = (
                            export_response.text
                        )


                    st.error(

                        f"{file_format.upper()} "
                        f"export failed: "
                        f"{error_detail}"

                    )


            except requests.RequestException as exc:

                st.error(

                    f"Export failed: {exc}"

                )

        else:

            st.button(

                button_label,

                disabled=True,

                key=(
                    f"disabled_{file_format}"
                ),

                use_container_width=True

            )


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.markdown(

    """
<div class="footer">

⚖️ <strong>LegalEase</strong>
&nbsp; | &nbsp;
AI-assisted legal document drafting
&nbsp; | &nbsp;
Review important documents professionally
before use.

</div>
""",

    unsafe_allow_html=True

)