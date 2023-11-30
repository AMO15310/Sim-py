import random
import pandas as pd

# Constants
num_students = 10000
server_speed = 1.0  # Adjust as needed

# Initialize variables
arrival_times = [random.uniform(0, 10) for _ in range(num_students)]  # Random arrival times
service_times = [random.uniform(0.5, 2.0) for _ in range(num_students)]  # Random service times
departure_times = [0] * num_students
queuing_times = [0] * num_students
time_spent_in_system = [0] * num_students
server_idle_time = 0.0

# Simulate the queuing system
for i in range(num_students):
    if arrival_times[i] > server_idle_time:
        server_idle_time = arrival_times[i]
    queuing_times[i] = server_idle_time - arrival_times[i]
    departure_times[i] = server_idle_time + service_times[i]
    time_spent_in_system[i] = departure_times[i] - arrival_times[i]
    server_idle_time = departure_times[i]

# Create a DataFrame to store the results
data = {
    'Arrival Time': arrival_times,
    'Service Time': service_times,
    'Departure Time': departure_times,
    'Queuing Time': queuing_times,
    'Time Spent in System': time_spent_in_system
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('queuing_system_simulation.xlsx', sheet_name='Simulation Results', index=False)

