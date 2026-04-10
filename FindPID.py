import psutil

# Specify the process name
process_name = "Brawlhalla.exe"  # Replace with your actual process name

# Loop through all running processes
for proc in psutil.process_iter(['pid', 'name']):
    try:
        if proc.info['name'] == process_name:
            print(f"Process '{process_name}' found with PID: {proc.info['pid']}")
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
