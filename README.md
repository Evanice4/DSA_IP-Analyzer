# IP Analyzer

## Overview

The IP Analyzer is a Python script that processes web server log files to count requests per IP address and identify the top N IPs.

## Features

- Counts requests from log files.
- Outputs the top N IP addresses.
- Handles input validation and errors.

## Usage

1. **Run the Script**:
   ```bash
   python ip_analyzer.py
2. Modify Parameters: Change the parameters in the process_log_file function to specify your log file, the number of top IPs, and the output file name.
Example
To analyze sample.log and get the top 3 IPs:
process_log_file('sample.log', 3, 'top_ips.txt')
Output
The output file will list the top N IPs and their request counts.

License
MIT License. See the LICENSE file for details.

Author
Nice Eva Karabaranga