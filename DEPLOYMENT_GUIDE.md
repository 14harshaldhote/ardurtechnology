# Deployment Guide for Ardur Technology Website

## 🚀 Vercel Deployment Instructions

### Prerequisites
- GitHub repository with the project code
- Vercel account (free tier works)
- Environment variables configured

### Step 1: Prepare Your Repository
Ensure your repository has these files:
- ✅ `app.py` (main Flask application)
- ✅ `requirements.txt` (Python dependencies)
- ✅ `vercel.json` (Vercel configuration)
- ✅ `.env.example` (environment variables template)

### Step 2: Vercel Project Settings
When creating a new project on Vercel:

**Framework Preset:** Flask
**Root Directory:** `./` (if app.py is in root)
**Build Command:** Leave empty
**Output Directory:** Leave empty
**Install Command:** `pip install -r requirements.txt`

### Step 3: Environment Variables
In Vercel dashboard, add these environment variables:

#### Required for Production:
```
SECRET_KEY=your-secure-random-secret-key-here
```

#### Optional (for email functionality):
```
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=info@ardurtechnology.com
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
```

### Step 4: Deploy
1. Connect your GitHub repository to Vercel
2. Configure the environment variables
3. Deploy!

## 🔧 Key Changes Made for Vercel Compatibility

### 1. Fixed Upload Folder Issue
**Problem:** Vercel has a read-only filesystem
**Solution:** Use temporary directory for uploads
```python
# Before (causes error on Vercel)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

# After (Vercel-compatible)
upload_dir = os.path.join(tempfile.gettempdir(), "uploads")
os.makedirs(upload_dir, exist_ok=True)
app.config["UPLOAD_FOLDER"] = upload_dir
```

### 2. Environment Variables
All sensitive configuration now uses environment variables:
- `SECRET_KEY` - Flask secret key
- `MAIL_USERNAME` - Email username
- `MAIL_PASSWORD` - Email password
- `MAIL_DEFAULT_SENDER` - Default sender email

### 3. Vercel Configuration
Added `vercel.json` with proper Python runtime configuration.

## 📝 Important Notes

### File Uploads
- Files are stored in `/tmp` directory on Vercel
- Files are **temporary** and will be deleted
- For production, consider using:
  - AWS S3
  - Cloudinary
  - Vercel Blob Storage

### Email Configuration
- Uses Gmail SMTP by default
- Requires app-specific password (not regular Gmail password)
- Can be disabled by not setting email environment variables

### Local Development
1. Copy `.env.example` to `.env`
2. Update values in `.env` file
3. Run: `python run.py`

### Production Deployment
1. Set environment variables in Vercel dashboard
2. Push to GitHub
3. Vercel auto-deploys

## 🔍 Troubleshooting

### Common Issues:

**1. "Read-only file system" error**
- ✅ Fixed: Now uses `tempfile.gettempdir()`

**2. "SECRET_KEY not set" error**
- Add `SECRET_KEY` environment variable in Vercel

**3. Email not working**
- Check `MAIL_USERNAME` and `MAIL_PASSWORD` are set
- Use Gmail app-specific password
- Verify SMTP settings

**4. Static files not loading**
- Ensure `app/static/` directory structure is correct
- Check Flask static_folder configuration

### Vercel Logs
Check Vercel function logs for detailed error messages:
1. Go to Vercel dashboard
2. Select your project
3. Click "Functions" tab
4. View logs for debugging

## 🎯 Next Steps for Production

1. **Custom Domain:** Add your domain in Vercel settings
2. **SSL Certificate:** Automatic with Vercel
3. **File Storage:** Implement cloud storage for uploads
4. **Database:** Add PostgreSQL or MongoDB if needed
5. **Monitoring:** Set up error tracking (Sentry, etc.)
6. **Analytics:** Add Google Analytics
7. **CDN:** Vercel provides global CDN automatically

## 📞 Support
If you encounter issues:
1. Check Vercel function logs
2. Verify environment variables are set
3. Test locally first with `python run.py`
4. Check this guide for common solutions
