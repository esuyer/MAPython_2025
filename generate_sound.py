import wave
import struct
import math

sample_rate = 22050
duration = 1.0

samples = []
total_samples = int(sample_rate * duration)

ho_times = [0.0, 0.3, 0.6]

for i in range(total_samples):
    t = i / sample_rate
    sample = 0
    
    for ho_start in ho_times:
        if ho_start <= t < ho_start + 0.2:
            local_t = t - ho_start
            freq = 180 - local_t * 200
            envelope = math.sin(math.pi * local_t / 0.2)
            sample += math.sin(2 * math.pi * freq * local_t) * envelope * 0.7
    
    samples.append(int(max(-32767, min(32767, sample * 32767))))

with wave.open("hohoho.wav", "w") as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(sample_rate)
    f.writeframes(struct.pack(f'{len(samples)}h', *samples))

print("Done!")
