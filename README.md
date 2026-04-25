# Women In Manufacturing Matchmaking Platform
**AI-Powered Mentor-Mentee Pairing System**
**Version 1.0 | May 2026**

---

## Overview

The WIM Matchmaking Platform is a standalone web application that automates the process of matching mentors and mentees for the KAM Women in Manufacturing Mentorship Programme. The platform combines intelligent algorithmic matching with human oversight, allowing KAM Admin to review, approve, reject, or manually adjust AI-suggested pairings with full transparency.

**Key Features:**
- ✅ Mentor and mentee intake questionnaires
- ✅ EOS "Right Seat" assessment (Get it, Want it, Capacity)
- ✅ AI-powered compatibility matching algorithm (6-factor weighted scoring)
- ✅ Intentional diversity recommendations with transparency and override option
- ✅ Admin dashboard for review and approval
- ✅ Match reveal interface for participants
- ✅ Automated email notifications
- ✅ Practice mode for testing
- ✅ Full audit trail of all decisions

---

## Technology Stack

- **Frontend:** Streamlit (Python web framework)
- **Backend:** Python (Streamlit handles this)
- **Database:** SQLite (embedded, zero cost)
- **Hosting:** Streamlit Community Cloud (free) or self-hosted
- **Matching Algorithm:** Custom Python with 6-factor weighted scoring

---

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Local Setup

1. **Clone or download the project:**
   ```bash
   cd /home/ubuntu/wim-matchmaking-platform
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```

   The app will open at `http://localhost:8501`

### Deploy to Streamlit Community Cloud (FREE)

