"""
=====================================================================
 portfolio_content.py — CENTRAL, EDITABLE CONTENT
=====================================================================
Everything a student might want to update lives in this one file.
You should NOT need to edit app.py or any HTML/CSS to add a link,
a project, a certificate or a reflection.

HOW TO EDIT
-----------
* Any value that is an empty string "" is treated as "not provided yet".
  The app will show a friendly placeholder instead of breaking.
* To add a link, paste the URL inside the quotes, e.g.
      "presentation_url": "https://www.canva.com/design/xxxx/view",
* To add an image, drop the file into the matching assets/ folder and
  write its relative path, e.g. "image": "assets/projects/waterbuddy.png".
* Keep the structure (the words before the colon) exactly the same.
=====================================================================
"""

# ---------------------------------------------------------------------
# STATUS LABELS
# ---------------------------------------------------------------------
IA_STATUS = "In Progress"

# ---------------------------------------------------------------------
# STUDENT PROFILE  (About Me + Contact)
# ---------------------------------------------------------------------
STUDENT = {
    "name": "Harini Priya Karthikeyan",
    "short_name": "Harini Priya K.",
    "grade": "Grade 12",
    "programme": "International Baccalaureate Career-related Programme (IBCP)",
    "school": "Jain Vidyalaya IB World School",
    "crs": "Artificial Intelligence",
    "quote": "Rooted in tradition, growing in knowledge.",
    # Optional profile photo. Leave the path; if the file is missing a
    # neat placeholder is shown automatically.
    "profile_image": "assets/profile.jpg",
}

# ---------------------------------------------------------------------
# CONTACT  (Page 7 — "Let's Connect")
# Only information you intentionally fill in is shown. Empty values
# display a "to be added" note instead of a broken link.
# ---------------------------------------------------------------------
CONTACT = {
    "email": "",      # e.g. "harini@example.com"
    "github": "",     # e.g. "https://github.com/username"
    "linkedin": "",   # e.g. "https://www.linkedin.com/in/username"
    "thank_you": (
        "Thank you for exploring my portfolio. It reflects my academic learning, "
        "practical projects, personal development, and experiences throughout the IBCP. "
        "I look forward to continuing my learning journey and exploring new opportunities "
        "in Computer Science and Artificial Intelligence."
    ),
}

# ---------------------------------------------------------------------
# NAVIGATION  (order matters — do not reorder)
# ---------------------------------------------------------------------
MAIN_NAV = [
    "About Me",
    "DP Subjects",
    "Core Components",
    "AI Career-related Studies",
    "Activities & Interests",
    "Certificates & Achievements",
    "Contact",
]

DP_NAV = ["Physics HL", "Chemistry SL", "Mathematics AA HL", "English B SL"]

CORE_NAV = [
    "Personal and Professional Skills",
    "Language and Cultural Studies",
    "Reflective Project",
    "Community Engagement",
]

