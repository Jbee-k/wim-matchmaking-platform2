# WIM Matchmaking Platform - UI/UX Guide
## Interface Overview for All Stakeholders

**Version:** 1.0
**Date:** May 2026

---

## Platform Architecture

The WIM Matchmaking Platform has **THREE DISTINCT USER INTERFACES**, each tailored to the specific needs of that stakeholder group:

```
┌─────────────────────────────────────────────────────────────┐
│   Women In Manufacturing Matchmaking Platform               │
│   AI-Powered Mentor-Mentee Pairing System                   │
└─────────────────────────────────────────────────────────────┘
         │                    │                    │
         ▼                    ▼                    ▼
    ┌─────────┐          ┌─────────┐          ┌─────────┐
    │ MENTOR  │          │ MENTEE  │          │  ADMIN  │
    │ PORTAL  │          │ PORTAL  │          │DASHBOARD│
    └─────────┘          └─────────┘          └─────────┘
         │                    │                    │
         ▼                    ▼                    ▼
    • Profile             • Profile             • Intake
    • My Match            • My Match              Monitoring
    • Mentoring           • Goals &              • Matching
      Tools               Learning                Algorithm
    • Progress            • Progress             • Review
      Tracking            Tracking               Matches
                                                • Approve
                                                  Pairings
                                                • Audit Trail
```

---

## 1. MENTOR PORTAL

### Purpose
Mentors use this interface to:
- Create their profile
- Complete the "Right Seat" assessment
- View their assigned mentee
- Access mentoring tools
- Track progress

### Key Features

#### 1.1 Login Page
```
┌─────────────────────────────────────────┐
│  👩‍💼 Women In Manufacturing             │
│     Matchmaking Platform                │
│                                         │
│  AI-Powered Mentor-Mentee Pairing      │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ 🔐 LOGIN                        │   │
│  │ Email: [_________________]      │   │
│  │ Password: [________________]    │   │
│  │ I am a: [Mentor ▼]             │   │
│  │ [Login Button]                 │   │
│  └─────────────────────────────────┘   │
│                                         │
│  OR                                     │
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ 📝 SIGN UP                      │   │
│  │ Email: [_________________]      │   │
│  │ Password: [________________]    │   │
│  │ I am a: [Mentor ▼]             │   │
│  │ [Sign Up Button]               │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
```

**What Mentors See:**
- Email and password fields
- User type selector (pre-selected: "Mentor")
- Login button
- Sign Up option

---

#### 1.2 Mentor Profile Form (10 Steps)

After login, mentors complete a multi-step form:

