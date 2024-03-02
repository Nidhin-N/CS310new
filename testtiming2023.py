import time

def test_timing(state):
    # Start a timer
    start = time.time()
    # Call minimax function
    value = minimax_value(state)
    end = time.time()
    #calculate and return
    duration = end-start
    #print('Time taken:', duration)
    return duration, value

output = (test_timing(([5,2,2,3],1)))
print("Time taken", output[0])
print("Value returned", output[1])