# ---------------------------------------------------------------------
# PAGE 1 — ABOUT ME
# ---------------------------------------------------------------------
ABOUT = {
    "hero_title": "Hello, I'm Harini Priya Karthikeyan.",
    "subtitle": "IBCP Student | Artificial Intelligence",
    "intro": (
        "Welcome to my portfolio! I am a Grade 12 IBCP student exploring my interests in "
        "technology, learning, and personal development. This portfolio brings together my "
        "academic experiences, projects, reflections, and activities throughout my learning journey."
    ),
    "who_i_am": (
        "I am a student who enjoys learning how things work and finding ways to use technology "
        "to solve everyday problems. Artificial Intelligence interests me because it combines "
        "programming, logic, and creativity. I like building small applications with Python, "
        "testing my ideas, and improving them step by step. Alongside technology, I enjoy creative "
        "work, learning new things, and taking on challenges that help me grow."
    ),
    "why_ibcp": (
        "I chose the IBCP because it lets me connect my academic subjects with practical, "
        "career-related learning. Through the programme, I can explore Artificial Intelligence by "
        "building programming projects while also developing communication, research, collaboration, "
        "and professional skills. The balance between academic study and hands-on work suits the way "
        "I like to learn."
    ),
    "why_ai": (
        "My interest in Artificial Intelligence comes from wanting to use Python and technology to "
        "solve practical problems. I enjoy turning an idea into a working application and seeing how "
        "it can help someone. Building these projects has made me more curious about how software is "
        "designed and has encouraged me to learn more about Computer Science."
    ),
    # Quick facts shown as a small list
    "journey_facts": [
        ("Current level", "Grade 12"),
        ("Programme", "International Baccalaureate Career-related Programme"),
        ("School", "Jain Vidyalaya IB World School"),
        ("Career-related Study", "Artificial Intelligence"),
    ],
    # Academic timeline
    "journey_timeline": [
        ("School learning",
         "Building a foundation across my subjects and discovering an interest in technology, "
         "problem-solving and creative work."),
        ("Grade 11",
         "Beginning the IBCP and choosing Artificial Intelligence as my career-related study, "
         "while starting to build small programming projects."),
        ("Grade 12",
         "Continuing to develop my skills through coursework and projects, and working on the "
         "Reflective Project and my Internal Assessments."),
        ("Future university aspirations",
         "Hoping to study Computer Science with a focus on Artificial Intelligence and Machine "
         "Learning, and to keep building useful applications."),
    ],
    # Interests cards (icon, title, text)
    "interests": [
        ("🤖", "Artificial Intelligence and technology",
         "Exploring how software can be designed to solve problems and support people."),
        ("🧩", "Programming and problem-solving",
         "Using Python to break problems into small steps and build working solutions."),
        ("🎨", "Creative digital design",
         "Designing clean, simple interfaces and presentations that make ideas easy to understand."),
        ("🗣️", "Language learning",
         "Improving my communication and learning how language connects people and cultures."),
        ("💃", "Classical dance experience",
         "My background in classical dance has taught me discipline, focus and expression."),
        ("🛠️", "Learning through practical projects",
         "I learn best by building, testing and improving real projects over time."),
    ],
    # Strengths (icon, title, text)
    "strengths": [
        ("🔥", "Persistence",
         "I keep working on a problem until I find a way forward."),
        ("🔍", "Curiosity",
         "I like asking questions and understanding how things work."),
        ("🧠", "Thoughtful problem-solving",
         "I try to look at a problem from more than one angle before deciding."),
        ("🎨", "Creativity",
         "I enjoy bringing original ideas into my designs and code."),
        ("🤝", "Collaboration",
         "I value working with others and listening to their ideas."),
        ("🌱", "Willingness to improve",
         "I try to learn from feedback and mistakes and keep getting better."),
    ],
    "approach": (
        "I continue to develop my skills through coursework, experiments, research, and programming "
        "projects. I recognise that some subjects are more challenging than others, and I value the "
        "process of practising, asking questions, and improving. I try to learn from mistakes and "
        "stay open to feedback."
    ),
    "quote": "Rooted in tradition, growing in knowledge.",
}

