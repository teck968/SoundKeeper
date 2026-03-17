import numpy as np
import sounddevice as sd
import os

# This script generates a sub-audible sine wave and plays it periodically to keep the line active.

# Write PID file so the process can be stopped externally
pid_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'soundkeeper.pid')
with open(pid_path, 'w') as f:
    f.write(str(os.getpid()))

fs = 44100 
period = 20 * 1000  # 20 seconds in milliseconds
duration = 3.0  
frequency = 30.0 
volume = 0.1 # Keep it very low

num_samples = int(fs * duration)
t = np.linspace(0, duration, num_samples, endpoint=False)
tone = volume * np.sin(2 * np.pi * frequency * t).astype(np.float32)

# Apply a short fade-in/fade-out to smooth transitions
fade_samples = int(fs * 0.05)  # 50ms fade
tone[:fade_samples] *= np.linspace(0, 1, fade_samples, dtype=np.float32)
tone[-fade_samples:] *= np.linspace(1, 0, fade_samples, dtype=np.float32)

# Build silence for the gap between tones
silence = np.zeros(int(fs * (period / 1000)), dtype=np.float32)

# Concatenate into one seamless loop: tone + silence
loop = np.concatenate([tone, silence])

# Play on a single persistent stream to avoid open/close clicks
with sd.OutputStream(samplerate=fs, channels=1, dtype='float32') as stream:
    while True:
        stream.write(loop.reshape(-1, 1))
