"""
CodeMentor-AI - Main Application Entry Point
An AI-powered platform for learning programming with real-time assistance
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL', 
    'sqlite:///codementor.db'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)


# Health check endpoint
@app.route('/health', methods=['GET'])
def health_check():
    """Check if the API is running"""
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'service': 'CodeMentor-AI'
    }), 200


# Main API endpoint
@app.route('/api/v1/welcome', methods=['GET'])
def welcome():
    """Welcome endpoint"""
    return jsonify({
        'message': 'Welcome to CodeMentor-AI',
        'description': 'Learn programming with AI-powered guidance',
        'endpoints': {
            'health': '/health',
            'challenges': '/api/v1/challenges',
            'tutors': '/api/v1/tutors',
            'progress': '/api/v1/progress'
        }
    }), 200


# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    
    # Run the application
    debug_mode = os.getenv('FLASK_ENV') == 'development'
    app.run(
        host='0.0.0.0',
        port=int(os.getenv('PORT', 5000)),
        debug=debug_mode
    )