# ---------------------------------------------------------------------
# PAGE 2 — DP SUBJECTS
# ---------------------------------------------------------------------
DP = {
    # ---------------------------------------------------------------
    "Physics HL": {
        "title": "Physics HL — Exploring the Science Behind Technology",
        "learning_experience": (
            "Physics involves understanding how the world works through scientific concepts, "
            "mathematical relationships, and experiments. I am exploring topics that I find "
            "challenging and am developing my ability to connect theoretical knowledge with "
            "experimental evidence. Some ideas take time to understand, but working through problems "
            "and practical work helps me build confidence."
        ),
        "csp": {
            "title": "Food-Step Electricity Generation",
            "overview": (
                "A collaborative science project exploring the idea of generating electricity from "
                "footsteps. The project looks at how movement could be turned into a small amount of "
                "electrical energy."
            ),
            "aim": (
                "To understand whether energy from footsteps could be captured and converted into "
                "electricity, and to explore the science behind this idea."
            ),
            "principles": [
                "Energy transfer and conservation",
                "Conversion of mechanical energy into electrical energy",
                "Electromagnetic induction and piezoelectric effects (as concepts)",
            ],
            "teamwork": (
                "The project was completed as a team, which meant sharing tasks, discussing ideas and "
                "combining our research. Working together helped us divide the work and learn from one "
                "another's strengths."
            ),
            "learned": (
                "I learned how to research a scientific idea, connect it to physics concepts, and "
                "present it clearly as part of a group. I also understood that turning an idea into a "
                "working system involves many practical considerations."
            ),
            "reflection": (
                "This project showed me that science is not only about theory but also about "
                "teamwork, planning and communicating ideas. It made me more curious about renewable "
                "energy and how physics is applied in real life."
            ),
            # Paste your Canva presentation link here (leave "" until ready)
            "presentation_url": "",
        },
        "ia": {
            "topic": (
                "Investigating the relationship between the rate of change of magnetic flux through "
                "a solenoid and the induced electromotive force."
            ),
            "research_question": (
                "How does the rate of change of magnetic flux through a solenoid affect the induced "
                "electromotive force?"
            ),
            "overview": (
                "This investigation studies electromagnetic induction by looking at how changing the "
                "magnetic flux through a solenoid affects the induced electromotive force."
            ),
            "variables": [
                "Independent variable: rate of change of magnetic flux",
                "Dependent variable: induced electromotive force (emf)",
                "Controlled variables: number of turns, solenoid dimensions, temperature",
            ],
            "approach": (
                "The plan is to change the magnetic flux through the solenoid at controlled rates and "
                "measure the resulting induced emf. The method will be refined as the investigation "
                "develops."
            ),
            "data_collection": "Data collection is in progress. Readings will be added here once the experiment is carried out.",
            "analysis": "Analysis and graphs will be added once the data has been collected.",
            "status": IA_STATUS,
            "notice": (
                "My Physics Internal Assessment is currently in progress. I will update this section "
                "with my completed experimental work, analysis, and final findings once the "
                "investigation is complete."
            ),
            # Add document / evidence links here (list of {title, url, description})
            "evidence": [],
        },
        "reflection": (
            "Physics develops scientific reasoning, precision, and experimental skills. It has taught "
            "me to interpret evidence carefully and to question results rather than accept them "
            "straight away."
        ),
    },
    # ---------------------------------------------------------------
    "Chemistry SL": {
        "title": "Chemistry SL — Learning Through Experiments",
        "learning_experience": (
            "Chemistry can be challenging, but I enjoy learning about chemical reactions and "
            "understanding concepts through practical experiments. I am still developing confidence "
            "in some areas and believe that practice and experimentation can help me improve. Seeing "
            "a reaction happen in the lab often makes the theory easier to understand."
        ),
        "csp": {
            # The Chemistry CSP topic has not been provided yet, so these are
            # clearly marked placeholders for the student to complete.
            "title": "",   # e.g. "Your Chemistry CSP title"
            "overview": "",  # short overview
            "aim": "",
            "concepts": "",  # scientific concepts involved
            "contribution": "",  # my contribution to the team
            "skills": "",
            "reflection": "",
            # Paste your video link here (leave "" until ready)
            "video_url": "",
        },
        "ia": {
            "topic": (
                "Investigating the effect of ferric nitrate concentration on the initial rate of "
                "oxidation of iodide ions."
            ),
            "research_question": (
                "How does the concentration of ferric nitrate affect the initial rate of oxidation "
                "of iodide ions?"
            ),
            "background": (
                "This investigation studies reaction kinetics and concentration. It looks at how "
                "changing the concentration of a reactant affects the initial rate of a reaction."
            ),
            "variables": [
                "Independent variable: concentration of ferric nitrate",
                "Dependent variable: initial rate of reaction",
                "Controlled variables: temperature, volume, concentration of iodide ions",
            ],
            "method": "The method will be finalised and added here before the experiment is carried out.",
            "data_collection": "Data collection is in progress.",
            "graphs": "Graphs will be added once the data has been collected.",
            "analysis": "Analysis will be added once the data has been processed.",
            "evaluation": "Evaluation will be added once the analysis is complete.",
            "status": IA_STATUS,
            "notice": (
                "My Chemistry Internal Assessment is currently in progress. The completed "
                "investigation, processed data, analysis, and final conclusion will be added here "
                "when ready."
            ),
            "evidence": [],
        },
        "reflection": (
            "Experiments help me connect chemical theory with observable changes. They develop "
            "laboratory skills, careful observation, and the ability to interpret data."
        ),
    },
    # ---------------------------------------------------------------
    "Mathematics AA HL": {
        "title": "Mathematics AA HL — Developing Logical Thinking",
        "learning_experience": (
            "Mathematics encourages logical reasoning, persistence, and systematic problem-solving. "
            "I am developing my understanding of advanced mathematical ideas and learning to apply "
            "them to different types of problems. I find that regular practice helps me build both "
            "accuracy and confidence."
        ),
        # Concepts grid (title, description)
        "concepts": [
            ("Numbers and algebra", "Working with number systems, indices, and algebraic manipulation."),
            ("Algebraic expressions and equations", "Simplifying expressions and solving equations accurately."),
            ("Functions and relations", "Understanding different types of functions, their graphs and behaviour."),
            ("Transformations", "Exploring how graphs and shapes change under different transformations."),
            ("Vectors", "Using vectors to represent and solve problems in two and three dimensions."),
            ("Calculus", "Introduction to differentiation and integration and their applications."),
            ("Other concepts", "Additional topics covered in class as the course progresses."),
        ],
        "classwork_intro": (
            "This area is for class notes, problem-solving exercises, practice work and mathematical "
            "investigations. Evidence will be added here as the course continues."
        ),
        # Add evidence items here (list of {title, url, description, image})
        "classwork_evidence": [],
        "ia": {
            "title": "",  # e.g. "My Mathematics IA title"
            "research_question": "",  # the final research question
            "document_url": "",  # link to the IA document
            "status": IA_STATUS,
            "notice": (
                "My Mathematics Internal Assessment is currently in progress. I will add the "
                "finalized research question, mathematical exploration, analysis, and reflection once "
                "the work is ready."
            ),
            "evidence": [],
        },
        "reflection": (
            "Mathematics develops logical reasoning, analytical thinking, and perseverance. It has "
            "taught me to approach problems step by step and to keep going when a solution is not "
            "immediately obvious."
        ),
    },
    # ---------------------------------------------------------------
    "English B SL": {
        "title": "English B SL — Improving Through Practice",
        "learning_experience": (
            "English is a subject in which I want to keep improving. Although I sometimes find "
            "expressing my ideas in English challenging, I enjoy learning the language and becoming "
            "more confident in communicating my thoughts. Through regular practice, reading, "
            "presentations, and classroom activities, I am working towards expressing myself more "
            "clearly."
        ),
        # Themes (title, description)
        "themes": [
            ("Identities", "Exploring who we are and how language and culture shape identity."),
            ("Human Ingenuity", "Looking at creativity, invention and how people solve problems."),
            ("Social Organization", "Understanding how societies and communities are structured."),
            ("Sharing the Planet", "Considering global issues and our shared responsibility for the environment."),
        ],
        "learning_experiences": [
            "Reading and understanding different types of texts",
            "Taking part in classroom discussions",
            "Preparing and giving presentations",
            "Practising oral communication",
            "Exploring cultural perspectives",
            "Developing vocabulary and writing skills",
        ],
        "reflection": (
            "English B supports clearer communication, confidence, and the ability to understand "
            "viewpoints from different cultures. It reminds me that language is a tool for connecting "
            "with people."
        ),
        "future_evidence_intro": (
            "This section is for future evidence such as presentations, written work and oral tasks."
        ),
        # Add evidence items here (list of {title, url, description})
        "future_evidence": [],
    },
}

