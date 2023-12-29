#!/bin/bash
coverage run -m evennia test --settings settings.py
coverage html
open coverage_html_report/index.html
