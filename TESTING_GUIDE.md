# Testing Guide - WIM Matchmaking Platform

## Test Scenarios

### Scenario 1: Mentor Sign Up and Profile Submission

**Objective:** Verify mentor can create account and submit profile

**Steps:**
1. Open app at `http://localhost:8501`
2. Click "Sign Up" tab
3. Enter:
   - Email: `mentor1@test.com`
   - Password: `password123`
   - I am a: `Mentor`
4. Click "Sign Up"
5. Should see: "✅ Account created! Please log in."
6. Login with same credentials
7. Fill out mentor profile:
   - Name: Test Mentor
   - Company: Test Company
   - Job Title: Operations Manager
   - Years Experience: 15
   - Sector: Food & Beverage
   - Is first time mentoring: No
   - Why mentoring: To give back to the community
   - Top 3 strengths: Select 3 options
   - Mentoring focus: Select 3 options
   - Communication style: Direct & challenging
   - Hours per month: 6-8
   - Meeting times: Select 2-3 options
   - GWC scores: All 4-5
   - Agree to terms: Check both boxes
8. Click "Submit Profile"
9. Should see: "✅ Profile submitted successfully!"

**Expected Result:** ✅ Profile saved to database with status='submitted'

---

### Scenario 2: Mentee Sign Up and Profile Submission

**Objective:** Verify mentee can create account and submit profile

**Steps:**
1. Open app at `http://localhost:8501`
2. Click "Sign Up" tab
3. Enter:
   - Email: `mentee1@test.com`
   - Password: `password123`
   - I am a: `Mentee`
4. Click "Sign Up"
5. Should see: "✅ Account created! Please log in."
6. Login with same credentials
7. Fill out mentee profile:
   - Name: Test Mentee
   - Company: Test Business
   - Job Title: Production Manager
   - Years Experience: 8
   - Sector: Food & Beverage
   - Biggest challenge: Scaling operations
   - Challenge duration: 1-2 years
   - Top 3 development areas: Select 3 options
   - Career aspirations: To become operations director
   - Employment type: Working in manufacturing company
   - Communication style: Collaborative & supportive
   - Hours per month: 4-6
   - Meeting times: Select 2-3 options
   - GWC scores: All 3-4
   - Agree to terms: Check both boxes
8. Click "Submit Profile"
9. Should see: "✅ Profile submitted successfully!"

**Expected Result:** ✅ Profile saved to database with status='submitted'

---

### Scenario 3: Admin Login and Dashboard Access

**Objective:** Verify admin can login and access dashboard

**Steps:**
1. Open app at `http://localhost:8501`
2. Login tab, select "Admin"
3. Enter:
   - Email: `admin@kam.co.ke`
   - Password: `admin123`
4. Click "Login"
5. Should see: "✅ Login successful!"
6. Should be redirected to Admin Dashboard
7. Should see tabs: "Intake Status", "Matching", "Approvals", "Audit Trail"

**Expected Result:** ✅ Admin dashboard loads with all tabs visible

---

### Scenario 4: Practice Mode - Load Sample Data

**Objective:** Verify sample data loads correctly

**Steps:**
1. Login as admin
2. Go to "Practice Mode" tab
3. Click "📥 Load Sample Mentor Profiles"
4. Should see: "✅ Sample mentor profiles loaded!"
5. Click "📥 Load Sample Mentee Profiles"
6. Should see: "✅ Sample mentee profiles loaded!"

**Expected Result:** ✅ 3 sample mentors and 3 sample mentees loaded

---

### Scenario 5: Run Matching Algorithm

**Objective:** Verify matching algorithm generates pairings

**Steps:**
1. Login as admin
2. Go to "Intake Status" tab
3. Should see metrics:
   - Mentors Submitted: 3
   - Mentees Submitted: 3
   - Total Profiles: 6
4. Click "🚀 Run Matching Algorithm"
5. Should see spinner and then: "✅ Matching algorithm completed!"
6. Should see: "Generated 3 pairings"

**Expected Result:** ✅ 3 pairings generated (one per mentee)

---

### Scenario 6: Review Matching Results

**Objective:** Verify admin can review AI-recommended pairings

**Steps:**
1. Login as admin
2. Go to "Matching" tab
3. Should see section: "⭐ Top AI-Recommended Matches"
4. For each mentee, should see:
   - Top 3 mentor options
   - Compatibility score (0-100%)
   - Breakdown of 6 factors
   - "✅ Approve #1", "✅ Approve #2", "✅ Approve #3" buttons
5. May also see: "🌍 Intentional Diversity Option" (if top 3 are same sector)

**Expected Result:** ✅ All pairings displayed with scores and breakdown

---

### Scenario 7: Approve a Pairing

**Objective:** Verify admin can approve a pairing

**Steps:**
1. Login as admin
2. Go to "Matching" tab
3. For first mentee, click "✅ Approve #1"
4. Should see: "✅ Pairing approved!"
5. Go to "Approvals" tab
6. Should see the approved pairing in the table

**Expected Result:** ✅ Pairing saved to database with admin_decision='approved'

---

### Scenario 8: View Approved Pairings

**Objective:** Verify admin can view all approved pairings

**Steps:**
1. Login as admin
2. Go to "Approvals" tab
3. Should see table with columns:
   - Pairing ID
   - Mentee
   - Mentor
   - Score %
   - Reason
   - Approved Date
4. Should see all approved pairings
5. Should see count: "✅ X pairings approved"

**Expected Result:** ✅ All approved pairings displayed in table

---

### Scenario 9: View Audit Trail

