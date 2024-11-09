import matplotlib.pyplot as plt
import numpy as np

def plot_signal(data, title):
    """Generates a step plot for a digital signal with middle section (-1, 0, 1) handling."""
    where_var = "post"
    
    if title in ["Manchester"]:
        where_var = "mid"

    fig, ax = plt.subplots(figsize=(10, 2))
    
    # Ensure the plot uses the full range including -1, 0, 1
    ax.step(range(len(data)), data, where=where_var, linewidth=2)
    
    
    # Adjust y-limits and ticks based on signal levels (-1, 0, 1)
    # Set y-ticks for Bipolar AMI and Pseudoternary
    if title == "Bipolar AMI Encoding" or title == "Pseudoternary Encoding":
        ax.set_yticks([-1, 0, 1])
        ax.set_ylim(-1.5, 1.5)  
    else:
        ax.set_yticks([0, 1])
        ax.set_ylim(-0.5, 1.5)  
    ax.grid(True)
    
    # Set x-labels corresponding to the binary input
    ax.set_xticks(range(len(data)))
    #use below for checking the range of plotting output, like how many bits it is able to show
    # ax.set_xticklabels([str(i) for i in range(len(data))]) 
    ax.set_xticklabels(list(data)) 

    
    
    ax.set_title(title)
    ax.legend()
    
    return fig




# # initial code for plotting
# import matplotlib.pyplot as plt
# import numpy as np

# def plot_signal(data, title):
#     """Generates a step plot for a digital signal."""

#     fig, ax = plt.subplots(figsize=(10, 2))
    
#     where_var = "post"
#     print(title)

#     if title in ["Manchester"]:
#         where_var = "mid"

#     # if title == "NRZ-L Encoding":
#     #     where_var = "post"
#     # elif title == "NRZ-I Encoding":
#     #     where_var = "post"
#     # elif title == "Bipolar AMI Encoding":
#     #     where_var = "mid"
#     #     # ax.step(range(len(data)), data, where=where_var, linewidth=2, label=title)
#     # elif title == "Pseudoternary Encoding":
#     #     where_var = "mid"
#     #     # ax.step(range(len(data)), data, where=where_var, linewidth=2, label=title)
#     # elif title == "Manchester Encoding":
#     #     where_var = "mid"
#     # elif title == "Differential Manchester Encoding":
#     #     where_var = "mid"

    
#     # Ensure the data is in the correct format for plotting (0 and 1)
#     if all(d in [0, 1] for d in data):
#         ax.step(range(len(data)), data, where=where_var, linewidth=2)
#     else:
#         # data for bipolar representation
#         adjusted_data = np.where(np.array(data) == -1, 0, data)  # Replace -1 with 0 for the plot
#         ax.step(range(len(adjusted_data)), adjusted_data, where="mid", linewidth=2)
    
#     ax.set_title(title)
#     ax.legend()
#     ax.set_ylim(-0.5, 1.5) 
#     # Set y-ticks for Bipolar AMI and Pseudoternary
#     if title == "Bipolar AMI Encoding" or title == "Pseudoternary Encoding":
#         ax.set_yticks([-1, 0, 1])  
#     else:
#         ax.set_yticks([0, 1])  
#     ax.grid(True)

#     # Set x-axis labels
#     ax.set_xticks(range(len(data)))
#     ax.set_xticklabels(list(data))  # Use the binary input as x-tick labels

#     return fig

