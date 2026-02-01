import numpy as np
import matplotlib.pyplot as plt

# Function to create a square wave pattern
def square_wave(pattern, repeat=10):
    """Generates a repeated digital waveform from a bit pattern"""
    return np.repeat(pattern, repeat)

# --- Define time ---
repeat = 20
time = np.arange(0, repeat * 8, 1)

# --- Input signals for 8 states (000 to 111) ---
A_pattern = [0,0,0,0,1,1,1,1]
B_pattern = [0,0,1,1,0,0,1,1]
Bin_pattern = [0,1,0,1,0,1,0,1]  # Only for Full Subtractor

A = square_wave(A_pattern, repeat)
B = square_wave(B_pattern, repeat)
Bin = square_wave(Bin_pattern, repeat)

# --- Half Subtractor Logic ---
D_half = np.logical_xor(A, B).astype(int)
B_out_half = np.logical_and(np.logical_not(A), B).astype(int)

# --- Full Subtractor Logic ---
D_full = np.logical_xor(np.logical_xor(A, B), Bin).astype(int)
B_out_full = np.logical_or(np.logical_and(np.logical_not(A), np.logical_or(B, Bin)),
                           np.logical_and(B, Bin)).astype(int)

# --- Plot Waveforms ---
plt.figure(figsize=(12,8))
plt.suptitle("Digital Waveform Simulation - Half and Full Subtractor", fontsize=14, fontweight='bold')

# HALF SUBTRACTOR
plt.subplot(2,1,1)
plt.title("Half Subtractor Waveforms")
plt.plot(time, A + 4, label="A", drawstyle='steps-pre')
plt.plot(time, B + 2, label="B", drawstyle='steps-pre')
plt.plot(time, D_half, label="Difference (D)", drawstyle='steps-pre')
plt.plot(time, B_out_half - 2, label="Borrow (B_out)", drawstyle='steps-pre')
plt.yticks([6,4,2,0,-2], ['A','B','D','B_out',''])
plt.xlabel("Time →")
plt.grid(True)
plt.legend(loc="upper right")

# FULL SUBTRACTOR
plt.subplot(2,1,2)
plt.title("Full Subtractor Waveforms")
plt.plot(time, A + 6, label="A", drawstyle='steps-pre')
plt.plot(time, B + 4, label="B", drawstyle='steps-pre')
plt.plot(time, Bin + 2, label="Borrow In", drawstyle='steps-pre')
plt.plot(time, D_full, label="Difference (D)", drawstyle='steps-pre')
plt.plot(time, B_out_full - 2, label="Borrow Out", drawstyle='steps-pre')
plt.yticks([8,6,4,2,0,-2], ['A','B','B_in','D','B_out',''])
plt.xlabel("Time →")
plt.grid(True)
plt.legend(loc="upper right")

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