# ---------------------------------------------------------------------
# PAGE 3 — CORE COMPONENTS
# ---------------------------------------------------------------------
CORE = {
    # ---------------------------------------------------------------
    "Personal and Professional Skills": {
        "title": "Personal and Professional Skills",
        "what_is": (
            "Personal and Professional Skills (PPS) supports the development of personal, "
            "interpersonal, communication, organisational, and professional skills needed for "
            "further education, work, and everyday life."
        ),
        "journey": (
            "Through activities, teamwork, reflection, and practical experiences, I am learning to "
            "recognise my strengths and identify areas where I can improve. Reflecting on what went "
            "well — and what did not — helps me understand how I work and how I can develop further."
        ),
        "skills": [
            ("💬", "Communication", "Sharing ideas clearly and listening to others."),
            ("🤝", "Collaboration", "Working with others towards a shared goal."),
            ("⏱️", "Self-management", "Organising my time and responsibilities."),
            ("🧠", "Critical thinking", "Looking at situations carefully before deciding."),
            ("🧩", "Problem-solving", "Finding practical ways to overcome difficulties."),
            ("🎯", "Personal responsibility", "Taking ownership of my work and actions."),
        ],
        # Learning outcomes — EDIT the wording to match your school's exact
        # requirements. These are intentionally left blank so nothing is invented.
        "outcomes": [
            {"code": "LO1", "outcome": "", "what_i_did": "", "skills": "", "evidence": "", "reflection": ""},
            {"code": "LO2", "outcome": "", "what_i_did": "", "skills": "", "evidence": "", "reflection": ""},
            {"code": "LO3", "outcome": "", "what_i_did": "", "skills": "", "evidence": "", "reflection": ""},
            {"code": "LO4", "outcome": "", "what_i_did": "", "skills": "", "evidence": "", "reflection": ""},
            {"code": "LO5", "outcome": "", "what_i_did": "", "skills": "", "evidence": "", "reflection": ""},
        ],
        # Add your PPS evidence links here (list of {title, url, description})
        "evidence_links": [],
        "reflection": (
            "PPS has helped me learn to manage my responsibilities, communicate with others, and "
            "reflect on my experiences. I am more aware of the areas I want to develop and of the "
            "skills I will need in the future."
        ),
    },
    # ---------------------------------------------------------------
    "Language and Cultural Studies": {
        "title": "Language and Cultural Studies",
        "what_is": (
            "Language and Cultural Studies explores the relationship between language, identity, "
            "culture, communication, and society. It encourages us to look beyond our own "
            "perspective and understand how others see the world."
        ),
        "engagements_intro": (
            "Learning engagements are planned activities or experiences through which students "
            "explore cultural, linguistic, social, or global issues and reflect on their learning."
        ),
        "reflection": (
            "Language and Cultural Studies has helped me broaden my perspective. I have learned that "
            "people can interpret the same issue differently depending on their experiences, culture, "
            "background, and values. Instead of assuming that everyone thinks the same way, I am "
            "learning to consider different viewpoints and understand why people may have different "
            "opinions."
        ),
        # Learning engagement cards — EDIT with your own engagements.
        # Each card: title, description, topic, learned, perspective, url, image
        "engagements": [
            {"title": "", "description": "", "topic": "", "learned": "", "perspective": "", "url": "", "image": ""},
            {"title": "", "description": "", "topic": "", "learned": "", "perspective": "", "url": "", "image": ""},
        ],
        "skills": [
            "Cultural awareness",
            "Communication",
            "Critical thinking",
            "Research",
            "Understanding multiple perspectives",
            "Reflection",
        ],
        # Add extra Canva / evidence links here (list of {title, url, description})
        "evidence_links": [],
    },
    # ---------------------------------------------------------------
    "Reflective Project": {
        "title": "My Reflective Project",
        "research_question": (
            "Should the use of Artificial Intelligence in education be limited even if it provides "
            "significant benefits to students?"
        ),
        "what_is": (
            "The Reflective Project is an independent research-based component of the IBCP that "
            "allows students to investigate an ethical dilemma connected to a relevant issue or "
            "career field and develop a reasoned position."
        ),
        "dilemma": (
            "The dilemma is the tension between the benefits of AI in education and the concerns it "
            "raises. AI can support learning, but it also raises questions about academic integrity, "
            "overdependence, critical thinking, privacy, and responsible use."
        ),
        "stakeholders": [
            ("🎓", "Students", "Those who use AI tools for learning and could benefit from or misuse them."),
            ("📚", "Teachers", "Those who guide learning and must consider integrity and fairness."),
            ("🏫", "Educational institutions", "Those who set policies and are responsible for responsible use."),
        ],
        # Research and analysis — EDIT as your project develops.
        "sections": [
            ("Background and context", ""),
            ("Benefits of AI in education", ""),
            ("Concerns and limitations", ""),
            ("Research findings", ""),
            ("Stakeholder perspectives", ""),
            ("Ethical analysis", ""),
            ("Personal position", ""),
        ],
        "status": "Final Draft to Be Added",
        "notice": (
            "My Reflective Project explores the ethical challenges of using Artificial Intelligence "
            "in education. My final draft and completed project evidence will be added here when they "
            "are ready."
        ),
        # Paste your final document link here
        "document_url": "",
    },
    # ---------------------------------------------------------------
    "Community Engagement": {
        "title": "Community Engagement — Learning Through Service",
        "what_is": (
            "Community Engagement involves contributing to the community through meaningful "
            "activities, collaboration, service, and reflection, while developing awareness of "
            "others' needs."
        ),
        "project": {
            "name": "Life Skills — Embroidery Design",
            "location": "Jobrito Andrea orphan house",
            "overview": (
                "Our community project involved working with students at Jobrito Andrea orphan "
                "house. We planned activities to support their learning by helping them practise "
                "English and learn embroidery. The experience gave us an opportunity to share useful "
                "skills while learning from the students and working together as a team."
            ),
            "why_embroidery": (
                "Embroidery is a practical life skill that encourages creativity, patience, "
                "concentration, and hand coordination. It can provide a useful creative activity and "
                "a skill that participants may continue developing in the future."
            ),
            "activities": [
                ("📝", "Project planning", "Deciding on goals, activities and how the sessions would run."),
                ("🧵", "Preparing materials", "Gathering and organising the materials needed for the sessions."),
                ("🔤", "English learning activities", "Helping students practise English through simple activities."),
                ("🪡", "Embroidery demonstrations", "Showing basic stitches and techniques step by step."),
                ("🤝", "Guided practice", "Supporting students as they tried the stitches themselves."),
                ("👥", "Collaboration", "Working with teammates to plan and run the sessions."),
                ("💭", "Reflection", "Thinking about what we learned and how the project could improve."),
            ],
            "developed": [
                "Patience when explaining and demonstrating a new skill",
                "Responsibility while preparing for activities",
                "Collaboration and communication with teammates",
                "Adaptability when activities did not go exactly as planned",
                "Appreciation for different learning needs",
                "Understanding the value of contributing to the community",
            ],
            # Two SEPARATE evidence areas — paste your Canva/document links.
            "proposal": {"title": "Project Proposal", "url": "", "description": "", "image": ""},
            "journal": {"title": "Community Engagement Learning Journal", "url": "", "description": "", "image": ""},
        },
    },
}

