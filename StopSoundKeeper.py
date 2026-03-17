import os
import signal
import sys

pid_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'soundkeeper.pid')

if not os.path.exists(pid_path):
    print("No PID file found. SoundKeeper may not be running.")
    sys.exit(1)

with open(pid_path, 'r') as f:
    pid = int(f.read().strip())

try:
    os.kill(pid, signal.SIGTERM)
    os.remove(pid_path)
    print(f"SoundKeeper (PID {pid}) stopped.")
except ProcessLookupError:
    os.remove(pid_path)
    print(f"Process {pid} not found. Removed stale PID file.")
except PermissionError:
    print(f"Permission denied when trying to stop PID {pid}.")
