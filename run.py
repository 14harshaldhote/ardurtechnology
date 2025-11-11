#!/usr/bin/env python3
"""
Ardur Technology LLC - Flask Application Runner

This script provides an easy way to start the Flask application with
proper configuration and error handling.

Usage:
    python run.py              # Run in development mode
    python run.py --prod       # Run in production mode
    python run.py --help       # Show help information
"""

import os
import sys
import argparse
from datetime import datetime

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from app import app
except ImportError as e:
    print(f"Error importing Flask application: {e}")
    print("Make sure you have installed all required dependencies:")
    print("pip install -r requirements.txt")
    sys.exit(1)


def setup_environment():
    """Set up environment variables and configuration"""

    # Load environment variables from .env file if it exists
    env_file = os.path.join(os.path.dirname(__file__), ".env")
    if os.path.exists(env_file):
        try:
            from dotenv import load_dotenv

            load_dotenv(env_file)
            print("✓ Loaded environment variables from .env file")
        except ImportError:
            print(
                "⚠ python-dotenv not installed. Environment variables from .env file will not be loaded."
            )

    # Ensure uploads directory exists
    uploads_dir = os.path.join(os.path.dirname(__file__), "uploads")
    if not os.path.exists(uploads_dir):
        os.makedirs(uploads_dir)
        print(f"✓ Created uploads directory: {uploads_dir}")


def print_startup_info(host, port, debug_mode):
    """Print startup information"""
    print("\n" + "=" * 60)
    print("🏢 ARDUR TECHNOLOGY LLC - FLASK APPLICATION")
    print("=" * 60)
    print(f"🌐 Server running at: http://{host}:{port}")
    print(f"🔧 Debug mode: {'ON' if debug_mode else 'OFF'}")
    print(f"📅 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🐍 Python version: {sys.version.split()[0]}")
    print("\n📋 Available endpoints:")
    print("   • /            - Homepage")
    print("   • /about       - About Us")
    print("   • /services    - Our Services")
    print("   • /industries  - Industries We Serve")
    print("   • /careers     - Career Opportunities")
    print("   • /contact     - Contact Information")
    print("\n💡 Tips:")
    print("   • Press Ctrl+C to stop the server")
    if debug_mode:
        print("   • Debug mode is ON - changes will auto-reload")
    print("   • Check the console for request logs")
    print("=" * 60 + "\n")


def main():
    """Main function to run the Flask application"""

    parser = argparse.ArgumentParser(
        description="Run Ardur Technology Flask Application"
    )
    parser.add_argument(
        "--host", default="127.0.0.1", help="Host to bind to (default: 127.0.0.1)"
    )
    parser.add_argument(
        "--port", type=int, default=5000, help="Port to bind to (default: 5000)"
    )
    parser.add_argument("--prod", action="store_true", help="Run in production mode")
    parser.add_argument(
        "--debug", action="store_true", help="Force debug mode (overrides --prod)"
    )

    args = parser.parse_args()

    # Setup environment
    setup_environment()

    # Determine debug mode
    if args.debug:
        debug_mode = True
    elif args.prod:
        debug_mode = False
    else:
        # Default to debug mode for development
        debug_mode = os.environ.get("FLASK_ENV") != "production"

    # Update app configuration
    if args.prod and not args.debug:
        app.config["DEBUG"] = False
        app.config["TESTING"] = False
        # In production, you might want to set additional configs
        if (
            not app.config.get("SECRET_KEY")
            or app.config["SECRET_KEY"] == "your-secret-key-change-in-production"
        ):
            print(
                "⚠ WARNING: Using default secret key! Set a secure SECRET_KEY in production."
            )
    else:
        app.config["DEBUG"] = True

    # Print startup information
    print_startup_info(args.host, args.port, debug_mode)

    # Check for common issues
    required_dirs = ["app/templates", "app/static", "uploads"]
    for dir_path in required_dirs:
        full_path = os.path.join(os.path.dirname(__file__), dir_path)
        if not os.path.exists(full_path):
            print(f"⚠ WARNING: Required directory not found: {dir_path}")

    try:
        # Run the Flask application
        app.run(
            host=args.host,
            port=args.port,
            debug=debug_mode,
            threaded=True,
            use_reloader=debug_mode,
        )

    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user")

    except OSError as e:
        if "Address already in use" in str(e):
            print(f"\n❌ Error: Port {args.port} is already in use.")
            print(
                f"   Try using a different port: python run.py --port {args.port + 1}"
            )
        else:
            print(f"\n❌ OS Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        if debug_mode:
            raise
        sys.exit(1)


if __name__ == "__main__":
    main()
