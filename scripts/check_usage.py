file_path = "data/server_usage.txt"

print("SERVER DISK USAGE REPORT")
print("========================")

with open(file_path, "r") as file:
    for line in file:
        line = line.strip()

        parts = line.split(",")

        server_name = parts[0]
        usage = parts[1]

        usage = int(usage)

        if usage >= 90:
            print("CRITICAL:", server_name, "is at", usage, "% disk usage")
        elif usage >= 80:
            print("WARNING:", server_name, "is at", usage, "% disk usage")
        else:
            print("OK:", server_name, "is at", usage, "% disk usage")

print("========================")
print("Disk usage check finished.")
