# app/health.py
from flask import jsonify

def register_health_route(app):
    @app.route('/api/health')
    def health():
        return jsonify({'status': 'ok'}), 200