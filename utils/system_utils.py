import psutil

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
    
    