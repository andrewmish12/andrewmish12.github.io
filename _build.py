"""Builds the static site from content.py.  Run:  python3 _build.py  (from the site folder)"""
import os, sys, html
sys.path.insert(0, os.path.dirname(__file__))
from _content import PROFILE, STATS, CATS, STATUS, PROJECTS, EDUCATION, HONORS, SKILLS

ROOT = os.path.dirname(os.path.abspath(__file__))
CSS = open(os.path.join(os.path.dirname(__file__), "_style.css")).read()
E = html.escape

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&family=Public+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400&display=swap" rel="stylesheet">')

JS = """<script>
document.documentElement.classList.add('js');
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});
document.querySelectorAll('.rv').forEach(el=>io.observe(el));
document.querySelectorAll('[data-filter]').forEach(b=>b.addEventListener('click',()=>{
 document.querySelectorAll('[data-filter]').forEach(x=>x.classList.toggle('on',x===b));
 const f=b.dataset.filter;document.querySelectorAll('.card').forEach(c=>{c.style.display=(f==='all'||c.dataset.cat===f)?'':'none'})}));
const mb=document.querySelector('.menu-btn');if(mb)mb.addEventListener('click',()=>document.body.classList.toggle('nav-open'));
</script>"""

def head(title, desc):
    return (f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
            f'<title>{E(title)}</title><meta name="description" content="{E(desc)}">'
            f'<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:image" content="andrew.jpg">'
            f'<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 64 64%22%3E%3Crect width=%2264%22 height=%2264%22 rx=%2214%22 fill=%22%230b0d12%22/%3E%3Ctext x=%2232%22 y=%2242%22 font-family=%22monospace%22 font-size=%2226%22 font-weight=%22700%22 text-anchor=%22middle%22 fill=%22%23ffffff%22%3EAM%3C/text%3E%3C/svg%3E">'
            f'{FONTS}<style>{CSS}</style></head><body>')

def nav(home=False):
    p = "" if home else "index.html"
    return (f'<header class="nav"><a class="logo" href="index.html">Andrew Mish</a>'
            f'<button class="menu-btn" aria-label="Menu">☰</button><nav>'
            f'<a href="{p}#work">Work</a><a href="{p}#experience">Experience</a><a href="{p}#about">About</a><a href="{p}#contact" class="nav-cta">Contact</a></nav></header>')

def footer():
    return (f'<footer id="contact"><div class="wrap foot"><div><p class="mono dim">Contact</p><h2>Let\'s build something.</h2>'
            f'<p class="dim">Internships, partnerships, or if you just want to argue about an idea. I\'m in.</p></div>'
            f'<div class="foot-links"><a href="tel:{PROFILE["phone_tel"]}">{PROFILE["phone"]} ↗</a><a href="mailto:{PROFILE["email"]}">{PROFILE["email"]} ↗</a><a href="{PROFILE["linkedin"]}" target="_blank" rel="noopener">LinkedIn ↗</a>'
            f'<a href="{PROFILE["github"]}" target="_blank" rel="noopener">GitHub ↗</a></div></div>'
            f'<div class="wrap mono dim small foot-bottom"><span>© 2026 Andrew Mish</span><span>Auburn, AL · Odenton, MD</span></div></footer>{JS}</body></html>')

def chip(status):
    lab, cls = STATUS[status]
    return f'<span class="status {cls}"><i></i>{lab}</span>'

# ------------------------------------------------------------------ demo panels
def flow(nodes, caption):
    items = '<span class="arrow">→</span>'.join(f'<div class="fnode"><span class="mono small dim">{E(a)}</span><b>{E(b)}</b></div>' for a, b in nodes)
    return f'<figure class="panel"><div class="flow">{items}</div><figcaption>{caption}</figcaption></figure>'

