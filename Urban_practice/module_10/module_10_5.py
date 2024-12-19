import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.strip():
                break
            all_data.append(line)

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time_linear = time.time()
for filename in filenames:
    read_info(filename)
end_time_linear = time.time()
print(f'{end_time_linear - start_time_linear} (линейный)')

if __name__ == "__main__":
    start_time_multiprocessing = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    end_time_multiprocessing = time.time()
    print(f'{end_time_multiprocessing - start_time_multiprocessing} (многопроцессный)')