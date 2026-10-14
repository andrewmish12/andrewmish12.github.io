# ---------------------------------------------------------------
# SITE CONTENT. Edit this file to update the site, then run _build.py.
# Every project is one dict. Order here = order on the home page (most recent first).
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
    ("50+", "automations, tools and fixes shipped at SilverStay"),
    ("15+", "Claude AI tools built with care navigators"),
    ("4+", "hospital sites using my work"),
    ("100+", "business ideas on my list"),
]

CATS = {
    "work": "Work",
    "build": "Builds",
    "venture": "Ventures",
    "write": "Writing",
    "lead": "Leadership",
    "eng": "Engineering",
    "job": "Jobs",
}

STATUS = {
    "live": ("Live", "s-live"),
    "inuse": ("In daily use", "s-live"),
    "poc": ("Proof of concept", "s-proto"),
    "proto": ("Prototype", "s-proto"),
    "early": ("Early build", "s-proto"),
    "idea": ("Idea pipeline", "s-idea"),
    "paused": ("Paused", "s-paused"),
    "done": ("Completed", "s-done"),
    "ongoing": ("Ongoing", "s-live"),
}

VIBE = ("<p class='note-sm'>How I build: I don't write code by hand. I vibe code. I decide what to build, describe it to Claude, "
        "test everything it gives me, and push back until it actually works.</p>")

MOCK_WORKLIST = (
"<figure class='panel'><p class='mono small dim'>daily worklist · sample</p>"
"<table class='wl'><tr><th>Tier</th><th>Patient</th><th>Days</th><th>Next step</th></tr>"
"<tr><td><span class='t g'>Med ready</span></td><td>Patient A</td><td>3</td><td>Bed offer pending</td></tr>"
"<tr><td><span class='t y'>T2</span></td><td>Patient B</td><td>6</td><td>Insurance auth submitted</td></tr>"
"<tr><td><span class='t r'>T3</span></td><td>Patient C</td><td>11</td><td>Family meeting Thursday</td></tr>"
"<tr><td><span class='t g'>Med ready</span></td><td>Patient D</td><td>2</td><td>Transport booked</td></tr></table>"
"<figcaption>Mockup with made-up data. It shows the layout of the daily worklist PDFs, not a real report.</figcaption></figure>")

MOCK_SLACK = (
"<figure class='panel'><p class='mono small dim'>slack alert · sample</p>"
"<div class='slack'><b>Nightly reset</b> <span class='dim'>7:02 AM</span><p>⚠️ Reset failed on one site's sheet: header row not found. Notes were <b>not</b> cleared. Check the sheet before tonight's run.</p></div>"
"<figcaption>Mockup of the error alert I added so a failed script tells someone instead of failing silently.</figcaption></figure>")

