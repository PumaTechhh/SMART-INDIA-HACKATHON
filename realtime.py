import csv
import random
from datetime import datetime, timedelta
import time
import os

ip_to_int = lambda x: int(''.join([format(int(i), '08b') for i in x.split('.')]), 2)

# Function to generate random timestamp within a given range
def generate_random_timestamp(start_date, end_date):
    time_delta = end_date - start_date
    random_days = random.randint(0, time_delta.days)
    random_seconds = random.randint(0, 86400 - 1)  # 86400 seconds in a day
    return (start_date + timedelta(days=random_days, seconds=random_seconds)).timestamp()

# Function to generate a random IP address
def generate_random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Function to convert IP address to integer
def ip_to_int(ip):
    return int(''.join(format(int(x), '08b') for x in ip.split('.')), 2)

# Function to generate a random port number
def generate_random_port():
    return random.randint(1, 65535)

# Function to generate a random protocol (TCP, UDP, ICMP)
def generate_random_protocol():
    protocols = ["TCP", "UDP", "ICMP"]
    return random.choice(protocols)

# Function to generate a random packet size
def generate_random_packet_size():
    return random.randint(64, 1500)  # Adjust the range based on your requirements

# Function to generate a random traffic category
def generate_random_traffic_category():
    categories = ["Web", "Email", "File Transfer", "Video", "VoIP", "Other"]
    return random.choice(categories)

# Function to generate a random app service
def generate_random_app_service():
    services = ["HTTP", "SMTP", "FTP", "DNS", "SSH", "Other"]
    return random.choice(services)

# Function to generate a random duration in seconds
def generate_random_duration():
    return random.randint(1, 3600)  # Adjust the range based on your requirements

# Function to generate a random number of connection attempts
def generate_random_connection_attempts():
    return random.randint(1, 10)  # Adjust the range based on your requirements

# Set the start and end date for timestamp generation
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Specify the path to store the CSV file
csv_file_path = "D:\\SIH\\SIH INTRUSION DETECTION\\realtime.csv"

# Check if the file is empty
is_empty = not os.path.exists(csv_file_path) or os.stat(csv_file_path).st_size == 0

# Infinite loop for continuous logging
while True:
    # Generate and append data to the CSV file
    with open(csv_file_path, mode="a", newline="") as file:
        writer = csv.writer(file)

        # Write data rows
        for _ in range(100):
            timestamp = generate_random_timestamp(start_date, end_date)
            source_ip = generate_random_ip()
            dest_ip = generate_random_ip()
            source_port = generate_random_port()
            dest_port = generate_random_port()
            protocol = generate_random_protocol()
            packet_size = generate_random_packet_size()
            traffic_category = generate_random_traffic_category()
            app_service = generate_random_app_service()
            duration = generate_random_duration()
            connection_attempts = generate_random_connection_attempts()

            # Convert timestamp, source IP, and destination IP to float
            timestamp = float(timestamp)
            source_ip = ip_to_int(source_ip)
            dest_ip = ip_to_int(dest_ip)

            row = [
                timestamp, source_ip, dest_ip, source_port, dest_port, protocol,
                packet_size, traffic_category, app_service, duration, connection_attempts
            ]

            writer.writerow(row)

    print(f"Dataset updated. Waiting for the next update...")

    # Delay for 5 seconds before the next update
    time.sleep(5)