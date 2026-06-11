"""
Master Pipeline Script
Bluestock Mutual Fund Analytics
"""

import subprocess

print("Running Data Ingestion...")
subprocess.run(["python", "scripts/data_ingestion.py"])

print("Running Live NAV Fetch...")
subprocess.run(["python", "scripts/live_nav_fetch.py"])

print("Pipeline Completed Successfully!")