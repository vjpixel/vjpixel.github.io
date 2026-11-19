"""One-off generator: writes the English static pages of the portfolio site."""
import sys
from pathlib import Path

OUT = Path(sys.argv[1])

NAV = [
    ("index.html", "Home"),
    ("experience.html", "Experience"),
    ("projects.html", "Projects"),
    ("talks.html", "Talks"),
    ("recognition.html", "Recognition"),
    ("about.html", "About"),
    ("index.html#contact", "Contact"),
]

LINKEDIN = "https://www.linkedin.com/in/vjpixel/"
GITHUB = "https://github.com/vjpixel"
SITE = "https://vjpixel.github.io/"


def page(fname, title, desc, body):
    nav = "\n".join(
        '          <li><a href="{0}"{2}>{1}</a></li>'.format(
            href, label, ' aria-current="page"' if href == fname else ""
        )
        for href, label in NAV
    )
    canonical = SITE + ("" if fname == "index.html" else fname)
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{canonical}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{SITE}assets/images/angelo-pixel.jpg" />
  <meta name="theme-color" content="#06090c" />
  <meta name="color-scheme" content="dark" />
  <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Crect width='16' height='16' fill='%2306090c'/%3E%3Crect x='4' y='4' width='8' height='8' fill='%2322d3ee'/%3E%3C/svg%3E" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
  <header class="site-header">
    <div class="container">
      <a class="brand" href="index.html"><span class="brand-mark" aria-hidden="true"></span>Angelo <span>Pixel</span></a>
      <nav aria-label="Main">
        <ul class="nav-links" id="nav-links">
{nav}
        </ul>
      </nav>
      <button type="button" class="nav-toggle" aria-controls="nav-links" aria-expanded="false">Menu</button>
    </div>
  </header>

  <main>
{body}
  </main>

  <footer class="site-footer">
    <div class="container">
      <p class="footer-note">&copy; 2026 Angelo Pixel.</p>
      <ul class="footer-links">
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
      </ul>
    </div>
  </footer>

  <script src="js/main.js"></script>
</body>
</html>
"""
    assert "—" not in html, fname
    (OUT / fname).write_text(html, encoding="utf-8", newline="\n")


def hero(eyebrow, h1, lede="", width="22ch", extra=""):
    lede_html = f'\n        <p class="lede">{lede}</p>' if lede else ""
    return f"""    <section class="hero hero-tight">
      <div class="container">
        <p class="eyebrow">{eyebrow}</p>
        <h1 style="max-width: {width};">{h1}</h1>{lede_html}{extra}
      </div>
    </section>
"""


def stats(items):
    cells = "\n".join(
        f"""        <div class="stat">
          <span class="num">{n}</span>
          <span class="label">{l}</span>
        </div>"""
        for n, l in items
    )
    return f"""    <section class="container">
      <div class="stat-strip">
{cells}
      </div>
    </section>
"""


def cards(items, linked=False):
    out = []
    for it in items:
        if linked:
            href, h, p = it
            ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
            out.append(
                f"""          <a class="teaser-card" href="{href}"{ext}>
            <h3>{h}</h3>
            <p>{p}</p>
            <span class="arrow" aria-hidden="true">&rarr;</span>
          </a>"""
            )
        else:
            pre, h, p = it
            pre_html = f'\n            <span class="timeline-period">{pre}</span>' if pre else ""
            out.append(
                f"""          <div class="teaser-card">{pre_html}
            <h3>{h}</h3>
            <p>{p}</p>
          </div>"""
            )
    return '        <div class="teaser-grid">\n' + "\n".join(out) + "\n        </div>"


def recog(items, cols4=False):
    cls = "recognition-grid cols-4" if cols4 else "recognition-grid"
    cells = "\n".join(
        f"""          <div class="recognition-item">
            <span class="year">{y}</span>
            <p>{b}</p>
          </div>"""
        for y, b in items
    )
    return f'        <div class="{cls}">\n{cells}\n        </div>'


def section(inner, alt=False, head=None, lede=None, narrow=False, flush=False):
    cls = "section section-alt" if alt else "section"
    style = ' style="padding-top: 0;"' if flush else ""
    cstyle = ' style="max-width: 72ch;"' if narrow else ""
    head_html = ""
    if head:
        lede_html = f'\n          <p class="lede">{lede}</p>' if lede else ""
        head_html = f"""        <div class="section-head">
          <h2>{head}</h2>{lede_html}
        </div>
"""
    return f"""    <section class="{cls}"{style}>
      <div class="container"{cstyle}>
{head_html}{inner}
      </div>
    </section>
"""


def timeline(items):
    out = []
    for period, role, org, summary, bullets, parallel in items:
        cls = "timeline-item is-parallel" if parallel else "timeline-item"
        lis = "\n".join(f"              <li>{b}</li>" for b in bullets)
        ul = f"\n            <ul>\n{lis}\n            </ul>" if bullets else ""
        org_html = f'\n            <span class="org">{org}</span>' if org else ""
        out.append(
            f"""          <div class="{cls}">
            <span class="timeline-period">{period}</span>
            <h3>{role}</h3>{org_html}
            <p>{summary}</p>{ul}
          </div>"""
        )
    return '        <div class="timeline">\n' + "\n".join(out) + "\n        </div>"


def case(tag, title, blocks, images=None, reverse=False, link=None, cid=None):
    cls = "case-study"
    media = ""
    if images:
        if reverse:
            cls += " reverse"
        imgs = "\n".join(
            f'              <img src="assets/images/{src}" alt="{alt}" loading="lazy" />'
            for src, alt in images
        )
        if len(images) == 1:
            media = f"""          <div class="case-media single">
{imgs}
          </div>
