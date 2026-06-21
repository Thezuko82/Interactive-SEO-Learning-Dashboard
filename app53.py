import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(
    page_title="Interactive SEO Learning Dashboard",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Interactive SEO Learning Dashboard")
st.markdown("Learn SEO concepts through interactive demonstrations.")

# Sidebar Navigation
topic = st.sidebar.selectbox(
    "Select Topic",
    [
        "1 Search Engine Working Process",
        "2 Keyword Research using SEO Tools",
        "3 Competitor Analysis",
        "4 On-Page SEO Optimization",
        "5 Technical SEO Basics",
        "6 SEO Audit Process",
        "7 Local SEO & Google Business Profile",
        "8 Link Building Basics",
        "9 SEO Reporting"
    ]
)

# ==========================================================
# 1 Search Engine Working Process
# ==========================================================

if topic == "1 Search Engine Working Process":

    st.header("Search Engine Working Process")

    st.markdown("""
    ### Search Engine Workflow

    1. Crawling
    2. Indexing
    3. Ranking
    4. Displaying Results
    """)

    stage = st.select_slider(
        "Select Stage",
        options=["Crawling", "Indexing", "Ranking", "Results"]
    )

    if stage == "Crawling":
        st.info("Bots discover webpages and follow links.")
    elif stage == "Indexing":
        st.info("Pages are stored in search engine databases.")
    elif stage == "Ranking":
        st.info("Algorithms determine page relevance.")
    elif stage == "Results":
        st.info("SERP results are displayed to users.")

# ==========================================================
# 2 Keyword Research
# ==========================================================

elif topic == "2 Keyword Research using SEO Tools":

    st.header("Keyword Research Simulator")

    keywords = pd.DataFrame({
        "Keyword": ["SEO", "SEO Course", "SEO Training Delhi",
                    "Best SEO Institute Delhi", "Digital Marketing Course"],
        "Search Volume": [120000, 30000, 8000, 3000, 45000],
        "Difficulty": [90, 70, 55, 40, 80]
    })

    st.dataframe(keywords)

    fig = px.scatter(
        keywords,
        x="Search Volume",
        y="Difficulty",
        text="Keyword",
        size="Search Volume",
        title="Keyword Opportunity Matrix"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Look for high volume and low difficulty keywords.")

# ==========================================================
# 3 Competitor Analysis
# ==========================================================

elif topic == "3 Competitor Analysis":

    st.header("Competitor Analysis Dashboard")

    competitor = pd.DataFrame({
        "Website": ["Your Site", "Competitor A", "Competitor B"],
        "Keywords": [120, 350, 290],
        "Backlinks": [800, 2500, 1900],
        "Domain Authority": [30, 60, 55]
    })

    st.dataframe(competitor)

    fig = px.bar(
        competitor,
        x="Website",
        y=["Keywords", "Backlinks"],
        barmode="group",
        title="Competitor Comparison"
    )

    st.plotly_chart(fig)

# ==========================================================
# 4 On-Page SEO
# ==========================================================

elif topic == "4 On-Page SEO Optimization":

    st.header("On-Page SEO Analyzer")

    title = st.text_input("Page Title")
    description = st.text_area("Meta Description")

    score = 0

    if len(title) >= 30 and len(title) <= 60:
        score += 50

    if len(description) >= 120 and len(description) <= 160:
        score += 50

    st.metric("SEO Score", score)

    if score == 100:
        st.success("Excellent On-Page SEO")
    else:
        st.warning("Optimize title and description.")

# ==========================================================
# 5 Technical SEO
# ==========================================================

elif topic == "5 Technical SEO Basics":

    st.header("Technical SEO Checklist")

    mobile = st.checkbox("Mobile Friendly")
    ssl = st.checkbox("HTTPS Enabled")
    sitemap = st.checkbox("XML Sitemap")
    robots = st.checkbox("Robots.txt Available")

    total = sum([mobile, ssl, sitemap, robots])

    st.progress(total / 4)

    st.metric("Technical SEO Score", total * 25)

# ==========================================================
# 6 SEO Audit
# ==========================================================

elif topic == "6 SEO Audit Process":

    st.header("SEO Audit Tool")

    audit_items = {
        "Title Tags": False,
        "Meta Description": False,
        "Broken Links": False,
        "Mobile Friendly": False,
        "Page Speed": False,
        "Backlinks": False,
        "Sitemap": False
    }

    completed = 0

    for item in audit_items:
        if st.checkbox(item):
            completed += 1

    percentage = int((completed / len(audit_items)) * 100)

    st.metric("Audit Completion", f"{percentage}%")

# ==========================================================
# 7 Local SEO
# ==========================================================

elif topic == "7 Local SEO & Google Business Profile":

    st.header("Local SEO Learning")

    city = st.text_input("Enter City")

    if city:

        st.success(f"""
        Local SEO Checklist for {city}

        ✓ Create Google Business Profile
        ✓ Add Photos
        ✓ Collect Reviews
        ✓ Add NAP Information
        ✓ Use Local Keywords
        """)

# ==========================================================
# 8 Link Building
# ==========================================================

elif topic == "8 Link Building Basics":

    st.header("Link Building Simulator")

    guest_posts = st.slider("Guest Posts", 0, 20, 5)
    directories = st.slider("Business Directories", 0, 20, 5)
    blogs = st.slider("Blog Outreach", 0, 20, 5)

    backlinks = guest_posts * 3 + directories + blogs * 2

    st.metric("Estimated Backlinks", backlinks)

    st.info("""
    Effective Link Building Methods:
    - Guest Posting
    - Resource Pages
    - Broken Link Building
    - Digital PR
    - Blog Outreach
    """)

# ==========================================================
# 9 SEO Reporting
# ==========================================================

elif topic == "9 SEO Reporting":

    st.header("SEO Reporting Dashboard")

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

    report = pd.DataFrame({
        "Month": months,
        "Organic Traffic": [1200, 1500, 1700, 2100, 2600, 3100],
        "Keywords Ranked": [40, 55, 70, 95, 120, 145]
    })

    st.dataframe(report)

    fig1 = px.line(
        report,
        x="Month",
        y="Organic Traffic",
        markers=True,
        title="Organic Traffic Growth"
    )

    st.plotly_chart(fig1)

    fig2 = px.line(
        report,
        x="Month",
        y="Keywords Ranked",
        markers=True,
        title="Keyword Ranking Growth"
    )

    st.plotly_chart(fig2)

    st.success("SEO reports help track performance and ROI.")