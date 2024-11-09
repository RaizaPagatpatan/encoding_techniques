# Data Communications and Networking - Encoding Techniques Visualizer

### Course Information
- **Course Number**: CS323
- **Course Title**: Data Communications and Networking

###Try the App 
https://encoding-techniques-sczye.streamlit.app/ 

### Project Objective
This application is designed to help students and professionals visualize the output of digital signals based on digital data inputs, using a range of encoding techniques. The goal is to deepen understanding of signal transmission and the different encoding methods commonly used in digital communications.

### Topics Covered
- **Signals**: Understanding and differentiating between various types of digital signals.
- **Signal Transmission**: Basics of how signals transmit data across different mediums.
- **Encoding Techniques**: Visual representation of data based on different encoding standards.

### Materials Needed
1. Individual workstation (PC or laptop).
2. Programming software (Python) or animation software to create visualizations.

### Instructions for Use
1. **Clone or Download the Repository**: 
   ```bash
   git clone <repository_url>

2. Install Required Packages
   ```bash
   pip install -r requirements.txt

3. Run the Application
   ```bash
   streamlit run main.py


### Encoding Techniques
| Encoding Type           | Description                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------|
| **NRZ-L**               | A constant positive or negative voltage represents a 1 or 0.                                |
| **NRZ-I**               | Voltage change occurs to signify a 1; no change signifies a 0.                              |
| **Bipolar AMI**         | Uses three voltage levels (positive, zero, negative) to represent binary data uniquely.     |
| **Pseudoternary**       | Similar to Bipolar AMI, but alternating voltage states represent binary 0 instead of 1.     |
| **Manchester**          | Bit is represented by a transition in the middle of the bit period.                         |
| **Differential Manchester** | Encoding based on transitions at the beginning of each bit period.                      |


