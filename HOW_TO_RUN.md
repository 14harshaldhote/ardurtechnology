# How to Run Ardur Technology Application

## ✅ Use `run.py` Only

The application now uses **`run.py`** as the single entry point. The `app.py` file contains only the application logic (routes, functions, configurations).

## 🚀 Quick Start

### Development Mode (Default)
```bash
python run.py
```
- Runs on: http://127.0.0.1:5000
- Debug mode: ON
- Auto-reload: ON

### Custom Port
```bash
python run.py --port 5001
```

### Production Mode
```bash
python run.py --prod
```
- Debug mode: OFF
- Auto-reload: OFF

### Custom Host (Allow External Access)
```bash
python run.py --host 0.0.0.0 --port 5000
```

## 📋 Available Commands

| Command | Description |
|---------|-------------|
| `python run.py` | Start development server |
| `python run.py --port 8080` | Use custom port |
| `python run.py --prod` | Production mode |
| `python run.py --debug` | Force debug mode |
| `python run.py --host 0.0.0.0` | Allow external access |
| `python run.py --help` | Show all options |

## 🌐 Access URLs

After starting the server, visit:

### Main Pages
- Homepage: http://127.0.0.1:5000/
- About: http://127.0.0.1:5000/about
- Services: http://127.0.0.1:5000/services
- Contact: http://127.0.0.1:5000/contact
- Careers: http://127.0.0.1:5000/careers

### Service Detail Pages
- Title Insurance: http://127.0.0.1:5000/service/title-insurance
- Title Plant Dev: http://127.0.0.1:5000/service/title-plant-development
- Tax Services: http://127.0.0.1:5000/service/tax-services
- Appraisal Mgmt: http://127.0.0.1:5000/service/appraisal-management-services
- BPO: http://127.0.0.1:5000/service/broker-price-opinion
- Vendor Mgmt: http://127.0.0.1:5000/service/appraisal-vendor-management

## 🛑 Stop Server

Press **Ctrl + C** in the terminal

## 📁 File Structure

```
ardurtechnology/
├── run.py                    ← START THE APP HERE (SINGLE ENTRY POINT)
├── app.py                    ← Application logic only (routes, functions)
├── app/
│   ├── templates/            ← HTML templates
│   ├── static/               ← CSS, JS, images
│   └── data/                 ← JSON data files
│       ├── services.json
│       └── services_detail.json
└── uploads/                  ← Resume uploads
```

## ⚙️ Environment Variables (Optional)

Create a `.env` file for sensitive data:

```env
SECRET_KEY=your-secret-key-here
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
```

## 🔧 Troubleshooting

### Port Already in Use
```bash
python run.py --port 5001
```

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### Permission Errors
```bash
chmod +x run.py
python run.py
```

---

**Remember**: Always use `python run.py` to start your application! 🚀
