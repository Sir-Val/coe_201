import itertools
import matplotlib.pyplot as plt
import networkx as nx

# --- Half Subtractor ---
def half_subtractor(A, B):
    D = A ^ B
    B_out = (not A) and B
    return int(D), int(B_out)

# --- Full Subtractor ---
def full_subtractor(A, B, B_in):
    D = A ^ B ^ B_in
    B_out = ((not A) and (B or B_in)) or (B and B_in)
    return int(D), int(B_out)

# --- Display Truth Tables ---
print("HALF SUBTRACTOR")
print("A B | D B_out")
for A, B in itertools.product([0,1],[0,1]):
    D, B_out = half_subtractor(A, B)
    print(f"{A} {B} | {D} {B_out}")

print("\nFULL SUBTRACTOR")
print("A B Bin | D Bout")
for A, B, B_in in itertools.product([0,1],[0,1],[0,1]):
    D, B_out = full_subtractor(A, B, B_in)
    print(f"{A} {B}  {B_in}  | {D}  {B_out}")

# --- Logic Diagram using networkx ---
def draw_logic_diagram(title, connections):
    G = nx.DiGraph()
    for src, dst in connections:
        G.add_edge(src, dst)

    plt.figure(figsize=(8,5))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=2500, font_size=10)
    plt.title(title)
    plt.show()

# Half Subtractor Diagram
half_connections = [
    ("A", "XOR Gate"), ("B", "XOR Gate"),
    ("A", "NOT Gate"), ("NOT Gate", "AND Gate"),
    ("B", "AND Gate"),
    ("XOR Gate", "Difference (D)"),
    ("AND Gate", "Borrow (B_out)")
]
draw_logic_diagram("Half Subtractor Logic Diagram", half_connections)

# Full Subtractor Diagram
full_connections = [
    ("A", "XOR1"), ("B", "XOR1"),
    ("XOR1", "XOR2"), ("B_in", "XOR2"),
    ("A", "NOT Gate"),
    ("NOT Gate", "AND1"), ("B", "AND1"),
    ("NOT Gate", "AND2"), ("B_in", "AND2"),
    ("B", "AND3"), ("B_in", "AND3"),
    ("AND1", "OR Gate"), ("AND2", "OR Gate"), ("AND3", "OR Gate"),
    ("XOR2", "Difference (D)"),
    ("OR Gate", "Borrow (B_out)")
]
draw_logic_diagram("Full Subtractor Logic Diagram", full_connections)