def demo(kind):
    if not kind: return ""
    if kind == "pipeline_ss":
        return flow([("input", "Forms & Sheets"), ("logic", "Apps Script"), ("ai", "Claude API"), ("output", "PDFs · Slack · Dashboards")],
                    "The basic shape of most things I build at SilverStay. Shown as a diagram, with no real data.")
    if kind == "pipeline_trades":
        return flow([("every 6h", "House disclosures"), ("parse", "PDF + OCR"), ("model", "Target weights"), ("human", "Email → I approve")],
                    "Nothing trades without a human saying yes.")
    if kind == "survey_easy":
        rows = [("Re-wear clothes before washing", 76.2), ("…and have \"in-between\" clothes", 86.2), ("Put them on a chair", 46.3), ("Put them on the floor", 45.5)]
        bars = "".join(f'<div class="bar"><span>{E(l)}</span><div class="track"><div class="fill" style="--w:{v}%"></div></div><b>{v}%</b></div>' for l, v in rows)
        return f'<figure class="panel"><p class="mono small dim">survey · n = 323</p>{bars}<figcaption>Real results from our market survey.</figcaption></figure>'
    if kind == "sms_barber":
        return ('<figure class="panel split"><div class="phone"><div class="bubble in">yo can i get a fade friday after 3? – marcus</div>'
                '<div class="bubble out">Got it! We\'ll check availability and confirm your appointment shortly.</div></div>'
                '<pre class="code"><span class="c">// what Claude hands back</span>\n{\n  <k>"name"</k>: <s>"Marcus"</s>,\n  <k>"requested_date"</k>: <s>"Friday"</s>,\n  <k>"requested_time"</k>: <s>"after 3"</s>,\n  <k>"service"</k>: <s>"fade"</s>,\n  <k>"intent"</k>: <s>"new_booking"</s>,\n  <k>"confidence"</k>: <s>"high"</s>\n}</pre>'
                '<figcaption>An example text and the structured output. The bot replies based on <code>intent</code>.</figcaption></figure>')
    if kind == "verdict_prereq":
        return ('<figure class="panel"><div class="ask mono">Does <b>COURSE 1234</b> count toward my core requirement?</div>'
                '<div class="verdict"><span class="vtag">COUNTS</span><p>Listed under the core requirement in the current Bulletin. You have no conflicting credit on file.</p>'
                '<p class="mono small dim">source → Auburn Bulletin, core curriculum rule</p></div>'
                '<figcaption>Mockup of the answer card. The rules engine makes the call; the AI only explains it.</figcaption></figure>')
    if kind == "phone_dining":
        items = [("Grilled Chicken Bowl", "520 cal", "42g protein"), ("Turkey Wrap", "430 cal", "31g protein"), ("Egg White Scramble", "260 cal", "24g protein")]
        li = "".join(f'<li><b>{a}</b><span>{b} · <em>{c}</em></span></li>' for a, b, c in items)
        return (f'<figure class="panel split"><div class="phone"><div class="ph-top mono small"><span>For You</span><span class="dim">Today</span></div>'
                f'<div class="ph-card"><p class="mono small dim">where to go · 6 min walk</p><h5>The Edge</h5><ul class="menu">{li}</ul></div></div>'
                f'<div class="tabs mono small"><span class="on">Menus</span><span>For You</span><span>Schedule</span><span>Profile</span><p class="dim">Rebuilt around 4 tabs after v1 got too crowded.</p></div>'
                f'<figcaption>Illustrative mockup. Real screenshots coming soon.</figcaption></figure>')
    if kind == "ring_sweat":
        return ('<figure class="panel split"><svg viewBox="0 0 120 120" class="ring"><circle cx="60" cy="60" r="48" class="r-bg"/><circle cx="60" cy="60" r="48" class="r-fg" style="--p:.71"/>'
                '<text x="60" y="58" text-anchor="middle" class="r-num">5/7</text><text x="60" y="76" text-anchor="middle" class="r-lab">this week</text></svg>'
                '<div class="iou"><p class="mono small dim">monday scoring</p><p><b>Missed goal → IOU created</b></p><p class="dim">Partner picks: ☕ coffee · $10 · 💐 flowers · custom</p><p class="mono small">claim → confirm → (dispute)</p></div>'
                '<figcaption>Illustrative mockup of the weekly ring and IOU flow.</figcaption></figure>')
    if kind == "funnel_ideas":
        rows = [("Screened", 90, 100), ("Worth a second look", 17, 19), ("Survived", 5, 6)]
        f = "".join(f'<div class="frow"><span>{a}</span><div class="track"><div class="fill" style="--w:{w}%"></div></div><b>{n}</b></div>' for a, n, w in rows)
        return f'<figure class="panel"><p class="mono small dim">idea funnel</p>{f}<figcaption>Most ideas should die early. That\'s the point.</figcaption></figure>'
    return ""

