import psutil

def get_system_resources():
    total_memory =  psutil.virtual_memory().total / (1024 ** 3)
    cpu_count = psutil.cpu_count(logical=False)
    if not cpu_count:
        cpu_count = psutil.cpu_count(logical=True) 

    dask_memory = int(total_memory * 1)
    worker_count =  max(1, cpu_count)
    memory_per_worker = int(dask_memory / worker_count)

    return {
        'worker_count': worker_count,
        'memory_per_worker': memory_per_worker,
        'total_memory': total_memory
    }

def estimated_file_size(file):
    return file.size / (1024 ** 3)


def format_time(seconds):
    if seconds is None:
        return "Not Complete"
    
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    
    elif seconds < 3600:
        minutes = seconds // 60
        remaining_seconds = seconds % 60
        return f"{int(minutes)} minutes, {remaining_seconds:.2f} seconds"
    
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        remaining_seconds = seconds % 60
        return f"{int(hours)} hours, {int(minutes)} minutes, {remaining_seconds:.2f} seconds"
    
def get_uploaded_files_length(files) -> int:
    #TODO - complete this
    pass