"""
        else:
            media = f"""          <div class="case-media">
            <div class="gallery">
{imgs}
            </div>
          </div>
"""
    else:
        cls += " no-media"
    bl = "\n".join(
        f"""              <div class="case-block">
                <h4>{h}</h4>
                <p>{p}</p>
              </div>"""
        for h, p in blocks
    )
    link_html = ""
    if link:
        links = link if isinstance(link, list) else [link]
        anchors = " &nbsp;&middot;&nbsp; ".join(
            f'<a href="{href}" target="_blank" rel="noopener">{label} &rarr;</a>' for href, label in links
        )
        link_html = f'\n            <p class="case-link">{anchors}</p>'
    id_attr = f' id="{cid}"' if cid else ""
    return f"""        <article{id_attr} class="{cls}">
{media}          <div class="case-copy">
            <span class="case-tag">{tag}</span>
            <h3>{title}</h3>
            <div class="case-blocks">
{bl}
            </div>{link_html}
          </div>
        </article>"""


def mosaic(items):
    cells = "\n".join(
        f"""          <div class="mosaic-item">
            <img src="assets/images/{src}" alt="{cap}" loading="lazy" />
            <p class="mosaic-caption">{cap}</p>
          </div>"""
        for src, cap in items
    )
    return f'        <div class="mosaic-grid">\n{cells}\n        </div>'


def channel(href, label, note, shown):
    return f"""          <li>
            <a href="{href}" target="_blank" rel="noopener">
              <span>
                <span>{label}</span><br />
                <span class="channel-label">{note}</span>
              </span>
              <span>{shown}</span>
            </a>
          </li>"""


contact_block = section(
    '        <ul class="contact-list" style="max-width: 60ch;">\n' + "\n".join([
        channel(LINKEDIN, "LinkedIn", "Full career history and recommendations", "linkedin.com/in/vjpixel"),
        channel(GITHUB, "GitHub", "Open-source code and experiments", "github.com/vjpixel"),
        channel("https://diar.ia.br", "diar.ia.br", "The AI newsletter I publish every weekday", "diar.ia.br"),
        channel("https://jandig.app/", "Jandig", "The AR platform I founded", "jandig.app"),
    ]) + "\n        </ul>",
    head="Contact",
    lede="About product, AI, open source, or where they meet. The fastest way to reach me is a LinkedIn message.",
).replace('<section class="section"', '<section id="contact" class="section"', 1)

# ------------------------------------------------------------------ HOME
home = f"""    <section class="hero hero-home">
      <div class="container hero-grid">
        <div class="hero-copy">
        <p class="eyebrow">Senior Product Manager &middot; AI, APIs and data products</p>
        <h1>I take products from zero to measurable business impact.</h1>
        <p class="lede">
          Senior Product Manager with 10+ years building AI, XR and data-driven products,
          at Amazon, AutoNation and in products of my own. Today I run a daily AI
          newsletter produced by a pipeline of AI agents that I built.
        </p>
        <div class="btn-row">
          <a class="btn btn-primary" href="experience.html">See my experience</a>
          <a class="btn btn-secondary" href="projects.html">See my projects</a>
        </div>
        </div>
        <figure class="hero-photo">
          <img src="assets/images/angelo-pixel.jpg" alt="Portrait of Angelo Pixel" width="1335" height="2000" />
        </figure>
      </div>
    </section>

