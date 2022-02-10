import time

def print_percentage_complete(iteration, total_iterations):
    print(f"{100 * iteration / total_iterations:.0f}%")

if __name__ == "__main__":
    total_iterations = 10
    for i in range(total_iterations):
        time.sleep(0.1)
        print_percentage_complete(i + 1, total_iterations)