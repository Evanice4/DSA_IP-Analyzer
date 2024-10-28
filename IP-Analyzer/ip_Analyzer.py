import heapq
from collections import defaultdict

def process_log_file(log_file_path, n, output_file_path):
    ip_counts = defaultdict(int)

    # Reads the log file line by line to count requests from each IP
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            # Removes whitespace and skips  empty lines

            line = line.strip()
            if not line:
                continue  # Skip empty lines

            # Split the line and handle potential unpacking issues
            parts = line.split(',')
            if len(parts) != 2:
                print(f"Warning: Line skipped due to unexpected format: {line}")
                continue  # Skip lines that don't have exactly 2 parts

            ip_address, count = parts
            try:
                ip_counts[ip_address] += int(count)
            except ValueError:
                print(f"Warning: Invalid count value for IP {ip_address}: {count}")
                continue  # Skip lines with invalid count values

    # Initialize an empty max heap
    max_heap = []
    
    for ip, count in ip_counts.items():
        # Push negative count to create a max heap
        heapq.heappush(max_heap, (-count, ip))

    # Extract top n IP addresses from the max heap
    top_n = []
    for _ in range(n):
        if max_heap:
            count, ip = heapq.heappop(max_heap)
            top_n.append((-count, ip))

    # Sort by count (descending), then by  IP (ascending)

    top_n.sort(key=lambda x: (-x[0], x[1]))

    # Write results to output file
    with open(output_file_path, 'w') as output_file:
        for importance, ip in top_n:
            output_file.write(f"{importance}, {ip}, {importance}\n")

# Example usage
if __name__ == "__main__":
    process_log_file('sample_01_easy.log', 3, 'sample_01_easy_result_n3.txt')
    process_log_file('sample_01_easy.log', 4, 'sample_01_easy_result_n4.txt')
    process_log_file('sample_01_easy.log', 6, 'sample_01_easy_result_n6.txt')