# ------------------------------------------------------------------ pages
def card(p, i):
    if p.get("wide"):
        st = "".join(f'<div><b>{a}</b><span>{E(b)}</span></div>' for a, b in p.get("results", [])[:4])
        hl = "".join(f'<li><b>{E(a)}</b>{E(b)}</li>' for a, b in p["highlights"])
        logo = f'<img class="clogo" src="{p["logo"]}" alt="{E(p["title"])} logo">' if p.get("logo") else ""
        return (f'<a class="card wide rv" data-cat="{p["cat"]}" href="{p["slug"]}.html">'
                f'<div><div class="card-top"><span class="mono small dim">{CATS[p["cat"]]} · {E(p["when"])}</span>{chip(p["status"])}</div>'
                f'{logo}<h3>{E(p["title"])}</h3><p class="mono small dim">{E(p["role"])}</p><p class="lede">{E(p["kicker"])}</p>'
                f'<div class="wide-stats">{st}</div><div class="tags">{"".join(f"<span>{E(s)}</span>" for s in p["stack"])}</div>'
                f'<p class="go mono" style="margin-top:16px">Read the full breakdown →</p></div>'
                f'<ul class="hl">{hl}</ul></a>')
    return (f'<a class="card rv" data-cat="{p["cat"]}" href="{p["slug"]}.html" style="--d:{(i%3)*70}ms">'
            f'<div class="card-top"><span class="mono small dim">{CATS[p["cat"]]} · {E(p["when"])}</span>{chip(p["status"])}</div>'
            f'<h3>{E(p["title"])}</h3><p>{E(p["card"])}</p>'
            f'<div class="tags">{"".join(f"<span>{E(s)}</span>" for s in p["stack"][:4])}</div><span class="go mono">Read more →</span></a>')

def home():
    feats = [p for p in PROJECTS if p["cat"] != "job"]
    jobs = [p for p in PROJECTS if p["cat"] in ("work", "job")]
    chips = '<button class="on" data-filter="all">All</button>' + "".join(
        f'<button data-filter="{k}">{v}</button>' for k, v in CATS.items() if k != "job" and any(p["cat"] == k for p in feats))
    stats = "".join(f'<div class="stat rv" style="--d:{i*80}ms"><b>{a}</b><span>{E(b)}</span></div>' for i, (a, b) in enumerate(STATS))
    timeline = "".join(
        f'<a class="tl rv" href="{p["slug"]}.html"><span class="mono small dim">{E(p["when"])}</span><div><h4>{E(p["title"])}</h4><p class="dim">{E(p["role"])}</p><p>{E(p["card"])}</p></div><span class="go mono">→</span></a>'
        for p in jobs)
    edu = "".join(f'<div class="edu"><h4>{E(a)}</h4><p class="dim">{E(b)}</p><span class="mono small dim">{E(c)}</span></div>' for a, b, c in EDUCATION)
    hon = "".join(f"<li>{E(h)}</li>" for h in HONORS)
    sk = "".join(f'<div><p class="mono small dim">{E(k)}</p><div class="tags">{"".join(f"<span>{E(x)}</span>" for x in v)}</div></div>' for k, v in SKILLS.items())
    body = f'''{nav(True)}
<section class="hero wrap">
 <div class="hero-txt">
  <p class="mono dim boot">LLM Implementation Engineer · Founder · Auburn University</p>
  <h1>I'm Andrew.<br><span class="grad">I build things that actually get used.</span></h1>
  <p class="lead">AI tools a hospital team runs on every day, apps I built because I needed them, and a running list of 100+ business ideas I'm working through. This site has all of it, with how each one works and my honest take on how it went.</p>
  <div class="cta"><a class="btn" href="#work">See the work</a><a class="btn ghost" href="mailto:{PROFILE["email"]}">Email me</a></div>
 </div>
 <div class="hero-img"><img src="andrew.jpg" alt="Andrew Mish"><div class="tag-now mono small"><i></i>Now: SilverStay · Auburn</div></div>
</section>
<section class="wrap stats">{stats}</section>
<section id="work" class="wrap sec">
 <div class="sec-head"><p class="mono dim">Portfolio</p><h2>Everything I've built</h2><p class="dim">Every project gets its own page with what it is, how it works, and what I'd do differently.</p></div>
 <div class="filters mono">{chips}</div>
 <div class="grid">{"".join(card(p, i) for i, p in enumerate(feats))}</div>
</section>
<section id="experience" class="wrap sec">
 <div class="sec-head"><p class="mono dim">Experience</p><h2>Where I've worked</h2></div>
 <div class="timeline">{timeline}</div>
</section>
<section id="about" class="wrap sec about">
 <div class="sec-head"><p class="mono dim">About</p><h2>The short version</h2></div>
 <div class="about-grid">
  <div class="about-txt rv"><p>I'm a freshman at Auburn studying business (intended finance, with a real estate minor). Before that I spent four years in PLTW engineering at Archbishop Spalding, which is where I got hooked on taking an idea from my head into the real world.</p>
  <p>At 17 I started at SilverStay building AI tools for hospital discharge teams, and I haven't stopped building since. I care less about credentials and more about whether the thing works and whether people use it.</p>
  <p>Outside of that: golf (2 years varsity, and one hole-in-one in a school match), guitar and piano, the gym, and whatever app I'm currently building.</p></div>
  <div class="about-side rv"><p class="mono small dim">education</p>{edu}<p class="mono small dim" style="margin-top:1.6rem">honors</p><ul class="honors">{hon}</ul></div>
 </div>
 <div class="skills rv">{sk}</div>
</section>
{footer()}'''
    return head("Andrew Mish — Builder, LLM Engineer, Founder", "Andrew Mish's portfolio: AI tools, apps, engineering projects and business ventures.") + body

