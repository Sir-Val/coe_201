import matplotlib.pyplot as plt
import numpy as np

# --- 1. Module Definition ---
class Mux2to1:
    def evaluate(self, a, b, sel):
        """
        Combinational Logic:
        If Selector is 0, Output is A.
        If Selector is 1, Output is B.
        """
        if sel == 1:
            return b
        else:
            return a

# --- 2. Simulation Parameters ---
steps = 20
time = np.arange(steps)

# --- 3. Student Inputs: Manipulate these arrays ---
# Input A: A slow alternating pattern
input_a = np.array([0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0])

# Input B: A fast alternating pattern
input_b = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])

# Selector: Switches between A and B halfway through
sel_in  = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])

# Storage for results
output_y = []

# --- 4. Simulation Loop ---
mux = Mux2to1()

for t in range(steps):
    # Combinational logic evaluates immediately (no clock required)
    val = mux.evaluate(input_a[t], input_b[t], sel_in[t])
    output_y.append(val)

# --- 5. Visualization ---
fig, ax = plt.subplots(4, 1, sharex=True, figsize=(10, 8))

# Plot Input A
ax[0].step(time, input_a, where='post', color='blue', linewidth=2)
ax[0].set_ylabel('Input A')
ax[0].grid(True)

# Plot Input B
ax[1].step(time, input_b, where='post', color='green', linewidth=2)
ax[1].set_ylabel('Input B')
ax[1].grid(True)

# Plot Selector
ax[2].step(time, sel_in, where='post', color='orange', linewidth=2)
ax[2].set_ylabel('Select')
ax[2].grid(True)

# Plot Output
ax[3].step(time, output_y, where='post', color='red', linewidth=2)
ax[3].set_ylabel('Output Y')
ax[3].grid(True)
ax[3].fill_between(time, output_y, step="post", alpha=0.2, color='red') # Highlight output

plt.xlabel('Time (Simulation Steps)')
plt.suptitle('Combinational Circuit: 2-to-1 MUX')
plt.show()
