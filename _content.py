# ---------------------------------------------------------------
# SITE CONTENT. Edit this file to update the site, then run build.py.
# Every project is one dict. Order here = order on the home page.
# ---------------------------------------------------------------

PROFILE = {
    "name": "Andrew Mish",
    "email": "andrewmish@gmail.com",
    "phone": "(410) 353-9119",
    "phone_tel": "+14103539119",
    "linkedin": "https://www.linkedin.com/in/andrew-mish-324a7a228/",
    "github": "https://github.com/andrewmish12",
    "location": "Auburn, AL · Odenton, MD",
}

STATS = [
    ("50+", "Apps Script automations shipped at SilverStay"),
    ("15+", "Claude AI tools built with care navigators"),
    ("4", "hospital sites using my workflows"),
    ("100+", "business ideas on my list"),
]

CATS = {
    "work": "Work",
    "build": "Builds",
    "venture": "Ventures",
    "eng": "Engineering",
    "job": "Jobs",
}

# status -> (label, css class)
STATUS = {
    "live": ("Live", "s-live"),
    "inuse": ("In daily use", "s-live"),
    "poc": ("Proof of concept", "s-proto"),
    "proto": ("Prototype", "s-proto"),
    "early": ("Early build", "s-proto"),
    "idea": ("Idea pipeline", "s-idea"),
    "paused": ("Paused", "s-paused"),
    "done": ("Completed", "s-done"),
}