1. **Push code to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: WIM Matchmaking Platform"
   git remote add origin https://github.com/your-username/wim-matchmaking-platform.git
   git push -u origin main
   ```

2. **Go to Streamlit Cloud:**
   - Visit https://share.streamlit.io/
   - Click "New app"
   - Select your GitHub repository
   - Select the branch and app file (app.py)
   - Click "Deploy"

3. **Your app is now live!** Share the URL with participants.

---

## User Flows

### For Mentors & Mentees

1. **Sign Up:** Create account with email and password
2. **Complete Profile:** Fill out intake questionnaire (10 steps)
   - Basic information (name, company, role, sector)
   - Professional background
   - Strengths and development focus
   - Communication style preferences
   - Availability
   - EOS Right Seat assessment (Get it, Want it, Capacity)
3. **Submit:** Profile is submitted and stored in database
4. **Wait for Matching:** Admin runs matching algorithm
5. **Receive Notification:** Email notification when match is revealed
6. **View Match:** Log in to platform to see mentor/mentee profile and contact details

### For Admin (KAM)

1. **Login:** Admin credentials (set up in database)
2. **Monitor Intake:** View number of submitted profiles
3. **Load Sample Data (optional):** Test with practice mode
4. **Run Matching Algorithm:** Click button to generate AI-recommended pairings
5. **Review Matches:** For each mentee, see:
   - Top 3 AI-recommended matches (ranked by compatibility score)
   - Intentional diversity option (if applicable)
   - Compatibility breakdown for each pairing
6. **Approve/Reject/Manually Pair:** For each mentee:
   - Approve the top AI recommendation
   - Choose an alternative match
   - Manually pair with a different mentor
   - Provide reason for any override
7. **Approve All Pairings:** Once all 15 mentees are paired
8. **Match Reveal:** Mentors and mentees receive notifications and can log in to see their match
9. **View Audit Trail:** See all decisions and reasons

---

## Matching Algorithm

### How It Works

The algorithm calculates a compatibility score (0-100) for each potential mentor-mentee pairing based on six weighted factors:

| Factor | Weight | How It's Calculated |
| :--- | :--- | :--- |
| **Sector Alignment** | 25% | Same sector = 100 pts. Different sector = 50 pts (flagged for intentional diversity). |
| **Challenge-Skill Match** | 30% | Does mentor's strength directly address mentee's development need? Perfect match = 100 pts. Partial = 70 pts. No match = 30 pts. |
| **Communication Style** | 15% | Exact match = 100 pts. One overlaps = 70 pts. No overlap = 30 pts. |
| **Availability Fit** | 15% | Can they meet at overlapping times? Perfect overlap = 100 pts. Some overlap = 70 pts. No overlap = 0 pts (rejected). |
| **GWC Alignment** | 10% | Both ≥ 3.5 = 100 pts. Both ≥ 3.0 = 70 pts. Below = 30 pts. |
| **Experience Match** | 5% | Mentor has 5+ more years experience = 100 pts. Less = 70 pts. |

**Final Score:** Weighted average of all six factors.

### Intentional Diversity Feature

If the top 3 matches are all same-sector, the algorithm flags a cross-sector option as "Intentional Diversity Recommendation" with:
- Clear labeling: "⭐ HIGHEST COMPATIBILITY (88%)" vs. "🌍 INTENTIONAL DIVERSITY (72%)"
- Explanation: Why the algorithm recommends it and what the trade-offs are
- Override option: Admin can choose either or manually pair, with required reason field
- Audit trail: All decisions logged with reasons

---

## Database Schema

### Tables

**mentors** - Mentor profiles
- mentor_id, email, name, phone, company, job_title, years_experience, sector
- is_first_time_mentor, num_previous_mentees, why_mentoring
- top_3_strengths, mentoring_focus, communication_style
- hours_per_month, preferred_meeting_times
- gwc_get_it, gwc_want_it, gwc_capacity, gwc_score
- conflicts_of_interest, specific_mentee_preference, additional_info
- profile_submitted_date, status, email_verified, verification_token

**mentees** - Mentee profiles
- mentee_id, email, name, phone, company, job_title, years_experience, sector
- biggest_challenge, challenge_duration, top_3_development_areas
- career_aspirations, employment_type, communication_style
- hours_per_month, preferred_meeting_times
- gwc_get_it, gwc_want_it, gwc_capacity, gwc_score
- mentor_preferences, conflicts_of_interest, additional_info
- profile_submitted_date, status, email_verified, verification_token

**pairings** - Mentor-mentee pairings
- pairing_id, mentee_id, mentor_id
- compatibility_score, sector_alignment_score, challenge_skill_match_score, etc.
- is_intentional_diversity, pairing_type
- admin_decision, admin_notes, admin_user, decision_date, reason_for_decision

**audit_trail** - All actions logged
- audit_id, action, user_id, mentee_id, mentor_id, details, timestamp

**admin_users** - Admin credentials
- admin_id, email, password_hash, name, created_date

---

## Admin Setup

### Create Admin User

1. Open Python shell in the project directory:
   ```bash
   python3
   ```

2. Run the following code:
   ```python
   import sqlite3
   import hashlib
   from datetime import datetime
   
   def hash_password(password):
       return hashlib.sha256(password.encode()).hexdigest()
   
   conn = sqlite3.connect('wim_matchmaking.db')
   c = conn.cursor()
   
   # Insert admin user
   c.execute('''
       INSERT INTO admin_users (admin_id, email, password_hash, name, created_date)
       VALUES (?, ?, ?, ?, ?)
   ''', ('admin_001', 'adline.murunga@kam.co.ke', hash_password('your_password_here'), 'Adline Murunga', datetime.now()))
   
   conn.commit()
   conn.close()
   print("Admin user created!")
   ```

3. Exit Python shell: `exit()`

---

## Practice Mode

### Testing the Platform

1. **Login as Admin**
2. **Go to "Practice Mode" tab**
3. **Load Sample Mentor Profiles:** Creates 2 sample mentors
4. **Load Sample Mentee Profiles:** Creates 2 sample mentees
5. **Go to "Dashboard" tab**
6. **Click "Run Matching Algorithm":** Generates AI-recommended pairings
7. **Review and approve pairings**

---

## Email Notifications

Currently, the app logs email notifications to the console. To enable actual email sending, integrate with:
- **SendGrid** (recommended)
- **AWS SES**
- **Gmail SMTP**

Update the `send_email()` function in `app.py` with your email service credentials.

---

## Deployment Checklist

Before going live with Cohort 1:

- [ ] All code pushed to GitHub
- [ ] App deployed to Streamlit Community Cloud
- [ ] Admin user created with KAM credentials
- [ ] Email notifications configured (or confirmed to use console logging)
- [ ] Practice mode tested with sample data
- [ ] Mentor and mentee intake forms tested
- [ ] Matching algorithm tested with sample data
- [ ] Admin dashboard tested
- [ ] Audit trail verified
- [ ] URL shared with KAM for participant access

---

## Troubleshooting

### App won't start
- Check Python version: `python3 --version` (should be 3.8+)
- Reinstall dependencies: `pip install -r requirements.txt`

### Database errors
- Delete `wim_matchmaking.db` and restart app (will create fresh database)
- Check file permissions: `chmod 644 wim_matchmaking.db`

### Email not sending
- Check email service credentials in `send_email()` function
- For MVP, emails are logged to console; check console output

### Matching algorithm not working
- Ensure at least 1 mentor and 1 mentee have submitted profiles
- Check that profiles have all required fields filled
- Review console for error messages

---

## Support & Documentation

For questions or issues:
1. Check the audit trail for decision history
2. Review the matching algorithm breakdown for each pairing
3. Contact Value Connect: mercy@valueconnectonline.com

---

## Version History

**v1.0 (May 2026)**
- Initial release
- Mentor and mentee intake forms
- 6-factor matching algorithm
- Intentional diversity feature
- Admin dashboard
- Practice mode
- Audit trail

**Future Enhancements:**
- Integration with main WIM Mentorship Platform
- Machine learning to improve algorithm over time
- Scaling to 100+ participants
- API integration with KAM member database
- Advanced reporting and analytics

---

## License

This platform is developed for the Kenya Association of Manufacturers (KAM) Women in Manufacturing Initiative. All rights reserved.

---

**Built with ❤️ by Value Connect Management Consultancy Ltd**