**Objective:** Verify audit trail logs all actions

**Steps:**
1. Login as admin
2. Go to "Audit Trail" tab
3. Should see table with columns:
   - ID
   - Action
   - User
   - Mentee
   - Mentor
   - Details
   - Timestamp
4. Should see entries for:
   - mentor_profile_submitted
   - mentee_profile_submitted
   - email_sent
   - pairing_approved

**Expected Result:** ✅ All actions logged in audit trail

---

### Scenario 10: Mentee Views Match

**Objective:** Verify mentee can view their approved match

**Steps:**
1. Approve at least one pairing as admin
2. Logout
3. Login as mentee (email: `mentee1@test.com`)
4. Go to "My Match" tab
5. Should see:
   - Mentor name
   - Mentor company, role, sector, experience
   - Mentor's strengths
   - Why they were matched
   - Compatibility score
   - Mentor's contact information
   - "Schedule First Meeting" button
6. Click "Schedule First Meeting"
7. Should see: "✅ Meeting scheduled! Check your email for calendar invite."

**Expected Result:** ✅ Mentee can view match details and schedule meeting

---

### Scenario 11: Mentor Views Match

**Objective:** Verify mentor can view their approved match

**Steps:**
1. Logout
2. Login as mentor (email: `mentor1@test.com`)
3. Go to "My Match" tab
4. Should see:
   - Mentee name
   - Mentee company, role, sector, experience
   - Mentee's development goals
   - Mentee's challenge
   - Why they were matched
   - Compatibility score
   - Mentee's contact information
   - "Schedule First Meeting" button

**Expected Result:** ✅ Mentor can view match details and schedule meeting

---

### Scenario 12: Intentional Diversity Option

**Objective:** Verify intentional diversity option appears when applicable

**Steps:**
1. Load sample data (3 mentors, 3 mentees - all same sector)
2. Run matching algorithm
3. Go to "Matching" tab
4. Should see "🌍 Intentional Diversity Option" for at least one mentee
5. Should show:
   - Cross-sector mentor
   - Lower compatibility score
   - Explanation: "This mentor brings a fresh perspective..."
   - "✅ Approve Diversity" button

**Expected Result:** ✅ Intentional diversity option displayed with explanation

---

## Test Data Validation

### Database Checks

**Check mentors table:**
```bash
sqlite3 wim_matchmaking.db "SELECT COUNT(*), status FROM mentors GROUP BY status;"
```
Expected: 3 submitted

**Check mentees table:**
```bash
sqlite3 wim_matchmaking.db "SELECT COUNT(*), status FROM mentees GROUP BY status;"
```
Expected: 3 submitted

**Check pairings table:**
```bash
sqlite3 wim_matchmaking.db "SELECT COUNT(*), admin_decision FROM pairings GROUP BY admin_decision;"
```
Expected: Approved pairings

**Check audit trail:**
```bash
sqlite3 wim_matchmaking.db "SELECT COUNT(*), action FROM audit_trail GROUP BY action;"
```
Expected: Multiple entries for different actions

---

## Performance Testing

### Load Testing
- Create 30 mentors and 30 mentees
- Run matching algorithm
- Verify it completes in < 10 seconds
- Verify all 30 pairings generated

### Database Performance
- Verify database file size < 10 MB
- Verify queries complete in < 1 second
- Verify no memory leaks after extended use

---

## Edge Cases

### Test 1: Duplicate Email
- Try to sign up with same email twice
- Expected: "❌ Email already registered"

### Test 2: Missing Required Fields
- Try to submit profile without filling required fields
- Expected: "❌ Please fill in all required fields"

### Test 3: No Availability Overlap
- Create mentor with "Early morning" only
- Create mentee with "Evening" only
- Run matching algorithm
- Expected: Pairing rejected (score = 0)

### Test 4: Invalid Login
- Try to login with wrong password
- Expected: "❌ Invalid email or password"

### Test 5: Unapproved Match
- Don't approve any pairings
- Try to view match as mentee
- Expected: "⏳ Your match hasn't been revealed yet"

---

## Regression Testing Checklist

After any code changes, verify:

- [ ] Mentor signup works
- [ ] Mentee signup works
- [ ] Admin login works
- [ ] Mentor profile submission works
- [ ] Mentee profile submission works
- [ ] Matching algorithm runs
- [ ] Matching results display correctly
- [ ] Admin can approve pairings
- [ ] Mentee can view match
- [ ] Mentor can view match
- [ ] Audit trail logs all actions
- [ ] No database errors
- [ ] No console errors

---

## Test Report Template

**Date:** [DATE]
**Tester:** [NAME]
**Version:** [VERSION]

| Scenario | Status | Notes |
| :--- | :--- | :--- |
| Mentor Sign Up | ✅/❌ | |
| Mentee Sign Up | ✅/❌ | |
| Admin Login | ✅/❌ | |
| Practice Mode | ✅/❌ | |
| Run Matching | ✅/❌ | |
| Review Matches | ✅/❌ | |
| Approve Pairing | ✅/❌ | |
| View Approvals | ✅/❌ | |
| View Audit Trail | ✅/❌ | |
| Mentee Views Match | ✅/❌ | |
| Mentor Views Match | ✅/❌ | |
| Intentional Diversity | ✅/❌ | |

**Overall Status:** ✅ PASS / ❌ FAIL

**Issues Found:**
1. [Issue 1]
2. [Issue 2]

**Recommendations:**
1. [Recommendation 1]
2. [Recommendation 2]

---

**Last Updated:** May 2026
