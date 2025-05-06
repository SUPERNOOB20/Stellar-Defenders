# This module initializes some settings in
# settings.py with nexus.txt values.

# For non-technical users: Let's just
# say it loads your progress and sends it
# to the world map when it opens up :)

def initialize_region_progress():

    settings_file = open("settings.py", "w")
    nexus_file = open("nexus.txt", "r")

    return