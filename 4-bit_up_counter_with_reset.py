import matplotlib.pyplot as plt
import numpy as np

# --- 1. Module Definition ---
class Counter4Bit:
    def __init__(self):
        self.count = 0 # State variable (Memory)

    def trigger(self, clk, reset, prev_clk):
        """
        Sequential Logic:
        Updates only on the RISING EDGE of the clock (0 -> 1).
        If Reset is High, count becomes 0.
        """
        # Detect Rising Edge: Current is 1, Previous was 0
        rising_edge = (clk == 1) and (prev_clk == 0)

        if rising_edge:
            if reset == 1:
                self.count = 0
            else:
                # Increment and wrap around at 15 (4-bit limit)
                if self.count >= 15:
                    self.count = 0
                else:
                    self.count += 1
        
        return self.count

# --- 2. Simulation Parameters ---
steps = 30
time = np.arange(steps)

# Generate a Clock (Toggles every 1 step for higher frequency)
clk = np.array([1 if i % 2 == 0 else 0 for i in range(steps)])

# --- 3. Student Inputs: Manipulate the Reset Line ---
# Try setting reset to 1 in the middle of the count to see it clear
reset_in = np.zeros(steps)
reset_in[12:16] = 1  # Example: Reset is high from step 12 to 16

# Storage
output_count = []

# --- 4. Simulation Loop ---
counter = Counter4Bit()
prev_clk_val = 0 # To store the state of the clock in the previous loop

for t in range(steps):
    current_val = counter.trigger(clk[t], reset_in[t], prev_clk_val)
    output_count.append(current_val)
    
    # Store current clock to use as "previous" in next iteration
    prev_clk_val = clk[t]

# --- 5. Visualization ---
fig, ax = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

# Plot Clock
ax[0].step(time, clk, where='post', color='black', linewidth=1.5)
ax[0].set_ylabel('Clock')
ax[0].grid(True)

# Plot Reset
ax[1].step(time, reset_in, where='post', color='red', linewidth=2)
ax[1].set_ylabel('Reset')
ax[1].grid(True)

# Plot Counter Output (displayed as integer value)
ax[2].step(time, output_count, where='post', color='purple', linewidth=2)
ax[2].set_ylabel('Count (Dec)')
ax[2].set_yticks(range(0, 16, 2)) # Y-axis marks every 2 numbers
ax[2].grid(True)

plt.xlabel('Time (Simulation Steps)')
plt.suptitle('Sequential Circuit: 4-Bit Up-Counter')
plt.show()
