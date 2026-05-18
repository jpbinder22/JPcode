#!/usr/bin/env python3
"""Ghostbusters Lab | Step 1"""

ghost_count = 0

def report_ghost_sighting(ghost_name, location="New York City"):
    """Prints a message about a ghost sighting."""
    global ghost_count
    ghost_count = ghost_count + 1
    print(f"{ghost_name} has beens ighted at {location}! Who you gonna call?")
    print(ghost_count, "ghosts have been spotted!")

# WHO YOU GONNA CALL?... no one, apparently!

# Function calls
report_ghost_sighting("Slimer", "Hotel Sedgewick")
report_ghost_sighting("Stay Puft")


