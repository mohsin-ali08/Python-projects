import time
import sys

def countdown_timer(total_seconds):
    print("\nCountdown Started! Get ready...\n")
    for remaining in range(total_seconds, -1, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        # Create a progress bar (20 blocks wide)
        progress = int(((total_seconds - remaining) / total_seconds) * 20) if total_seconds > 0 else 20
        bar = "[" + "#" * progress + "-" * (20 - progress) + "]"
        # Print the timer and progress bar on the same line
        sys.stdout.write(f"\r{timer} {bar}")
        sys.stdout.flush()
        time.sleep(1)
    print("\n\nTime's up!\n")

try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown_timer(total_seconds)
except ValueError:
    print("Please enter a valid number. Try again!")