# ---------------------------------------------------------------------
# PAGE 4 — CAREER-RELATED STUDIES: ARTIFICIAL INTELLIGENCE
# ---------------------------------------------------------------------
CRS = {
    "title": "Career-related Studies — Artificial Intelligence",
    "what_is": (
        "Career-related Studies provide practical and career-focused learning alongside the IBCP "
        "academic and core components. In this portfolio, my CRS focus is Artificial Intelligence."
    ),
    "why_ai": (
        "My interest in Artificial Intelligence comes from my curiosity about programming, "
        "technology, and solving practical problems. Through projects, I have explored how "
        "applications can help people manage information, understand problems, and interact with "
        "technology. These experiences have encouraged me to continue developing my skills in "
        "Computer Science."
    ),
    # Skills — presented as areas of learning, not verified proficiency levels.
    "skills": [
        ("🐍", "Python programming", "Writing programs and building small applications."),
        ("📊", "Streamlit application development", "Creating simple interactive web apps."),
        ("🗄️", "Basic SQLite database work", "Storing and retrieving simple data."),
        ("🌐", "HTML fundamentals", "Structuring content for the web."),
        ("🧩", "Problem-solving", "Breaking problems into smaller, workable steps."),
        ("🎨", "User interface design", "Making apps clear and easy to use."),
        ("📈", "Data handling", "Organising and presenting data."),
        ("🚀", "Project development", "Planning, building and improving projects."),
    ],
    # PROJECT SHOWCASE — five projects. Fill in the links when ready.
    # Each project: name, icon, intro, problem, purpose, features,
    #               technologies, learning, image, github, streamlit, presentation
    "projects": [
        {
            "name": "WaterBuddy",
            "icon": "💧",
            "intro": (
                "WaterBuddy is a hydration tracking application designed to help users record their "
                "water intake and follow daily hydration goals."
            ),
            "problem": "It can be easy to forget to drink enough water during a busy day.",
            "purpose": "To help users build a simple, consistent hydration habit.",
            "features": [
                "Age-based hydration targets",
                "Water intake logging",
                "Challenges",
                "Badges",
                "Dashboard",
            ],
            "technologies": ["Python", "Streamlit", "SQLite"],
            "learning": (
                "I learned how to model a daily goal, store user data, and show progress in a simple "
                "dashboard. I also practised making the app easy to use."
            ),
            "image": "assets/projects/waterbuddy.png",
            "github": "",
            "streamlit": "",
            "presentation": "",
        },
        {
            "name": "MedTimer",
            "icon": "⏰",
            "intro": (
                "MedTimer is a medicine reminder application concept designed to help users organise "
                "their medication schedules and remember planned doses."
            ),
            "problem": "Remembering to take medication on time can be difficult.",
            "purpose": "To explore how a simple reminder tool could support a regular routine.",
            "features": [
                "Reminder scheduling",
                "Calendar",
                "Medication records",
                "User interface",
                "Data storage",
            ],
            "technologies": ["Python", "Streamlit", "SQLite"],
            "learning": (
                "I learned about scheduling logic and thinking carefully about how a health-related "
                "tool should behave. This is a concept project and is not a medical device."
            ),
            "image": "assets/projects/medtimer.png",
            "github": "",
            "streamlit": "",
            "presentation": "",
        },
        {
            "name": "SmartFarm AI",
            "icon": "🌱",
            "intro": (
                "SmartFarm AI is an agricultural assistant concept that explores how AI can provide "
                "accessible farming guidance."
            ),
            "problem": "Useful farming information is not always easy to access or understand.",
            "purpose": "To explore how AI could answer simple farming questions in an accessible way.",
            "features": [
                "Farmer questions",
                "Agricultural recommendations",
                "AI-assisted responses",
                "Language accessibility",
            ],
            "technologies": ["Python", "Streamlit"],
            "learning": (
                "I learned to think about who the user is and how to present information clearly. "
                "The project is a concept and does not claim verified farming outcomes."
            ),
            "image": "assets/projects/smartfarm.png",
            "github": "",
            "streamlit": "",
            "presentation": "",
        },
        {
            "name": "SafeFall AI",
            "icon": "🛡️",
            "intro": (
                "SafeFall AI explores the use of artificial intelligence for recognising human "
                "activities and identifying possible falls."
            ),
            "problem": "Falls can be dangerous, especially for people who live alone.",
            "purpose": "To explore how AI could help recognise a possible fall and raise awareness.",
            "features": [
                "Activity recognition",
                "Possible fall detection",
                "Monitoring view",
                "Alerts (concept)",
            ],
            "technologies": ["Python", "Computer Vision", "Machine Learning"],
            "learning": (
                "I learned about activity recognition and the importance of testing carefully. This "
                "is an exploration and does not claim reliable real-world fall detection or medical "
                "accuracy."
            ),
            "image": "assets/projects/safefall.png",
            "github": "",
            "streamlit": "",
            "presentation": "",
        },
        {
            "name": "StockSense Pro",
            "icon": "📈",
            "intro": (
                "StockSense Pro is a stock analytics dashboard designed to help users visualise "
                "financial data and explore market trends."
            ),
            "problem": "Raw market data can be difficult to interpret.",
            "purpose": "To present financial data in a clear, visual way for exploration.",
            "features": [
                "Market data visualisation",
                "Dashboard metrics",
                "Trend exploration",
                "Interactive filters",
            ],
            "technologies": ["Python", "Streamlit", "Pandas", "Plotly"],
            "learning": (
                "I learned how to handle and visualise data over time. The dashboard is for "
                "exploration only and does not provide investment recommendations."
            ),
            "image": "assets/projects/stocksense.png",
            "github": "",
            "streamlit": "",
            "presentation": "",
        },
    ],
    "reflection": (
        "Developing these projects has helped me practise programming, think about users' needs, "
        "learn from errors, and understand the process of building an application from an idea to "
        "something that works. Each project taught me something new and showed me what I want to "
        "learn next."
    ),
}