**Step 1: Basic Information**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 1 of 10        │
│ ▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 👤 Basic Information                 │
│                                      │
│ Full Name: [___________________]    │
│ Email: [___________________]        │
│ Phone: [___________________]        │
│ Company: [___________________]      │
│ Job Title: [___________________]    │
│ Years of Experience: [___]          │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 2: Manufacturing Sector**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 2 of 10        │
│ ▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 🏭 Manufacturing Sector              │
│                                      │
│ Which sector? (Select one)           │
│ ☐ Food & Beverage                   │
│ ☐ Textiles                          │
│ ☐ Metal & Engineering               │
│ ☐ Chemical & Plastics               │
│ ☐ Automotive                        │
│ ☐ Other: [___________________]      │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 3: Mentoring Experience**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 3 of 10        │
│ ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 🎓 Mentoring Experience              │
│                                      │
│ Is this your first time mentoring?   │
│ ◉ Yes  ○ No                         │
│                                      │
│ Why do you want to mentor?           │
│ [_____________________________]      │
│ [_____________________________]      │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 4: Top 3 Strengths**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 4 of 10        │
│ ▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 💪 Your Top 3 Strengths              │
│    (Select 3)                        │
│                                      │
│ ☐ Operations Excellence             │
│ ☐ Team Building & Leadership        │
│ ☐ Strategic Planning                │
│ ☐ Financial Management              │
│ ☐ Sales & Marketing                 │
│ ☐ Quality & Compliance              │
│ ☐ Innovation & Technology           │
│ ☐ Supply Chain Management           │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 5: Mentoring Focus Areas**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 5 of 10        │
│ ▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 🎯 Mentoring Focus Areas             │
│    (Select 3)                        │
│                                      │
│ ☐ Business Growth & Scaling         │
│ ☐ Operational Efficiency            │
│ ☐ Leadership Development            │
│ ☐ Financial Management              │
│ ☐ Market Expansion                  │
│ ☐ Team Development                  │
│ ☐ Innovation & Technology           │
│ ☐ Risk Management                   │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 6: Communication Style**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 6 of 10        │
│ ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 💬 Communication Style               │
│                                      │
│ How do you prefer to mentor?         │
│ ◉ Collaborative & Supportive        │
│ ○ Direct & Challenging              │
│ ○ Hands-on & Directive              │
│ ○ Coaching & Questioning            │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 7: Availability**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 7 of 10        │
│ ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ ⏰ Availability                       │
│                                      │
│ Hours per month: [4-6 ▼]            │
│                                      │
│ Preferred meeting times:             │
│ ☐ Early morning (6-9 AM)            │
│ ☐ Mid-morning (9-12 PM)             │
│ ☐ Afternoon (12-3 PM)               │
│ ☐ Late afternoon (3-6 PM)           │
│ ☐ Evening (6-9 PM)                  │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 8: EOS Right Seat Assessment**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 8 of 10        │
│ ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 🎯 EOS Right Seat Assessment         │
│                                      │
│ For each statement, rate 1-5:        │
│ (1 = Disagree, 5 = Strongly Agree)  │
│                                      │
│ "I GET IT"                           │
│ I understand the EOS framework       │
│ ★★★★☆ (4/5)                        │
│                                      │
│ "I WANT IT"                          │
│ I'm committed to this mentorship     │
│ ★★★★★ (5/5)                        │
│                                      │
│ "I HAVE THE CAPACITY"               │
│ I have time to mentor effectively    │
│ ★★★★☆ (4/5)                        │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 9: Mentoring Approach**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 9 of 10        │
│ ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 📋 Mentoring Approach                │
│                                      │
│ How will you support your mentee?    │
│ [_____________________________]      │
│ [_____________________________]      │
│ [_____________________________]      │
│                                      │
│ What challenges can you help with?   │
│ [_____________________________]      │
│ [_____________________________]      │
│                                      │
│ [Previous] [Next]                   │
└──────────────────────────────────────┘
```

**Step 10: Terms & Confirmation**
```
┌──────────────────────────────────────┐
│ Mentor Profile - Step 10 of 10       │
│ ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ ✅ Terms & Confirmation              │
│                                      │
│ ☐ I agree to the mentorship terms   │
│ ☐ I commit to bi-monthly meetings   │
│ ☐ I will provide honest feedback    │
│                                      │
│ [Submit Profile]                    │
│                                      │
│ ✅ Profile submitted successfully!  │
│ Your mentor profile is now active.  │
│ You'll be matched with a mentee     │
│ within 7 days.                      │
└──────────────────────────────────────┘
```

---

#### 1.3 Mentor Dashboard (After Matching)

Once matched, mentors see:

```
┌─────────────────────────────────────────────┐
│ 👩‍💼 Mentor Dashboard                         │
│ Welcome, Sarah!                             │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 🎯 My Match                          │   │
│ │ ┌──────────────────────────────────┐ │   │
│ │ │ Mentee: Jane Mwangi              │ │   │
│ │ │ Company: TechStart Manufacturing │ │   │
│ │ │ Role: Production Manager         │ │   │
│ │ │ Sector: Textiles                 │ │   │
│ │ │ Experience: 8 years              │ │   │
│ │ │                                  │ │   │
│ │ │ Challenge: Scaling operations    │ │   │
│ │ │ Goal: Become Operations Director │ │   │
│ │ │                                  │ │   │
│ │ │ Compatibility Score: 87%         │ │   │
│ │ │ ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░ │ │   │
│ │ │                                  │ │   │
│ │ │ [Schedule First Meeting]         │ │   │
│ │ └──────────────────────────────────┘ │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 📅 Upcoming Meetings                 │   │
│ │ • May 31, 2 PM - First Meeting      │   │
│ │ • June 14, 2 PM - Check-in          │   │
│ │ • June 28, 2 PM - Progress Review   │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 🛠️ Mentoring Tools                   │   │
│ │ • Level 10 Meeting Agenda           │   │
│ │ • 90-Day Rocks Tracker              │   │
│ │ • EOS Scorecard Template            │   │
│ │ • IDS Meeting Log                   │   │
│ │ • Progress Notes                    │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 📊 My Progress                       │   │
│ │ Meetings Completed: 1/6             │   │
│ │ ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│ │ Last Meeting: May 31                │   │
│ │ Next Meeting: June 14               │   │
│ └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## 2. MENTEE PORTAL