{stats([
    ("USD 11MM", "yearly profit increase at Amazon Brazil from Spider, an API product I led"),
    ("587%", "peak lift in fee-based revenue at AutoNation after rebuilding the fee system"),
    ("40", "specialized AI agents in the pipeline that produces diar.ia.br every weekday"),
    ("150K+", "people reached each month by diar.ia.br, across its own and partner audiences"),
])}
{section(recog([
    ("Anthropic &middot; 2026", "Selected for the Claude for Open Source Program."),
    ("United Nations &middot; 2024", "Invited to represent Brazil at the OSPOs for Good Symposium."),
    ("Mozilla &middot; 2018", "Open Source Support Award for Jandig."),
    ("Google &middot; 2014", "Impact Challenge award for Rede InfoAmazonia."),
], cols4=True), head="Recognized by")}
{section(cards([
    ("projects.html#diaria", "diar.ia.br Studio",
     "A public multi-agent pipeline on Claude Code that takes each newsletter edition from research to scheduling."),
    ("projects.html#spider", "Spider at Amazon",
     "An internal API product I took from prototype to product, with a three-year plan and 4.5x more impact in a year."),
    ("projects.html#jandig", "Jandig",
     "An open-source augmented reality platform, awarded by Mozilla and used by artists, educators and NGOs."),
    ("projects.html#jeo", "Jeo",
     "An open-source geojournalism platform for WordPress, adopted by newsrooms on three continents."),
], linked=True), alt=True, head="Selected work",
   lede="Products I led inside companies, and products I started from nothing. Each one is a case study.")}
{contact_block}"""
page("index.html", "Angelo Pixel | Senior Product Manager, AI and data products",
     "Senior Product Manager with 10+ years building AI, XR and data-driven products at Amazon, AutoNation and InfoAmazonia. Founder of diar.ia.br and Jandig.",
     home)

# ------------------------------------------------------------ EXPERIENCE
jobs = [
    ("07/2025 to present", "Founder and Editor", "diar.ia.br",
     'Weekday AI newsletter in Portuguese (<a href="https://diar.ia.br" target="_blank" rel="noopener">diar.ia.br</a>).',
     ['Built <a href="https://github.com/vjpixel/diaria-studio" target="_blank" rel="noopener">diar.ia.br Studio</a>, a public production pipeline on Claude Code that takes each edition from research to scheduling in six stages, with human review at two of them.',
      "Orchestrate 40 specialized AI agents and 44 skills, integrated with 20+ external APIs and 8 MCP servers.",
      "Automated the work previously done by a team member.",
      "Reach 150,000+ people a month across the newsletter's own audience and partner audiences."], False),
    ("10/2023 to 02/2025", "Senior Product Manager", "Software Mind / AutoNation",
     "AutoNation is the largest and most recognized automotive retailer in the USA.",
     ["Rebuilt the fee system from hardcoded logic into a fully configurable, self-serve dashboard, letting business teams launch and adjust fees without engineering, lifting fee-based revenue by up to 587%.",
      "Redesigned the fee flow end-to-end (quote to invoice), improving accuracy and cutting manual work.",
      "Led the Mobile Service's Partner API from zero to the first customer."], False),
    ("01/2022 to 01/2023", "Technical Product Manager II", "Amazon",
     "A global technology leader in e-commerce, cloud computing, and logistics.",
     ["Led Spider, an API product that increased Amazon Brazil's yearly profitability by USD 11MM.",
      "Created a vision and a three-year plan, evolving Spider from prototype to product.",
      "Developed and prioritized the roadmap, increasing Spider's impact by 4.5 times in one year.",
      "Spearheaded the Innovation Pipeline, an initiative focused on crowdsourcing and validating ideas for new products."], False),
    ("10/2020 to 12/2021", "Product Manager", "Stefanini Manufacturing",
     "Industrial maintenance-focused subsidiary of the Stefanini group.",
     ["Led the discovery of Watchtower, an AI product for industrial maintenance, leading a diverse team of five (developer, data scientist, sales, marketing, and UX designer).",
      "Saved company resources that would have been spent on product development by advising the C-level to discontinue the product for technical and commercial reasons.",
      "Eliminated a two-month delivery delay within one week of taking over the development management of another product through backlog prioritization."], False),
    ("10/2009 to 09/2020", "Founder", "memeLab",
     "Independent open-source XR lab, run alongside the roles below.",
     ["Led product and development for 10+ open-source products across mixed reality (Meta Quest), desktop, and mobile.",
      'Created and pitched the <a href="https://jandig.app/" target="_blank" rel="noopener">Jandig</a> XR platform at MozFest (London), winning a Mozilla Seed Award. Jandig is now used by artists, educators, and NGOs internationally.',
      "Secured grant funding and managed 50+ projects across Europe, North and South America."], True),
    ("03/2013 to 12/2016", "Head of Product and Technology", "InfoAmazonia",
     "Independent media outlet that uses maps, data, and geolocalized reports to tell stories about the Amazon region.",
     ["Changed business strategy and built a highly productive and lean team, implementing agile practices to improve the speed of development and product quality, increasing revenue by 80% within a year.",
      "Launched five products and led two existing ones, achieving up to a 400% increase in pageviews in one year.",
      "Conceived and led the development of Jeo, an open-source geojournalism platform for WordPress adopted by newsrooms on three continents.",
      "Conceived and led the IoT platform Rede InfoAmazonia, one of the 10 projects among 800+ that received funding from Google Impact Challenge Brazil 2014."], False),
]
skills = [
    ("AI and ML", "Generative AI, AI Agents, Multi-agent Systems, Prompt Engineering, MCP (Model Context Protocol), Machine Learning, n8n"),
    ("Product", "Product Discovery, Roadmapping, User Stories, Product Owner, A/B Testing, Agile / Scrum, SaaS, Mobile Apps &amp; PWA"),
    ("Technical and data", "Python, SQL, JavaScript, JSON, CI/CD, Google Analytics"),
    ("Tools", "Jira, Confluence, Figma, Miro"),
]
skills_html = "\n".join(
    f"""        <h3 class="tag-heading">{label}</h3>
        <ul class="tag-list">
{chr(10).join(f'          <li>{s.strip()}</li>' for s in items.split(','))}
        </ul>"""
    for label, items in skills
)
exp = (
    hero("Experience", "Product roles with numbers attached.",
         "Ten-plus years in product, across media, industrial maintenance, e-commerce and automotive retail. "
         "The pink dot marks memeLab, the open-source lab I ran in parallel for eleven years.",
         width="20ch")
    + section(timeline(jobs) + f"""
        <div class="btn-row" style="margin-top: var(--space-4);">
          <a class="btn btn-secondary" href="{LINKEDIN}" target="_blank" rel="noopener">Full history on LinkedIn</a>
          <a class="btn btn-secondary" href="recognition.html">Awards and press</a>
          <a class="btn btn-secondary" href="talks.html">Talks</a>
        </div>""", flush=True)
    + section(skills_html, alt=True, head="Skills")
    + section(cards([
        ("2020 to 2021", "AI Product Manager", "Nanodegree, Udacity."),
        ("2001 to 2004", "Computer Science", "UniRuy Wyden. Completed 88% of the degree credits."),
    ]) + """
        <p class="fineprint">Certificates and courses: Google Prompting Essentials (2025); Generative AI for Startups (2025); A/B Testing (2023); Communication and Influence (2023); Microsoft Certified: Azure AI Fundamentals (2021); Data Analytics for Business Professionals (2021); Learning Agility (2021); Product Discovery (2021); Certified Lean Inception Facilitator (2021); Product Management (2020); Open Leadership (2018).</p>""",
        head="Education")
)
page("experience.html", "Experience | Angelo Pixel",
     "Product roles at Amazon, AutoNation, Stefanini Manufacturing and InfoAmazonia, plus diar.ia.br and memeLab.",
     exp)

# -------------------------------------------------------------- PROJECTS
company_cases = "\n\n".join([
    case("Amazon / API product", "Spider", [
        ("Problem", "Amazon's supply chain software was built for the United States, where sales tax is added on top of the price. In Brazil, tax is part of the price, so it is a cost to the company, and it changes from state to state. The systems were miscalculating what it cost to ship a product from each warehouse."),
        ("My role", "When I joined, Spider was a project that touched a single supply chain system. I was hired to turn it into a product: an API that other systems consult to get that calculation right."),
        ("What I did", "Wrote the product vision and a three-year plan, and PRFAQs for new features. Created a discovery framework and KPIs, and used the metrics to find new opportunities, such as better caching and new transfer routes. The product depended on many stakeholders, so I set up one communication mechanism per audience, from a short monthly report for leadership to weekly meetings with the direct team, aligning operations, business, tax, finance and technology."),
        ("Outcome", "Spider increased Amazon Brazil's yearly profitability by USD 11MM, and its impact grew 4.5 times in one year. What I took from it: a product vision does most of the work of aligning stakeholders."),
    ], cid="spider"),
    case("AutoNation / Internal platform", "Configurable fee system", [
        ("Problem", "The fees charged by AutoNation's mobile service were hardcoded. Launching or changing a fee required engineering work."),
        ("My role", "It started as a single task. I interviewed stakeholders and grew it into a product vision. Having worked with tax at Amazon helped me make the case to leadership."),
        ("What I did", "Designed a fee model that finance configures without code. A fee can apply to a whole repair order, a repair or a component; be a fixed amount or a percentage of the total, of labor or of parts; and follow rules by state, customer type, partner and validity dates. Permissions follow roles: finance creates fees, account managers assign them to fleets, and operations adjusts them on an order. I also wrote the role-based training, the launch announcement and the demo."),
        ("Outcome", "Launched in January 2025. Business teams now launch and adjust fees on their own, and fee-based revenue rose by up to 587%. On the same team I led the Mobile Service Partner API from zero to its first customer, including how quotes are exposed to partners: fully quoted, a price range, or pending."),
    ], cid="fees"),
    case("Stefanini Manufacturing / AI product discovery", "Watchtower", [
        ("Problem", "Watchtower was a proposed AI product for industrial maintenance. My job was discovery: find out whether the problem was real and whether the company could build a product that solved it."),
        ("My role", "Product manager leading a team of five (developer, data scientist, sales, marketing and UX designer), presenting the status to C-level executives every month."),
        ("What I did", "Ran nine months of discovery. Tested demand with landing pages and ads from the first week. Interviewed maintenance teams, which led us to pivot the problem we were solving. Wrote a product vision, ran a Lean Inception and designed an MVP simpler than first planned. Studied the market and the competition."),
        ("Outcome", "The discovery showed that a competitive product needed an AI accuracy that depends on a volume of data the company did not have, in a market filling up with cheaper solutions. The product was discontinued before it was built, saving the cost of developing it."),
    ], cid="watchtower"),
])

proj_cases = "\n\n".join([
    case("AI agents / Open source", "diar.ia.br Studio", [
        ("My role", "Founder and editor of diar.ia.br, a weekday AI newsletter in Portuguese. I designed and built the pipeline that produces it."),
        ("Product", "A public production pipeline on Claude Code that takes each edition from research to scheduling in six stages, with human review at two of them. Each edition reviews about 300 articles and publishes nine, and goes out at 6 a.m., Monday to Friday."),
        ("How it works", "40 specialized AI agents and 44 skills, integrated with 20+ external APIs and 8 MCP servers. Built in TypeScript on Node, with typecheck, unit tests and an end-to-end smoke test on every pull request."),
        ("Outcomes", "Automated the work previously done by a team member. The newsletter reaches 150,000+ people a month across its own audience and partner audiences."),
    ], images=[
        ("diaria/diaria-01-edition-cover.jpg", "Cover illustration of a diar.ia.br edition"),
    ], link=[("https://github.com/vjpixel/diaria-studio", "Code on GitHub"), ("https://diar.ia.br", "diar.ia.br")], cid="diaria"),
    case("Augmented reality / Open source", "Jandig", [
        ("My role", "I started Jandig in 2011: researched its feasibility, negotiated the first two exhibitions, and ran weekly meetings with a small group that built the app, the website and an open call for digital artworks. In 2018 I pitched it at MozFest in London, winning a Mozilla Seed Award. I still lead product, community and technical coordination."),
        ("Product", "An open-source augmented reality platform for people who do not code. It runs in a standard mobile browser, with no app to install, and a first-time user takes about 12 minutes to publish a work."),
        ("Evolution", 'The first marker was pasted in November 2011. Low-cost phones of the time could not keep up, so the team paused the project and resumed it in 2017. The platform launched in 2019. In 2025 we began a mixed reality viewer for Meta Quest, first shown at Mozilla Festival in Barcelona. <a href="talks.html">See the talks</a>.'),
        ("Outcomes", "More than 7,200 active users in the 12 months to July 2026. Used in a Rosas de Ouro carnival parade in S&atilde;o Paulo at the invitation of USP, by more than 200 UEMG students over three years, and in a Sesc arts circuit across nine cities. Mozilla Open Source Support Award and Software Livres Culturais award (2018). Selected by Anthropic for the Claude for Open Source Program (2026)."),
    ], images=[
        ("jandig/jandig-04-brazilian-myths-mixed-reality.jpg", "Outdoor AR sculpture of a creature from Brazilian folklore"),
        ("jandig/jandig-05-mozilla-festival-barcelona.jpg", "People trying a mixed reality headset at Mozilla Festival in Barcelona"),
        ("jandig/jandig-01-exposicao-janelas-digitais.jpg", "The Janelas Digitais exhibition with AR markers"),
        ("jandig/jandig-03-intervencao-urbana-poste.jpg", "Urban intervention with AR stickers on a lamp post"),
    ], link=[("https://jandig.app/", "jandig.app"), ("https://github.com/memeLab/Jandig", "Code on GitHub")], cid="jandig"),
    case("Geojournalism / Open-source platform", "Jeo", [
        ("My role", "InfoAmazonia already existed when I joined: I was hired as a consultant to diagnose its platform and propose improvements. From that work I conceived Jeo, made the case for building it, and led its development, later heading product and technology with a team of designers, engineers and data analysts."),
        ("Product", "An open-source geojournalism platform for WordPress: news stories geo-referenced on maps. It grew out of the system behind InfoAmazonia, which aggregates news in Portuguese, Spanish and English from partners and the public."),
        ("Evolution", "Before, InfoAmazonia ran on a manual Jekyll-based system that generated static content published straight to a Git repository, without even a search box. With no budget to maintain a proprietary platform long term, I proposed an open-source WordPress theme and a community around it, so that the cost of maintenance would be shared. That became Jeo."),
        ("Outcomes", "InfoAmazonia's pageviews grew by up to 400% in one year. In its first year, Jeo was forked by 10 developers and gave rise to five new geojournalism platforms. I coordinated its adaptation for newsrooms on three continents, including Ekuatorial (Indonesia), LandQuest (Kenya) and Oxpeckers (South Africa); InfoNile (Nile Basin) adopted it later. It is still maintained as a WordPress plugin, and InfoAmazonia still runs on it."),
    ], images=[
        ("jeo/jeo-01-infoamazonia-home-2015.jpg", "InfoAmazonia home page in 2015, built on Jeo"),
    ], reverse=True, link=("https://github.com/InfoAmazonia/jeo-plugin", "Jeo on GitHub"), cid="jeo"),
    case("Open hardware / IoT", "Rede InfoAmazonia", [
        ("My role", "The idea was mine. I presented it to the InfoAmazonia team, led the proposal submitted to Google, planned the project, hired the team, managed hardware and software development, led the test deployment and managed the partnerships."),
        ("Product", "M&atilde;e d'&Aacute;gua, an open-source, modular device that measures water quality every hour (pH, ORP, conductivity and temperature) and sends the data over the mobile network. The software was designed for three audiences: an API for developers, a web interface with history for scientists, and SMS alerts for communities. The device cost under USD 2,000 when the cheapest commercial equipment for real-time monitoring cost more than USD 4,000."),
        ("Evolution", "One of the 10 projects funded among 800+ applicants to Google Impact Challenge Brazil 2014. A specialist told me that giving communities a direct verdict on their water was not feasible, so I changed the scope: the sensors raise an alert, and a partner university laboratory tests the water. In late 2015, the communities themselves installed the equipment at 18 points in three cities in Par&aacute;; two more went to S&atilde;o Paulo."),
        ("Outcomes", "The Google funding sustained the project for two years. The technology was used in research at six Brazilian public universities and institutes and in a master's thesis, and it inspired groups in Spain and China to build their own open-source water monitors. I was invited to present it at open science events in Brazil, Chile, China and the USA."),
    ], images=[
        ("rede/rede-01-mae-dagua-sensor.jpg", "M&atilde;e d'&Aacute;gua sensor number 2 installed on a water tank"),
        ("rede/rede-02-site-sensor-map.jpg", "Rede InfoAmazonia website with the map of sensors around Santar&eacute;m"),
        ("rede/rede-03-pedra-branca-water-tower.jpg", "Community water tower at Pedra Branca, one of the monitored sites"),
        ("rede/rede-04-site-water-supply.jpg", "Map of access to water supply in the Amazon states on the project website"),
    ], link=[("https://github.com/InfoAmazonia/rede-hardware", "Hardware on GitHub"), ("https://youtu.be/4t60jJCaQEM", "Video")], cid="rede"),
])

more_projects = cards([
    ("2019 to today", "X-Reality USP",
     "A festival of extended reality at the University of S&atilde;o Paulo, born from a partnership I proposed between USP and London's Raindance festival. I have been one of its curators since the first edition, and on the opening panel of every edition: 2019, 2021, 2022, 2024 and 2026."),
    ("2025 to 2026", "Extended Mythology",
     'Brazilian myths such as Curupira and Saci retold in mixed reality as socio-environmental warnings, with an educational kit. Funded by S&atilde;o Paulo\'s ProAC program, it produced Jandig\'s open-source viewer for Meta Quest. <a href="https://jandig.app/me/" target="_blank" rel="noopener">jandig.app/me</a>'),
    ("2017", "AdvoHelp",
     "A legal-tech startup with an app that finds, in real time, a lawyer who is already at the courthouse. As CTO, I led the proposal that took it into the Lemonade pre-accelerator, where it won the Best Team award."),
    ("2015", "Rede C&oacute;digo Urbano",
     'Built during the Red Bull Basement hacker residency: a platform that brings air and water monitoring together, drawing on my earlier sensor projects. <a href="https://github.com/vjpixel/rcu" target="_blank" rel="noopener">Code on GitHub</a>'),
    ("2014", "Chronica Mobilis",
     "A geolocated interactive performance with game dynamics, created by a team of Brazilian and Spanish artists during a residency at Hangar, in Barcelona. Teams in the streets and at a base rebuild a character's memories."),
    ("2012 to 2013", "Incubadora",
     "A theater play in which the audience steers the narrative from their phones. memeLab directed the technology and built the app."),
    ("2011", "Photolink",
     "Photos sent by the public, projected as a mosaic by 24 projectors along more than 100 meters at S&atilde;o Paulo's Virada Cultural."),
    ("2004 to 2010", "Public-sector digital inclusion",
     "Brazilian federal and state programs: Cultura Digital at the Ministry of Culture, Casa Brasil, Territ&oacute;rios Digitais and AcessaSP. I helped design projects and coordinated technology teams and workshops in several states."),
])

proj = (
    hero("Projects", "Case studies, from Amazon to open source.",
         "The problem, what I decided and what came of it. Company cases leave out confidential figures: "
         'the numbers shown are the ones on my r&eacute;sum&eacute;, in <a href="experience.html">Experience</a>.',
         width="20ch")
    + section(company_cases, flush=True, head="Product work at companies")
    + section(proj_cases, alt=True, head="Products I started")
    + section(more_projects, head="More projects")
    + section(mosaic([
        ("memelab/memelab-01-narrative-navigation-app.jpg", "Narrative Navigation, an augmented reality app for urban wayfinding, created in a residency at NIMk in Amsterdam"),
        ("memelab/memelab-02-nowhere-everywhere-installation.jpg", "Coordenadas 31 15'15.53 N, 24 15'30.53 O (2019), a 360&deg; short film shown at festivals in France, Peru and Brazil"),
        ("memelab/memelab-03-new-old-games-pacman-projection.jpg", "New/Old Games, a giant projected Pac-Man controlled by body movement"),
        ("memelab/memelab-04-goodnight-sleep-tight-performance.jpg", "Good Night, Sleep Tight, a virtual reality performance by ZU-UK, for which memeLab directed the 360&deg; video"),
        ("memelab/memelab-05-festival-x-reality-vr-headset.jpg", "VR headset demo at the X-Reality festival"),
        ("memelab/memelab-06-mostra-clipes-360-marte-festival.jpg", "360&deg; video showcase at Festival MARTE"),
    ]) + """
        <div class="btn-row" style="margin-top: var(--space-3);">
          <a class="btn btn-secondary" href="talks.html">See talks</a>
          <a class="btn btn-secondary" href="recognition.html">See awards and press</a>
        </div>""", alt=True, head="memeLab experiments",
        lede="memeLab, the extended reality lab I ran from 2009 to 2020, produced 10+ experiments across AR, VR and MR. A few records:")
)
page("projects.html", "Projects | Angelo Pixel",
     "Case studies: Spider at Amazon, the AutoNation fee system, Watchtower, diar.ia.br Studio, Jandig, Jeo and Rede InfoAmazonia.",
     proj)

# ----------------------------------------------------------------- TALKS
press = [
    ("https://youtu.be/kpJGMomXe-U", "TEDx Talks, 2013", "Redescobrindo Games: VJ Pixel at TEDxSalvador (video)"),
    ("https://blog.mozilla.org/en/mozilla/moss-2018-year-in-review/", "Mozilla Blog, 2019", "MOSS 2018 year in review, listing Jandig among the seed awards"),
    ("", "Circuito Sesc de Artes, 2019", "Realidades aut&ocirc;nomas tempor&aacute;rias, on Jandig's tour of S&atilde;o Paulo state"),
    ("https://desafiosocial.withgoogle.com/brazil2014/charity/associacao-o-eco", "Google Impact Challenge Brazil, 2014", "Project page for Rede InfoAmazonia, by Associa&ccedil;&atilde;o O Eco"),
    ("https://ijnet.org/en/story/journalism-reloaded-buenos-aires-media-party", "IJNet, 2013", "On the Buenos Aires Media Party, where VJ Pixel showed MapPress"),
    ("https://www.select.art.br/do-artista-ao-articulador/", "Revista Select, 2012", "Do artista ao articulador"),
    ("https://www.select.art.br/jandig-culturadigitalbr/", "Revista Select, 2011", "Jandig #CulturaDigitalBR"),
    ("https://www.vice.com/en/article/memelab-fly-the-flag-of-freedom-through-open-source", "VICE, 2011", "Profile of memeLab and VJ Pixel"),
    ("", "Correio Braziliense, 2010", "Full-page interview: &quot;Brasil investe pouco em softwares livres&quot; (print)"),
]
press_html = '        <ul class="press-list">\n' + "\n".join(
    (f'          <li><span class="press-source">{src}</span> <a href="{href}" target="_blank" rel="noopener">{title}</a></li>'
     if href else f'          <li><span class="press-source">{src}</span> <span>{title}</span></li>')
    for href, src, title in press
) + "\n        </ul>"

talks = (
    """    <section class="hero hero-tight hero-talks">
      <div class="container hero-grid">
        <div class="hero-copy">
        <p class="eyebrow">Talks</p>
        <h1>Twenty-four years of stages, VJ booths and classrooms.</h1>
        <p class="lede">From free software and VJing to internationally awarded augmented reality.</p>
        </div>
        <figure class="hero-figure">
          <img src="assets/images/talks/talks-01-sao-paulo-innovation-week-2026.jpg" alt="Angelo Pixel speaking on stage at S&atilde;o Paulo Innovation Week" width="1000" height="1250" />
          <figcaption>S&atilde;o Paulo Innovation Week, 2026. Photo: Bruna Quevedo.</figcaption>
        </figure>
      </div>
    </section>
