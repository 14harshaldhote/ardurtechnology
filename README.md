# Ardur Technology LLC - Company Website

A professional Flask-based website for Ardur Technology LLC, showcasing business process management services, digital transformation solutions, and comprehensive outsourcing capabilities.

## 🏢 About Ardur Technology

Founded in 2013 by Satish Sable, Ardur Technology LLC is a leading provider of technology-driven business process solutions. We help organizations reduce costs, increase efficiency, and achieve transformation through innovation across multiple industries including healthcare, financial services, real estate, and aviation.

## ✨ Features

- **Responsive Design**: Mobile-first approach with pure CSS media queries
- **Modern UI**: Clean, professional design with company branding
- **Service Showcase**: Comprehensive display of all business services
- **Industry Focus**: Dedicated pages for different industry verticals
- **Career Portal**: Job listings with application functionality
- **Contact System**: Multi-channel contact forms with email integration
- **SEO Optimized**: Proper meta tags, structured data, and semantic HTML
- **Performance**: Optimized loading with lazy images and efficient CSS/JS
- **Accessibility**: WCAG compliant design with proper ARIA labels

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ardurtechnology
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   SECRET_KEY=your-secret-key-here
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   MAIL_DEFAULT_SENDER=info@ardurtechnology.com
   ```

5. **Run the application**
   ```bash
   python app.py
   ```

6. **Visit the website**
   Open your browser and go to `http://localhost:5000`

## 📁 Project Structure

```
ardurtechnology/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
├── uploads/                       # File upload directory
├── app/
│   ├── data/
│   │   └── services.json          # Service data configuration
│   ├── static/
│   │   ├── css/
│   │   │   └── main.css           # Main stylesheet
│   │   ├── js/
│   │   │   └── main.js            # Main JavaScript file
│   │   └── images/
│   │       ├── logo.svg           # Company logo
│   │       └── favicon.ico        # Website favicon
│   └── templates/
│       ├── base.html              # Base template
│       ├── home.html              # Homepage
│       ├── about.html             # About us page
│       ├── services.html          # Services overview
│       ├── service_detail.html    # Individual service pages
│       ├── industries.html        # Industries we serve
│       ├── careers.html           # Careers page
│       ├── contact.html           # Contact page
│       ├── 404.html               # 404 error page
│       └── 500.html               # 500 error page
```

## 🎨 Design System

### Color Palette
- **Primary Navy**: `#003366`
- **Primary Blue**: `#0099cc` 
- **White**: `#ffffff`
- **Light Grey**: `#f2f2f2`
- **Text Dark**: `#333333`
- **Text Light**: `#777777`

### Typography
- **Font Family**: Poppins (Google Fonts)
- **Responsive scaling**: Desktop, tablet, and mobile optimized

### Components
- Header with sticky navigation
- Hero sections with call-to-action buttons
- Service cards with hover effects
- Contact forms with validation
- Footer with company information

## ⚙️ Configuration

### Email Configuration
Update the email settings in `app.py` or use environment variables:

```python
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "your-email@gmail.com"
app.config["MAIL_PASSWORD"] = "your-app-password"
```

### Service Data
Services are configured in `app/data/services.json`. You can modify this file to update:
- Service categories
- Service descriptions
- Service lists
- Icons and styling

### File Uploads
- Maximum file size: 16MB
- Allowed formats: PDF, DOC, DOCX
- Upload directory: `uploads/`

## 🔧 Development

### Running in Development Mode
```bash
export FLASK_ENV=development  # On Windows: set FLASK_ENV=development
python app.py
```

### Code Style
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Comment complex logic
- Maintain consistent indentation

### Adding New Pages
1. Create HTML template in `app/templates/`
2. Add route in `app.py`
3. Update navigation in `base.html`
4. Add any required static assets

## 🚀 Deployment

### Production Setup

1. **Install production server**
   ```bash
   pip install gunicorn
   ```

2. **Create production configuration**
   ```python
   # config.py
   import os
   
   class ProductionConfig:
       SECRET_KEY = os.environ.get('SECRET_KEY')
       MAIL_SERVER = os.environ.get('MAIL_SERVER')
       # ... other production settings
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 app:app
   ```

### Environment Variables for Production
```env
SECRET_KEY=production-secret-key
FLASK_ENV=production
MAIL_SERVER=smtp.your-provider.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-production-email
MAIL_PASSWORD=your-production-password
```

### Deployment Platforms
- **Railway**: Connect repository and deploy automatically
- **Heroku**: Use Procfile with `web: gunicorn app:app`
- **DigitalOcean**: Deploy using App Platform or Droplets
- **AWS**: Use Elastic Beanstalk or EC2
- **GoDaddy**: Follow shared hosting deployment guide

## 📱 Features Overview

### Homepage
- Company overview and mission
- Service highlights
- Statistics and achievements
- Call-to-action sections

### Services
- Six main service categories
- Detailed service descriptions
- Industry-specific solutions
- Process methodology

### Industries
- Financial Services
- Healthcare
- Real Estate & Mortgage
- Aviation

### Careers
- Current job openings
- Company benefits
- Application forms
- Equal opportunity information

### Contact
- Multiple contact methods
- Department-specific contacts
- Contact form with validation
- Business information

## 🔒 Security Features

- CSRF protection with Flask-WTF
- File upload validation
- Email validation
- Form input sanitization
- Secure headers
- Environment variable configuration

## 📈 SEO & Analytics

- Semantic HTML structure
- Meta tags optimization
- Open Graph tags
- Structured data markup
- Sitemap friendly URLs
- Google Analytics ready

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

### Contribution Guidelines
- Follow the existing code style
- Add comments for complex logic
- Update documentation as needed
- Test your changes thoroughly

## 📞 Support & Contact

- **Website**: https://ardurtechnology.com
- **Email**: info@ardurtechnology.com
- **Phone**: +1 (702) 809 2713 / +1 (702) 451 1125
- **Address**: Las Vegas, Nevada, USA

## 📄 License

This project is proprietary software owned by Ardur Technology LLC. All rights reserved.

## 🚀 Version History

- **v1.0.0** - Initial release with full website functionality
- Complete service showcase
- Career portal with job applications
- Multi-industry focus
- Responsive design implementation

---

**Built with ❤️ by Ardur Technology LLC**