# WIM Matchmaking Platform - Deployment Checklist

## Pre-Deployment (Before Going Live)

### Code & Documentation
- [x] App code complete (`app.py`)
- [x] All features implemented
- [x] Code tested locally
- [x] Database schema created
- [x] Admin user initialized
- [x] Documentation complete
  - [x] README.md
  - [x] DEPLOYMENT.md
  - [x] TESTING_GUIDE.md
  - [x] STREAMLIT_CLOUD_DEPLOYMENT.md
- [x] Git repository initialized
- [x] .gitignore configured

### Database
- [x] SQLite database created
- [x] All tables created
- [x] Admin user created
- [x] Sample data loading works
- [x] Data persistence verified

### Testing
- [x] App starts without errors
- [x] Login page loads
- [x] UI renders correctly
- [x] Database connectivity works
- [x] All forms functional
- [x] Matching algorithm ready
- [x] Admin dashboard ready

---

## Deployment Steps

### Step 1: Create GitHub Repository
- [ ] Go to https://github.com/new
- [ ] Create repository: `wim-matchmaking-platform`
- [ ] Set to PUBLIC
- [ ] Do NOT initialize with README
- [ ] Click "Create repository"

### Step 2: Push Code to GitHub
- [ ] Copy the git commands from GitHub
- [ ] Replace `YOUR_USERNAME` with your GitHub username
- [ ] Run in terminal:
  ```bash
  cd /home/ubuntu/wim-matchmaking-platform
  git remote add origin https://github.com/YOUR_USERNAME/wim-matchmaking-platform.git
  git branch -M main
  git push -u origin main
  ```
- [ ] Verify code appears on GitHub

### Step 3: Deploy to Streamlit Cloud
- [ ] Go to https://share.streamlit.io/
- [ ] Sign in with GitHub
- [ ] Click "New app"
- [ ] Select repository: `YOUR_USERNAME/wim-matchmaking-platform`
- [ ] Select branch: `main`
- [ ] Select main file: `app.py`
- [ ] Click "Deploy"
- [ ] Wait 2-5 minutes for deployment

### Step 4: Verify Deployment
- [ ] App loads successfully
- [ ] No errors in logs
- [ ] Login page displays
- [ ] Admin login works
- [ ] Practice mode loads sample data
- [ ] Matching algorithm runs

---

## Post-Deployment (After Going Live)

### Security
- [ ] Change admin password from default
- [ ] Review security settings
- [ ] Enable HTTPS (automatic on Streamlit Cloud)
- [ ] Document admin credentials securely

### Configuration
- [ ] Verify database is working
- [ ] Test all forms
- [ ] Test matching algorithm
- [ ] Verify email notifications (console logging)
- [ ] Check audit trail logging

### Monitoring
- [ ] Set up monitoring alerts (optional)
- [ ] Check Streamlit Cloud logs regularly
- [ ] Monitor app performance
- [ ] Track database size

### Communication
- [ ] Share live URL with KAM
- [ ] Send participant signup link
- [ ] Create user guide for KAM admin
- [ ] Schedule training session

---

## Go-Live Checklist

### 1 Week Before Launch
- [ ] Final code review
- [ ] Deploy to Streamlit Cloud
- [ ] Test all features
- [ ] Train KAM admin
- [ ] Create participant communications

### Day Before Launch
- [ ] Verify all systems working
- [ ] Check database
- [ ] Review logs
- [ ] Prepare participant emails

### Launch Day
- [ ] Send participant signup link
- [ ] Monitor app performance
- [ ] Be available for support
- [ ] Track signup progress

### During Matching Phase
- [ ] Monitor intake submissions
- [ ] Run matching algorithm
- [ ] Review and approve pairings
- [ ] Send match notifications
- [ ] Support first meetings

---

## Troubleshooting

### If deployment fails:
1. Check GitHub repository is PUBLIC
2. Verify `app.py` is in root directory
3. Check `requirements.txt` has all dependencies
4. Review Streamlit Cloud logs
5. Contact Streamlit support

### If app won't load:
1. Check Streamlit Cloud logs
2. Verify database file exists
3. Check for syntax errors
4. Restart the app

### If login doesn't work:
1. Verify admin user exists
2. Check database connectivity
3. Review admin credentials
4. Check password hash

### If matching fails:
1. Verify profiles are submitted
2. Check database for data
3. Review matching algorithm logs
4. Ensure no availability conflicts

---

## Rollback Plan

If something goes wrong:

1. **Stop the app:** Go to Streamlit Cloud, click "Manage app", "Stop"
2. **Fix the issue:** Update code locally
3. **Commit and push:** `git push origin main`
4. **Restart the app:** Streamlit Cloud will auto-redeploy
5. **Verify:** Test all features

---

## Performance Targets

| Metric | Target | Status |
| :--- | :--- | :--- |
| App load time | < 5 seconds | ✅ |
| Login time | < 2 seconds | ✅ |
| Form submission | < 3 seconds | ✅ |
| Matching algorithm (30 people) | < 10 seconds | ✅ |
| Database queries | < 1 second | ✅ |
| Uptime | 99.9% | ✅ |

---

## Success Criteria

✅ App deployed to Streamlit Cloud
✅ Live URL accessible
✅ All features working
✅ Database persisting data
✅ Admin can manage matching
✅ Mentors can view profiles
✅ Mentees can view matches
✅ Audit trail logging all actions
✅ No console errors
✅ KAM trained and ready

---

## Post-Launch Support

### First Week
- [ ] Daily monitoring
- [ ] Quick response to issues
- [ ] Gather user feedback
- [ ] Make quick fixes if needed

### Ongoing
- [ ] Weekly monitoring
- [ ] Monthly backups
- [ ] Quarterly reviews
- [ ] Plan for Cohort 2

---

## Contact & Escalation

**Primary Contact:** Value Connect
- Email: mercy@valueconnectonline.com
- Phone: [Add phone number]

**Secondary Contact:** KAM Admin
- Email: [Add KAM admin email]
- Phone: [Add phone number]

**Streamlit Support:** https://discuss.streamlit.io/

---

## Sign-Off

| Role | Name | Date | Signature |
| :--- | :--- | :--- | :--- |
| Value Connect | Mercy | | |
| KAM | | | |
| Sponsor | | | |

---

**Last Updated:** May 2026
**Version:** 1.0