"""
    + stats([
        ("150+", "talks and workshops since 2002"),
        ("4", "continents where I have presented work"),
        ("4", "artist residencies abroad (Netherlands, Spain, UK, Colombia)"),
        ("TEDx", 'TEDx Salvador, 2013: &quot;Redescobrindo Games&quot; (<a href="https://youtu.be/kpJGMomXe-U" target="_blank" rel="noopener">watch the talk</a>)'),
    ])
    + section(cards([
        ("May 2026 &middot; S&atilde;o Paulo, Brazil", "S&atilde;o Paulo Innovation Week",
         "Panel &quot;XR Futures: Games, Art, and the Expansion of Immersive Worlds&quot;, with Almir Almas (USP) and Ana Arruda (XR curator), moderated by Daniel Lima."),
        ("Nov 2025 &middot; Barcelona, Spain", "Mozilla Festival",
         "The installation &quot;Jandig - Brazilian Myths in Mixed Reality&quot;, accepted by the festival committee: the first public demo of Jandig's mixed reality viewer."),
        ("Jul 2024 &middot; New York, USA", "OSPOs for Good, United Nations",
         "Invited to the two-day symposium on open source at the UN Headquarters in New York, selected by a committee for a history of open collaboration and innovation."),
        ("Since 2019 &middot; S&atilde;o Paulo, Brazil", "X-Reality USP",
         "Creator and curator of the festival, in partnership with the Raindance Film Festival, with editions in 2019, 2021, 2022, 2024 and 2026. I have been on the opening panel of every edition. For Festival MARTE I curated a showcase of 360&deg; music videos in partnership with X-Reality."),
        ("Nov 2018 &middot; London, UK", "Mozilla Festival",
         "Pitched Jandig at the Mozilla Festival and received the Mozilla Open Source Support Award."),
        ("Aug 2013 &middot; Buenos Aires, Argentina", "Hacks/Hackers Media Party",
         "The talk &quot;The EcoLab, bringing innovation to environmental reporting&quot; and the workshop &quot;Using Jeo to create your own mapping platform&quot;."),
        ("Mar 2012 &middot; Amsterdam, Netherlands", "NIMk, Netherlands Media Art Institute",
         "The talk &quot;Narrative navigation&quot;, during an artist residency."),
        ("2009 and 2010 &middot; New York, USA", "Open Video Conference",
         "Joined the discussions in 2009 and came back in 2010 for the panel &quot;Open Video in Brazil&quot;."),
        ("Mar 2010 &middot; Montevideo, Uruguay", "Campamento Latinoamericano de J&oacute;venes Activistas Sociales",
         "A talk on free video."),
        ("Feb 2009 &middot; Bangalore, India", "Info-Activism Camp",
         "Workshops on video editing and on compressing and encoding video."),
    ]), head="Highlights")
    + section(timeline([
        ("2013 to 2014", "Data journalism and open hardware", "",
         "The TEDx Salvador talk &quot;Redescobrindo Games&quot;; Jeo workshops and three moderated debates on journalism and technology at Campus Party; a DustDuino workshop at an environmental journalists' meeting hosted at Google in San Francisco.", [], False),
        ("2012", "Jandig's busiest year", "",
         "The talk &quot;Jandig: art in augmented reality&quot; and the panel &quot;Copyleft Cities&quot; at FISL (Porto Alegre); the SESC Sorocaba opening as an exhibiting artist (&quot;VideoPong&quot;, &quot;Electro-Organic Experiments&quot;); Campus Party; Circuito Vivo Arte.mov.", [], False),
        ("2009 to 2011", "Info-activism and VJing", "",
         "Three sessions at FISL 11 in Porto Alegre, including the founding debate of the Free Video Alliance, and Campus Party in S&atilde;o Paulo.", [], False),
        ("2002 to 2008", "Free-software beginnings", "",
         "First talk in September 2002, in Salvador. A professional VJ career (2002 to 2018, &quot;retired&quot; after a performance in China); talks and workshops at FISL, Latinoware, the World Social Forum, and the Brazilian Digital Culture Forum.", [], False),
    ]), alt=True, head="Two decades on stage")
    + section(mosaic([
        ("jandig/jandig-02-instalacao-360-marcadores.jpg", "A 360&deg; circular installation covered in AR markers"),
        ("jandig/jandig-06-carnaval-rosas-de-ouro.jpg", "Carnival: an AR intervention in the Rosas de Ouro parade"),
        ("jandig/jandig-07-narrativas-territoriais-ouro-preto.jpg", "Urban intervention in Ouro Preto (Territorial Narratives)"),
        ("jandig/jandig-08-exposicao-itinerante-sesc.jpg", "Jandig's traveling exhibit at a SESC cultural center"),
        ("jandig/jandig-09-criancas-cubos-ra.jpg", "Kids playing with AR marker cubes at a traveling workshop"),
        ("jandig/jandig-10-colecao-remexe-grupo.jpg", "Remexe collection: upcycled clothing tagged with AR markers"),
        ("jandig/jandig-11-campus-party-palestra.jpg", "A talk on stage at Campus Party"),
        ("jandig/jandig-12-silkscreen-oficina.jpg", "Silkscreen workshop printing Jandig's visual identity"),
    ]), head="Field notes")
)
page("talks.html", "Talks | Angelo Pixel",
     "150+ talks and workshops on four continents since 2002, including TEDx, the Mozilla Festival and the United Nations.",
     talks)

# ----------------------------------------------------------- RECOGNITION
recognition = (
    hero("Recognition", "Awards, programs, residencies and press.",
         lede="What others have said and decided about the work, from 2006 to today.")
    + section(recog([
        ("2026", "Claude for Open Source Program, Anthropic, for Jandig."),
        ("2024", "Invited by the United Nations to the OSPOs for Good Symposium."),
        ("2018", "Mozilla Open Source Support Award, for Jandig."),
        ("2018", "Software Livres Culturais award, from the Brazilian Ministry of Culture, for Jandig."),
        ("2015", "Hacker residency, Red Bull Basement."),
        ("2014", "Google Impact Challenge Brazil, for Rede InfoAmazonia."),
        ("2014", "Artist residency at Hangar, Barcelona (Chronica Mobilis)."),
        ("2012", "SESC Sorocaba award, for &quot;Electro-Organic Experiments&quot;."),
        ("2012", "Nimk/Vivo Arte.mov artist residency (Brazil/Netherlands)."),
        ("2011", "CEMEC Creative Entrepreneurs award."),
        ("2006", "Est&uacute;dio Livre Collaboration Award."),
    ]), head="Awards, programs and residencies")
    + section(press_html, alt=True, head="In the press and on video")
)
page("recognition.html", "Recognition | Angelo Pixel",
     "Awards, programs and residencies from Anthropic, the United Nations, Mozilla and Google, plus press coverage and video.",
     recognition)

# ----------------------------------------------------------------- ABOUT
about_text = """        <p>As a child, I opened an Atari cartridge and, with the help of some cables, plugged it straight into the power socket. The cartridge broke and my home's power went out. It is my first memory of failure. Many more came later, and they guide my successes.</p>
        <p>I carry that curiosity and daring with me. It is what led me to create <a href="https://jandig.app/" target="_blank" rel="noopener">Jandig</a>, an open-source augmented reality platform awarded by Mozilla; Rede InfoAmazonia, an open-source IoT platform for water monitoring funded by a Google award; and Jeo, a geojournalism platform adopted by newsrooms on three continents. Their stories are in <a href="projects.html">Projects</a>.</p>
        <p>Since then I have taken that way of working to larger companies: an AI product for industrial maintenance at Stefanini, an API product at Amazon, and a fee system and a partner API at AutoNation. Today I run <a href="https://diar.ia.br" target="_blank" rel="noopener">diar.ia.br</a>, a weekday AI newsletter produced by a pipeline of AI agents that I built.</p>
        <p>Two decades managing projects taught me some valuable lessons. With my mind constantly bubbling with ideas, prioritization is my mantra. I have lost count of how many prototypes I have built. I do it for pleasure, and I am not attached to ideas that do not prove useful. Working with developer communities, I learned that the best way to manage is to understand people's motivations and encourage them, and that the best way to lead is by example.</p>"""
