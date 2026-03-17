# SoundKeeper

Prevents audio devices from entering sleep mode by periodically playing a short, sub-audible low-frequency tone. Useful for speakers or DACs that power down after a period of silence, causing delays or pops when audio resumes.

## How It Works

`SoundKeeper.py` opens a persistent audio stream and loops a 3-second 30 Hz sine wave followed by 20 seconds of silence. The tone is kept at low volume with fade-in/fade-out to avoid audible clicks. A PID file (`soundkeeper.pid`) is written on startup so the process can be stopped cleanly.

## Requirements

- Python 3
- [PortAudio](http://www.portaudio.com/) (required by `sounddevice`)

Install Python dependencies:

```
pip install -r requirements.txt
```

## Usage

Start:

```
python SoundKeeper.py
```

Stop:

```
python StopSoundKeeper.py
```

## Configuration

These values can be adjusted at the top of `SoundKeeper.py`:

- **`frequency`** — Tone frequency in Hz (default: `30.0`)
- **`volume`** — Tone amplitude, 0.0–1.0 (default: `0.1`)
- **`duration`** — Length of each tone burst in seconds (default: `3.0`)
- **`period`** — Silence gap between tones in milliseconds (default: `20000`)
