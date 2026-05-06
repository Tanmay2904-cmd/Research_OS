import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="ResearchOS", page_icon="⚡", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@300;400;500&display=swap');

:root {
    --bg:#060608; --s1:#0e0e12; --s2:#16161d; --s3:#1e1e28;
    --border:rgba(255,255,255,0.07); --border2:rgba(255,255,255,0.12);
    --p:#a78bfa; --p2:#7c3aed; --g:#34d399; --o:#fb923c;
    --text:#f0f0f8; --muted:#6b7280; --muted2:#9ca3af;
}
*,*::before,*::after{box-sizing:border-box;}
html,body,[class*="css"],.stApp{font-family:'Space Grotesk',sans-serif!important;background:var(--bg)!important;color:var(--text)!important;}
.stApp{background:var(--bg)!important;background-image:radial-gradient(ellipse 120% 60% at 50% -10%,rgba(124,58,237,0.13) 0%,transparent 60%),radial-gradient(ellipse 80% 50% at 90% 90%,rgba(52,211,153,0.04) 0%,transparent 50%)!important;min-height:100vh;}
#MainMenu,footer,header,.stDeployButton{visibility:hidden!important;}
section[data-testid="stSidebar"]{display:none;}
.block-container{padding:0 2.5rem 5rem!important;max-width:1000px!important;}

/* topbar */
.topbar{display:flex;align-items:center;justify-content:space-between;padding:1.5rem 0 1rem;border-bottom:1px solid var(--border);margin-bottom:3.5rem;}
.logo{display:flex;align-items:center;gap:10px;}
.logo-icon{width:32px;height:32px;background:linear-gradient(135deg,var(--p2),var(--p));border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:16px;}
.logo-name{font-size:1.1rem;font-weight:700;letter-spacing:-0.02em;color:var(--text);}
.logo-name span{color:var(--p);}
.nav-pills{display:flex;gap:6px;}
.nav-pill{font-family:'JetBrains Mono',monospace;font-size:0.68rem;padding:4px 10px;border-radius:100px;border:1px solid var(--border2);color:var(--muted2);background:var(--s1);}

