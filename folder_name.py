#!/usr/bin/env python3

from datetime import datetime

def global_variable():
    current_datetime = datetime.now()
    formatted_timestamp = current_datetime.strftime("%Y-%m-%d_%H%M.%S")
    destination_folder = ("./RenamedImages_" + formatted_timestamp)
    return destination_folder