def project(p, i):
    order = PROJECTS
    prev, nxt = order[i - 1], order[(i + 1) % len(order)]
    spec = (f'<div class="spec mono small"><div><span class="dim">status</span>{chip(p["status"])}</div><div><span class="dim">when</span>{E(p["when"])}</div>'
            f'<div><span class="dim">role</span>{E(p["role"])}</div><div><span class="dim">stack</span><span class="tags">{"".join(f"<span>{E(s)}</span>" for s in p["stack"])}</span></div></div>')
    secs = "".join(f'<section class="psec rv"><h2>{E(h)}</h2>{b}</section>' for h, b in p["sections"])
    res = ""
    if p.get("results"):
        res = '<div class="results rv">' + "".join(f'<div><b>{a}</b><span>{E(b)}</span></div>' for a, b in p["results"]) + "</div>"
    d = demo(p.get("demo"))
    d = f'<section class="psec rv"><h2>See it</h2>{d}</section>' if d else ""
    links = ""
    if p.get("links"):
        links = '<div class="plinks">' + "".join(f'<a href="{u}" target="_blank" rel="noopener">{E(t)} ↗</a>' for t, u in p["links"]) + "</div>"
    nexts = f'<section class="psec rv"><h2>What\'s next</h2>{p["next"]}</section>' if p.get("next") else ""
    body = f'''{nav()}
<article class="wrap proj">
 <p class="mono dim crumb"><a href="index.html">Home</a> &nbsp;/&nbsp; {CATS[p["cat"]]}</p>
 {f'<img class="plogo" src="{p["logo"]}" alt="{E(p["title"])} logo">' if p.get("logo") else ""}<h1>{E(p["title"])}</h1>
 <p class="lead">{E(p["kicker"])}</p>
 {spec}{res}
 <div class="pbody">{secs}{d}
  <section class="psec honest rv"><p class="mono small">My honest take</p>{p["honest"]}</section>
  {nexts}{links}
 </div>
 <nav class="pn mono"><a href="{prev["slug"]}.html">← {E(prev["title"])}</a><a href="index.html#work">all work</a><a href="{nxt["slug"]}.html">{E(nxt["title"])} →</a></nav>
</article>
{footer()}'''
    return head(f'{p["title"]} — Andrew Mish', p["kicker"]) + body

if __name__ == "__main__":
    open(os.path.join(ROOT, "index.html"), "w").write(home())
    for i, p in enumerate(PROJECTS):
        open(os.path.join(ROOT, p["slug"] + ".html"), "w").write(project(p, i))
    print("built", 1 + len(PROJECTS), "pages")