# ---------------------------------------------------------------------
# PAGE 5 — ACTIVITIES AND INTERESTS
# ---------------------------------------------------------------------
ACTIVITIES = {
    "title": "Beyond Academics",
    "intro": (
        "Alongside my studies, I have interests and experiences that shape who I am and how I learn. "
        "These are part of my personal growth rather than formal academic achievements."
    ),
    "cards": [
        ("💃", "Classical Dance",
         "I have experience in Bharatanatyam and value the discipline, dedication, expression, and "
         "cultural connection that classical dance brings. This is a past experience and a personal "
         "interest rather than current formal training."),
        ("💻", "Technology and Creative Design",
         "I enjoy exploring technology, designing presentations, creating digital projects, and "
         "experimenting with different ways to present ideas clearly."),
        ("🗣️", "Language Learning",
         "I am interested in learning languages and discovering how language connects people and "
         "cultures, and how it can change the way we understand one another."),
        ("🌍", "Exploring the World",
         "I hope to travel around the world, experience different cultures, explore new places, and "
         "learn from people with different backgrounds. This is an aspiration for the future."),
        ("🌱", "Personal Growth",
         "I try to stay curious, be patient, learn from mistakes, and remain open to new experiences. "
         "Growth, for me, is a steady process rather than a single moment."),
    ],
    # Optional photos — add image paths here (list of {image, caption})
    "photos": [],
}

# ---------------------------------------------------------------------
# PAGE 6 — CERTIFICATES AND ACHIEVEMENTS
# ---------------------------------------------------------------------
CERTIFICATES = {
    "title": "Certificates and Achievements",
    # Confirmed academic details only. Do not invent others.
    "confirmed": [
        ("Grade 11 overall result", "94.5%"),
        ("Highest mark in Artificial Intelligence", "At school"),
    ],
    "sections": [
        "Academic achievements",
        "Course certificates",
        "Workshops",
        "Competitions",
        "Technology-related achievements",
        "Other recognitions",
    ],
    # Add real certificates here. Each item:
    #   {title, organisation, date, description, category, image, url}
    # Leave the list empty until you have real certificates to show.
    "items": [],
}

# ---------------------------------------------------------------------
# FOOTER
# ---------------------------------------------------------------------
FOOTER = {
    "brand": "Harini Priya K.",
    "tagline": "IBCP Portfolio · Artificial Intelligence",
}
