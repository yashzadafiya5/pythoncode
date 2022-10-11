import psutil

no_of_cores = psutil.cpu_count(logical=False)
print(no_of_cores)