### Purpose
Mentees use this interface to:
- Create their profile
- Complete the "Right Seat" assessment
- View their assigned mentor
- Set and track goals
- Access learning resources
- Track progress

### Key Features

#### 2.1 Mentee Profile Form (10 Steps)

Similar structure to mentor, but focused on:
- Career goals
- Challenges and pain points
- Development areas
- Learning preferences
- EOS Right Seat assessment

```
┌──────────────────────────────────────┐
│ Mentee Profile - Step 1 of 10        │
│ ▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │
│                                      │
│ 👤 Basic Information                 │
│                                      │
│ Full Name: [___________________]    │
│ Email: [___________________]        │
│ Phone: [___________________]        │
│ Company: [___________________]      │
│ Job Title: [___________________]    │
│ Years of Experience: [___]          │
│                                      │
│ [Next]                              │
└──────────────────────────────────────┘
```

#### 2.2 Mentee Dashboard (After Matching)

```
┌─────────────────────────────────────────────┐
│ 👩‍💼 Mentee Dashboard                         │
│ Welcome, Jane!                              │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 🎯 My Mentor                         │   │
│ │ ┌──────────────────────────────────┐ │   │
│ │ │ Mentor: Sarah Kipchoge           │ │   │
│ │ │ Company: Leading Manufacturing   │ │   │
│ │ │ Role: Operations Director        │ │   │
│ │ │ Sector: Food & Beverage          │ │   │
│ │ │ Experience: 15 years             │ │   │
│ │ │                                  │ │   │
│ │ │ Expertise: Operations Excellence │ │   │
│ │ │ Mentoring Style: Collaborative   │ │   │
│ │ │                                  │ │   │
│ │ │ Compatibility Score: 87%         │ │   │
│ │ │ ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░ │ │   │
│ │ │                                  │ │   │
│ │ │ [Schedule First Meeting]         │ │   │
│ │ └──────────────────────────────────┘ │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 🎯 My 90-Day Goals (Rocks)           │   │
│ │ ☐ Implement new production process  │   │
│ │ ☐ Reduce waste by 20%               │   │
│ │ ☐ Train team on EOS framework       │   │
│ │ ☐ Improve on-time delivery to 95%   │   │
│ │ ☐ Develop succession plan           │   │
│ │                                      │   │
│ │ Progress: 2/5 completed             │   │
│ │ ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 📅 Upcoming Meetings                 │   │
│ │ • May 31, 2 PM - First Meeting      │   │
│ │ • June 14, 2 PM - Check-in          │   │
│ │ • June 28, 2 PM - Progress Review   │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 📊 My Progress                       │   │
│ │ Meetings Completed: 1/6             │   │
│ │ ▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│ │ Goals Achieved: 2/5                 │   │
│ │ ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│ │ Last Meeting: May 31                │   │
│ │ Next Meeting: June 14               │   │
│ └──────────────────────────────────────┘   │
│                                             │
│ ┌──────────────────────────────────────┐   │
│ │ 📚 Learning Resources                │   │
│ │ • EOS Scorecard Template            │   │
│ │ • 90-Day Rocks Planner              │   │
│ │ • Level 10 Meeting Guide            │   │
│ │ • IDS Meeting Notes                 │   │
│ │ • Progress Journal                  │   │
│ └──────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

---

## 3. KAM ADMIN DASHBOARD

### Purpose
KAM Admin uses this interface to:
- Monitor mentor and mentee intake
- Run the matching algorithm
- Review AI-recommended pairings
- Approve or reject matches
- View complete audit trail
- Manage the entire matching process

### Key Features

#### 3.1 Admin Login
```
┌─────────────────────────────────────────────┐
│  👩‍💼 Women In Manufacturing                 │
│     Matchmaking Platform                    │
│                                             │
│  AI-Powered Mentor-Mentee Pairing          │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │ 🔐 ADMIN LOGIN                      │   │
│  │ Email: [_________________]          │   │
│  │ Password: [________________]        │   │
│  │ I am a: [Admin ▼]                  │   │
│  │ [Login Button]                     │   │
│  └─────────────────────────────────────┘   │
└─────────────────────────────────────────────┘
```

#### 3.2 Admin Dashboard - Intake Status
```
┌─────────────────────────────────────────────────────┐
│ 👨‍💼 Admin Dashboard                                 │
│ Welcome, KAM Admin!                                 │
│                                                     │
│ ┌─────────────────────────────────────────────┐   │
│ │ 📊 INTAKE STATUS                            │   │
│ │                                             │   │
│ │ Mentors Submitted: 18/30 (60%)              │   │
│ │ ▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│ │                                             │   │
│ │ Mentees Submitted: 22/30 (73%)              │   │
│ │ ▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ │   │
│ │                                             │   │
│ │ Total Profiles: 40                          │   │
│ │                                             │   │
│ │ Intake Deadline: June 5, 2026               │   │
│ │ Days Remaining: 3                           │   │
│ │                                             │   │
│ │ [🚀 Run Matching Algorithm]                 │   │
│ │ (Ready when all profiles submitted)         │   │
│ └─────────────────────────────────────────────┘   │
│                                                     │
│ Tabs: [Intake Status] [Matching] [Approvals]      │
│       [Audit Trail] [Practice Mode]               │
└─────────────────────────────────────────────────────┘
```

#### 3.3 Admin Dashboard - Matching Results
```
┌──────────────────────────────────────────────────────┐
│ 👨‍💼 Admin Dashboard - Matching Results               │
│                                                      │
│ ┌────────────────────────────────────────────────┐  │
│ │ 🎯 MATCHING RESULTS                            │  │
│ │                                                │  │
│ │ Mentee: Jane Mwangi (Textiles)                │  │
│ │ ────────────────────────────────────────────  │  │
│ │                                                │  │
│ │ ⭐ OPTION 1: HIGHEST COMPATIBILITY (87%)      │  │
│ │ ┌──────────────────────────────────────────┐  │  │
│ │ │ Mentor: Sarah Kipchoge                   │  │  │
│ │ │ Company: Leading Manufacturing           │  │  │
│ │ │ Sector: Food & Beverage                  │  │  │
│ │ │ Experience: 15 years                     │  │  │
│ │ │                                          │  │  │
│ │ │ Compatibility Breakdown:                 │  │  │
│ │ │ • Sector Alignment: 50% (cross-sector)   │  │  │
│ │ │ • Challenge-Skill Match: 95% (excellent) │  │  │
│ │ │ • Communication Style: 90%               │  │  │
│ │ │ • Availability Fit: 85%                  │  │  │
│ │ │ • GWC Alignment: 80%                     │  │  │
│ │ │ • Experience Match: 100%                 │  │  │
│ │ │                                          │  │  │
│ │ │ Why This Match:                          │  │  │
│ │ │ Sarah's operations expertise directly    │  │  │
│ │ │ addresses Jane's scaling challenge.      │  │  │
│ │ │ Both prefer collaborative mentoring.     │  │  │
│ │ │                                          │  │  │
│ │ │ [✅ Approve #1] [View Profile]           │  │  │
│ │ └──────────────────────────────────────────┘  │  │
│ │                                                │  │
│ │ ⭐ OPTION 2: HIGHEST COMPATIBILITY (84%)      │  │
│ │ ┌──────────────────────────────────────────┐  │  │
│ │ │ Mentor: Grace Omondi                     │  │  │
│ │ │ Company: Textile Excellence              │  │  │
│ │ │ Sector: Textiles (same sector)           │  │  │
│ │ │ Experience: 12 years                     │  │  │
│ │ │                                          │  │  │
│ │ │ Compatibility: 84%                       │  │  │
│ │ │ [✅ Approve #2] [View Profile]           │  │  │
│ │ └──────────────────────────────────────────┘  │  │
│ │                                                │  │
│ │ 🌍 INTENTIONAL DIVERSITY OPTION (72%)         │  │
│ │ ┌──────────────────────────────────────────┐  │  │
│ │ │ Mentor: David Kariuki                    │  │  │
│ │ │ Company: Tech Manufacturing              │  │  │
│ │ │ Sector: Automotive (cross-sector)        │  │  │
│ │ │ Experience: 10 years                     │  │  │
│ │ │                                          │  │  │
│ │ │ Why This Option:                         │  │  │
│ │ │ David brings fresh perspective from      │  │  │
│ │ │ automotive sector. His innovation        │  │  │
│ │ │ approach could help Jane think beyond    │  │  │
│ │ │ traditional textile solutions.           │  │  │
│ │ │                                          │  │  │
│ │ │ [✅ Approve Diversity] [View Profile]    │  │  │
│ │ └──────────────────────────────────────────┘  │  │
│ │                                                │  │
│ │ [🔄 Manually Pair] [❌ Reject All]            │  │
│ └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

#### 3.4 Admin Dashboard - Approvals
```
┌──────────────────────────────────────────────────────┐
│ 👨‍💼 Admin Dashboard - Approvals                       │
│                                                      │
│ ┌────────────────────────────────────────────────┐  │
│ │ ✅ APPROVED PAIRINGS (12/30)                   │  │
│ │                                                │  │
│ │ Pairing │ Mentee      │ Mentor      │ Score   │  │
│ │ ────────┼─────────────┼─────────────┼─────────│  │
│ │ #1      │ Jane M.     │ Sarah K.    │ 87%     │  │
│ │ #2      │ Alice N.    │ Grace O.    │ 84%     │  │
│ │ #3      │ Betty L.    │ David K.    │ 82%     │  │
│ │ #4      │ Carol M.    │ Emma W.     │ 85%     │  │
│ │ #5      │ Diana P.    │ Frank J.    │ 80%     │  │
│ │ #6      │ Eve Q.      │ George H.   │ 83%     │  │
│ │ #7      │ Fiona R.    │ Henry B.    │ 81%     │  │
│ │ #8      │ Grace S.    │ Isaac M.    │ 86%     │  │
│ │ #9      │ Helen T.    │ James C.    │ 79%     │  │
│ │ #10     │ Iris U.     │ Kevin L.    │ 84%     │  │
│ │ #11     │ Julia V.    │ Liam D.     │ 82%     │  │
│ │ #12     │ Karen W.    │ Mark A.     │ 85%     │  │
│ │                                                │  │
│ │ Average Compatibility: 83%                    │  │
│ │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░ │  │
│ │                                                │  │
│ │ [Reveal Matches to Participants]              │  │
│ │ [Export Report]                               │  │
│ └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

#### 3.5 Admin Dashboard - Audit Trail
```
┌──────────────────────────────────────────────────────┐
│ 👨‍💼 Admin Dashboard - Audit Trail                     │
│                                                      │
│ ┌────────────────────────────────────────────────┐  │
│ │ 📋 AUDIT TRAIL (All Activity Logged)           │  │
│ │                                                │  │
│ │ ID │ Action │ User │ Details │ Timestamp      │  │
│ │ ───┼────────┼──────┼─────────┼────────────────│  │
│ │ 45 │ mentor_│ Sarah│ Profile │ May 28, 2 PM  │  │
│ │    │ submit │ K.   │ submit  │               │  │
│ │ 46 │ mentee_│ Jane │ Profile │ May 28, 3 PM  │  │
│ │    │ submit │ M.   │ submit  │               │  │
│ │ 47 │ email_ │ SYS  │ Match   │ May 29, 10 AM │  │
│ │    │ sent   │      │ notif   │               │  │
│ │ 48 │ pairing│ Admin│ Approved│ May 29, 11 AM │  │
│ │    │ approv │      │ Jane-   │               │  │
│ │    │ ed     │      │ Sarah   │               │  │
│ │ 49 │ pairing│ Admin│ Rejected│ May 29, 11:15 │  │
│ │    │ reject │      │ Alice-  │               │  │
│ │    │ ed     │      │ David   │               │  │
│ │ 50 │ manual_│ Admin│ Paired  │ May 29, 11:30 │  │
│ │    │ pairing│      │ Alice-  │               │  │
│ │    │        │      │ Grace   │               │  │
│ │                                                │  │
│ │ [Download CSV] [Filter by Date] [Search]      │  │
│ └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
```

---

## User Interface Features Summary

### Mentor Portal
| Feature | Description |
| :--- | :--- |
| **Profile Creation** | 10-step guided form with EOS assessment |
| **My Match** | View assigned mentee with compatibility details |
| **Mentoring Tools** | Level 10 agenda, Rocks tracker, Scorecard |
| **Meeting Calendar** | Schedule and track bi-monthly meetings |
| **Progress Tracking** | Visual progress on goals and meetings |
| **Communication** | In-app messaging with mentor |

### Mentee Portal
| Feature | Description |
| :--- | :--- |
| **Profile Creation** | 10-step guided form with EOS assessment |
| **My Mentor** | View assigned mentor with expertise details |
| **Goal Setting** | Create and track 90-day Rocks |
| **Learning Resources** | Access EOS templates and guides |
| **Progress Dashboard** | Track goals, meetings, and development |
| **Communication** | In-app messaging with mentor |

### Admin Dashboard
| Feature | Description |
| :--- | :--- |
| **Intake Monitoring** | Real-time view of profile submissions |
| **Matching Algorithm** | One-click execution of AI matching |
| **Match Review** | View all options with compatibility scores |
| **Approval Workflow** | Approve, reject, or manually pair |
| **Intentional Diversity** | Cross-sector options with transparency |
| **Audit Trail** | Complete log of all decisions |
| **Practice Mode** | Test with sample data before going live |

---

## User Experience Flow

### Mentor Journey
```
1. Sign Up
   ↓
2. Complete 10-Step Profile
   ↓
3. Wait for Matching (7 days)
   ↓
4. View My Match
   ↓
5. Schedule First Meeting
   ↓
6. Bi-Monthly Mentoring Sessions
   ↓
7. Track Progress
   ↓
8. Graduation & Feedback
```

### Mentee Journey
```
1. Sign Up
   ↓
2. Complete 10-Step Profile
   ↓
3. Wait for Matching (7 days)
   ↓
4. View My Mentor
   ↓
5. Schedule First Meeting
   ↓
6. Set 90-Day Goals (Rocks)
   ↓
7. Bi-Monthly Check-ins
   ↓
8. Track Goal Progress
   ↓
9. Graduation & Celebration
```

### Admin Journey
```
1. Monitor Intake
   ↓
2. When Ready: Run Matching Algorithm
   ↓
3. Review All Pairings
   ↓
4. Approve/Reject Each Pairing
   ↓
5. Reveal Matches to Participants
   ↓
6. Monitor Ongoing Mentoring
   ↓
7. Review Audit Trail
   ↓
8. Generate Final Report
```

---

## Design Principles

✅ **Stakeholder-Centric:** Each interface is tailored to specific user needs
✅ **Clear Navigation:** Intuitive menu structure with clear labels
✅ **Progress Visibility:** Users can see where they are in the process
✅ **Data Transparency:** Admin can see exactly why pairings were recommended
✅ **Mobile-Friendly:** Works on desktop, tablet, and mobile
✅ **Accessible:** Clear fonts, good contrast, simple language
✅ **Professional:** Clean design that reflects KAM's brand

---

## Next Steps

1. **Deploy to Streamlit Cloud** - Get live URL
2. **Share with Stakeholders** - Get feedback on interface
3. **Train Users** - Conduct training sessions
4. **Go Live** - Launch the 1-day orientation workshop
5. **Monitor Usage** - Track user engagement
6. **Iterate** - Improve based on feedback

---

**Last Updated:** May 2026
**Version:** 1.0
