# location of the file with the server names and disk usage numbers
file_path = "data/server_usage.txt"

# print the title of the report
print("SERVER DISK USAGE REPORT")
print("========================")

# opens the server usage file so python can read it
with open(file_path, "r") as file:

    # goes through the file one line at a time
    for line in file:
        
        # remove extra spaces or blank lines from the line
        line = line.strip()

        # split the line into two parts using the comma
        parts = line.split(",")

        # first part is the server name
        server_name = parts[0]

        # second part is the disk usage number
        usage = parts[1]

        # change usage from text into a number
        usage = int(usage)

        # if usage is 90 or higher, it is critical
        if usage >= 90:
            print("CRITICAL:", server_name, "is at", usage, "% disk usage")
        
        # if usage is 80 or higher, it is a warning
        elif usage >= 80:
            print("WARNING:", server_name, "is at", usage, "% disk usage")
        # anything below 80 is okay
        else:
            print("OK:", server_name, "is at", usage, "% disk usage")

# print a message when the check is done
print("========================")
print("Disk usage check finished.")