curios = [
    "In 2018 I spent a month traveling around the world, leaving Jandig stickers wherever I went.",
    "I am a father of twins.",
    "I never get tired of traveling to the Brazilian Amazon.",
    "A good friend taught me how to scuba dive, and I cannot wait to do it again!",
]
about = (
    """    <section class="hero hero-tight hero-about">
      <div class="container hero-grid">
        <div class="hero-copy">
        <p class="eyebrow">About me</p>
        <h1>I create award-winning products by alternating between business strategy and hands-on work.</h1>
        </div>
        <figure class="hero-photo">
          <img src="assets/images/angelo-pixel.jpg" alt="Portrait of Angelo Pixel" width="1335" height="2000" />
        </figure>
      </div>
    </section>
"""
    + section(about_text, narrow=True, flush=True)
    + section(cards([
        ("", "Ideation", "As an artist, my focus is to create a feeling in a specific context, and there are countless ways to do that. I learned ideation techniques to make interactive digital artworks possible: prototyping, Five Whys analysis, storyboarding, Crazy 8s."),
        ("", "Prioritization", "This goes back more than a decade, when I led a small team of very creative people. Everyone had lots of ideas, and we had to decide together what to build with limited resources. A tool I like is the Value vs. Effort matrix: simple to understand, and it forces you to think about the two variables that matter most, outcomes and resources."),
        ("", "Communication", "I love to teach. Adding up all the talks and workshops I have given, the number goes past 150. Teaching requires empathy with the audience: a time-constrained context where you cannot assume people already know something. I apply the same method whenever I need to communicate with anyone."),
        ("", "Stakeholder management", "I worked on a Brazilian government project with more than 10 funders, some of whom we partnered with daily. At the same time, as Technology Coordinator, I had to synchronize my team's work with other teams' to maximize outcomes."),
        ("", "Leadership", "My work as a community manager in open-source projects is based on &quot;selling&quot; ideas so that people invest their time in them, for free. To make that happen, you need to share a vision of what you want to build and lead people in building it."),
    ]), alt=True, head="How I learned my skills")
    + section("        <ul>\n" + "\n".join(f"          <li>{c}</li>" for c in curios) + "\n        </ul>",
              narrow=True, head="Curiosities")
)
page("about.html", "About | Angelo Pixel",
     "The story behind the products: from breaking an Atari cartridge as a kid to Amazon, open source and AI agents.",
     about)


print("ok")
