# Test interarrival times
interarrival_times = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9, 0]

# Test service times
service_times = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6, 0]

# Define variables
i_idx = 0  # Arrival index
s_idx = 0  # Service index
server_status = 0  # 0 if idle, 1 if busy
arrival_times_queue = []  # Buffer of events in order of the time in which they arrived
num_of_customers_in_queue = 0  # Number of customers in queue
time_of_last_event = float("inf")  # Initially inf as no event has occurred
system_clock = 0  # Tracks the system time

# TODO: Implement Poisson distribution for interarrival times instead of predefined ones
next_arrival = interarrival_times[i_idx]
next_departure = float("inf")  # Initially no customers in the system

# Statistical counters
area_under_qt = 0  # Waiting time
area_under_bt = 0  # Server utilization

"""
This function determines if the next event is an arrival or a departure.
"""
def timing():
    return 1 if next_arrival <= next_departure else 0


"""
Arrival event handling.
"""
def arrive():
    global system_clock, server_status, next_departure, s_idx, next_arrival, i_idx
    global num_of_customers_in_queue, time_of_last_event, area_under_bt, area_under_qt

    
    time_of_last_event = system_clock # Update time of previous event
    system_clock = next_arrival # Move to next event time (arrival)

    # Update area under Qt (queue time)
    if num_of_customers_in_queue > 0:
        area_under_qt += (system_clock - time_of_last_event) * num_of_customers_in_queue

    # If server is idle, start servicing
    if server_status == 0:
        server_status = 1  # Set server to busy
        next_departure = system_clock + service_times[s_idx]  # Next departure time
        s_idx += 1
    else:
        # If server is busy, queue the arrival
        arrival_times_queue.append(next_arrival)
        num_of_customers_in_queue += 1
        area_under_bt += (system_clock - time_of_last_event)  # Update server utilization

    # Schedule the next arrival
    i_idx += 1
    next_arrival += interarrival_times[i_idx]

"""
Departure event handling.
"""
def depart():
    global system_clock, server_status, next_departure, s_idx, next_arrival, i_idx
    global num_of_customers_in_queue, time_of_last_event, area_under_bt, area_under_qt

    time_of_last_event = system_clock  # Update time of previous event
    system_clock = next_departure # Move to next event time (departure)

    # Update area under Qt (queue time)
    if num_of_customers_in_queue > 0:
        area_under_qt += (system_clock - time_of_last_event) * num_of_customers_in_queue

    # If customers are in the queue, start servicing the next one
    if num_of_customers_in_queue > 0:
        next_departure = system_clock + service_times[s_idx]
        num_of_customers_in_queue -= 1
        arrival_times_queue.pop(0)  # Remove the first customer from the queue
        s_idx += 1
    else:
        # If no customers in queue, server becomes idle
        server_status = 0
        next_departure = float("inf")

    # Update server utilization
    area_under_bt += (system_clock - time_of_last_event)

"""
Main logic for M/M/1 queue simulation.
"""
def main():
    iterations = 14  # Run the simulation for a fixed number of iterations

    while iterations > 0:
        print(server_status, num_of_customers_in_queue, arrival_times_queue,
              time_of_last_event, system_clock, next_arrival, next_departure,
              area_under_qt, area_under_bt)

        # Determine if the next event is an arrival or departure
        next_event = timing()

        if next_event:  # Arrival event
            arrive()
        else:  # Departure event
            depart()

        iterations -= 1

# Run the simulation
if __name__ == "__main__":
    main()
