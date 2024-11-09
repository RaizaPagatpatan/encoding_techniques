import matplotlib.pyplot as plt
import numpy as np

def plot_signal(data, title):
    """Generates a step plot for a digital signal."""

    where_var = "post"
    print(title)
    if title == "NRZ-L Encoding":
        where_var = "post"
    elif title == "NRZ-I Encoding":
        where_var = "post"
    elif title == "Bipolar AMI Encoding":
        where_var = "mid"
    elif title == "Pseudoternary Encoding":
        where_var = "mid"
    elif title == "Manchester Encoding":
        where_var = "mid"
    elif title == "Differential Manchester Encoding":
        where_var = "mid"
    

    fig, ax = plt.subplots(figsize=(10, 2))
    
    # Ensure the data is in the correct format for plotting (0 and 1)
    if all(d in [0, 1] for d in data):
        ax.step(range(len(data)), data, where=where_var, linewidth=2)
    else:
        # data for bipolar representation
        adjusted_data = np.where(np.array(data) == -1, 0, data)  # Replace -1 with 0 for the plot
        ax.step(range(len(adjusted_data)), adjusted_data, where="mid", linewidth=2)
    
    ax.set_title(title)
    ax.set_ylim(-0.5, 1.5)  # Adjust y-axis limits to reflect only valid signal levels
    ax.set_yticks([0, 1])  # Show only the levels 0 and 1
    ax.grid(True)

    # Set x-axis labels
    ax.set_xticks(range(len(data)))
    ax.set_xticklabels(list(data))  # Use the binary input as x-tick labels

    return fig