PROJECTS = [
# ================================================================ SILVERSTAY
{
"slug": "silverstay", "cat": "work", "status": "live", "featured": True, "strip": True, "logo": "silverstay-logo.png",
"title": "SilverStay",
"kicker": "I build the automations and AI tools a hospital discharge team runs on.",
"card": "I automate the boring parts of hospital discharge work: nightly scripts, daily reports, Claude tools and more, across 4+ hospitals.",
"when": "June 2025 – Present", "role": "LLM Implementation Engineer Intern (remote)",
"stack": ["Claude", "Google Apps Script", "AppSheet", "Google Sheets", "AWS", "DocuSign", "ElevenLabs", "Slack"],
"highlights": [
("Nightly archive & reset scripts", "Archive each day's notes, then clear the inputs, across several hospital sites. Tested on a copy first"),
("Daily PDF worklists", "Morning reports emailed at 7:30 AM. I adapted the set for a second hospital"),
("Claude AI tools", "15+ tools built with care navigators for notes, audits and search"),
("AppSheet app", "Mobile data-entry app on top of a tracking sheet, built for a care manager"),
("Referral intake", "Form submission → auto-generated referral PDF → emailed to the placement team. Live"),
("Report data-quality fixes", "Tracked down duplicate and missing patients in a daily report and added dedupe"),
("Surveys + AWS short link", "Before/after rollout surveys behind a branded link (Route 53 → CloudFront → S3)"),
("And more", "Voice agent prototype, DocuSign forms, formula repairs, metrics fixes, Slack alerts…"),
],
"sections": [
("What SilverStay does",
"<p>SilverStay helps hospitals get patients discharged to the right place (rehab, a nursing facility, home) faster. Care navigators and care managers do a lot of manual work: charting notes, tracking every patient's status, chasing vendors, filling out forms. My job is to find the parts that shouldn't be manual and automate them.</p>"
"<p class='note-sm'>Everything on this page is described at the workflow level. No patient data, hospital names or real internal screenshots appear on this site, on purpose. The examples below are mockups with made-up data.</p>"),
("What I built",
"<div class='builds'>"
"<div class='build'><h4>Nightly archive & reset scripts</h4><p>Apps Script jobs that save each day's charting notes to an archive and clear the input columns for the next day, across several hospital sites. I rewrote one site's archive to skip inactive patients and unchanged notes. For another site, I built a reset that keeps one tier's notes, plus a test that runs on a copy of the sheet (12 of 12 checks passed) and a one-click restore from the archive.</p></div>"
"<div class='build'><h4>Daily PDF worklists</h4><p>Morning worklist PDFs, emailed automatically at 7:30 AM. I adapted an existing set of reports for a second hospital. The test runs covered 28 patients.</p></div>"
"<div class='build'><h4>Claude AI tools</h4><p>15+ Claude tools built with care navigators: a case-note assistant, a progress-note auditor, a search tool for internal resources and a long-term-care placement navigator.</p></div>"
"<div class='build'><h4>AppSheet data-entry app</h4><p>A mobile app on top of a care-coordination sheet: a list of active patients, a notes form, a one-tap discharge button, and a new-patient form that checks for duplicate IDs. It's a working prototype; it's not rolled out yet.</p></div>"
"<div class='build'><h4>Referral intake automation</h4><p>A form submission becomes a generated referral PDF, emailed straight to the placement team. It replaced an add-on that was sending emails twice. Live.</p></div>"
"<div class='build'><h4>Daily report data-quality fixes</h4><p>A daily tiered patient report (green, yellow and red tiers) had duplicates and a missing patient. I traced it to patients moving between care managers' lists and a tier with no group for it, and I added dedupe to the script that feeds the report's next-steps column.</p></div>"
"<div class='build'><h4>Formula & metrics repairs</h4><p>Fixed a contracts sheet where a script only checked new rows, so old broken formulas never got fixed. The first version Claude gave me was 223 lines; I sent it back and we landed on 12. I also fixed a metrics script that shifted 10 days of values one column over.</p></div>"
"<div class='build'><h4>Rollout surveys + AWS short link</h4><p>Pre- and post-rollout surveys for care navigators (custom HTML on Google Sites, one Apps Script backend, QR codes), behind a branded short link on AWS. The pre-rollout survey is live and collecting responses.</p></div>"
"<div class='build'><h4>Voice agent prototype</h4><p>An ElevenLabs agent that calls transport and equipment vendors for navigators. It says it's an AI, refuses to share patient info, reads back the booking and logs 10 fields per call. Tested in text mode only; it hasn't made a real call.</p></div>"
"<div class='build'><h4>DocuSign forms & more</h4><p>A ~150-field benefits enrollment web form with signer routing, Slack error alerts on nightly scripts, sheet structure fixes, link cleanups and plain-English reviews of existing scripts.</p></div>"
"</div>"),
],
"proof": [MOCK_WORKLIST, MOCK_SLACK],
"results": [("50+","automations, tools & fixes"),("15+","Claude tools"),("4+","hospital sites")],
"honest":
"<p>I don't know how to code. I vibe code: I figure out what the team needs, describe it to Claude, and then my real job is testing it and pushing back. When Claude handed me a 223-line fix for a 12-line problem, I sent it back. When it said something was tested and it wasn't, I made it run the test on a copy of the sheet.</p>"
"<p>That testing matters because this is real work for real people. Once, a reset cleared notes it shouldn't have, because the original script had a rule about which days to skip that got missed. We restored everything from the archive, and since then every change runs on a copy first.</p>"
"<p>Healthcare also makes you careful. Every tool has to assume it's touching sensitive data, which slows things down, and honestly it should.</p>",
"next": "<p>Roll the AppSheet app out to the care manager, get the post-rollout survey approved, and keep turning the team's most repetitive work into things that run on their own.</p>",
},
# ================================================================ PREREQ
{
"slug": "prereq", "cat": "venture", "status": "early", "featured": True, "logo": "prereq-logo.png",
"title": "Prereq",
"kicker": "A conversational AI that builds your class schedule for you, down to the exact CRNs.",
"card": "A conversational AI that builds your Auburn schedule. Pitched at the Ideas Jam and accepted into the New Venture Accelerator. 73% of 22 students surveyed would use it.",
"when": "Sept 2026 – Present", "role": "Founder · Auburn Ideas Jam pitch · Accepted into the New Venture Accelerator",
"stack": ["Conversational AI", "Auburn Bulletin data", "Public course schedule", "Claude"],
"sections": [
("The problem",
"<p>A few weeks into my first semester, I got an email from my advisor: it's time to plan for spring 2027. So I logged into DegreeWorks and got a wall of text. I ended up in ChatGPT, trying to piece together my own schedule by hand.</p>"
"<p>I'm not the only one. Advisors average 270 to 300 students each, sometimes only 10 minutes per student, and 40.8% of advisors report burnout weekly or more (NACADA, n=821).</p>"),
("What Prereq is",
"<p><strong>Prereq is a conversational AI you actually talk to.</strong> Tell it your major, when you want to graduate, how many credit hours you want, even your Strong Interest Inventory results. It builds one clear plan with the exact CRNs ready to register, and generates a one-page report you can bring straight to your advisor for approval.</p>"
"<p>It runs on public data: the Auburn Bulletin for degree rules and the public course schedule for CRNs. You type in the classes you've taken, so it never touches student records. When it can't verify a rule, it says so instead of guessing.</p>"),
("Where it's been",
"<ul class='feat'><li>Pitched at the <b>Auburn Ideas Jam</b> (Harbert College of Business), Sept 29, 2026</li>"
"<li><b>Accepted into Auburn's New Venture Accelerator</b> (October 2026)</li>"
"<li>Surveyed 22 Auburn students, freshman through grad: <b>73%</b> would use a free AI tool that builds their schedule, <b>68%</b> find DegreeWorks confusing, and 60% needed outside help just to plan a schedule</li>"
"<li>Built a proof of concept as a Claude Project on real Auburn Finance degree requirements</li>"
"<li>The model: free for students; universities pay a monthly subscription for advisor tools and course-demand insights</li>"
"<li>Pitch budget for the $1,000 prize: $450 AI compute, $150 hosting, $250 for 50 student pilot users, $150 to verify data against the Bulletin</li></ul>"),
],
"demo": "chat_prereq",
"proof": ["<p class='dim'>My New Venture Accelerator deck:</p><figure class='panel pimg '><img src='prereq-slide-1.jpg' alt='Slide 1: the problem' loading='lazy'><figcaption>Slide 1: the problem</figcaption></figure><figure class='panel pimg '><img src='prereq-slide-2.jpg' alt='Slide 2: the fix, the model and the survey' loading='lazy'><figcaption>Slide 2: the fix, the model and the survey</figcaption></figure><figure class='panel pimg '><img src='prereq-slide-3.jpg' alt='Slide 3: why it wins and the ask' loading='lazy'><figcaption>Slide 3: why it wins and the ask</figcaption></figure><figure class='panel pimg '><img src='prereq-slide-4.jpg' alt='Slide 4: about the founder' loading='lazy'><figcaption>Slide 4: about the founder</figcaption></figure>"],
"results": [("73%","of 22 students would use it"),("68%","find DegreeWorks confusing"),("~270","students per advisor")],
"honest":
"<p>Prereq came straight from my own frustration. I was overwhelmed by scheduling, and the tools Auburn gives you aren't built for a freshman trying to figure it out alone. That's the best kind of idea, because I'm the customer.</p>"
"<p>The hard truth: Degree Works and Stellic already exist, and selling to a university can take one to two years. Twenty-two survey responses is a signal, not proof. The thing I have to get right is trust. A confident wrong answer here costs somebody a semester, so it has to show its work every time.</p>",
"next": "<p>Build a working version on real Bulletin data, survey a bigger group of students, and get it in front of actual advisors.</p>",
},
# ================================================================ AU DINING
{
"slug": "au-dining", "cat": "build", "status": "inuse", "featured": True, "logo": "au-dining-logo.png",
"proof": ["<figure class='panel pimg phone-shot'><img src='au-dining-screenshot.jpg' alt='The real app on my phone: all three halls, every meal and live hours' loading='lazy'><figcaption>The real app on my phone: all three halls, every meal and live hours</figcaption></figure>"],
"title": "AU Dining",
"kicker": "All three Auburn dining hall menus in one place, organized the way they should be, with calories and protein built in.",
"card": "The Edge, Tiger Zone and Wellness Kitchen menus in one app, with calorie and protein filters and meal building.",
"when": "2026 – Present", "role": "Solo builder (vibe coded)",
"stack": ["Google Apps Script", "Auburn dining data", "Web app"],
"sections": [
("Why I built it",
"<p>I just wanted to see all three dining hall menus at once. The Edge, Tiger Zone and Wellness Kitchen were each on a different website, and they were organized in the worst way possible. So I built one place that shows all three, cleanly.</p>"
"<p>Once that worked, I kept going: calories, protein, filters and building meals.</p>"),
("What it does",
"<ul class='feat'>"
"<li><b>All three halls in one place</b>: The Edge, Tiger Zone and Wellness Kitchen, pulled live from Auburn's own dining data when you open the app</li>"
"<li><b>Every meal</b>: breakfast, brunch, lunch and dinner by hall, with posted hours, plus a Today/Tomorrow toggle</li>"
"<li><b>Filters</b>: vegetarian, vegan, made without gluten, high protein (20g+), and a calorie range</li>"
"<li><b>Where to Go</b>: ranks the halls by walking distance, your class schedule and the foods you like</li>"
"<li><b>Build My Plate</b>: builds a meal close to your calorie target</li>"
"<li><b>Station alerts</b>: a morning email if Auburn adds, removes or renames a station</li>"
"</ul>"
"<p>It's on my phone's home screen as an app, and everything saves on your phone with no account needed.</p>" + VIBE),
],
"demo": None,
"results": [("3","dining halls in one place"),("20g+","protein filter"),("Live","menus when you open it")],
"honest":
"<p>Version one got way too crowded. I kept piling on features until it was overwhelming, so I redesigned it around four simple tabs: Menus, For You, Schedule and Profile. That redesign is what made it actually usable.</p>"
"<p>Pulling Auburn's real data fixed a lot too. I had typed-in hours that were wrong, and breakfast and dinner items were getting mixed together. Lesson: never hard-code something that already exists as real data.</p>",
"next": "<p>Sync meal swipe balances automatically (right now it's a manual counter), move it to its own hosting so it feels like a real app, and get it into more students' hands.</p>",
},
# ================================================================ AU RECAPS
{
"slug": "au-recaps", "cat": "write", "status": "ongoing", "featured": True, "logo": "au-recaps-logo.png",
"title": "AU Recaps",
"kicker": "My own Auburn football game recaps, written after every game and sent to a growing email list.",
"card": "Game-by-game Auburn football recaps with Three Stars and The Good, the Bad & the Ugly. On Substack and emailed to a growing list.",
"when": "Fall 2026 – Present", "role": "Writer",
"stack": ["Writing", "Substack", "Claude Projects", "ESPN box scores"],
"links": [("Read AU Recaps on Substack", "https://substack.com/@andrewmish")],
"sections": [
("What it is",
"<p>After every Auburn game, I write a recap: what happened, who showed up, and what I actually think. Every recap has <b>Three Stars</b> and a <b>Good, Bad & Ugly</b> section. It goes out to an email list that keeps growing, and it's on <a href='https://substack.com/@andrewmish' target='_blank' rel='noopener'>my Substack</a>.</p>"),
("How I write it",
"<p>I talk through my notes and reactions right after the game. Claude checks my facts against the ESPN play-by-play and box score, asks me questions, and drafts it. Then I rewrite it heavily in my own voice. I set it up as a Claude Project called AU RECAP, with my style rules saved, so every week starts from the same place.</p>"),
],
"demo": None,
"results": [("1","recap per game"),("~1,200+","words each")],
"honest":
"<p>This is the most fun thing on this page. It's the same skill as everything else I do: take what's in my head and turn it into something real that people read, on a deadline.</p>",
"next": "<p>Keep growing the list, one game at a time.</p>",
},
# ================================================================ TRADE TRACKER
{
"slug": "trade-tracker", "cat": "build", "status": "live", "featured": False,
"title": "Congressional Trade Tracker",
"kicker": "An automated system that watches public congressional stock-trade filings and emails me instructions to hand to Claude.",
"card": "Checks House disclosure filings every 6 hours, reads the PDFs, and emails me a prompt to paste into Claude, which handles the trade after I confirm.",
"when": "2026", "role": "Solo builder (vibe coded)",
"stack": ["Google Apps Script", "OCR", "Google Sheets", "Claude"],
"sections": [
("The idea",
"<p>Members of Congress have to publicly disclose their stock trades. Paid apps copy those trades for you. I wanted to see if I could build the same thing myself for free.</p>"),
("How it works",
"<p>Every 6 hours, Apps Script checks the House Clerk's disclosure site for new filings and reads the PDFs with OCR. It figures out the proportional trades, logs everything to a sheet, and emails me.</p>"
"<p>The email isn't just a summary. It's a set of instructions to copy and paste into Claude, which is connected to my brokerage account. Claude then does the work: it confirms every trade with me before placing it, sticks to common stock only (no options, no margin) and doesn't change anything based on its own opinion.</p>"
"<p>Tiny trades under the $1 minimum build up until they're big enough. There's a cap on trade size, and anything it can't read gets flagged for me instead of guessed.</p>" + VIBE),
],
"demo": "pipeline_trades",
"results": [("6 hrs","between checks"),("100%","of trades confirmed by me"),("0","guesses on unreadable filings")],
"honest":
"<p>My first plan was to have the script place trades directly through the brokerage. I spent days fighting login and permission restrictions before giving up on that and switching to \"email me instructions, Claude executes, I confirm.\" It turned out to be the better design anyway, because I stay in the loop on every trade.</p>"
"<p>The other reality: filings can show up as late as 45 days after the trade, so you're always copying old moves. It's a great automation project. I wouldn't call it an investing edge.</p>"
"<p class='note-sm'>Personal project using public data. Not investment advice.</p>",
"next": "<p>Let it run long enough to compare it against just holding an index fund.</p>",
},
# ================================================================ COMMAND CENTER
{
"slug": "command-center", "cat": "build", "status": "live", "featured": False, "image": "command-center-city.jpg", "card_image": "command-center-city.jpg",
"title": "Automation Command Center",
"kicker": "A SimCity-style night city where every automation I run is a district I can click into.",
"card": "A living 3D map of my automation stack. Each district is a running project, and each building opens its dashboard.",
"when": "2026", "role": "Solo builder (vibe coded)",
"stack": ["Muse", "Google Apps Script", "Plaid", "Claude", "Python"],
"sections": [
("The idea",
"<p>A friend showed me a 3D dashboard of all his automations and I wanted one of my own. Not a spreadsheet of scheduled jobs, but a city. So I built one: a night-time SimCity-style map where each district is an automation and clicking a building opens its dashboard.</p>"),
("The districts",
"<p><strong>Trading Floor</strong>: my portfolio, refreshed hourly. <strong>Civic Center</strong>: a Canvas watchdog that pings me about upcoming assignments. <strong>Fitness District</strong>: SweatBuddies verdicts and forfeit tracking. <strong>Bakery Row</strong>: orders and payments for a sourdough side business. <strong>Capitol</strong>: the congressional trade tracker. <strong>News Tower</strong>: a twice-daily news briefing. <strong>Storage Watch</strong>: a weekly Mac cleanup scan. The Media District (social content) is paused for now.</p>"),
],
"demo": None,
"results": [("8", "districts on the map"), ("1", "click from city to any dashboard"), ("0", "spreadsheets of scheduled jobs")],
"honest":
"<p>The building statuses are set by hand for now. Wiring live telemetry into each district is the next step. And the city doesn't have a name yet. Naming it is somehow the hardest part of the whole project.</p>",
"next": "<p>Wire real automation health into the map, then name the city.</p>",
},
# ================================================================ SWEATBUDDIES
{
"slug": "sweatbuddies", "cat": "build", "status": "inuse", "featured": False, "logo": "sweatbuddies-logo.svg",
"title": "SweatBuddies",
"kicker": "A two-person workout accountability app with photo check-ins, weekly goals, and real stakes if you slack off.",
"card": "Photo-proof workouts, streaks, weekly goals, and an IOU system: miss your goal and you owe your partner.",
"when": "2025 – Present", "role": "Solo builder (vibe coded)",
"stack": ["Google Apps Script", "Google Sheets", "Google Drive"],
"sections": [
("Why I built it",
"<p>Accountability apps exist, but I wanted one built exactly for me and my workout partner, with stakes that actually matter to us.</p>"),
("What it does",
"<ul class='feat'>"
"<li><b>Photo check-ins</b> stored in Drive as proof of every workout</li>"
"<li><b>Weekly goal ring + streaks</b> that track your progress</li>"
"<li><b>IOUs</b>: every Monday it scores the week, and whoever missed owes the other person a coffee, $10, flowers or a custom penalty, with claim, confirm and dispute steps</li>"
"<li><b>Thursday nudge</b> if you're behind, plus comments and likes on each other's workouts</li>"
"</ul>" + VIBE),
],
"demo": "ring_sweat",
"results": [("2","users (on purpose)"),("Daily","actual use"),("14","max workouts / week")],
"honest":
"<p>This is the one I actually use every day, and that's what made it good. Every bug I found came from real use. Two workouts in one day only counted once. The progress ring stayed at zero because Google Sheets was quietly converting my dates. Small bugs, but you only find them by using your own product.</p>",
"next": "<p>Maybe open it up to more pairs. For now it does exactly what we need.</p>",
},
# ================================================================ BARBER BOT
{
"slug": "barber-bot", "cat": "build", "status": "poc", "featured": True, "logo": "barber-bot-logo.svg",
"title": "AI Barber Bot",
"kicker": "A text-message scheduling assistant for barbershops. Text it like you'd text your barber, and Claude figures out what you want.",
"card": "Twilio + Claude SMS bot that turns messy texts like \"can I get a fade fri after 3\" into structured booking requests. Proof of concept.",
"when": "2025 – Present", "role": "Solo builder (vibe coded)",
"stack": ["Twilio Functions", "Claude API", "SMS"],
"sections": [
("Why I built it",
"<p>Most barbers book appointments by text, between cuts, with their hands full. Clients send things like \"yo can I get in friday after 3 for a fade.\" That's easy for a person to read and annoying for software, which is exactly what AI is good at.</p>"),
("How it works",
"<p>A client texts the shop's Twilio number. A Twilio Function sends the message to Claude with a strict prompt: pull out the name, date, time, service and intent (new booking, cancel, reschedule or question), plus a confidence level, and return <strong>only JSON</strong>. The bot replies based on the intent, so cancellations and reschedules get different responses than new bookings.</p>"
"<p>If anything breaks (bad JSON, an API error), it falls back to a friendly \"we'll get back to you\" instead of leaving the client hanging.</p>" + VIBE),
],
"demo": "sms_barber",
"results": [("6","fields pulled from each text"),("4","intents handled")],
"honest":
"<p>Honestly, I haven't gotten this fully working end to end yet. The proof of concept is there: it understands requests really well. But it doesn't check a calendar or lock in the appointment, so a human still confirms.</p>"
"<p>The interesting lesson was forcing the AI to answer in JSON only. Once the output is structured, everything after it is just normal logic, and that's how I build almost everything now.</p>",
"next": "<p>Connect it to a real calendar so it can check availability and confirm on its own, add reminder texts, and get one real barbershop to pilot it.</p>",
},
# ================================================================ IDEAS
{
"slug": "ideas", "cat": "venture", "status": "idea", "featured": True,
"title": "The Idea Pipeline",
"kicker": "I keep a running list of business ideas, 100+ and counting. Here's every one, and how I decide which are worth building.",
"card": "100+ ideas on the list. I ran a batch of 96 through an AI-scored diagnostic, pushed back where it got things wrong, and picked Prereq to pitch.",
"when": "Ongoing", "role": "Founder",
"stack": ["Customer research", "Competitive research", "AI scoring"],
"sections": [
("How I filter ideas",
"<p>Ideas are cheap. I've got a notes app with 100+ of them. Before Auburn's Ideas Jam (screened in September 2026), I had Claude score a batch of 96 against the Ideas Jam judging rubric (out of 70) and run a blunt product diagnostic on each: who has the problem, how badly, what they use now, and whether anyone would pay.</p>"
"<p>The AI did the scoring, and I didn't just take its word for it. When I thought it got something wrong, I pushed back, and I was right more than once:</p>"
"<ul class='feat'>"
"<li><b>Real estate reports</b>: I told it the idea was proven because I know someone who does basically this and makes a lot of money. It rescored it to the top of the list.</li>"
"<li><b>Designated driver service</b>: it assumed I meant college campuses only. I meant anywhere, and it conceded.</li>"
"<li><b>The \"prop\" score</b>: it invented a criterion for whether you could bring a prop to the pitch. That isn't the point of the Ideas Jam, so we threw it out.</li>"
"<li><b>EASy Clean</b>: it doubted the device would work, so I ran a petri dish test myself.</li>"
"</ul>"),
("The ones still alive", "__IDEAS_KEEP_DATED__"),
("The full list", "__IDEAS_LOCKED__"),
],
"demo": "funnel_ideas",
"results": [("100+","ideas on the list"),("96","scored"),("~12","still alive"),("1","pitched: Prereq")],
"honest":
"<p>The most useful (and annoying) feedback I got: a lot of my ideas came from imagination, not observation. The good ones start with a problem you've actually watched someone deal with, like Prereq, which started with me staring at DegreeWorks.</p>"
"<p>The other lesson was about using AI to judge ideas. It's fast and it's blunt, which is great. But it's also confidently wrong sometimes, and you have to be willing to argue with it.</p>",
"next": "<p>Talk to real customers for the top few, and kill or build each one based on what they say, not on what I think.</p>",
},
# ================================================================ EASY CLEAN
{
"slug": "easy-clean", "cat": "eng", "status": "done", "featured": True, "logo": "easy-clean-logo.svg", "image": "easy-clean-prototype.jpg",
"title": "EASy Clean",
"kicker": "My PLTW capstone: a UV chair cover that sanitizes the clothes you're not sure are clean or dirty.",
"card": "PLTW Engineering Design & Development capstone. 323 survey responses, 4 design pivots, and a working prototype built for ~$104.",
"when": "2025 – 2026 school year", "role": "Team of 3 (with Sebastian White & Emily Paine)",
"stack": ["Fusion 360 CAD", "UV-A LED strips", "Soldering", "Survey research", "Petri dish testing"],
"sections": [
("The problem",
"<p>Everybody has <em>the chair</em>, the one in your room covered in clothes you wore once. They're not dirty enough to wash and not clean enough to put away. Washing them anyway wastes water (about 41 gallons a load), and sprays like Febreze only cover up the smell.</p>"
"<p>We surveyed people to see if this was real. <strong>323 responses</strong> later, it was.</p>"),
("How it evolved",
"<p>This project changed direction more than anything else I've built. We started with UV light, switched to a heated-airflow cabinet, then a two-part heat-and-cool cabinet. After a design review, we realized we'd been designing a whole appliance when the problem was literally a chair. So we went back to UV and turned it into a <strong>chair cover</strong>.</p>"
"<ul class='steps'><li><b>01</b> UV cabinet idea</li><li><b>02</b> Heated airflow cabinet (won our decision matrix)</li><li><b>03</b> Top/bottom heat + cool cabinet</li><li><b>04</b> UV chair cover (final, Feb 2026)</li></ul>"),
("The final build",
"<p>A polyester cover that drapes over any desk chair, with UV-A LED strips attached by Velcro so you can pull the electronics off and wash the cover.</p>"
"<p><strong>Why UV-A and not UV-C?</strong> UV-C is the type that kills germs fastest, but it can burn skin and damage eyes, so it isn't safe for something sitting in your bedroom. UV-A is much weaker at killing bacteria but far safer around people. We chose safety, and we knew it would cost us cleaning power.</p>"
"<p>We wrote 8 design requirements, including at least 80% bacteria reduction, a cycle of 15 minutes or less, a footprint under 2 cubic feet, and more than 90% of the garment exposed to light. We compared 6 concepts in a decision matrix and benchmarked against washers, sprays, charcoal bags and an existing UV-cabinet patent. Budget was about $100; we came in at <strong>$103.57</strong>.</p>"),
("Testing",
"<p><strong>Durability:</strong> passed. We pulled the light strips off and put them back repeatedly, and neither the Velcro nor the adhesive lifted.</p>"
"<p><strong>Bacteria:</strong> our first round of petri dishes failed. Condensation built up under the lights and nothing grew, not even on the control, so we got no data. We switched dishes and ran it again. That time the treated dish showed no growth and the control showed heavy growth. It's an informal classroom test, not a lab result, but it was the result we wanted.</p>"),
],
"demo": "survey_easy",
"proof": ["<figure class='panel pimg '><img src='easy-clean-prototype.jpg' alt='The final prototype: UV-A LED strips on the chair cover, and the battery pack on the back' loading='lazy'><figcaption>The final prototype: UV-A LED strips on the chair cover, and the battery pack on the back</figcaption></figure><figure class='panel pimg '><img src='easy-clean-build.jpg' alt='Mid-build: attaching the light strips with Velcro' loading='lazy'><figcaption>Mid-build: attaching the light strips with Velcro</figcaption></figure><figure class='panel pimg '><img src='easy-clean-sketches.jpg' alt='Our design sketches: the final UV chair (left) and the earlier steam + freezer cabinet (right)' loading='lazy'><figcaption>Our design sketches: the final UV chair (left) and the earlier steam + freezer cabinet (right)</figcaption></figure>"],
"results": [("323","survey responses"),("76.2%","re-wear clothes"),("6","concepts scored"),("$103.57","prototype cost")],
"honest":
"<p>We pivoted late, and it cost us. Changing to the chair cover in February meant relearning CAD, soldering and connectors on a deadline. But it was the right call. The cabinet was a cool engineering problem; the chair cover actually fits how people live.</p>"
"<p>The weakest part of the build is how the lights attach. Right now the Velcro is glued on, and glue won't survive a lot of trips through the wash. Next time I'd have the Velcro sewn into the cover so it holds up long-term.</p>",
"next": "<p>Figure out whether this could be a real product. A UV device that claims to kill bacteria counts as a regulated pesticide device under EPA rules, so that's the first wall to look at.</p>",
"links": [("Original team project site (school account)", "https://sites.google.com/spaldinghs.org/sea/home")],
},
# ================================================================ COLLABIFY
{
"slug": "collabify", "cat": "venture", "status": "paused", "featured": False, "logo": "collabify-logo.png",
"title": "Collabify",
"kicker": "An iOS app to match small businesses with influencers for paid promotions. It's like a dating app for brand deals.",
"card": "An iOS app prototype I vibe coded in Xcode, then pressure-tested hard enough to pause.",
"when": "2025", "role": "Founder (vibe coded)",
"stack": ["SwiftUI", "Xcode", "iOS", "Claude"],
"sections": [
("The idea",
"<p>Small businesses want influencer marketing but don't know where to start. Small influencers want paid deals but can't find them. Collabify would match the two sides, handle payment in the app, and take a small fee.</p>"),
("What I built",
"<p>I built an iOS prototype in Xcode with SwiftUI: profiles for both sides, the matching flow, and separate dashboards for businesses and creators. To be clear, I don't know Swift. I built it the way I build everything, by directing AI, testing what it made and pushing back until it worked.</p>"),
],
"demo": None,
"results": [("2","sided marketplace"),("1","iOS prototype")],
"honest":
"<p>When I seriously pressure-tested this, it didn't hold up. Collabstr, Aspire and JoinBrands already do this, and I had zero real evidence that businesses would pay for my version. So I paused it.</p>"
"<p>It still wasn't wasted. It was my first time building an iOS app, and I learned to look for proof of demand <em>before</em> building anything. My instinct now is \"something like this probably already exists, so go find it first.\"</p>",
"next": "<p>Parked. A local, Auburn-only version is the one angle that still looked alive.</p>",
},
# ================================================================ PLTW
{
"slug": "pltw", "cat": "eng", "status": "done", "featured": True, "logo": "pltw-logo.png",
"title": "PLTW Engineering",
"kicker": "Four years of Project Lead The Way engineering at Archbishop Spalding: CAD, prototyping, robotics, and a lot of trial and error.",
"card": "Four years, four PLTW courses: IED, POE, Digital Electronics and the EDD capstone. Catapults, 3D printing, robotics, logic circuits and EASy Clean.",
"when": "2022 – 2026", "role": "PLTW Engineering student (4 years)",
"stack": ["Fusion 360", "3D printing", "Laser cutting", "VEX robotics", "Digital circuits", "Engineering design process"],
"sections": [
("Intro to Engineering Design (IED)",
"<div class='builds'>"
"<div class='build'><h4>Carnival game launcher</h4><p>A popsicle-stick catapult built to knock down a tower of 10 cups. On test day we pulled off a rubber band at the last second, trading power for accuracy. It worked.</p></div>"
"<div class='build'><h4>Block project</h4><p>Built a 7–10 block shape and sketched every orthographic view, including hidden lines. The hard part wasn't the drawing, it was designing a shape that hit every constraint.</p></div>"
"<div class='build'><h4>3D-printed ornament</h4><p>A gift-box ornament in Fusion 360 that had to fit in a 3×3×0.5 in. box. I forgot to account for the bow's height and had to scale the whole thing down.</p></div>"
"<div class='build'><h4>Miniature train</h4><p>Modeled every component of a train in Fusion 360, assembled it, and produced a 5-sheet technical drawing set with exploded views and dimensions.</p></div>"
"<div class='build'><h4>Reverse engineering</h4><p>Took apart a real product with my team, analyzed how each part worked, and rebuilt every component in CAD to the right dimensions.</p></div>"
"<div class='build'><h4>Automata</h4><p>A moving desk toy based on the Chrome dinosaur game. I picked the wrong cams and had already glued everything, so I improvised with hot glue and tape to get the dino jumping higher.</p></div>"
"</div>"),
("Principles of Engineering (POE)",
"<div class='builds'>"
"<div class='build'><h4>Self-driving vehicle</h4><p>Programmed a robot with dead-reckoning navigation to drive a path around a table without falling off. The final run turned right at the edge.</p></div>"
"<div class='build'><h4>VEX gear-ratio car</h4><p>Designed and raced a VEX car optimized through gear ratios. Our parts didn't line up, so we pushed a long screw through two plates at an angle to make it work.</p></div>"
"</div>"),
("Digital Electronics (DE), junior year",
"<div class='builds'>"
"<div class='build'><h4>Random number generator</h4><p>Assembled and soldered a working circuit board. It didn't work at first because of one misaligned component, so I traced the connections, found it and fixed it.</p></div>"
"<div class='build'><h4>Majority vote machine</h4><p>A four-person board voting machine where the president breaks ties, built using only AND, OR and inverter gates. Simplifying the circuit took my team many failed iterations before we got it.</p></div>"
"<div class='build'><h4>Fireplace safety circuit</h4><p>Redesigned a gas fireplace's shut-off logic so it stays on when 3 of 4 flame sensors agree, using only NAND gates, plus a faulty-sensor indicator using only NOR gates. Truth tables, K-maps, Multisim, then a real breadboard.</p></div>"
"<div class='build'><h4>Seven-segment date display</h4><p>A combinational circuit that counts through 8 states and drives a seven-segment display to show a date. Two segments were wrong until I went back and rechecked my K-map expressions.</p></div>"
"</div>"),
("Engineering Design & Development (EDD), senior year",
"<p>My senior capstone, <a href='easy-clean.html'>EASy Clean</a>: a full year taking a real problem from research to a working, tested prototype, documented across 9 design elements.</p>"),
],
"demo": None,
"results": [("4","PLTW courses, 4 years"),("21+","documented projects & design elements"),("1","year-long capstone")],
"honest":
"<p>PLTW is where I learned how to build anything. Not the specific tools, but the process: define the problem, research what already exists, generate options, score them in a decision matrix, prototype, test, and change direction when the test tells you to. EASy Clean pivoted four times because of that process.</p>"
"<p>I use the exact same loop now, just with software and business ideas instead of popsicle sticks and Fusion 360.</p>",
"next": None,
"links": [("Original class portfolio (school account)", "https://sites.google.com/spaldinghs.org/andrewmish-engineeringportfoli/home")],
},
# ================================================================ CLUB AMERICA
{
"slug": "club-america", "cat": "lead", "status": "done", "featured": False, "logo": "https://www.clubamerica.com/images/menu/club-america-logo.webp",
"title": "Club America (TPUSA) Chapter",
"kicker": "I led a group of classmates in starting a Club America chapter, Turning Point USA's high school program, at Archbishop Spalding.",
"card": "Led the push to start a Club America (TPUSA) chapter at Archbishop Spalding and got 35+ students to sign up. The school wouldn't approve it.",
"when": "Sept 2025", "role": "Founder & student leader",
"stack": ["Leadership", "Organizing", "Recruiting"],
"sections": [
("What happened",
"<p>Right after Charlie Kirk was shot in September 2025, a group of my classmates and I wanted to start a Club America chapter, Turning Point USA's high school program, at Archbishop Spalding. I took the leadership role and organized the effort.</p>"
"<p>We got <b>35+ students</b> to put their names down to join. The school wouldn't approve the club, and it was shut down before it got off the ground.</p>"),
],
"demo": None,
"results": [("35+","students signed up")],
"honest":
"<p>It didn't end the way I wanted, but it showed me I can rally people around something fast. Getting 35+ students to commit in a short window is the same skill as getting early users for anything I build.</p>",
"next": "<p>I'm now involved with Conservatives at Auburn, Turning Point USA's college chapter.</p>",
},
# ================================================================ ENTREPRENEURSHIP CLUB
{
"slug": "entrepreneurship-club", "cat": "lead", "status": "done", "featured": False, "proof": ["<figure class='panel pimg phone-shot'><img src='entrepreneurship-club-flyer.jpg' alt='Entrepreneurship Club recruiting flyer' loading='lazy'><figcaption>The flyer I made to recruit members. The QR code went to the sign-up form.</figcaption></figure>"],
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
# ================================================================ JOBS
{
"slug": "walden", "cat": "job", "status": "done", "featured": False, "logo": "https://cdn.cybergolf.com/images/1309/Walden-CC_logo-trans-web.png",
"title": "Walden Country Club",
"kicker": "Golf Cart Attendant & Kitchen Assistant, Crofton, MD.",
"card": "Started in the kitchen washing dishes, then moved to the cart barn: a 70-cart fleet and 5 new hires trained.",
"when": "May 2024 – Sept 2025", "role": "Golf Cart Attendant & Kitchen Assistant",
"stack": ["Teamwork", "Training", "Hard work"],
"sections": [
("First: Kitchen Assistant",
"<p>I started out in the kitchen.</p><ul class='feat'><li>Long shifts on my feet, washing dishes and keeping up during busy service</li>"
"<li>Prepping and helping the cooks wherever they needed it</li></ul>"),
("Then: Golf Cart Attendant",
"<p>Partway through, I switched over to the cart barn for the rest of my time there.</p><ul class='feat'><li>Coordinated a <b>70-cart fleet</b> with teammates so members stayed on schedule at peak tee times</li>"
"<li>Trained <b>5 new employees</b></li></ul>"),
],
"demo": None, "results": [("70","carts"),("5","employees trained")],
"honest": "<p>The kitchen side of this job was the real work: hours on my feet, a lot of dishes, and the kitchen staff didn't get a share of the tips. It wasn't glamorous, but it taught me how to grind through a shift and still do the job right.</p>",
"next": None,
},
{
"slug": "wild-birds", "cat": "job", "status": "done", "featured": False, "logo": "https://gambrills.wbu.com/templates/wbu3/staticresources/assets/images/logo.webp",
"title": "Wild Birds Unlimited",
"kicker": "Sales Associate, Gambrills, MD.",
"card": "Advised ~50 customers per shift and kept the stockroom running: unloading, labeling and stacking pallets of birdseed.",
"when": "June 2023 – Dec 2023", "role": "Sales Associate",
"stack": ["Sales", "Customer service", "Inventory"],
"sections": [
("Sales floor",
"<ul class='feat'><li>Advised around <b>50 customers per shift</b>, building rapport and matching products to what they actually needed</li>"
"<li>Answered questions on feeders, seed and what attracts which birds</li></ul>"),
("Stockroom",
"<ul class='feat'><li>Unloaded pallets of birdseed when deliveries came in</li>"
"<li>Organized, labeled and stacked the bags in the back of the store</li>"
"<li>Pulled stock from the back to keep the floor full</li></ul>"),
],
"demo": None, "results": [("~50","customers / shift")],
"honest": "<p>Half this job was sales and half was manual labor. On the sales side I learned that selling is really just listening: people came in knowing their problem, not the product. On the stockroom side I learned that a lot of work is just showing up and moving the heavy stuff.</p>",
"next": None,
},
{
"slug": "waugh-chapel", "cat": "job", "status": "done", "featured": False, "logo": "waugh-chapel-logo.png",
"title": "Waugh Chapel Swim Club",
"kicker": "Snack Bar Attendant, Gambrills, MD.",
"card": "Cooked a lot of food, handled cash and served guests through peak summer rushes.",
"when": "May 2023 – Sept 2023", "role": "Snack Bar Attendant",
"stack": ["Cash handling", "Food prep", "Working under pressure"],
"sections": [("What I did",
"<ul class='feat'><li>Made a lot of food for a lot of hungry swimmers</li>"
"<li>Handled cash accurately and served guests under pressure during peak summer rushes</li></ul>")],
"demo": None, "results": [],
"honest": "<p>My first job, and honestly not one I loved. It was hot, nonstop and repetitive. But it taught me to stay calm and keep moving when the line is out the door, and it made me want to build things that make work less miserable.</p>",
"next": None,
},
]

# ---------------------------------------------------------------- idea list
# (title, one-line description). KEEP = still alive.
IDEAS_KEEP = [
("Prereq", "A conversational AI that builds your class schedule. Picked to pitch."),
("AI land & zoning reports", "Fast reports on a property or lot for developers and investors."),
("EasyEats", "A budget-capped meal plan that turns into a grocery cart. Prototyped with two friends."),
("Sidewalk gum removal", "A service for a gross, expensive problem nobody wants to deal with."),
("Designated driver service", "Two drivers come to you, so you and your car both get home."),
("EASy Clean", "The UV chair cover from my PLTW capstone."),
("AI barber booking bot", "Text-message booking for barbershops."),
("Elderly ride service", "Reliable rides for older adults."),
("Dining-hall delivery", "Dining hall food delivered, funded by a meal-plan markup."),
("High school golf livestreams", "Streaming high school golf matches."),
("Microwave bulking dinners", "High-protein, high-calorie microwave meals."),
("Composting app", "Making composting easy to start and stick with."),
]

IDEAS_LIST_UPDATED = "October 13, 2026"
IDEAS_SCREENED = "September 2026"
IDEAS_COUNT = 102

EDUCATION = [
("Auburn University", "B.S. Business Administration · Pre-Business (Intended Finance) · Intended Real Estate minor", "Expected May 2030", "https://ocm.auburn.edu/brand-center/logos/auburn/informal_horiz/fullcolor/auburn_informal_h_fullcolor_digital.png", "crop"),
("Archbishop Spalding High School", "GPA 4.2 · PLTW Engineering (4 years) · Golf (2-year varsity)", "2022 – 2026", "spalding-logo.png"),
]

HONORS = [
"Pioneer Leadership Scholarship, 4-year recipient",
"National Honor Society",
"Honor Roll, 8 semesters",
]

# (name, what I do / note, logo url)
CL = "https://se-images.campuslabs.com/clink/images/"
INVOLVEMENT = [
("New Venture Accelerator", "Accepted with Prereq · Oct 2026", "https://nva.auburn.edu/files/2022/05/logo-newventure-white-icon2-01.png", "dark"),
("Auburn Ideas Jam", "Pitched Prereq · Harbert College of Business, Sept 2026", "ideas-jam-logo.png", ""),
("Investment Club at Auburn", "Member", CL + "ca6cacb7-472c-4137-9b83-0a3a7b2d4a98caf8b9b5-e3ad-4a1e-b71b-903c574b449b.PNG?preset=med-sq", ""),
("Financial Literacy Club", "Member", "financial-literacy-logo.png", "fill"),
("Entrepreneurs at Auburn", "Member", CL + "d6fd89fc-10c7-4a0a-b35e-c3fea4c06fbcbdcfb4c8-db04-4341-b254-f401ef680841.png?preset=med-sq", ""),
("AI Experience at Auburn", "Member", CL + "02410c89-d28e-42bf-9ef2-7dd2a266f32639aaea47-a32d-4c3b-aa61-efe2e469274e.png?preset=med-sq", ""),
("AU Catholics", "Auburn Catholic Campus Ministry", "https://se-images.campuslabs.com/clink/images/2e6a3869-48df-4b28-8e76-4a3c1be4f96fb1da0333-d3f0-4918-9ba5-872aca162d06.png?preset=med-sq", ""),
("College Republicans at Auburn", "Member", CL + "420e4728-7d07-4b51-b83c-7f3e5fdc214a85f88b04-abb8-477c-a4a0-ecaeb47c500b.jpeg?preset=med-sq", ""),
("Students for Life at Auburn", "Member", CL + "0f4aabf6-2857-4eb6-b1a8-af900d4602e29bfac61d-b601-49fb-94c6-1daf200c9806.jpg?preset=med-sq", ""),
("Conservatives at Auburn (Turning Point USA)", "Member", CL + "3845cde7-b8c1-42ac-bdd9-387087b564d756700907-7df4-4204-93f6-34634d60e9c7.png?preset=med-sq", ""),
]

SKILLS = {
"How I build": ["Vibe coding with Claude", "Testing & QA", "Prompting", "Plain-English specs"],
"Tools I build on": ["Claude & Claude API", "Google Apps Script", "AppSheet", "Google Sheets", "Twilio", "ElevenLabs"],
"Platforms": ["AWS", "Google Cloud", "DocuSign", "Slack", "Xcode", "Fusion 360"],
"Business": ["Customer research", "Pitching", "Process improvement", "Training"],
}
