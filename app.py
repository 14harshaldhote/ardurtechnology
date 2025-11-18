from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from flask_mail import Mail, Message
from flask_wtf.csrf import CSRFProtect
from werkzeug.utils import secure_filename
import os
import json
import tempfile
from datetime import datetime
import re

app = Flask(__name__, template_folder="app/templates", static_folder="app/static")

# Configuration
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "your-secret-key-change-in-production")
csrf = CSRFProtect(app)

# Use writable temp directory for uploads (Vercel-compatible)
upload_dir = os.path.join(tempfile.gettempdir(), "uploads")
os.makedirs(upload_dir, exist_ok=True)
app.config["UPLOAD_FOLDER"] = upload_dir
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 1024  # 16MB max file size

# Email configuration
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER", "smtp.gmail.com")
app.config["MAIL_PORT"] = int(os.environ.get("MAIL_PORT", 587))
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER", "info@ardurtechnology.com")
mail = Mail(app)

# Allowed file extensions for resume uploads
ALLOWED_EXTENSIONS = {"pdf", "doc", "docx"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def load_services_data():
    """Load services data from JSON file"""
    try:
        with open("app/data/services.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "business_process_management": {
                "title": "Business Process Management (BPM)",
                "services": [
                    "Title & Appraisal Services",
                    "Tax Services",
                    "Vendor Management",
                    "Document Indexing",
                    "Title Curative",
                    "Order Entry, QC, and Data Entry",
                ],
            },
            "mortgage_real_estate": {
                "title": "Mortgage & Real Estate Services",
                "services": [
                    "Pre-processing, Processing & Underwriting",
                    "Title Search & Closing Support",
                    "Post-closing Audit",
                    "Property & Lien Search",
                    "Loan Boarding",
                    "Appraisal Review",
                ],
            },
        }


