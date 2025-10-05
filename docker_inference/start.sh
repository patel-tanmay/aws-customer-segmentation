#!/bin/bash
set -e

echo "Starting Flask inference server..."
exec gunicorn --bind 0.0.0.0:8080 inference:app
