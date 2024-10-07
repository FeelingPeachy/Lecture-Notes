# test interarrival times
interarrival_times = [0.4, 1.2, 0.5, 1.7, 0.2, 1.6, 0.2, 1.4, 1.9, 0]

# test service times
service_times = [2.0, 0.7, 0.2, 1.1, 3.7, 0.6, 0]


# define variables
i_idx = 0 # arrival idx
s_idx = 0 # service idx

server_status = 0 # 0 if idle 1 if busy
arrival_times_queue = [] # buffer of events in order of the time in which they arrived
num_of_customers_in_queue = 0
time_of_last_event = float("inf") # so we can calc time of event, intially inf as no last event
system_clock = 0 # tracks the time of the sys



# TODO the posion dist thingy instead of predifined interavial times
next_arrival = interarrival_times[i_idx]
next_departure = float("inf") # initially no customers in the sys


# statistical counters
area_under_qt = 0 # waiting time
area_under_bt = 0 # server utilistation
total_delay = 0
number_of_packets = 0



"""
this function determines if the next event is an arrival or a departure
"""
def timing():
    if next_arrival <= next_departure:
        return 1
    else:
        return 0

def arrive():
    global system_clock, server_status, next_departure, s_idx, next_arrival, i_idx, num_of_customers_in_queue, time_of_last_event, area_under_bt, area_under_qt

    # update time of prev event 
    time_of_last_event = system_clock

    # first we move to next event time
    system_clock = next_arrival


    # update are under qt
    # essentially we are checking if elments are waiting in the queue
    # if there are, to calc what we are adding to the sum, we note that all elements in queue have been waiting since the same point in time (time of last event), therefore we use the largest val in queue as the point from which we calc the wait time
    if num_of_customers_in_queue > 0:
        area_under_qt += (system_clock - time_of_last_event) * num_of_customers_in_queue


    # check if the server is busy, if idle start servicing and update the time it will depart
    if server_status == 0:
        server_status = 1 # busy
        next_departure = system_clock + service_times[s_idx] # next time the server will be free
        s_idx += 1


    else: # if it is busy
        arrival_times_queue.append(next_arrival)
        num_of_customers_in_queue += 1

        # calc server utilisation
        # if time has elapsed whilst the server has been occupied we increment
        area_under_bt +=  (system_clock - time_of_last_event) # adding more time since last event recorded



    

    # update time for next arrival
    i_idx += 1
    next_arrival += interarrival_times[i_idx]


def depart():
    global system_clock, server_status, next_departure, s_idx, next_arrival, i_idx, num_of_customers_in_queue, time_of_last_event, area_under_bt, area_under_qt

    # update time of prev event 
    time_of_last_event = system_clock

    system_clock = next_departure

    if num_of_customers_in_queue > 0:
        area_under_qt += (system_clock - time_of_last_event) * num_of_customers_in_queue



    # if there is elements waiting start servinig, and update the next departure to when it will finish
    if num_of_customers_in_queue > 0:
        next_departure = system_clock + service_times[s_idx]
        num_of_customers_in_queue -= 1
        original_arrive_time = arrival_times_queue.pop(0)
        s_idx += 1

    else:
        server_status = 0
        next_departure = float("inf") # server not doing anything    


    area_under_bt +=  (system_clock - time_of_last_event)


# main logic for m/m/1 queue
def main():

    """
    init_routine() # Invoke the initialization routine
    timing_routine() #Invoke the timing routine
    event_routine() # invoke event routine
    """
    i = 14

    while i > 0:
        print(server_status, num_of_customers_in_queue, arrival_times_queue, time_of_last_event, system_clock, next_arrival, next_departure, area_under_qt, area_under_bt)
        next_event = timing()
        if next_event: # if arrival
            arrive()

        else:
            depart()

        i -= 1



if __name__ == "__main__":
    main()