# Deployment Guide - WIM Matchmaking Platform

## Quick Start (Local Testing)

### 1. Install Dependencies
```bash
cd /home/ubuntu/wim-matchmaking-platform
pip install -r requirements.txt
```

### 2. Run Locally
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

### 3. Test Admin Login
- **Email:** admin@kam.co.ke
- **Password:** admin123

---

## Deployment to Streamlit Cloud (FREE)

### Step 1: Prepare GitHub Repository

1. **Initialize git:**
   ```bash
   cd /home/ubuntu/wim-matchmaking-platform
   git init
   git add .
   git commit -m "Initial commit: WIM Matchmaking Platform v1.0"
   ```

2. **Create GitHub repository:**
   - Go to https://github.com/new
   - Create a new repository (e.g., `wim-matchmaking-platform`)
   - Do NOT initialize with README, .gitignore, or license

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/wim-matchmaking-platform.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud:**
   - Visit https://share.streamlit.io/
   - Sign in with GitHub account

2. **Create new app:**
   - Click "New app"
   - Select your GitHub repository
   - Select branch: `main`
   - Select file path: `app.py`
   - Click "Deploy"

3. **Wait for deployment:**
   - Streamlit will build and deploy your app (takes 2-5 minutes)
   - You'll get a public URL like: `https://wim-matchmaking-platform.streamlit.app`

4. **Share the URL:**
   - Send to KAM for participant access
   - Share with mentors and mentees

---

## Production Checklist

Before going live:

- [ ] Change admin password from default (`admin123`)
- [ ] Test all forms with real data
- [ ] Test matching algorithm with sample data
- [ ] Verify email notifications work (or confirm console logging)
- [ ] Test admin dashboard workflows
- [ ] Test match reveal interface
- [ ] Verify audit trail logging
- [ ] Check database backups
- [ ] Document any custom configurations
- [ ] Create user guide for KAM admin

---

## Admin Password Change

To change the admin password:

1. **Connect to the database:**
   ```bash
   python3
   ```

2. **Run this code:**
   ```python
   import sqlite3
   import hashlib
   
   def hash_password(password):
       return hashlib.sha256(password.encode()).hexdigest()
   
   conn = sqlite3.connect('wim_matchmaking.db')
   c = conn.cursor()
   
   new_password = "your_new_password_here"
   c.execute('UPDATE admin_users SET password_hash = ? WHERE email = ?',
             (hash_password(new_password), 'admin@kam.co.ke'))
   
   conn.commit()
   conn.close()
   print("✅ Password changed!")
   ```

3. **Exit Python:** `exit()`

---

## Database Backup

### Local Backup
```bash
cp /home/ubuntu/wim-matchmaking-platform/wim_matchmaking.db \
   /home/ubuntu/wim_matchmaking_backup_$(date +%Y%m%d_%H%M%S).db
```

### Automated Backup (Cron Job)
```bash
# Add to crontab
0 2 * * * cp /home/ubuntu/wim-matchmaking-platform/wim_matchmaking.db /backups/wim_matchmaking_$(date +\%Y\%m\%d).db
```

---

## Troubleshooting

### App won't start
```bash
# Check Python version
python3 --version  # Should be 3.8+

# Reinstall dependencies
pip install -r requirements.txt

# Check for syntax errors
python3 -m py_compile app.py
```

### Database errors
```bash
# Reset database (WARNING: deletes all data)
rm wim_matchmaking.db
streamlit run app.py  # Will create fresh database

# Check database integrity
sqlite3 wim_matchmaking.db "PRAGMA integrity_check;"
```

### Login issues
```bash
# Verify admin user exists
sqlite3 wim_matchmaking.db "SELECT * FROM admin_users;"

# Reset admin user
python3 setup_admin.py
```

### Matching algorithm not working
```bash
# Check if profiles exist
sqlite3 wim_matchmaking.db "SELECT COUNT(*) FROM mentors WHERE status='submitted';"
sqlite3 wim_matchmaking.db "SELECT COUNT(*) FROM mentees WHERE status='submitted';"

# Check for errors in console
streamlit run app.py --logger.level=debug
```

---

## Monitoring

### Check App Status
```bash
# View running Streamlit processes
ps aux | grep streamlit

# View logs (if running with nohup)
tail -f streamlit.log
```

### Database Queries

**Count profiles:**
```bash
sqlite3 wim_matchmaking.db "SELECT 'Mentors' as type, COUNT(*) FROM mentors UNION SELECT 'Mentees', COUNT(*) FROM mentees;"
```

**View recent activity:**
```bash
sqlite3 wim_matchmaking.db "SELECT * FROM audit_trail ORDER BY timestamp DESC LIMIT 20;"
```

**Check pairings:**
```bash
sqlite3 wim_matchmaking.db "SELECT COUNT(*) FROM pairings WHERE admin_decision='approved';"
```

---

## Scaling to Multiple Cohorts

### For Cohort 2:

1. **Archive Cohort 1 data:**
   ```bash
   sqlite3 wim_matchmaking.db "CREATE TABLE mentors_cohort1 AS SELECT * FROM mentors;"
   sqlite3 wim_matchmaking.db "CREATE TABLE mentees_cohort1 AS SELECT * FROM mentees;"
   sqlite3 wim_matchmaking.db "CREATE TABLE pairings_cohort1 AS SELECT * FROM pairings;"
   ```

2. **Clear active tables:**
   ```bash
   sqlite3 wim_matchmaking.db "DELETE FROM mentors; DELETE FROM mentees; DELETE FROM pairings;"
   ```

3. **Run Cohort 2 intake and matching**

---

## Support

For issues or questions:
1. Check the README.md for general information
2. Review the audit trail for decision history
3. Contact Value Connect: mercy@valueconnectonline.com

---

**Last Updated:** May 2026
**Version:** 1.0
