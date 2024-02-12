#!/bin/bash

# API URLs array
api_urls=(
    "http://127.0.0.1:8081/health_check"
    "http://127.0.0.1:8081/download_external_logs"
)

# Log path
log_file="/var/log/health_check.log"

for api_url in "${api_urls[@]}"; do
    status=""
    http_response=""
    timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    # Make the HTTP request
    http_response=$(curl -s -o /dev/null -w "%{http_code}" "$api_url")

    # Check the HTTP response code
    if [ "$http_response" == "200" ]; then
        status="reachable - Health check passed"
    else
        status="unreachable - Health check failed (HTTP $http_response)"
    fi

    # Write the result to the log file
    echo "$timestamp: API at $api_url is $status" >> "$log_file"
done
