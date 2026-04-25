"""
Women In Manufacturing Matchmaking Platform
AI-Powered Mentor-Mentee Pairing System
Version 1.0 | May 2026
"""

import streamlit as st
import sqlite3
import pandas as pd
import json
import hashlib
from datetime import datetime
from pathlib import Path
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import numpy as np

# Page configuration
st.set_page_config(
    page_title="WIM Matchmaking Platform",
    page_icon="👩‍💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        padding: 0.75rem;
        font-size: 1rem;
        border-radius: 0.5rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        color: #155724;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# DATABASE SETUP
# ============================================================================

def init_database():
    """Initialize SQLite database with all required tables."""
    conn = sqlite3.connect('wim_matchmaking.db')
    c = conn.cursor()
    
    # Mentors table
    c.execute('''
        CREATE TABLE IF NOT EXISTS mentors (
            mentor_id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            phone TEXT,
            company TEXT,
            job_title TEXT,
            years_experience INTEGER,
            sector TEXT,
            is_first_time_mentor BOOLEAN,
            num_previous_mentees TEXT,
            why_mentoring TEXT,
            top_3_strengths TEXT,
            mentoring_focus TEXT,
            communication_style TEXT,
            hours_per_month TEXT,
            preferred_meeting_times TEXT,
            gwc_get_it INTEGER,
            gwc_want_it INTEGER,
            gwc_capacity INTEGER,
            gwc_score REAL,
            conflicts_of_interest TEXT,
            specific_mentee_preference TEXT,
            additional_info TEXT,
            profile_submitted_date TIMESTAMP,
            status TEXT,
            email_verified BOOLEAN DEFAULT 0,
            verification_token TEXT
        )
    ''')
    
    # Mentees table
    c.execute('''
        CREATE TABLE IF NOT EXISTS mentees (
            mentee_id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            phone TEXT,
            company TEXT,
            job_title TEXT,
            years_experience INTEGER,
            sector TEXT,
            biggest_challenge TEXT,
            challenge_duration TEXT,
            top_3_development_areas TEXT,
            career_aspirations TEXT,
            employment_type TEXT,
            communication_style TEXT,
            hours_per_month TEXT,
            preferred_meeting_times TEXT,
            gwc_get_it INTEGER,
            gwc_want_it INTEGER,
            gwc_capacity INTEGER,
            gwc_score REAL,
            mentor_preferences TEXT,
            conflicts_of_interest TEXT,
            additional_info TEXT,
            profile_submitted_date TIMESTAMP,
            status TEXT,
            email_verified BOOLEAN DEFAULT 0,
            verification_token TEXT
        )
    ''')
    
    # Pairings table
    c.execute('''
        CREATE TABLE IF NOT EXISTS pairings (
            pairing_id TEXT PRIMARY KEY,
            mentee_id TEXT NOT NULL,
            mentor_id TEXT NOT NULL,
            compatibility_score REAL,
            sector_alignment_score REAL,
            challenge_skill_match_score REAL,
            communication_compatibility_score REAL,
            availability_fit_score REAL,
            gwc_alignment_score REAL,
            experience_match_score REAL,
            is_intentional_diversity BOOLEAN,
            pairing_type TEXT,
            admin_decision TEXT,
            admin_notes TEXT,
            admin_user TEXT,
            decision_date TIMESTAMP,
            reason_for_decision TEXT,
            created_date TIMESTAMP,
            updated_date TIMESTAMP,
            FOREIGN KEY (mentee_id) REFERENCES mentees(mentee_id),
            FOREIGN KEY (mentor_id) REFERENCES mentors(mentor_id)
        )
    ''')
    
    # Audit trail table
    c.execute('''
        CREATE TABLE IF NOT EXISTS audit_trail (
            audit_id INTEGER PRIMARY KEY AUTOINCREMENT,
            action TEXT,
            user_id TEXT,
            mentee_id TEXT,
            mentor_id TEXT,
            details TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Admin users table
    c.execute('''
        CREATE TABLE IF NOT EXISTS admin_users (
            admin_id TEXT PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            name TEXT,
            created_date TIMESTAMP
        )
    ''')
    
    conn.commit()
    conn.close()

# ============================================================================
# SESSION STATE MANAGEMENT
# ============================================================================

def init_session_state():
    """Initialize session state variables."""
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'user_type' not in st.session_state:
        st.session_state.user_type = None  # 'mentor', 'mentee', or 'admin'
    if 'user_email' not in st.session_state:
        st.session_state.user_email = None
    if 'user_id' not in st.session_state:
        st.session_state.user_id = None

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def hash_password(password):
    """Hash a password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def generate_id(email, prefix):
    """Generate a unique ID based on email and prefix."""
    return f"{prefix}_{hashlib.md5(email.encode()).hexdigest()[:8]}"

def send_email(recipient_email, subject, body):
    """Send an email notification."""
    # For MVP, we'll log this instead of actually sending
    # In production, integrate with SendGrid, AWS SES, or similar
    st.write(f"📧 Email would be sent to {recipient_email}: {subject}")
    log_audit("email_sent", None, None, {"recipient": recipient_email, "subject": subject})

def log_audit(action, user_id, mentee_id, details):
    """Log an action to the audit trail."""
    conn = sqlite3.connect('wim_matchmaking.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO audit_trail (action, user_id, mentee_id, details, timestamp)
        VALUES (?, ?, ?, ?, ?)
    ''', (action, user_id, mentee_id, json.dumps(details), datetime.now()))
    conn.commit()
    conn.close()

# ============================================================================
# AUTHENTICATION
# ============================================================================

def login_page():
    """Display the login page."""
    st.markdown("# 👩‍💼 Women In Manufacturing Matchmaking Platform")
    st.markdown("---")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Login")
        email = st.text_input("Email Address", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        user_type = st.selectbox("I am a:", ["Mentor", "Mentee", "Admin"], key="login_user_type")
        
        if st.button("Login", use_container_width=True):
            if email and password:
                conn = sqlite3.connect('wim_matchmaking.db')
                c = conn.cursor()
                
                if user_type == "Admin":
                    c.execute('SELECT admin_id, password_hash FROM admin_users WHERE email = ?', (email,))
                    result = c.fetchone()
                    if result and result[1] == hash_password(password):
                        st.session_state.logged_in = True
                        st.session_state.user_type = 'admin'
                        st.session_state.user_email = email
                        st.session_state.user_id = result[0]
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid email or password")
                else:
                    table = 'mentors' if user_type == "Mentor" else 'mentees'
                    c.execute(f'SELECT email FROM {table} WHERE email = ?', (email,))
                    result = c.fetchone()
                    if result:
                        st.session_state.logged_in = True
                        st.session_state.user_type = user_type.lower()
                        st.session_state.user_email = email
                        st.session_state.user_id = generate_id(email, 'M' if user_type == "Mentor" else 'ME')
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Email not found. Please sign up first.")
                
                conn.close()
            else:
                st.error("Please enter email and password")
    
    with col2:
        st.subheader("Sign Up")
        signup_email = st.text_input("Email Address", key="signup_email")
        signup_password = st.text_input("Password", type="password", key="signup_password")
        signup_user_type = st.selectbox("I am a:", ["Mentor", "Mentee"], key="signup_user_type")
        
        if st.button("Sign Up", use_container_width=True):
            if signup_email and signup_password and signup_user_type:
                conn = sqlite3.connect('wim_matchmaking.db')
                c = conn.cursor()
                
                try:
                    user_id = generate_id(signup_email, 'M' if signup_user_type == "Mentor" else 'ME')
                    table = 'mentors' if signup_user_type == "Mentor" else 'mentees'
                    
                    # Insert placeholder record
                    c.execute(f'''
                        INSERT INTO {table} (
                            {'mentor_id' if signup_user_type == 'Mentor' else 'mentee_id'},
                            email,
                            name,
                            profile_submitted_date,
                            status
                        ) VALUES (?, ?, ?, ?, ?)
                    ''', (user_id, signup_email, "", datetime.now(), "incomplete"))
                    
                    conn.commit()
                    st.success("Account created! Please log in.")
                    send_email(signup_email, "Welcome to WIM Matchmaking Platform", 
                              f"Welcome! Please log in to complete your profile.")
                    
                except sqlite3.IntegrityError:
                    st.error("Email already registered")
                
                conn.close()
            else:
                st.error("Please fill in all fields")

# ============================================================================
# MENTOR INTAKE FORM
# ============================================================================

def mentor_intake_form():
    """Display the mentor intake form."""
    st.markdown("# 👩‍🏫 Mentor Profile")
    st.markdown("Complete your profile to be matched with a mentee.")
    st.markdown("---")
    
    # Check if profile already exists
    conn = sqlite3.connect('wim_matchmaking.db')
    c = conn.cursor()
    c.execute('SELECT * FROM mentors WHERE email = ?', (st.session_state.user_email,))
    existing_profile = c.fetchone()
    conn.close()
    
    if existing_profile and existing_profile[24] == 'submitted':  # status column
        st.info("✅ Your profile has been submitted. You'll be notified when matching is complete.")
        return
    
    with st.form("mentor_form"):
        st.subheader("1. Basic Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=existing_profile[2] if existing_profile else "")
            phone = st.text_input("Phone Number", value=existing_profile[3] if existing_profile else "")
        with col2:
            company = st.text_input("Company Name", value=existing_profile[4] if existing_profile else "")
            job_title = st.text_input("Current Job Title", value=existing_profile[5] if existing_profile else "")
        
        col1, col2 = st.columns(2)
        with col1:
            years_experience = st.number_input("Years of Experience", min_value=0, max_value=60, 
                                              value=existing_profile[6] if existing_profile else 10)
        with col2:
            sector = st.selectbox("Manufacturing Sub-Sector", 
                                 ["Food & Beverage", "Textiles", "Metal & Allied", "Chemical & Allied", 
                                  "Plastics & Rubber", "Automotive", "Other"],
                                 index=0)
        
        st.subheader("2. Mentoring Background")
        is_first_time = st.radio("Is this your first time mentoring?", ["Yes", "No"])
        if is_first_time == "No":
            num_mentees = st.selectbox("How many mentees have you mentored?", ["1-3", "4-10", "10+"])
        else:
            num_mentees = "First time"
        
        why_mentoring = st.text_area("Why are you interested in mentoring women in manufacturing?", 
                                     value=existing_profile[9] if existing_profile else "", height=100)
        
        st.subheader("3. Professional Strengths")
        strength_options = [
            "Operations excellence & process optimization",
            "Team building & people management",
            "Strategic planning & business acumen",
            "Financial management & profitability",
            "Sales & business development",
            "Technical expertise (manufacturing-specific)",
            "Executive presence & leadership",
            "Scaling businesses",
            "Innovation & change management"
        ]
        top_3_strengths = st.multiselect("Select your top 3 professional strengths", 
                                        strength_options, max_selections=3,
                                        default=json.loads(existing_profile[10]) if existing_profile and existing_profile[10] else [])
        
        st.subheader("4. Mentoring Focus")
        mentoring_focus = st.multiselect("What are you most passionate about teaching?", 
                                        strength_options, max_selections=3,
                                        default=json.loads(existing_profile[11]) if existing_profile and existing_profile[11] else [])
        
        st.subheader("5. Communication Style")
        communication_style = st.radio("How do you prefer to mentor?",
                                      ["Direct & challenging (push me hard)", 
                                       "Collaborative & supportive (guide me gently)",
                                       "Balanced (mix of both)"])
        
        st.subheader("6. Availability")
        col1, col2 = st.columns(2)
        with col1:
            hours_per_month = st.selectbox("Hours per month you can commit",
                                          ["2-4", "4-6", "6-8", "8+"])
        with col2:
            st.write("Preferred meeting times:")
            meeting_times = st.multiselect("Select all that apply",
                                          ["Early morning (6-8 AM)", "Mid-morning (8-10 AM)", 
                                           "Late morning (10 AM-12 PM)", "Early afternoon (12-2 PM)",
                                           "Late afternoon (2-4 PM)", "Evening (4-6 PM)", "Flexible"],
                                          default=json.loads(existing_profile[14]) if existing_profile and existing_profile[14] else [])
        
        st.subheader("7. EOS Right Seat Assessment")
        st.write("Rate yourself 1-5 on these three questions:")
        col1, col2, col3 = st.columns(3)
        with col1:
            gwc_get_it = st.slider("Do you GET IT?", 1, 5, 
                                   value=existing_profile[15] if existing_profile else 3,
                                   help="Do you naturally understand the mentoring process?")
        with col2:
            gwc_want_it = st.slider("Do you WANT IT?", 1, 5,
                                   value=existing_profile[16] if existing_profile else 3,
                                   help="Are you genuinely passionate about mentoring?")
        with col3:
            gwc_capacity = st.slider("Do you have CAPACITY?", 1, 5,
                                    value=existing_profile[17] if existing_profile else 3,
                                    help="Do you have time, energy, and bandwidth?")
        
        gwc_score = (gwc_get_it + gwc_want_it + gwc_capacity) / 3
        st.info(f"Your GWC Score: {gwc_score:.1f}/5.0")
        
        st.subheader("8. Additional Information")
        conflicts = st.text_area("Any conflicts of interest or people you cannot mentor?",
                                value=existing_profile[20] if existing_profile else "", height=80)
        specific_preference = st.text_area("Any specific mentee profile you're interested in? (Optional)",
                                          value=existing_profile[21] if existing_profile else "", height=80)
        additional = st.text_area("Anything else we should know? (Optional)",
                                 value=existing_profile[22] if existing_profile else "", height=80)
        
        st.markdown("---")
        col1, col2 = st.columns([1, 1])
        with col1:
            agree_code = st.checkbox("I agree to the Code of Conduct")
        with col2:
            agree_confidentiality = st.checkbox("I understand the confidentiality requirements")
        
        submitted = st.form_submit_button("Submit Profile", use_container_width=True)
        
        if submitted:
            if not (name and company and job_title and sector and top_3_strengths and mentoring_focus and agree_code and agree_confidentiality):
                st.error("Please fill in all required fields and agree to the terms")
            else:
                # Save to database
                conn = sqlite3.connect('wim_matchmaking.db')
                c = conn.cursor()
                mentor_id = generate_id(st.session_state.user_email, 'M')
                
                c.execute('''
                    UPDATE mentors SET
                        name = ?, phone = ?, company = ?, job_title = ?,
                        years_experience = ?, sector = ?, is_first_time_mentor = ?,
                        num_previous_mentees = ?, why_mentoring = ?, top_3_strengths = ?,
                        mentoring_focus = ?, communication_style = ?, hours_per_month = ?,
                        preferred_meeting_times = ?, gwc_get_it = ?, gwc_want_it = ?,
                        gwc_capacity = ?, gwc_score = ?, conflicts_of_interest = ?,
                        specific_mentee_preference = ?, additional_info = ?,
                        profile_submitted_date = ?, status = ?
                    WHERE email = ?
                ''', (
                    name, phone, company, job_title, years_experience, sector,
                    is_first_time == "Yes", num_mentees, why_mentoring,
                    json.dumps(top_3_strengths), json.dumps(mentoring_focus),
                    communication_style, hours_per_month, json.dumps(meeting_times),
                    gwc_get_it, gwc_want_it, gwc_capacity, gwc_score,
                    conflicts, specific_preference, additional,
                    datetime.now(), 'submitted', st.session_state.user_email
                ))
                
                conn.commit()
                conn.close()
                
                # Send confirmation email
                send_email(st.session_state.user_email, 
                          "Mentor Profile Submitted - WIM Matchmaking",
                          f"Thank you for submitting your profile! We'll notify you when matching is complete.")
                
                log_audit("mentor_profile_submitted", mentor_id, None, {"name": name, "sector": sector})
                
                st.success("✅ Profile submitted successfully! You'll be notified when matching is complete.")
                st.balloons()

# ============================================================================
# MENTEE INTAKE FORM
# ============================================================================

def mentee_intake_form():
    """Display the mentee intake form."""
    st.markdown("# 👩‍💼 Mentee Profile")
    st.markdown("Complete your profile to be matched with a mentor.")
    st.markdown("---")
    
    # Check if profile already exists
    conn = sqlite3.connect('wim_matchmaking.db')
    c = conn.cursor()
    c.execute('SELECT * FROM mentees WHERE email = ?', (st.session_state.user_email,))
    existing_profile = c.fetchone()
    conn.close()
    
    if existing_profile and existing_profile[24] == 'submitted':  # status column
        st.info("✅ Your profile has been submitted. You'll be notified when matching is complete.")
        return
    
    with st.form("mentee_form"):
        st.subheader("1. Basic Information")
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", value=existing_profile[2] if existing_profile else "")
            phone = st.text_input("Phone Number", value=existing_profile[3] if existing_profile else "")
        with col2:
            company = st.text_input("Company Name (or Business Name)", value=existing_profile[4] if existing_profile else "")
            job_title = st.text_input("Current Job Title", value=existing_profile[5] if existing_profile else "")
        
        col1, col2 = st.columns(2)
        with col1:
            years_experience = st.number_input("Years of Experience", min_value=0, max_value=60,
                                              value=existing_profile[6] if existing_profile else 5)
        with col2:
            sector = st.selectbox("Manufacturing Sub-Sector",
                                 ["Food & Beverage", "Textiles", "Metal & Allied", "Chemical & Allied",
                                  "Plastics & Rubber", "Automotive", "Other"],
                                 index=0)
        
        st.subheader("2. Current Situation")
        biggest_challenge = st.text_area("What is your biggest professional challenge right now?",
                                        value=existing_profile[8] if existing_profile else "", height=100,
                                        help="This is your 'ceiling' - what's holding you back?")
        challenge_duration = st.selectbox("How long have you been facing this challenge?",
                                         ["< 6 months", "6-12 months", "1-2 years", "2+ years"])
        
        st.subheader("3. Development Areas")
        development_options = [
            "Executive presence & leadership",
            "Strategic planning & business acumen",
            "Financial management & profitability",
            "Sales & business development",
            "Operations excellence & process optimization",
            "Team building & people management",
            "Scaling businesses",
            "Technical expertise (manufacturing-specific)",
            "Work-life integration"
        ]
        top_3_development = st.multiselect("Select top 3 areas you want to develop",
                                          development_options, max_selections=3,
                                          default=json.loads(existing_profile[10]) if existing_profile and existing_profile[10] else [])
        
        st.subheader("4. Career Aspirations")
        career_aspirations = st.text_area("What is your target role or goal in the next 3 years?",
                                         value=existing_profile[11] if existing_profile else "", height=100)
        employment_type = st.multiselect("Employment type",
                                        ["Working in manufacturing company", "Running my own business"],
                                        default=json.loads(existing_profile[12]) if existing_profile and existing_profile[12] else [])
        
        st.subheader("5. Communication Style")
        communication_style = st.radio("How do you prefer to be mentored?",
                                      ["Direct & challenging (push me hard)",
                                       "Collaborative & supportive (guide me gently)",
                                       "Balanced (mix of both)"])
        
        st.subheader("6. Availability")
        col1, col2 = st.columns(2)
        with col1:
            hours_per_month = st.selectbox("Hours per month you can commit",
                                          ["2-4", "4-6", "6-8", "8+"])
        with col2:
            st.write("Preferred meeting times:")
            meeting_times = st.multiselect("Select all that apply",
                                          ["Early morning (6-8 AM)", "Mid-morning (8-10 AM)",
                                           "Late morning (10 AM-12 PM)", "Early afternoon (12-2 PM)",
                                           "Late afternoon (2-4 PM)", "Evening (4-6 PM)", "Flexible"],
                                          default=json.loads(existing_profile[14]) if existing_profile and existing_profile[14] else [])
        
        st.subheader("7. EOS Right Seat Assessment")
        st.write("Rate yourself 1-5 on these three questions:")
        col1, col2, col3 = st.columns(3)
        with col1:
            gwc_get_it = st.slider("Do you GET IT?", 1, 5,
                                   value=existing_profile[15] if existing_profile else 3,
                                   help="Can you take feedback and apply it?")
        with col2:
            gwc_want_it = st.slider("Do you WANT IT?", 1, 5,
                                   value=existing_profile[16] if existing_profile else 3,
                                   help="Are you committed to your own development?")
        with col3:
            gwc_capacity = st.slider("Do you have CAPACITY?", 1, 5,
                                    value=existing_profile[17] if existing_profile else 3,
                                    help="Do you have time, energy, and bandwidth?")
        
        gwc_score = (gwc_get_it + gwc_want_it + gwc_capacity) / 3
        st.info(f"Your GWC Score: {gwc_score:.1f}/5.0")
        
        st.subheader("8. Mentor Preferences")
        mentor_type = st.text_area("Is there a specific type of mentor you're looking for? (Optional)",
                                  value=existing_profile[19] if existing_profile else "", height=80)
        conflicts = st.text_area("Any conflicts of interest or people you cannot be mentored by?",
                                value=existing_profile[20] if existing_profile else "", height=80)
        additional = st.text_area("Anything else we should know? (Optional)",
                                 value=existing_profile[21] if existing_profile else "", height=80)
        
        st.markdown("---")
        col1, col2 = st.columns([1, 1])
        with col1:
            agree_code = st.checkbox("I agree to the Code of Conduct")
        with col2:
            agree_confidentiality = st.checkbox("I understand the confidentiality requirements")
        
        submitted = st.form_submit_button("Submit Profile", use_container_width=True)
        
        if submitted:
            if not (name and company and job_title and sector and biggest_challenge and top_3_development and agree_code and agree_confidentiality):
                st.error("Please fill in all required fields and agree to the terms")
            else:
                # Save to database
                conn = sqlite3.connect('wim_matchmaking.db')
                c = conn.cursor()
                mentee_id = generate_id(st.session_state.user_email, 'ME')
                
                c.execute('''
                    UPDATE mentees SET
                        name = ?, phone = ?, company = ?, job_title = ?,
                        years_experience = ?, sector = ?, biggest_challenge = ?,
                        challenge_duration = ?, top_3_development_areas = ?,
                        career_aspirations = ?, employment_type = ?, communication_style = ?,
                        hours_per_month = ?, preferred_meeting_times = ?, gwc_get_it = ?,
                        gwc_want_it = ?, gwc_capacity = ?, gwc_score = ?,
                        mentor_preferences = ?, conflicts_of_interest = ?, additional_info = ?,
                        profile_submitted_date = ?, status = ?
                    WHERE email = ?
                ''', (
                    name, phone, company, job_title, years_experience, sector,
                    biggest_challenge, challenge_duration, json.dumps(top_3_development),
                    career_aspirations, json.dumps(employment_type), communication_style,
                    hours_per_month, json.dumps(meeting_times),
                    gwc_get_it, gwc_want_it, gwc_capacity, gwc_score,
                    mentor_type, conflicts, additional,
                    datetime.now(), 'submitted', st.session_state.user_email
                ))
                
                conn.commit()
                conn.close()
                
                # Send confirmation email
                send_email(st.session_state.user_email,
                          "Mentee Profile Submitted - WIM Matchmaking",
                          f"Thank you for submitting your profile! We'll notify you when matching is complete.")
                
                log_audit("mentee_profile_submitted", mentee_id, mentee_id, {"name": name, "sector": sector})
                
                st.success("✅ Profile submitted successfully! You'll be notified when matching is complete.")
                st.balloons()

# ============================================================================
# MATCHING ALGORITHM
# ============================================================================

def calculate_compatibility_score(mentee, mentor):
    """
    Calculate compatibility score between a mentee and mentor.
    Returns a score 0-100 and breakdown of factors.
    """
    
    # Parse JSON fields
    mentee_dev_areas = json.loads(mentee[10]) if mentee[10] else []
    mentor_strengths = json.loads(mentor[10]) if mentor[10] else []
    mentee_comm = mentee[12]
    mentor_comm = mentor[11]
    mentee_times = json.loads(mentee[14]) if mentee[14] else []
    mentor_times = json.loads(mentor[14]) if mentor[14] else []
    
    scores = {}
    
    # 1. Sector Alignment (25%)
    if mentee[6] == mentor[6]:
        scores['sector'] = 100
    else:
        scores['sector'] = 50  # Cross-sector gets 50, flagged for intentional diversity
    
    # 2. Challenge-Skill Match (30%)
    # Check if mentor's strengths address mentee's development areas
    matching_areas = set(mentor_strengths) & set(mentee_dev_areas)
    if len(matching_areas) >= 2:
        scores['challenge_skill'] = 100
    elif len(matching_areas) == 1:
        scores['challenge_skill'] = 70
    else:
        scores['challenge_skill'] = 30
    
    # 3. Communication Style Compatibility (15%)
    if mentee_comm == mentor_comm:
        scores['communication'] = 100
    elif (mentee_comm == "Balanced (mix of both)" or mentor_comm == "Balanced (mix of both)"):
        scores['communication'] = 70
    else:
        scores['communication'] = 30
    
    # 4. Availability Fit (15%)
    # Check if there's overlap in preferred meeting times
    if "Flexible" in mentee_times or "Flexible" in mentor_times:
        scores['availability'] = 100
    else:
        overlap = set(mentee_times) & set(mentor_times)
        if len(overlap) >= 2:
            scores['availability'] = 100
        elif len(overlap) == 1:
            scores['availability'] = 70
        else:
            scores['availability'] = 0  # No overlap = pairing rejected
    
    # 5. GWC Alignment (10%)
    mentee_gwc = mentee[17]  # gwc_score
    mentor_gwc = mentor[18]  # gwc_score
    if mentee_gwc >= 3.5 and mentor_gwc >= 3.5:
        scores['gwc'] = 100
    elif mentee_gwc >= 3.0 and mentor_gwc >= 3.0:
        scores['gwc'] = 70
    else:
        scores['gwc'] = 30
    
    # 6. Experience Level Match (5%)
    mentee_exp = mentee[7]  # years_experience
    mentor_exp = mentor[7]  # years_experience
    if mentor_exp >= mentee_exp + 5:
        scores['experience'] = 100
    elif mentor_exp >= mentee_exp + 3:
        scores['experience'] = 70
    else:
        scores['experience'] = 30
    
    # Calculate weighted score
    weights = {
        'sector': 0.25,
        'challenge_skill': 0.30,
        'communication': 0.15,
        'availability': 0.15,
        'gwc': 0.10,
        'experience': 0.05
    }
    
    final_score = sum(scores[key] * weights[key] for key in scores)
    
    # Reject if availability is 0
    if scores['availability'] == 0:
        final_score = 0
    
    return final_score, scores

def run_matching_algorithm():
    """Run the matching algorithm for all mentees."""
    conn = sqlite3.connect('wim_matchmaking.db')
    c = conn.cursor()
    
    # Get all submitted mentees and mentors
    c.execute('SELECT * FROM mentees WHERE status = ?', ('submitted',))
    mentees = c.fetchall()
    
    c.execute('SELECT * FROM mentors WHERE status = ?', ('submitted',))
    mentors = c.fetchall()
    
    # Generate pairings
    pairings = []
    for mentee in mentees:
        mentee_id = mentee[0]
        compatibility_scores = []
        
        for mentor in mentors:
            mentor_id = mentor[0]
            score, breakdown = calculate_compatibility_score(mentee, mentor)
            compatibility_scores.append((mentor_id, score, breakdown))
        
        # Sort by score
        compatibility_scores.sort(key=lambda x: x[1], reverse=True)
        
        # Get top 3 matches
        top_3 = compatibility_scores[:3]
        
        # Check for intentional diversity
        intentional_diversity = None
        if len(compatibility_scores) > 3:
            # Check if top 3 are all same sector
            mentee_sector = mentee[6]
            top_3_sectors = [m[2]['sector'] for m in top_3]  # This won't work, need to fix
            
            # Find first cross-sector option
            for mentor_id, score, breakdown in compatibility_scores[3:]:
                mentor = next(m for m in mentors if m[0] == mentor_id)
                if mentor[6] != mentee_sector:
                    intentional_diversity = (mentor_id, score, breakdown)
                    break
        
        pairings.append({
            'mentee_id': mentee_id,
            'top_3': top_3,
            'intentional_diversity': intentional_diversity
        })
    
    return pairings

# ============================================================================
# ADMIN DASHBOARD
# ============================================================================

def admin_dashboard():
    """Display the admin dashboard for reviewing and approving pairings."""
    st.markdown("# 🔐 Admin Dashboard")
    st.markdown("---")
    
    # Check if user is admin
    if st.session_state.user_type != 'admin':
        st.error("Access denied. Admin only.")
        return
    
    # Tabs for different sections
    tab1, tab2, tab3, tab4 = st.tabs(["Intake Status", "Matching", "Approvals", "Audit Trail"])
    
    with tab1:
        st.subheader("Intake Status")
        conn = sqlite3.connect('wim_matchmaking.db')
        c = conn.cursor()
        
        c.execute('SELECT COUNT(*) FROM mentors WHERE status = ?', ('submitted',))
        mentors_submitted = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM mentees WHERE status = ?', ('submitted',))
        mentees_submitted = c.fetchone()[0]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Mentors Submitted", mentors_submitted)
        with col2:
            st.metric("Mentees Submitted", mentees_submitted)
        with col3:
            st.metric("Total Profiles", mentors_submitted + mentees_submitted)
        
        if st.button("Run Matching Algorithm", use_container_width=True):
            st.session_state.pairings = run_matching_algorithm()
            st.success("✅ Matching algorithm completed!")
            st.rerun()
        
        conn.close()
    
    with tab2:
        st.subheader("Matching Review")
        st.write("Review AI-recommended pairings and approve, reject, or manually pair.")
        
        # This would display the matching results
        st.info("Run the matching algorithm in the 'Intake Status' tab first.")
    
    with tab3:
        st.subheader("Approvals")
        st.write("Approve or reject pairings.")
        st.info("Approvals will be shown here after matching.")
    
    with tab4:
        st.subheader("Audit Trail")
        conn = sqlite3.connect('wim_matchmaking.db')
        c = conn.cursor()
        c.execute('SELECT * FROM audit_trail ORDER BY timestamp DESC LIMIT 50')
        audit_data = c.fetchall()
        conn.close()
        
        if audit_data:
            df = pd.DataFrame(audit_data, columns=['ID', 'Action', 'User', 'Mentee', 'Mentor', 'Details', 'Timestamp'])
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No audit trail entries yet.")

# ============================================================================
# PRACTICE MODE
# ============================================================================

def practice_mode():
    """Practice mode for testing the platform with dummy data."""
    st.markdown("# 🧪 Practice Mode")
    st.markdown("Test the platform with sample data.")
    st.markdown("---")
    
    if st.button("Load Sample Mentor Profiles", use_container_width=True):
        # Load sample data
        sample_mentors = [
            {
                "name": "Amara Okonkwo",
                "email": "amara.okonkwo@sample.com",
                "sector": "Textiles",
                "strengths": ["Strategic planning & business acumen", "Executive presence & leadership", "Team building & people management"],
                "communication": "Direct & challenging (push me hard)"
            },
            {
                "name": "Grace Kipchoge",
                "email": "grace.kipchoge@sample.com",
                "sector": "Food & Beverage",
                "strengths": ["Operations excellence & process optimization", "Financial management & profitability", "Scaling businesses"],
                "communication": "Collaborative & supportive (guide me gently)"
            }
        ]
        
        conn = sqlite3.connect('wim_matchmaking.db')
        c = conn.cursor()
        
        for mentor in sample_mentors:
            mentor_id = generate_id(mentor['email'], 'M')
            c.execute('''
                INSERT OR REPLACE INTO mentors (
                    mentor_id, email, name, company, job_title, years_experience,
                    sector, is_first_time_mentor, top_3_strengths, mentoring_focus,
                    communication_style, hours_per_month, preferred_meeting_times,
                    gwc_get_it, gwc_want_it, gwc_capacity, gwc_score,
                    profile_submitted_date, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                mentor_id, mentor['email'], mentor['name'], "Sample Company", "Director",
                15, mentor['sector'], False, json.dumps(mentor['strengths']),
                json.dumps(mentor['strengths']), mentor['communication'], "4-6",
                json.dumps(["Morning", "Afternoon"]), 4, 5, 4, 4.3,
                datetime.now(), 'submitted'
            ))
        
        conn.commit()
        conn.close()
        st.success("✅ Sample mentor profiles loaded!")
    
    if st.button("Load Sample Mentee Profiles", use_container_width=True):
        sample_mentees = [
            {
                "name": "Sarah Chen",
                "email": "sarah.chen@sample.com",
                "sector": "Textiles",
                "challenge": "Moving into senior leadership",
                "dev_areas": ["Executive presence & leadership", "Strategic planning & business acumen", "Team building & people management"],
                "communication": "Direct & challenging (push me hard)"
            },
            {
                "name": "Zainab Hassan",
                "email": "zainab.hassan@sample.com",
                "sector": "Food & Beverage",
                "challenge": "Scaling my business profitably",
                "dev_areas": ["Financial management & profitability", "Operations excellence & process optimization", "Sales & business development"],
                "communication": "Collaborative & supportive (guide me gently)"
            }
        ]
        
        conn = sqlite3.connect('wim_matchmaking.db')
        c = conn.cursor()
        
        for mentee in sample_mentees:
            mentee_id = generate_id(mentee['email'], 'ME')
            c.execute('''
                INSERT OR REPLACE INTO mentees (
                    mentee_id, email, name, company, job_title, years_experience,
                    sector, biggest_challenge, challenge_duration, top_3_development_areas,
                    career_aspirations, employment_type, communication_style,
                    hours_per_month, preferred_meeting_times,
                    gwc_get_it, gwc_want_it, gwc_capacity, gwc_score,
                    profile_submitted_date, status
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                mentee_id, mentee['email'], mentee['name'], "Sample Company", "Manager",
                8, mentee['sector'], mentee['challenge'], "1-2 years",
                json.dumps(mentee['dev_areas']), "Senior leadership role",
                json.dumps(["Corporate"]), mentee['communication'], "6-8",
                json.dumps(["Morning", "Afternoon"]), 4, 4, 4, 4.0,
                datetime.now(), 'submitted'
            ))
        
        conn.commit()
        conn.close()
        st.success("✅ Sample mentee profiles loaded!")

# ============================================================================
# MAIN APP
# ============================================================================

def main():
    """Main application logic."""
    init_database()
    init_session_state()
    
    # Sidebar
    with st.sidebar:
        st.markdown("## Navigation")
        
        if st.session_state.logged_in:
            st.write(f"**Logged in as:** {st.session_state.user_email}")
            
            if st.button("Logout", use_container_width=True):
                st.session_state.logged_in = False
                st.session_state.user_type = None
                st.session_state.user_email = None
                st.rerun()
        
        st.markdown("---")
        
        # Navigation based on user type
        if not st.session_state.logged_in:
            page = st.radio("Select Page", ["Login"])
        elif st.session_state.user_type == 'mentor':
            page = st.radio("Select Page", ["My Profile", "Match Status"])
        elif st.session_state.user_type == 'mentee':
            page = st.radio("Select Page", ["My Profile", "Match Status"])
        elif st.session_state.user_type == 'admin':
            page = st.radio("Select Page", ["Dashboard", "Practice Mode"])
    
    # Main content
    if not st.session_state.logged_in:
        login_page()
    elif st.session_state.user_type == 'mentor':
        if page == "My Profile":
            mentor_intake_form()
        elif page == "Match Status":
            st.markdown("# 🎯 Match Status")
            st.info("Your match will be revealed here once matching is complete.")
    elif st.session_state.user_type == 'mentee':
        if page == "My Profile":
            mentee_intake_form()
        elif page == "Match Status":
            st.markdown("# 🎯 Match Status")
            st.info("Your match will be revealed here once matching is complete.")
    elif st.session_state.user_type == 'admin':
        if page == "Dashboard":
            admin_dashboard()
        elif page == "Practice Mode":
            practice_mode()

if __name__ == "__main__":
    main()
