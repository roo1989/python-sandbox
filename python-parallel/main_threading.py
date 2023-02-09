import time
import threading

def calculate_sum_squares(n):
    sum_of_square = 0

    for i in range(n):
        sum_of_square += i ** 2

    print(sum_of_square)        

def sleep_a_little(seconds):
   time.sleep(seconds)

def main_threading():
   calc_start_time = time.time()

   for i in range(5):
    maximum_value = (i + 1) * 1000000
    t = threading.Thread(target=calculate_sum_squares, args=(maximum_value, ))
    t.start()

    print(f"Calculating sum of squares took: { round(time.time() - calc_start_time, 1) }")
    
    sleep_start_time = time.time()

    for seconds in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(seconds, ))
        t.start()

    print(f"Sleep took: { round(time.time() - sleep_start_time, 1) }")


if __name__ == "__main__":
    main_threading()