/* hero — all inline, no h1/p tags to avoid Streamlit override */
.eyebrow{display:inline-flex;align-items:center;gap:8px;font-family:'JetBrains Mono',monospace;font-size:0.68rem;letter-spacing:0.15em;text-transform:uppercase;color:var(--p);border:1px solid rgba(167,139,250,0.25);padding:6px 14px;border-radius:100px;margin-bottom:1.8rem;background:rgba(167,139,250,0.06);}
.eyebrow::before{content:'';width:6px;height:6px;border-radius:50%;background:var(--p);animation:blink 2s infinite;}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0.2}}
.hero-title{font-family:'Space Grotesk',sans-serif;font-size:clamp(2.8rem,6vw,4.5rem);font-weight:700;line-height:1.05;letter-spacing:-0.04em;color:#f0f0f8;margin-bottom:1.2rem;}
.hero-title em{font-style:normal;background:linear-gradient(135deg,#a78bfa,#c4b5fd);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.hero-sub{font-family:'Space Grotesk',sans-serif;font-size:1rem;color:#9ca3af;max-width:460px;margin:0 auto 2rem;line-height:1.75;font-weight:300;}
.agent-chain{display:inline-flex;align-items:center;background:var(--s1);border:1px solid var(--border2);border-radius:100px;padding:5px 7px;margin-bottom:2.5rem;}
.achip{font-family:'JetBrains Mono',monospace;font-size:0.69rem;padding:4px 11px;border-radius:100px;color:var(--muted2);}
.achip.on{background:rgba(167,139,250,0.12);color:var(--p);border:1px solid rgba(167,139,250,0.25);}
.aarrow{color:var(--muted);font-size:0.75rem;padding:0 2px;}

/* input */
.stTextInput>div>div{background:var(--s1)!important;border:1px solid var(--border2)!important;border-radius:14px!important;padding:0.9rem 1.3rem!important;font-family:'Space Grotesk',sans-serif!important;font-size:1rem!important;color:var(--text)!important;transition:all 0.2s!important;}
.stTextInput>div>div:focus-within{border-color:rgba(167,139,250,0.45)!important;box-shadow:0 0 0 4px rgba(167,139,250,0.08)!important;}
.stTextInput>div>div>input{color:var(--text)!important;background:transparent!important;}
.stTextInput>div>div>input::placeholder{color:var(--muted)!important;}
.stTextInput label{display:none!important;}
div[data-testid="stHorizontalBlock"]{align-items:flex-end!important;gap:10px!important;}

/* button */
.stButton>button{background:linear-gradient(135deg,var(--p2),var(--p))!important;color:#fff!important;border:none!important;border-radius:12px!important;padding:0.88rem 1.5rem!important;font-family:'Space Grotesk',sans-serif!important;font-size:0.92rem!important;font-weight:600!important;width:100%!important;transition:all 0.15s!important;}
.stButton>button:hover{transform:translateY(-2px)!important;box-shadow:0 8px 24px rgba(124,58,237,0.3)!important;}
.stButton>button:active{transform:translateY(0)!important;}

.hdiv{height:1px;background:var(--border);margin:2rem 0;}

/* pipeline */
.ph-label{font-family:'JetBrains Mono',monospace;font-size:0.68rem;letter-spacing:0.12em;text-transform:uppercase;color:var(--muted);margin-bottom:0.8rem;}
.step-row{display:flex;align-items:center;gap:14px;padding:0.9rem 1.1rem;border-radius:11px;border:1px solid var(--border);background:var(--s1);margin-bottom:7px;transition:all 0.3s;}
.step-row.sa{border-color:rgba(167,139,250,0.35);background:rgba(167,139,250,0.05);}
.step-row.sd{border-color:rgba(52,211,153,0.28);background:rgba(52,211,153,0.04);}
.snum{font-family:'JetBrains Mono',monospace;font-size:0.72rem;width:26px;height:26px;border-radius:7px;display:flex;align-items:center;justify-content:center;background:var(--s2);border:1px solid var(--border2);color:var(--muted);flex-shrink:0;}
.step-row.sa .snum{background:rgba(167,139,250,0.18);border-color:rgba(167,139,250,0.45);color:var(--p);}
.step-row.sd .snum{background:rgba(52,211,153,0.18);border-color:rgba(52,211,153,0.38);color:var(--g);}
.sinfo{flex:1;}
.sname{font-size:0.86rem;font-weight:600;color:var(--muted2);}
.step-row.sa .sname,.step-row.sd .sname{color:var(--text);}
.sdesc{font-family:'JetBrains Mono',monospace;font-size:0.68rem;color:var(--muted);margin-top:2px;}
.stag{font-family:'JetBrains Mono',monospace;font-size:0.66rem;}
.step-row.sa .stag{color:var(--p);}
.step-row.sd .stag{color:var(--g);}

/* results */
.sec-label{display:flex;align-items:center;gap:9px;margin:2rem 0 0.9rem;}
.sec-dot{width:7px;height:7px;border-radius:50%;}
.sec-txt{font-family:'JetBrains Mono',monospace;font-size:0.69rem;letter-spacing:0.1em;text-transform:uppercase;color:var(--muted2);}

.rcard{background:var(--s1);border:1px solid var(--border2);border-radius:14px;overflow:hidden;margin-bottom:1rem;}
.rcard-top{display:flex;align-items:center;justify-content:space-between;padding:0.9rem 1.3rem;border-bottom:1px solid var(--border);background:var(--s2);}
.rcard-title{font-size:0.84rem;font-weight:600;color:var(--text);}
.rcard-badge{font-family:'JetBrains Mono',monospace;font-size:0.63rem;padding:3px 9px;border-radius:100px;background:rgba(167,139,250,0.1);color:var(--p);border:1px solid rgba(167,139,250,0.22);}
.rcard-body{padding:1.6rem 1.8rem;font-size:0.91rem;line-height:1.85;color:#c0c0d0;}

/* Streamlit markdown inside rcard-body */
.rcard-body p{color:#c0c0d0;font-size:0.91rem;line-height:1.85;margin-bottom:0.6rem;}
.rcard-body strong{color:var(--text);font-weight:600;}
.rcard-body a{color:var(--p)!important;text-decoration:underline;}
.rcard-body ul,.rcard-body ol{padding-left:1.4rem;margin:0.5rem 0;}
.rcard-body li{margin-bottom:0.35rem;color:#c0c0d0;}

/* Fix Streamlit injected markdown headings inside rcard-body */
.rcard-body [data-testid="stMarkdownContainer"] h1{font-family:'Space Grotesk',sans-serif!important;font-size:1.3rem!important;font-weight:700!important;color:var(--text)!important;margin:1.4rem 0 0.5rem!important;letter-spacing:-0.02em!important;}
.rcard-body [data-testid="stMarkdownContainer"] h2{font-family:'Space Grotesk',sans-serif!important;font-size:1.05rem!important;font-weight:600!important;color:var(--text)!important;margin:1.2rem 0 0.5rem!important;border-bottom:1px solid var(--border);padding-bottom:0.35rem;}
.rcard-body [data-testid="stMarkdownContainer"] h3{font-family:'Space Grotesk',sans-serif!important;font-size:0.92rem!important;font-weight:600!important;color:var(--p)!important;margin:1rem 0 0.4rem!important;}
.rcard-body [data-testid="stMarkdownContainer"] p{color:#c0c0d0!important;font-size:0.91rem!important;line-height:1.85!important;}
.rcard-body [data-testid="stMarkdownContainer"] a{color:var(--p)!important;}
.rcard-body [data-testid="stMarkdownContainer"] li{color:#c0c0d0!important;}

.ccard{background:var(--s1);border:1px solid rgba(251,146,60,0.2);border-radius:14px;overflow:hidden;margin-bottom:1rem;}
.ccard-top{display:flex;align-items:center;padding:0.9rem 1.3rem;border-bottom:1px solid rgba(251,146,60,0.12);background:rgba(251,146,60,0.04);}
.ccard-title{font-size:0.84rem;font-weight:600;color:var(--text);}
.ccard-badge{font-family:'JetBrains Mono',monospace;font-size:0.63rem;padding:3px 9px;border-radius:100px;background:rgba(251,146,60,0.1);color:var(--o);border:1px solid rgba(251,146,60,0.22);margin-left:auto;}
.ccard-body{padding:1.4rem 1.8rem;font-family:'JetBrains Mono',monospace;font-size:0.8rem;line-height:1.85;color:#c0c0d0;white-space:pre-wrap;}

.done-bar{display:flex;align-items:center;gap:12px;padding:0.9rem 1.3rem;background:rgba(52,211,153,0.05);border:1px solid rgba(52,211,153,0.18);border-radius:11px;margin-bottom:0.5rem;}
.done-icon{width:28px;height:28px;border-radius:50%;background:rgba(52,211,153,0.12);border:1px solid rgba(52,211,153,0.28);display:flex;align-items:center;justify-content:center;font-size:13px;flex-shrink:0;}
.done-txt{font-size:0.86rem;font-weight:600;color:var(--g);}
.done-sub{font-family:'JetBrains Mono',monospace;font-size:0.67rem;color:var(--muted2);margin-top:1px;}

details{background:var(--s1)!important;border:1px solid var(--border)!important;border-radius:11px!important;margin-bottom:7px!important;}
summary{font-family:'JetBrains Mono',monospace!important;font-size:0.73rem!important;color:var(--muted2)!important;padding:0.85rem 1.1rem!important;cursor:pointer!important;}

.stDownloadButton>button{background:var(--s2)!important;color:var(--muted2)!important;border:1px solid var(--border2)!important;border-radius:11px!important;font-family:'JetBrains Mono',monospace!important;font-size:0.76rem!important;padding:0.72rem 1.4rem!important;width:100%!important;transition:all 0.2s!important;}
.stDownloadButton>button:hover{color:var(--text)!important;background:var(--s3)!important;}
</style>
""", unsafe_allow_html=True)

# TOP BAR
st.markdown("""
<div class="topbar">
    <div class="logo">
        <div class="logo-icon">⚡</div>
        <div class="logo-name">Research<span>OS</span></div>
    </div>
    <div class="nav-pills">
        <div class="nav-pill">LangGraph</div>
        <div class="nav-pill">Tavily</div>
        <div class="nav-pill">Groq · Llama 3.3</div>
    </div>
</div>
""", unsafe_allow_html=True)

# HERO — using divs with inline styles, NOT h1/p (Streamlit overrides those)
st.markdown("""
<div style="text-align:center; padding:0 0 3rem;">
    <div class="eyebrow">Multi-Agent Research Pipeline</div>
    <div class="hero-title">
        Research at the<br>speed of <em>thought</em>
    </div>
    <div class="hero-sub">
        Four AI agents search, scrape, write and critique —<br>
        delivering a full research report in seconds.
    </div>
    <div class="agent-chain">
        <div class="achip on">🔍 Search</div>
        <div class="aarrow">›</div>
        <div class="achip on">📄 Scrape</div>
        <div class="aarrow">›</div>
        <div class="achip on">✍️ Write</div>
        <div class="aarrow">›</div>
        <div class="achip on">🧠 Critique</div>
    </div>
</div>
""", unsafe_allow_html=True)

# INPUT
col1, col2 = st.columns([5, 1], gap="small")
with col1:
    topic = st.text_input("t", placeholder="Enter any research topic — e.g. Quantum computing breakthroughs 2025", label_visibility="collapsed")
with col2:
    st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
    run_btn = st.button("⚡ Run", use_container_width=True)

st.markdown('<div class="hdiv"></div>', unsafe_allow_html=True)

# STEP RENDERER
STEPS = [
    ("01", "Search Agent",  "Tavily live web search"),
    ("02", "Reader Agent",  "BeautifulSoup URL scrape"),
    ("03", "Writer Chain",  "Structured report draft"),
    ("04", "Critic Chain",  "Quality evaluation & score"),
]

def render_pipeline(active, done):
    st.markdown('<div class="ph-label">// pipeline status</div>', unsafe_allow_html=True)
    for i, (num, name, desc) in enumerate(STEPS):
        if i < done:
            cls, tag, icon = "sd", "✓ complete", "✓"
        elif i == active:
            cls, tag, icon = "sa", "● running...", num
        else:
            cls, tag, icon = "", "○ waiting", num
        st.markdown(f"""
        <div class="step-row {cls}">
            <div class="snum">{icon}</div>
            <div class="sinfo">
                <div class="sname">{name}</div>
                <div class="sdesc">{desc}</div>
            </div>
            <div class="stag">{tag}</div>
        </div>""", unsafe_allow_html=True)

# RUN
if run_btn:
    if not topic.strip():
        st.warning("Enter a research topic to begin.")
        st.stop()

    steps_ph = st.empty()
    status_ph = st.empty()
    results = {}

    try:
        with steps_ph.container(): render_pipeline(0, 0)
        status_ph.info("🔍 Search Agent querying Tavily...")
        from agents import build_search_agent
        sa = build_search_agent()
        sr = sa.invoke({"messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]})
        results["search"] = sr['messages'][-1].content

        with steps_ph.container(): render_pipeline(1, 1)
        status_ph.info("📄 Reader Agent scraping top resource...")
        from agents import build_reader_agent
        ra = build_reader_agent()
        rr = ra.invoke({"messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{results['search'][:800]}")]})
        results["scraped"] = rr['messages'][-1].content

        with steps_ph.container(): render_pipeline(2, 2)
        status_ph.info("✍️ Writer Chain drafting report...")
        from agents import writer_chain
        combined = f"SEARCH RESULTS:\n{results['search']}\n\nDETAILED SCRAPED CONTENT:\n{results['scraped']}"
        results["report"] = writer_chain.invoke({"topic": topic, "research": combined})

        with steps_ph.container(): render_pipeline(3, 3)
        status_ph.info("🧠 Critic Chain evaluating...")
        from agents import critic_chain
        results["feedback"] = critic_chain.invoke({"report": results["report"]})

        with steps_ph.container(): render_pipeline(-1, 4)
        status_ph.empty()

    except Exception as e:
        status_ph.error(f"Pipeline error: {e}")
        st.stop()

    # RESULTS
    st.markdown('<div class="hdiv"></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="done-bar">
        <div class="done-icon">✓</div>
        <div>
            <div class="done-txt">Research complete</div>
            <div class="done-sub">topic: {topic}</div>
        </div>
    </div>""", unsafe_allow_html=True)

    report_text = results["report"] if isinstance(results["report"], str) else str(results["report"])
    feedback_text = results["feedback"] if isinstance(results["feedback"], str) else str(results["feedback"])

    # Report
    st.markdown("""
    <div class="sec-label">
        <div class="sec-dot" style="background:#a78bfa"></div>
        <div class="sec-txt">// Final Report</div>
    </div>
    <div class="rcard">
        <div class="rcard-top">
            <div class="rcard-title">Research Report</div>
            <div class="rcard-badge">Writer Agent · Groq</div>
        </div>
    </div>""", unsafe_allow_html=True)

    with st.container():
        st.markdown(f'<div class="rcard-body">', unsafe_allow_html=True)
        st.markdown(report_text)
        st.markdown('</div>', unsafe_allow_html=True)

    # Critic
    st.markdown(f"""
    <div class="sec-label">
        <div class="sec-dot" style="background:#fb923c"></div>
        <div class="sec-txt">// Critic Feedback</div>
    </div>
    <div class="ccard">
        <div class="ccard-top">
            <div class="ccard-title">Quality Assessment</div>
            <div class="ccard-badge">Critic Agent</div>
        </div>
        <div class="ccard-body">{feedback_text}</div>
    </div>""", unsafe_allow_html=True)

    # Raw
    st.markdown("""
    <div class="sec-label">
        <div class="sec-dot" style="background:#4b5563"></div>
        <div class="sec-txt">// Raw Agent Data</div>
    </div>""", unsafe_allow_html=True)
    with st.expander("🔍  Raw Search Results"):
        st.code(results["search"], language=None)
    with st.expander("📄  Scraped Content"):
        st.code(results["scraped"], language=None)

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)
    full_output = f"# Research Report: {topic}\n\n{report_text}\n\n---\n\n## Critic Feedback\n\n{feedback_text}"
    st.download_button(
        label="⬇  Download Full Report (.txt)",
        data=full_output,
        file_name=f"research_{topic[:30].replace(' ','_')}.txt",
        mime="text/plain",
        use_container_width=True,
    )