PROJECTS = [
# ---------------------------------------------------------------- SILVERSTAY
{
"slug": "silverstay", "cat": "work", "status": "live", "featured": True, "wide": True, "logo": "silverstay-logo.png",
"highlights": [
("Apps Script automation layer", "50+ automations for data sync, tracking, dashboards and Slack updates across 4 hospital sites"),
("Claude AI tools", "15+ tools built with care navigators: case-note assistant, progress-note auditor, resource search, placement navigator"),
("Daily PDF reports", "Apps Script + Claude + Cloud Functions put a formatted report in Drive every morning, hands-off"),
("Voice AI agent", "Calls transport and equipment vendors, reads back bookings, and pulls 10 fields per call (proof of concept)"),
("Referral intake rebuild", "Form submission → auto-generated referral PDF → emailed to the placement team"),
("DocuSign web forms", "Digital paperwork, including a ~150-field benefits enrollment form with signer routing"),
("Call-quality insights", "Claude scores recorded calls against a sales methodology and returns coaching notes"),
("Rollout survey site", "Before/after surveys measuring an AI rollout, on AWS (Route 53 → CloudFront → S3)"),
],
"title": "SilverStay",
"kicker": "I build the AI tools and automations a hospital discharge team runs on.",
"card": "50+ automations, 15+ Claude tools, a voice agent, and the plumbing that keeps it all moving across 4 hospital sites.",
"when": "June 2025 – Present", "role": "LLM Implementation Engineer Intern (remote)",
"stack": ["Claude API", "Google Apps Script", "Python", "ElevenLabs", "AWS", "DocuSign", "Google Cloud"],
"sections": [
("What SilverStay does",
"<p>SilverStay helps hospitals get patients discharged to the right place (rehab, nursing facility, home) faster. Care navigators handle a lot of manual work: digging through notes, chasing vendors, filling out forms. My job is to find the parts that shouldn't be manual and make them not manual.</p>"
"<p class='note-sm'>Everything here is described at the workflow level. No patient data, hospital names, or internal screenshots appear on this site, and that's on purpose.</p>"),
("What I built",
"<div class='builds'>"
"<div class='build'><h4>Apps Script automation layer</h4><p>50+ Google Apps Script automations across 4 hospital sites: data syncing between sheets, screening and tracking workflows, dashboard refreshes, and automatic Slack updates. Most of the team's daily reporting now runs on its own.</p></div>"
"<div class='build'><h4>Claude AI tools for notes and audits</h4><p>I worked with care navigators to design 15+ Claude-powered tools, including a case-note assistant, a progress-note auditor, a search tool for internal resources, and a long-term-care placement navigator. I sat with the people using them, saw where they got stuck, and built for that.</p></div>"
"<div class='build'><h4>Automated daily PDF reports</h4><p>A pipeline where Apps Script pulls the day's data, Claude helps generate the report layout code, a Cloud Function runs it, and a formatted PDF lands in Drive every morning. Nobody has to touch it once it's set up.</p></div>"
"<div class='build'><h4>Voice AI agent for vendor calls</h4><p>An AI phone agent that calls transport and medical-equipment vendors so navigators don't sit on hold. It discloses that it's an AI, refuses to share sensitive details, reads back what it booked, and pulls 10 structured fields out of every call (outcome, time, confirmation number, caveats, compliance flags).</p></div>"
"<div class='build'><h4>Referral intake rebuild</h4><p>I replaced an add-on-based process with a custom Apps Script trigger: a form submission becomes a generated referral PDF that's emailed straight to the placement team. I also built DocuSign web forms for paperwork that used to be filled out by hand.</p></div>"
"<div class='build'><h4>Call-quality insights</h4><p>A Claude-powered tool that reviews recorded calls, scores them against a sales methodology, and hands back specific coaching notes, so feedback doesn't depend on someone listening to every call.</p></div>"
"<div class='build'><h4>Rollout survey site</h4><p>Before and after a new AI tool rolled out, leadership wanted to measure whether it actually saved time. I built custom survey forms feeding one Apps Script backend, and put them behind a branded short link using AWS (Route 53 → CloudFront → S3).</p></div>"
"</div>"),
],
"demo": "pipeline_ss",
"results": [("50+","automations"),("15+","Claude tools"),("4","hospital sites"),("8","tools & systems built")],
"honest":
"<p>The biggest thing I learned: the hard part isn't the code, it's figuring out what people actually need. A tool nobody opens is worthless, so the best builds came from sitting with navigators and watching what slowed them down.</p>"
"<p>The voice agent taught me a weird lesson about prompting. The first model kept hanging up right after asking its own question, and every \"don't do X\" rule I added either got ignored or froze the agent. Switching to Claude Haiku 4.5 and rewriting everything as positive instructions (\"do Y\") fixed it. To be clear, the voice agent is still a proof of concept. It works in testing, but it isn't making real calls yet because phone service and the healthcare compliance paperwork still have to be finished. I'd rather say that than oversell it.</p>"
"<p>Healthcare also makes you careful. Every tool has to assume it's touching sensitive data, which slows things down, and honestly it should.</p>",
"next": "<p>Get the voice agent through compliance and onto real calls, and add an approval button so a navigator signs off before the agent acts.</p>",
},
# ---------------------------------------------------------------- EASY CLEAN
{
"slug": "easy-clean", "cat": "eng", "status": "done", "featured": True,
"title": "EASy Clean",
"kicker": "My PLTW capstone: a UV chair cover that sanitizes the clothes you're not sure are clean or dirty.",
"card": "PLTW Engineering Design & Development capstone. 323 survey responses, 4 pivots, and one prototype built for ~$104.",
"when": "2025 – 2026 school year", "role": "Team of 3 (with Sebastian White & Emily Paine)",
"stack": ["Fusion 360 CAD", "UV-A LEDs", "Soldering", "Survey research", "Petri dish testing"],
"sections": [
("The problem",
"<p>Everybody has <em>the chair</em>, the one in your room covered in clothes you wore once. They're not dirty enough to wash and not clean enough to put away. Washing them anyway wastes water (about 41 gallons a load), and sprays like Febreze only cover up the smell.</p>"
"<p>We surveyed people to see if this was real. <strong>323 responses</strong> later, it was.</p>"),
("How it evolved",
"<p>This project changed direction more than anything else I've built. We started with UV light, switched to a heated-airflow cabinet, then a two-part heat-and-cool cabinet. After a design review, we realized we'd been designing a whole appliance when the problem was literally a chair. So we went back to UV and turned it into a <strong>chair cover</strong>.</p>"
"<ul class='steps'><li><b>01</b> UV cabinet idea</li><li><b>02</b> Heated airflow cabinet (won our decision matrix)</li><li><b>03</b> Top/bottom heat + cool cabinet</li><li><b>04</b> UV chair cover (final, Feb 2026)</li></ul>"),
("The final build",
"<p>A polyester cover that drapes over any desk chair, with UV-A LED strips attached by Velcro so you can pull the electronics off and wash the cover. We picked UV-A over UV-C on purpose: it's weaker at killing bacteria, but much safer for something sitting in your bedroom.</p>"
"<p>We wrote 8 design requirements, including at least 80% bacteria reduction, a cycle of 15 minutes or less, a footprint under 2 cubic feet, and more than 90% of the garment exposed to light. We compared 6 concepts in a decision matrix and benchmarked against washers, sprays, charcoal bags and an existing UV-cabinet patent. Budget was about $100; we came in at <strong>$103.57</strong>.</p>"),
("Testing",
"<p><strong>Durability:</strong> passed. We ripped the light strips off and put them back repeatedly, and neither the Velcro nor the adhesive lifted.</p>"
"<p><strong>Bacteria:</strong> our first round of petri dishes failed. Condensation built up under the lights and nothing grew, not even on the controls, so we got no data. We switched dish types and started over.</p>"),
],
"demo": "survey_easy",
"results": [("323","survey responses"),("76.2%","re-wear clothes"),("6","concepts scored"),("$103.57","prototype cost")],
"honest":
"<p>We pivoted late, and it cost us. Changing to the chair cover in February meant relearning CAD, soldering and connectors on a deadline. But it was the right call. The cabinet was a cool engineering problem; the chair cover actually fits how people live.</p>"
"<p>The failed petri dish test stung, but it taught me more than a clean pass would have: control your test conditions <em>before</em> you trust your results. If I did it again, I'd sew the Velcro on instead of gluing it, and I'd run a tiny test batch before the real one.</p>",
"next": "<p>Finish the redo of the bacteria test, and figure out whether this could be a real product. A UV device that claims to kill bacteria counts as a regulated pesticide device under EPA rules, so that's the first wall to look at.</p>",
"links": [("Original team project site (school account)", "https://sites.google.com/spaldinghs.org/sea/home")],
},
# ---------------------------------------------------------------- BARBER BOT
{
"slug": "barber-bot", "logo": "barber-bot-logo.svg", "cat": "build", "status": "proto", "featured": True,
"title": "AI Barber Bot",
"kicker": "A text-message scheduling assistant for barbershops. Text it like you'd text your barber, and Claude figures out what you want.",
"card": "Twilio + Claude SMS bot that turns messy texts like \"can I get a fade fri after 3\" into structured booking requests.",
"when": "2025 – Present", "role": "Solo builder",
"stack": ["Twilio Functions", "Claude API", "JavaScript", "SMS"],
"sections": [
("Why I built it",
"<p>Most barbers book appointments by text, between cuts, with their hands full. Clients send things like \"yo can I get in friday after 3 for a fade.\" That's easy for a person to read and annoying for software, which is exactly the kind of thing LLMs are good at.</p>"),
("How it works",
"<p>A client texts the shop's Twilio number. A Twilio Function sends the message to Claude with a strict prompt: pull out the name, date, time, service and intent (new booking, cancel, reschedule, or question), plus a confidence level, and return <strong>only JSON</strong>. The bot then replies based on the intent, so cancellations and reschedules get different responses than new bookings.</p>"
"<p>If anything breaks (bad JSON, API error), it falls back to a friendly \"we'll get back to you\" instead of leaving the client hanging.</p>"),
],
"demo": "sms_barber",
"results": [("6","fields extracted per text"),("4","intents handled"),("1","function, ~70 lines")],
"honest":
"<p>Right now this is the smart front door, not the whole house. It understands requests really well, but it doesn't check the calendar or lock in the appointment yet. A human still confirms. I'd rather show you that than pretend it's fully autonomous.</p>"
"<p>The interesting lesson was forcing an LLM to answer in JSON only. Once the output is structured, everything after it is just normal code, and that pattern is now how I build almost everything.</p>",
"next": "<p>Connect it to a real calendar so it can check availability and confirm on its own, add reminder texts, and get one real barbershop to pilot it.</p>",
},
# ---------------------------------------------------------------- PREREQ
{
"slug": "prereq", "cat": "venture", "status": "early", "featured": True,
"title": "Prereq",
"kicker": "Degree planning that answers \"does this class count?\" in seconds, and shows you the exact catalog rule.",
"card": "My Auburn Ideas Jam pitch. 65% of 20 surveyed students said they'd use it. Built so the AI explains answers but never makes them up.",
"when": "Sept 2026 – Present", "role": "Founder · Pitched at Auburn Ideas Jam (Harbert College of Business)",
"stack": ["Python rules engine", "Auburn Bulletin data", "LLM explanations"],
"sections": [
("The problem",
"<p>Figuring out whether a class counts toward your requirements means digging through the course catalog, an advising appointment, or guessing. A wrong guess can cost you a semester.</p>"),
("How it works",
"<p>You type in a class and your completed coursework. A <strong>deterministic Python rules engine</strong>, not an AI, checks it against the public Auburn Bulletin and returns one of three verdicts: <b>Counts</b>, <b>Doesn't count</b>, or <b>Not verified</b>. The AI only explains the verdict in plain English and cites the rule it came from.</p>"
"<p>It never touches student records. You enter your own classes, so there's no privacy risk with student data.</p>"),
],
"demo": "verdict_prereq",
"results": [("65%","of 20 students would use it"),("3","possible verdicts"),("0","guesses allowed")],
"honest":
"<p>\"It never guesses\" is the whole idea. If the rules aren't verified, it says so instead of sounding confident and being wrong.</p>"
"<p>The hard truth: tools like Degree Works and Stellic already exist, and selling to a university can take one to two years. Twenty survey responses is a signal, not proof. I need a lot more students, and I need to find out whether advisors would actually point people to it.</p>",
"next": "<p>Finish the rules engine and test suite, survey a bigger group, and get a demo in front of real advisors.</p>",
},
# ---------------------------------------------------------------- AU DINING
{
"slug": "au-dining", "cat": "build", "status": "inuse", "featured": True,
"title": "AU Dining",
"kicker": "A web app that pulls Auburn's live dining menus and tells you where to eat between classes, based on your macros.",
"card": "Live Auburn menu data, filters for calories and protein, \"Build My Plate,\" and a ranking of where to eat by walking distance.",
"when": "2025 – Present", "role": "Solo builder",
"stack": ["Google Apps Script", "JavaScript", "Live dining data", "Geolocation"],
"sections": [
("Why I built it",
"<p>I wanted to hit protein goals at Auburn without opening three dining menus and doing math in my head between classes. So I built the app I wanted.</p>"),
("What it does",
"<ul class='feat'>"
"<li><b>Live menus</b> for The Edge, Tiger Zone and Wellness, pulled straight from Auburn's dining data with calories, protein and diet tags, refreshed every 10 minutes</li>"
"<li><b>Filters</b> for high protein (20g+), calorie range, diet tags, and today vs. tomorrow</li>"
"<li><b>Where to Go</b> ranks dining halls using your location, walking times, your class schedule, and the foods you like or don't</li>"
"<li><b>Build My Plate</b> builds a meal within ~10% of your calorie target using at most two stations</li>"
"<li><b>Morning alert</b> email at 7AM if Auburn adds, removes or renames a station</li>"
"</ul>"
"<p>No accounts. Everything saves on your phone.</p>"),
],
"demo": "phone_dining",
"results": [("3","dining halls"),("10 min","data refresh"),("20g+","protein filter")],
"honest":
"<p>Version one was way too much. I kept piling on features until it was overwhelming, so I redesigned the whole thing around four simple tabs. That redesign made it actually usable.</p>"
"<p>I also had typed-in hours that were wrong, and breakfast and dinner items getting mixed together. Switching to Auburn's live data fixed both. Lesson: never hard-code something that already exists as real data.</p>"
"<p>I deliberately left out pulling meal-swipe balances and class schedules automatically. It would've meant handling student logins, and that's not worth the privacy risk for a side project.</p>",
"next": "<p>Move it to its own hosting so it feels like a real app, then get it into friends' hands and see what they actually use.</p>",
},
# ---------------------------------------------------------------- TRADE TRACKER
{
"slug": "trade-tracker", "cat": "build", "status": "live", "featured": False,
"title": "Congressional Trade Tracker",
"kicker": "An automated system that watches public congressional stock-trade filings every 6 hours and turns them into proposed trades.",
"card": "Scrapes House disclosure filings every 6 hours, reads the PDFs, and drafts proportional trades for me to approve.",
"when": "2026", "role": "Solo builder",
"stack": ["Google Apps Script", "OCR", "Google Sheets", "Claude"],
"sections": [
("The idea",
"<p>Members of Congress have to publicly disclose their stock trades. Paid apps copy those trades for you. I wanted to see if I could build the same thing myself for free.</p>"),
("How it works",
"<p>Every 6 hours, Apps Script checks the House Clerk's disclosure site for new filings and reads the PDFs with OCR. It turns the changes into target portfolio weights and logs everything to a sheet. Then it emails me a ready-to-go trade summary. <strong>Nothing executes without me confirming it.</strong></p>"
"<p>It carries small changes forward until they're big enough to actually trade, caps how big any single trade can be, and flags anything it can't read (like options) instead of guessing.</p>"),
],
"demo": "pipeline_trades",
"results": [("6 hrs","check interval"),("100%","human-approved trades"),("0","guesses on unclear filings")],
"honest":
"<p>My first plan was to have it place trades directly through the brokerage. I spent days fighting login and permission restrictions before admitting that wasn't going to work, and switched to \"email me a summary, I approve it.\" Honestly, that's the better design anyway.</p>"
"<p>The other reality: filings can come in up to 45 days after the trade, so you're always copying old moves. It's a great automation project. I wouldn't call it an investing edge.</p>"
"<p class='note-sm'>Personal project with public data. Not investment advice.</p>",
"next": "<p>Let it run long enough to compare its performance against just holding an index fund.</p>",
},
# ---------------------------------------------------------------- SWEATBUDDIES
{
"slug": "sweatbuddies", "logo": "sweatbuddies-logo.svg", "cat": "build", "status": "inuse", "featured": False,
"title": "SweatBuddies",
"kicker": "A two-person workout accountability app with photo check-ins, weekly goals, and real stakes if you slack off.",
"card": "Photo-proof workouts, streaks, weekly goals, and an IOU system: miss your goal and you owe your partner.",
"when": "2025 – Present", "role": "Solo builder",
"stack": ["Google Apps Script", "Google Sheets", "Google Drive", "JavaScript"],
"sections": [
("Why I built it",
"<p>Accountability apps exist, but I wanted one built exactly for me and my workout partner, with stakes that actually matter to us.</p>"),
("What it does",
"<ul class='feat'>"
"<li><b>Photo check-ins</b> stored in Drive as proof of every workout</li>"
"<li><b>Weekly goal ring + streaks</b> that track your progress</li>"
"<li><b>IOUs:</b> every Monday it scores the week, and whoever missed owes the other person a coffee, $10, flowers, or a custom penalty, with claim, confirm and dispute steps</li>"
"<li><b>Thursday nudge</b> if you're behind, plus comments and likes on each other's workouts</li>"
"</ul>"),
],
"demo": "ring_sweat",
"results": [("2","users (on purpose)"),("Daily","actual use"),("14","max workouts / week")],
"honest":
"<p>This is the one I actually use every day, and that's what made it good. Every bug I found came from real use. Two workouts in one day only counted once. The progress ring stayed at zero because Google Sheets was secretly converting my dates. Small bugs, but you only find them by using your own product.</p>",
"next": "<p>Maybe open it up to more pairs. For now it does exactly what we need.</p>",
},
# ---------------------------------------------------------------- COLLABIFY
{
"slug": "collabify", "cat": "venture", "status": "paused", "featured": False,
"title": "Collabify",
"kicker": "An iOS app to match small businesses with influencers for paid promotions. It's like a dating app for brand deals.",
"card": "Learned SwiftUI from scratch to prototype it, then pressure-tested the idea hard enough to pause it.",
"when": "2025", "role": "Founder & developer",
"stack": ["SwiftUI", "Xcode", "iOS"],
"sections": [
("The idea",
"<p>Small businesses want influencer marketing but don't know where to start. Small influencers want paid deals but can't find them. Collabify would match the two sides, handle payment in the app, and take a small fee.</p>"),
("What I built",
"<p>I taught myself SwiftUI to build the prototype: profiles for both sides, the matching flow, and separate dashboards for businesses and creators.</p>"),
],
"demo": None,
"results": [("1","new language learned (Swift)"),("2","sided marketplace")],
"honest":
"<p>When I seriously pressure-tested this, it didn't hold up. Collabstr, Aspire and JoinBrands already do this, and I had zero real evidence that businesses would pay for my version. So I paused it.</p>"
"<p>It still wasn't wasted. I learned iOS development, and I learned to look for proof of demand <em>before</em> I write a line of code. My instinct now is \"something like this probably already exists, so go find it first.\"</p>",
"next": "<p>Parked. If I find a niche the big players ignore, I'll come back to it.</p>",
},
# ---------------------------------------------------------------- IDEAS
{
"slug": "ideas", "cat": "venture", "status": "idea", "featured": True,
"title": "The Idea Pipeline",
"kicker": "I keep a running list of business ideas, 100+ and counting. Here's how I decide which ones are worth building.",
"card": "100+ ideas on the list. I ran a batch of 90 through six forcing questions: 73 killed, 12 need more info, 5 survived.",
"when": "Ongoing", "role": "Founder, Entrepreneurship Club (Archbishop Spalding)",
"stack": ["Customer surveys", "Competitive research", "Prototyping"],
"sections": [
("How I filter ideas",
"<p>Ideas are cheap. I've got a notes app with 100+ of them. Before pitching at Auburn's Ideas Jam, I ran 90 of them through a product diagnostic: six blunt questions about who has the problem, how badly they have it, what they use now, and whether anyone would pay.</p>"),
("The ones that survived",
"<div class='builds'>"
"<div class='build'><h4>Prereq</h4><p>Degree-planning answers you can trust. <a href='prereq.html'>See the project →</a></p></div>"
"<div class='build'><h4>Real estate site reports</h4><p>Fast, clear reports on a property or lot for buyers and investors. This one ties into my real estate minor.</p></div>"
"<div class='build'><h4>EasyEats</h4><p>A budget meal planner and grocery list, already prototyped and deployed as a web app with a 3-person team.</p></div>"
"<div class='build'><h4>Gum removal</h4><p>A service and product angle on a gross, expensive problem nobody wants to deal with.</p></div>"
"<div class='build'><h4>Designated driver service</h4><p>A safer way for college students to get themselves and their cars home.</p></div>"
"<div class='build'><h4>AI golf glasses</h4><p>Smart glasses that track your practice sessions. Golf + AI, my two favorite things.</p></div>"
"</div>"),
],
"demo": "funnel_ideas",
"results": [("90","ideas screened"),("73","killed"),("12","need more info"),("5","survived")],
"honest":
"<p>The most useful (and annoying) feedback I got: most of my ideas came from imagination, not observation. The good ones start with a problem you've actually watched someone deal with. That changed how I come up with ideas.</p>"
"<p>I also learned to push back. When I thought the scoring was wrong, I said so, and I was right twice. Being open to feedback doesn't mean agreeing with all of it.</p>",
"next": "<p>Talk to real customers for the top 5, and kill or build each one based on what they say, not on what I think.</p>",
},
# ---------------------------------------------------------------- PLTW
{
"slug": "pltw", "cat": "eng", "status": "done", "featured": True,
"title": "PLTW Engineering",
"kicker": "Four years of Project Lead The Way engineering at Archbishop Spalding: CAD, prototyping, robotics, and a lot of trial and error.",
"card": "IED, POE and an EDD capstone. Catapults, 3D-printed parts, a reverse-engineered product, automata, a self-driving robot and a VEX car.",
"when": "2022 – 2026", "role": "PLTW Engineering student",
"stack": ["Fusion 360", "3D printing", "Laser cutting", "VEX robotics", "Engineering design process"],
"sections": [
("Intro to Engineering Design (IED)",
"<div class='builds'>"
"<div class='build'><h4>Carnival game launcher</h4><p>A popsicle-stick catapult built to knock down a tower of 10 cups. On test day we pulled off a rubber band at the last second, trading power for accuracy. It worked.</p></div>"
"<div class='build'><h4>Block project</h4><p>Built a 7–10 block shape and sketched every orthographic view, including hidden lines. The hard part wasn't the drawing, it was designing a shape that hit every constraint.</p></div>"
"<div class='build'><h4>3D-printed ornament</h4><p>A gift-box ornament in Fusion 360 that had to fit in a 3×3×0.5 in. box. I forgot to account for the bow's height and had to scale the whole thing down. Lesson learned: honor the constraints the first time.</p></div>"
"<div class='build'><h4>Miniature train</h4><p>Modeled every component of a train in Fusion 360, assembled it, and produced a 5-sheet technical drawing set with exploded views and dimensions.</p></div>"
"<div class='build'><h4>Reverse engineering</h4><p>Took apart a real product with my team, analyzed how each part worked, and rebuilt every component in CAD to the right dimensions.</p></div>"
"<div class='build'><h4>Automata</h4><p>A moving desk toy based on the Chrome dinosaur game. I picked the wrong cams and had already glued everything, so I improvised with hot glue and tape to get the dino jumping higher.</p></div>"
"</div>"),
("Principles of Engineering (POE)",
"<div class='builds'>"
"<div class='build'><h4>Self-driving vehicle</h4><p>Programmed a robot with dead-reckoning navigation to drive a path around a table without falling off. The final run turned right at the edge.</p></div>"
"<div class='build'><h4>VEX gear-ratio car</h4><p>Designed and raced a VEX car optimized through gear ratios. Our parts didn't line up, so we pushed a long screw through two plates at an angle to make it work.</p></div>"
"</div>"),
("Engineering Design & Development (EDD)",
"<p>My capstone, <a href='easy-clean.html'>EASy Clean</a>: a full year of taking a real problem from research to a working prototype.</p>"),
],
"demo": None,
"results": [("8+","documented projects"),("3","PLTW courses"),("1","year-long capstone")],
"honest":
"<p>Looking back at my sophomore reflections, the same lesson keeps showing up: plan before you build. Forgetting the bow on the ornament, gluing the automata before testing the cams, missing one step in a CAD video. Every mistake was a version of rushing. I still have to remind myself of that, just with code now instead of popsicle sticks.</p>"
"<p>PLTW is also where I figured out that I love taking something from my head to the real world. That's basically what I do now, just with software and businesses.</p>",
"next": None,
"links": [("Original class portfolio (school account)", "https://sites.google.com/spaldinghs.org/andrewmish-engineeringportfoli/home")],
},
# ---------------------------------------------------------------- ENTREPRENEURSHIP CLUB
{
"slug": "entrepreneurship-club", "cat": "venture", "status": "done", "featured": False,
"title": "Entrepreneurship Club",
"kicker": "I founded my high school's entrepreneurship club and recruited ~30 students to join.",
"card": "Founded at Archbishop Spalding. ~30 student sign-ups through a simple Google Form.",
"when": "Aug 2024 – June 2026", "role": "Founder",
"stack": ["Leadership", "Recruiting", "Public speaking"],
"sections": [
("What it was",
"<p>There wasn't a place at school for students who wanted to start things, so I made one. I recruited around 30 students through a Google Form and word of mouth, and we used meetings to talk through ideas and how real businesses get started.</p>"),
],
"demo": None,
"results": [("~30","student sign-ups")],
"honest":
"<p>Getting people to sign up was the easy part. Keeping them showing up is the real test of whether you're giving them something valuable. That's the same problem every product has.</p>",
"next": None,
},
# ---------------------------------------------------------------- JOBS
{
"slug": "walden", "logo": "https://cdn.cybergolf.com/images/1309/Walden-CC_logo-trans-web.png", "cat": "job", "status": "done", "featured": False,
"title": "Walden Country Club",
"kicker": "Golf Cart Attendant & Kitchen Assistant, Crofton, MD.",
"card": "Trained 5 new hires and kept a 70-cart fleet running at peak tee times.",
"when": "May 2024 – Sept 2025", "role": "Golf Cart Attendant & Kitchen Assistant",
"stack": ["Training", "Teamwork", "Operations"],
"sections": [("What I did",
"<ul class='feat'><li>Trained <b>5 new employees</b> and simplified our end-of-day closing procedures</li>"
"<li>Coordinated a <b>70-cart fleet</b> with teammates so members stayed on schedule at peak times</li>"
"<li>Helped out in the kitchen during busy service</li></ul>")],
"demo": None, "results": [("70","carts"),("5","employees trained")],
"honest": "<p>This is where I first noticed I like fixing processes. Closing up took longer than it needed to, so I helped simplify it. Same instinct I use at SilverStay, just with golf carts.</p>",
"next": None,
},
{
"slug": "wild-birds", "logo": "https://gambrills.wbu.com/templates/wbu3/staticresources/assets/images/logo.webp", "cat": "job", "status": "done", "featured": False,
"title": "Wild Birds Unlimited",
"kicker": "Sales Associate, Gambrills, MD.",
"card": "Advised ~50 customers per shift and matched them with the right products.",
"when": "June 2023 – Dec 2023", "role": "Sales Associate",
"stack": ["Sales", "Customer service", "Product knowledge"],
"sections": [("What I did",
"<ul class='feat'><li>Advised around <b>50 customers per shift</b>, building rapport and matching products to what they actually needed</li>"
"</ul>")],
"demo": None, "results": [("~50","customers / shift")],
"honest": "<p>Sales is really just listening. People came in knowing their problem, not the product. Figuring out the real need first is the same skill I use when I build tools for people.</p>",
"next": None,
},
{
"slug": "waugh-chapel", "cat": "job", "status": "done", "featured": False,
"title": "Waugh Chapel Swim Club",
"kicker": "Snack Bar Attendant, Gambrills, MD.",
"card": "Handled cash and served guests through peak summer rushes.",
"when": "May 2023 – Sept 2023", "role": "Snack Bar Attendant",
"stack": ["Cash handling", "Customer service", "Working under pressure"],
"sections": [("What I did",
"<ul class='feat'><li>Handled cash accurately and served guests under pressure during peak summer rushes</li></ul>")],
"demo": None, "results": [],
"honest": "<p>My first job. A line of hungry kids at 1pm in July teaches you to stay calm and keep moving.</p>",
"next": None,
},
]

EDUCATION = [
("Auburn University", "B.S. Business Administration · Pre-Business (Intended Finance) · Intended Real Estate minor", "Expected May 2030", "https://ocm.auburn.edu/brand-center/logos/auburn/informal_horiz/fullcolor/auburn_informal_h_fullcolor_digital.png"),
("Archbishop Spalding High School", "GPA 4.2 · PLTW Engineering · Golf (2-year varsity)", "2022 – 2026", "https://bbk12e1-cdn.myschoolcdn.com/ftpimages/906/logo/60_logo_whitebackground.png"),
]

HONORS = [
"Pioneer Leadership Scholarship, 4-year recipient",
"National Honor Society",
"Honor Roll, 8 semesters",
"Auburn Ideas Jam competitor, Harbert College of Business",
]

SKILLS = {
"AI & APIs": ["Claude API", "OpenAI API", "ElevenLabs", "Twilio", "MCP"],
"Code": ["Python", "JavaScript / Apps Script", "SwiftUI", "HTML/CSS"],
"Cloud & tools": ["AWS", "Google Cloud", "Google Workspace", "DocuSign", "Fusion 360"],
"Business": ["Customer research", "Pitching", "Process improvement", "Training"],
}
