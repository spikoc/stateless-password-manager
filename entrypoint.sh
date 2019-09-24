#!/bin/sh
# Run a local development server.

# .....................................ensure the virtual environment is enabled
flask --help > /dev/null 2>&1
[ $? -gt 0 ] && echo " * Activate virtual environment: venv" && . venv/bin/activate

python manage.py run -h 0.0.0.0
