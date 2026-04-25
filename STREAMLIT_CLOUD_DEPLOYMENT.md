# Streamlit Cloud Deployment Guide
## Women In Manufacturing Matchmaking Platform

**Deployment Time:** 5 minutes
**Cost:** FREE
**Hosting:** Streamlit Community Cloud

---

## Quick Start (Easiest Method)

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Create a new repository:
   - **Repository name:** `wim-matchmaking-platform`
   - **Description:** "AI-Powered Mentor-Mentee Pairing System for KAM Women in Manufacturing"
   - **Visibility:** Public (required for free Streamlit Cloud)
   - **Initialize:** Do NOT check "Add a README" or ".gitignore"
3. Click "Create repository"

### Step 2: Push Code to GitHub

After creating the repository, you'll see instructions. Run these commands:

```bash
cd /home/ubuntu/wim-matchmaking-platform

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/wim-matchmaking-platform.git

# Rename branch to main
git branch -M main

# Push code
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username**

### Step 3: Deploy to Streamlit Cloud

1. Go to https://share.streamlit.io/
2. Sign in with your GitHub account
3. Click "New app"
4. Fill in:
   - **Repository:** `YOUR_USERNAME/wim-matchmaking-platform`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click "Deploy"

**Wait 2-5 minutes for deployment to complete**

### Step 4: Share Your Live URL

Once deployed, you'll get a URL like:
```
https://wim-matchmaking-platform.streamlit.app
```

**Share this URL with KAM and all participants!**

---

## Test Your Deployment

1. Open your Streamlit Cloud URL
2. Test admin login:
   - Email: `admin@kam.co.ke`
   - Password: `admin123`
3. Test mentor signup
4. Test mentee signup
5. Test practice mode

---

## Important Notes

### Database Persistence

⚠️ **Important:** Streamlit Cloud uses ephemeral storage. This means:
- Database file (`wim_matchmaking.db`) will be reset when the app restarts
- For production, you need persistent storage

**For Cohort 1 (MVP):** This is acceptable - data only needs to persist during the matching phase (a few days)

**For Production:** Upgrade to Streamlit Cloud paid tier or use external database (PostgreSQL, Firebase, etc.)

### Admin Password

⚠️ **CHANGE THE DEFAULT PASSWORD IMMEDIATELY:**

1. Go to your Streamlit Cloud app
2. In the sidebar, click the menu (⋮)
3. Click "Settings"
4. Look for "Secrets" section
5. Add your new admin password

Or contact Value Connect to change it programmatically.

---

## Troubleshooting

### App won't deploy
- Check that repository is PUBLIC
- Verify `app.py` is in the root directory
- Check that `requirements.txt` has all dependencies

### App deploys but shows error
- Check the "Logs" tab in Streamlit Cloud
- Common issues:
  - Missing dependencies in `requirements.txt`
  - Syntax errors in `app.py`
  - Database file not created

### Login doesn't work
- Admin user might not exist (database was reset)
- Run `setup_admin.py` locally to recreate admin user
- Or contact Value Connect

### Database lost after restart
- This is expected behavior on free tier
- Data persists during a session but resets after app restarts
- For production, use paid tier or external database

---

## Advanced: Custom Domain

If you want a custom domain (e.g., `matchmaking.kam.co.ke`):

1. Go to your Streamlit Cloud app settings
2. Click "Custom domain"
3. Enter your domain
4. Follow DNS configuration instructions

---

## Monitoring Your App

### View Logs
- Go to your Streamlit Cloud dashboard
- Click on your app
- Click "Logs" tab
- See real-time activity

### Performance
- Free tier: Limited resources
- Sufficient for 30 mentors + 30 mentees
- If you get "Resource limit exceeded", upgrade to paid tier

### Uptime
- Streamlit Cloud: 99.9% uptime SLA
- Free tier: Best effort

---

## Next Steps

1. **Deploy the app** using steps above
2. **Share URL with KAM**
3. **Train KAM admin** on how to use the dashboard
4. **Start mentor/mentee signup**
5. **Run matching algorithm**
6. **Approve pairings**
7. **Reveal matches**

---

## Support

For issues:
1. Check Streamlit Cloud logs
2. Review DEPLOYMENT.md
3. Check TESTING_GUIDE.md
4. Contact Value Connect: mercy@valueconnectonline.com

---

## Cost Summary

| Component | Cost | Notes |
| :--- | :--- | :--- |
| Streamlit Cloud (Free) | $0/month | Sufficient for MVP |
| Custom Domain | $0 | Optional |
| Database (SQLite) | $0 | Included |
| **Total** | **$0/month** | **FREE** |

---

## Upgrade Path (When Ready)

When you scale to Cohort 2+:

| Tier | Cost | Features |
| :--- | :--- | :--- |
| Free | $0/month | Ephemeral storage, limited resources |
| Starter | $5/month | Persistent storage, more resources |
| Pro | $15/month | Priority support, custom domain |
| Business | $99/month | Team collaboration, SLA |

---

**Last Updated:** May 2026
**Version:** 1.0