def load_services_detail():
    """Load detailed services data from JSON file"""
    try:
        with open("app/data/services_detail.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def load_blogs():
    """Load blogs data from JSON file"""
    try:
        with open("app/data/blogs.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def load_leadership():
    """Load leadership team data from JSON file"""
    try:
        with open("app/data/leadership.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"team_members": [], "company_values": []}


def load_case_studies():
    """Load case studies data from JSON file"""
    try:
        with open("app/data/case_studies.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


# Routes
@app.route("/")
def home():
    """Home page with company overview and highlights"""
    return render_template(
        "home.html",
        title="Ardur Technology LLC - Business Process Management & IT Solutions",
        meta_description="Technology-driven business process solutions helping organizations reduce cost, increase efficiency, and achieve transformation through innovation.",
    )


@app.route("/about")
def about():
    """About us page with company information"""
    return render_template(
        "about.html",
        title="About Us - Ardur Technology LLC",
        meta_description="Learn about Ardur Technology LLC, founded in 2013 by Satish Sable, providing business process management and IT solutions.",
    )


@app.route("/services")
def services():
    """Services overview page"""
    services_data = load_services_data()
    return render_template(
        "services.html",
        services_data=services_data,
        title="Our Services - Ardur Technology LLC",
        meta_description="Comprehensive business process management, mortgage services, finance & accounting, healthcare, and digital transformation solutions.",
    )


@app.route("/services/<service_category>")
def service_detail(service_category):
    """Individual service category page"""
    services_data = load_services_data()

    if service_category not in services_data:
        return render_template("404.html"), 404

    service = services_data[service_category]
    return render_template(
        "service_detail.html",
        service=service,
        service_key=service_category,
        title=f"{service['title']} - Ardur Technology LLC",
        meta_description=f"Professional {service['title'].lower()} services by Ardur Technology LLC.",
    )


@app.route("/service/<service_slug>")
def service_page(service_slug):
    """Individual service detail page with dynamic content"""
    services_detail = load_services_detail()
    
    if service_slug not in services_detail:
        return render_template("404.html"), 404
    
    service = services_detail[service_slug]
    return render_template(
        "service_page.html",
        service=service,
        title=f"{service['title']} - Ardur Technology LLC",
        meta_description=f"{service.get('subtitle', '')} - Professional services by Ardur Technology LLC.",
    )


@app.route("/industries")
def industries():
    """Industries we serve"""
    return render_template(
        "industries.html",
        title="Industries We Serve - Ardur Technology LLC",
        meta_description="Serving mortgage, healthcare, finance, real estate, and aviation industries with specialized business process solutions.",
    )


@app.route("/blogs")
def blogs():
    """Blog listing page"""
    blogs_data = load_blogs()
    return render_template(
        "blogs.html",
        blogs=blogs_data,
        title="Blog - Industry Insights & Updates | Ardur Technology LLC",
        meta_description="Expert insights on mortgage services, aircraft asset management, and industry best practices from Ardur Technology LLC.",
    )


@app.route("/blog/<blog_slug>")
def blog_detail(blog_slug):
    """Individual blog post detail page"""
    blogs_data = load_blogs()
    
    if blog_slug not in blogs_data:
        return render_template("404.html"), 404
    
    blog = blogs_data[blog_slug]
    
    # Get 3 related blogs (excluding current one)
    related_blogs = {k: v for k, v in list(blogs_data.items()) if k != blog_slug}
    related_blogs = dict(list(related_blogs.items())[:3])
    
    return render_template(
        "blog_detail.html",
        blog=blog,
        related_blogs=related_blogs,
        title=f"{blog['title']} - Ardur Technology LLC",
        meta_description=blog.get('excerpt', '')[:160],
    )


@app.route("/careers")
def careers():
    """Careers page with job listings"""
    return render_template(
        "careers.html",
        title="Careers - Join Ardur Technology LLC",
        meta_description="Join our team at Ardur Technology LLC. Explore career opportunities in business process management and technology solutions.",
    )


@app.route("/leadership")
def leadership():
    """Leadership team page"""
    leadership_data = load_leadership()
    return render_template(
        "leadership.html",
        team_members=leadership_data.get("team_members", []),
        company_values=leadership_data.get("company_values", []),
        title="Leadership Team - Ardur Technology LLC",
        meta_description="Meet the leadership team at Ardur Technology LLC. Experienced professionals driving innovation in business process management.",
    )


@app.route("/case-studies")
def case_studies():
    """Case studies listing page"""
    case_studies_data = load_case_studies()
    return render_template(
        "case_studies.html",
        case_studies=case_studies_data,
        title="Case Studies - Success Stories | Ardur Technology LLC",
        meta_description="Explore real-world success stories and case studies showcasing our expertise in predictive analytics and aircraft maintenance.",
    )


@app.route("/case-study/<study_slug>")
def case_study_detail(study_slug):
    """Individual case study detail page"""
    case_studies_data = load_case_studies()
    
    if study_slug not in case_studies_data:
        return render_template("404.html"), 404
    
    case_study = case_studies_data[study_slug]
    
    return render_template(
        "case_study_detail.html",
        case_study=case_study,
        case_studies=case_studies_data,
        title=f"{case_study['title']} - Case Study | Ardur Technology LLC",
        meta_description=case_study.get('subtitle', '')[:160],
    )


@app.route("/careers/apply", methods=["POST"])
def apply_job():
    """Handle job applications"""
    if request.method == "POST":
        # Validate form data
        required_fields = ["name", "email", "phone", "position"]
        for field in required_fields:
            if not request.form.get(field):
                flash(f"{field.capitalize()} is required", "error")
                return redirect(url_for("careers"))

        # Validate email
        email = request.form.get("email")
        if not validate_email(email):
            flash("Please enter a valid email address", "error")
            return redirect(url_for("careers"))

        # Handle file upload
        resume_filename = None
        if "resume" in request.files:
            file = request.files["resume"]
            if file and file.filename and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_")
                resume_filename = timestamp + filename
                file.save(os.path.join(app.config["UPLOAD_FOLDER"], resume_filename))

        # Send email notification
        try:
            msg = Message(
                subject=f"New Job Application - {request.form.get('position')}",
                recipients=["info@ardurtechnology.com"],
                body=f"""
                New job application received:

                Name: {request.form.get("name")}
                Email: {request.form.get("email")}
                Phone: {request.form.get("phone")}
                Position: {request.form.get("position")}
                Experience: {request.form.get("experience", "Not specified")}
                Cover Letter: {request.form.get("cover_letter", "No cover letter provided")}
                Resume: {resume_filename if resume_filename else "No resume uploaded"}

                Submitted on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                """,
            )
            mail.send(msg)
            flash("Your application has been submitted successfully!", "success")
        except Exception as e:
            flash(
                "There was an error submitting your application. Please try again.",
                "error",
            )

        return redirect(url_for("careers"))


@app.route("/contact")
def contact():
    """Contact us page"""
    return render_template(
        "contact.html",
        title="Contact Us - Ardur Technology LLC",
        meta_description="Get in touch with Ardur Technology LLC. Located in Las Vegas, Nevada. Call +1 (702) 809 2713 or email info@ardurtechnology.com",
    )


@app.route("/contact", methods=["POST"])
def contact_form():
    """Handle contact form submissions"""
    if request.method == "POST":
        # Validate form data
        required_fields = ["name", "email", "subject", "message"]
        for field in required_fields:
            if not request.form.get(field):
                flash(f"{field.capitalize()} is required", "error")
                return redirect(url_for("contact"))

        # Validate email
        email = request.form.get("email")
        if not validate_email(email):
            flash("Please enter a valid email address", "error")
            return redirect(url_for("contact"))

        # Send email
        try:
            msg = Message(
                subject=f"Contact Form: {request.form.get('subject')}",
                recipients=["info@ardurtechnology.com"],
                reply_to=email,
                body=f"""
                New contact form submission:

                Name: {request.form.get("name")}
                Email: {request.form.get("email")}
                Company: {request.form.get("company", "Not specified")}
                Phone: {request.form.get("phone", "Not specified")}
                Subject: {request.form.get("subject")}

                Message:
                {request.form.get("message")}

                Submitted on: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
                """,
            )
            mail.send(msg)
            flash(
                "Your message has been sent successfully! We will get back to you soon.",
                "success",
            )
        except Exception as e:
            flash(
                "There was an error sending your message. Please try again or contact us directly.",
                "error",
            )

        return redirect(url_for("contact"))

@app.route("/privacy-policy")
def privacy_policy():
    return render_template("privacy_policy.html")

# API Routes
@app.route("/api/services")
def api_services():
    """API endpoint for services data"""
    return jsonify(load_services_data())


# Error handlers
@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template("500.html"), 500


@app.errorhandler(413)
def too_large(error):
    flash("File too large. Please upload a file smaller than 16MB.", "error")
    return redirect(request.url)


# Template context processors
@app.template_filter('format_date')
def format_date(date_string):
    """Format date string to readable format"""
    try:
        date_obj = datetime.strptime(date_string, '%Y-%m-%d')
        return date_obj.strftime('%B %d, %Y')
    except:
        return date_string


@app.context_processor
def inject_globals():
    """Inject global variables into all templates"""
    return {
        "company_name": "Ardur Technology LLC",
        "company_email": "info@ardurtechnology.com",
        "company_phone": "+1 (702) 809 2713",
        "company_address": "Las Vegas, Nevada, USA",
        "current_year": datetime.now().year,
        "founder": "Satish Sable",
    }


# Handle Chrome DevTools and other common requests to prevent 404 errors
@app.route('/.well-known/appspecific/com.chrome.devtools.json')
@app.route('/.well-known/<path:filename>')
def handle_well_known(filename=None):
    """Handle .well-known requests to prevent 404 errors"""
    abort(204)  # No Content - prevents error logs

@app.route('/robots.txt')
def robots_txt():
    """Serve robots.txt"""
    return "User-agent: *\nAllow: /", 200, {'Content-Type': 'text/plain'}

@app.route('/sitemap.xml')
def sitemap_xml():
    """Basic sitemap"""
    return '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url><loc>https://ardurtechnology.com/</loc></url>
    <url><loc>https://ardurtechnology.com/services</loc></url>
    <url><loc>https://ardurtechnology.com/about</loc></url>
    <url><loc>https://ardurtechnology.com/contact</loc></url>
</urlset>''', 200, {'Content-Type': 'application/xml'}

# Upload folder is created above using tempfile.gettempdir() for Vercel compatibility

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
