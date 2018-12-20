#!/bin/bash

# Start Gunicorn w/ server
echo Starting Gunicorn...
exec gunicorn code_review.wsgi:application \
    --bind 0.0.0.0:8000 \
    --workers 9
