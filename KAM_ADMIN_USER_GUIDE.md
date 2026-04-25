# KAM Admin User Guide
## Women In Manufacturing Matchmaking Platform

**For:** KAM Admin Team
**Version:** 1.0
**Date:** May 2026

---

## Table of Contents

1. [Getting Started](#getting-started)
2. [Login](#login)
3. [Dashboard Overview](#dashboard-overview)
4. [Managing Intake](#managing-intake)
5. [Running Matching Algorithm](#running-matching-algorithm)
6. [Reviewing Matches](#reviewing-matches)
7. [Approving Pairings](#approving-pairings)
8. [Viewing Audit Trail](#viewing-audit-trail)
9. [Practice Mode](#practice-mode)
10. [Troubleshooting](#troubleshooting)

---

## Getting Started

### What is the WIM Matchmaking Platform?

The Women In Manufacturing Matchmaking Platform is an AI-powered system that:
- Collects mentor and mentee profiles
- Automatically matches mentors with mentees based on 6 factors
- Allows you to review and approve pairings
- Tracks all decisions and activities

### Your Role as Admin

As KAM Admin, you will:
1. Monitor mentor and mentee signups
2. Review AI-recommended matches
3. Approve or reject pairings
4. View the complete audit trail
5. Manage the matching process

---

## Login

### Step 1: Open the Platform

Go to: `https://wim-matchmaking-platform.streamlit.app`

(Your actual URL will be provided by Value Connect)

### Step 2: Enter Credentials

1. Select **"Admin"** from the "I am a:" dropdown
2. Enter your email: `admin@kam.co.ke`
3. Enter your password: `[Your password]`
4. Click **"Login"**

### Step 3: You're In!

You should see the Admin Dashboard with several tabs.

---

## Dashboard Overview

### Main Tabs

After logging in, you'll see these tabs:

#### 1. 📊 Intake Status
- Shows how many mentors have submitted profiles
- Shows how many mentees have submitted profiles
- Displays total profiles received
- Shows the "Run Matching Algorithm" button

#### 2. 🎯 Matching
- Displays AI-recommended matches
- Shows compatibility scores for each pairing
- Displays the 6 factors that influenced the match
- Shows intentional diversity options (if applicable)

#### 3. ✅ Approvals
- Shows all pairings you've approved
- Displays the approval date
- Shows the reason for each approval
- Allows you to view approved pairing details

#### 4. 📋 Audit Trail
- Complete log of all platform activity
- Shows who did what and when
- Tracks all decisions
- Useful for compliance and troubleshooting

#### 5. 🧪 Practice Mode
- Load sample mentor profiles
- Load sample mentee profiles
- Test the matching algorithm
- Practice before going live

---

## Managing Intake

### Monitoring Signups

1. Go to the **"📊 Intake Status"** tab
2. You'll see:
   - **Mentors Submitted:** Number of completed mentor profiles
   - **Mentees Submitted:** Number of completed mentee profiles
   - **Total Profiles:** Combined count

### What Happens During Intake

- Mentors and mentees receive signup links
- They create accounts (email + password)
- They fill out their profile (10 steps each)
- They submit their profile
- You see the count increase in real-time

### Intake Timeline

- **Orientation Workshop:** Day 1
- **Intake Period:** Days 2-7
- **Matching:** Day 8-9
- **Approvals:** Day 10-11
- **Match Reveal:** Day 12

---

## Running Matching Algorithm

### Prerequisites

Before running the algorithm, ensure:
- ✅ At least 15 mentors have submitted profiles
- ✅ At least 15 mentees have submitted profiles
- ✅ All profiles are complete

### Step 1: Go to Intake Status Tab

1. Click the **"📊 Intake Status"** tab
2. Look for the button: **"🚀 Run Matching Algorithm"**

### Step 2: Click the Button

1. Click **"🚀 Run Matching Algorithm"**
2. You'll see a loading spinner
3. Wait 10-30 seconds (depending on number of profiles)

### Step 3: Confirm Success

You should see:
- ✅ "Matching algorithm completed!"
- Generated X pairings (one per mentee)
- All pairings saved to database

### What the Algorithm Does

The algorithm calculates a **Compatibility Score (0-100%)** for each potential mentor-mentee pair based on:

| Factor | Weight | What It Measures |
| :--- | :--- | :--- |
| Sector Alignment | 25% | Same manufacturing sector |
| Challenge-Skill Match | 30% | Does mentor's strength address mentee's need? |
| Communication Style | 15% | Compatible mentoring preferences |
| Availability Fit | 15% | Overlapping meeting times |
| GWC Alignment | 10% | Get it, Want it, Capacity scores |
| Experience Match | 5% | Mentor has sufficient experience |

---

## Reviewing Matches

### Step 1: Go to Matching Tab

1. Click the **"🎯 Matching"** tab
2. You'll see all mentee names listed

### Step 2: Review Top 3 Options

For each mentee, you'll see:

**Option 1: ⭐ HIGHEST COMPATIBILITY**
- Mentor name and company
- Compatibility score (e.g., 88%)
- Breakdown of 6 factors
- Why they were matched

**Option 2: ⭐ HIGHEST COMPATIBILITY (if different)**
- Alternative mentor option
- Compatibility score
- Breakdown of factors

**Option 3: ⭐ HIGHEST COMPATIBILITY (if different)**
- Third option
- Compatibility score
- Breakdown of factors

### Step 3: Review Intentional Diversity (If Available)

If all top 3 options are from the same sector, you'll also see:

**🌍 INTENTIONAL DIVERSITY OPTION**
- Cross-sector mentor
- Lower compatibility score (e.g., 72%)
- Explanation: "This mentor brings a fresh perspective..."
- Why you might choose this

### Understanding Compatibility Scores

| Score | Meaning | Action |
| :--- | :--- | :--- |
| 85-100% | Excellent match | Approve with confidence |
| 75-84% | Good match | Approve |
| 65-74% | Acceptable match | Review carefully before approving |
| Below 65% | Poor match | Consider rejecting or manually pairing |

---

## Approving Pairings

### Option 1: Approve Top Match

1. For each mentee, click **"✅ Approve #1"**
2. Pairing is saved immediately
3. You'll see: "✅ Pairing approved!"

### Option 2: Approve Alternative Match

1. Click **"✅ Approve #2"** or **"✅ Approve #3"**
2. Pairing is saved
3. You'll see: "✅ Pairing approved!"

### Option 3: Approve Intentional Diversity

1. If you want the cross-sector option, click **"✅ Approve Diversity"**
2. Pairing is saved
3. You'll see: "✅ Pairing approved!"

### Option 4: Manually Pair

1. If you want to pair someone different:
   - Click **"🔄 Manually Pair"**
   - Select mentor from dropdown
   - Enter reason (required)
   - Click "Save"

### Option 5: Reject All Options

1. If none of the options are good:
   - Click **"❌ Reject All"**
   - Enter reason
   - Click "Save"
   - You'll need to manually pair this mentee later

---

## Viewing Audit Trail

### Step 1: Go to Audit Trail Tab

1. Click the **"📋 Audit Trail"** tab
2. You'll see a table with all platform activity

### What You'll See

| Column | What It Shows |
| :--- | :--- |
| **ID** | Unique action ID |
| **Action** | What happened (e.g., "mentor_profile_submitted") |
| **User** | Who did it (email address) |
| **Mentee** | Mentee involved (if applicable) |
| **Mentor** | Mentor involved (if applicable) |
| **Details** | Additional information |
| **Timestamp** | When it happened |

### Common Actions

- `mentor_profile_submitted` - Mentor completed their profile
- `mentee_profile_submitted` - Mentee completed their profile
- `email_sent` - Notification email sent
- `pairing_approved` - You approved a pairing
- `pairing_rejected` - You rejected a pairing
- `manual_pairing_created` - You manually paired someone

### Using the Audit Trail

- **Verify decisions:** See exactly what was approved and when
- **Troubleshoot:** Find where things went wrong
- **Compliance:** Document all decisions for KAM
- **Learning:** Understand which matches worked best

---

## Practice Mode

### Why Use Practice Mode?

Before going live, you should:
1. Test the platform
2. Learn how to use it
3. Practice the matching process
4. Understand the interface

### Step 1: Go to Practice Mode Tab

1. Click the **"🧪 Practice Mode"** tab
2. You'll see two buttons

### Step 2: Load Sample Data

1. Click **"📥 Load Sample Mentor Profiles"**
   - 3 sample mentors will be created
   - You'll see: "✅ Sample mentor profiles loaded!"

2. Click **"📥 Load Sample Mentee Profiles"**
   - 3 sample mentees will be created
   - You'll see: "✅ Sample mentee profiles loaded!"

### Step 3: Test the Matching Algorithm

1. Go to **"📊 Intake Status"** tab
2. Click **"🚀 Run Matching Algorithm"**
3. You'll see 3 pairings generated

### Step 4: Practice Approving Matches

1. Go to **"🎯 Matching"** tab
2. Review the sample matches
3. Practice clicking "✅ Approve #1"
4. See the pairings appear in **"✅ Approvals"** tab

### Step 5: Review Audit Trail

1. Go to **"📋 Audit Trail"** tab
2. See all your test actions logged
3. Understand how the audit trail works

### Clearing Practice Data

To start fresh:
1. Contact Value Connect
2. They can reset the database
3. Or wait for the app to restart (data will be cleared)

---

## Troubleshooting

### Problem: Can't Login

**Solution:**
1. Verify email is correct: `admin@kam.co.ke`
2. Verify password is correct
3. Check that you selected "Admin" from dropdown
4. Contact Value Connect if still having issues

### Problem: No Profiles Showing

**Solution:**
1. Check that mentors/mentees have submitted profiles
2. Go to Practice Mode to load sample data
3. Test with sample data first
4. Wait for real participants to submit

### Problem: Matching Algorithm Won't Run

**Solution:**
1. Ensure at least 15 mentors have submitted profiles
2. Ensure at least 15 mentees have submitted profiles
3. Check for database errors
4. Try again in a few minutes
5. Contact Value Connect if error persists

### Problem: Compatibility Scores Don't Make Sense

**Solution:**
1. Review the 6-factor breakdown
2. Check if mentee's challenge matches mentor's strength
3. Verify availability overlap
4. Check GWC scores
5. Consider using intentional diversity option

### Problem: Can't Approve a Pairing

**Solution:**
1. Ensure you've selected a mentor
2. Check that the pairing hasn't already been approved
3. Try refreshing the page
4. Contact Value Connect if issue persists

### Problem: Database Lost Data

**Solution:**
1. This can happen on free tier if app restarts
2. For production, upgrade to paid Streamlit tier
3. Or contact Value Connect for backup restoration
4. Practice mode data is expected to be temporary

---

## Best Practices

### Before Matching

✅ **Do:**
- Verify all profiles are complete
- Check that mentors and mentees understand the program
- Have a clear timeline
- Communicate expectations

❌ **Don't:**
- Rush the matching process
- Approve pairings without reviewing
- Ignore the compatibility scores
- Skip the audit trail review

### During Matching

✅ **Do:**
- Review all three options for each mentee
- Consider intentional diversity options
- Document your reasoning
- Check the audit trail

❌ **Don't:**
- Approve without reviewing
- Ignore low compatibility scores
- Make emotional decisions
- Skip the approval process

### After Matching

✅ **Do:**
- Review the audit trail
- Communicate matches to participants
- Support first meetings
- Gather feedback

❌ **Don't:**
- Change pairings without reason
- Forget to document decisions
- Skip follow-up
- Ignore participant feedback

---

## Key Contacts

**For Technical Issues:**
- Email: mercy@valueconnect.com
- Phone: [Add phone number]

**For Program Questions:**
- Email: [Add KAM contact]
- Phone: [Add phone number]

**For Streamlit Issues:**
- Website: https://discuss.streamlit.io/
- Email: support@streamlit.io

---

## Quick Reference

### Login Credentials
- Email: `admin@kam.co.ke`
- Password: `[Your password]`
- User Type: Admin

### Platform URL
- https://wim-matchmaking-platform.streamlit.app

### Key Buttons
- 🚀 Run Matching Algorithm
- ✅ Approve #1, #2, #3
- ✅ Approve Diversity
- 🔄 Manually Pair
- ❌ Reject All

### Key Tabs
- 📊 Intake Status
- 🎯 Matching
- ✅ Approvals
- 📋 Audit Trail
- 🧪 Practice Mode

---

## Feedback & Suggestions

We'd love to hear from you!

- What worked well?
- What was confusing?
- What could be improved?
- Any bugs or issues?

**Contact:** mercy@valueconnect.com

---

**Last Updated:** May 2026
**Version:** 1.0
**Status:** Ready for Production
