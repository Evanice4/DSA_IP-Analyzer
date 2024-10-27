import heapq
from collections import defaultdict

def process_log_file(log_file_path, n, output_file_path):
    ip_counts = defaultdict(int)

    # Read the log file and count requests per IP address
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            ip_address, count = line.strip().split(',')
            ip_counts[ip_address] += int(count)

    # Create a max heap for the top n IP addresses
    max_heap = []
    
    for ip, count in ip_counts.items():
        # Push negative count to create a max heap
        heapq.heappush(max_heap, (-count, ip))

    # Extract top n IP addresses
    top_n = []
    for _ in range(n):
        if max_heap:
            count, ip = heapq.heappop(max_heap)
            top_n.append((-count, ip))

    # Sort the results first by count (descending) then by IP (ascending)
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