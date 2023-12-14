import re
import matplotlib.pyplot as plt

def parse_training_output(text):
    pattern = re.compile(
        r"(Train|Test) Epoch: (\d+)\((\d+)%\)\s+"
        r"Local-Loss: ([\d.]+)\s+"
        r"Local-Accuracy: ([\d.]+)\s+.*?"
        r"(Global-Loss: ([\d.]+)\s+"
        r"Global-Accuracy: ([\d.]+))?"
    )

    results = []
    for match in pattern.findall(text):
        epoch_type, epoch, percent, local_loss, local_accuracy, _, global_loss, global_accuracy = match
        epoch_id = int(epoch) + int(percent) / 100  # Create a unique identifier for each entry
        result = {
            "Epoch": epoch_id,
            "Local Loss": local_loss,
            "Local Accuracy": local_accuracy,
            "Global Loss": global_loss if global_loss else None,
            "Global Accuracy": global_accuracy if global_accuracy else None
        }
        results.append(result)

    return results

def plot_data(parsed_data):
    epochs = [data["Epoch"] for data in parsed_data]
    local_accuracies = [float(data["Local Accuracy"]) for data in parsed_data]
    
    # Prepare data for global accuracies where available
    global_epochs = [data["Epoch"] for data in parsed_data if data["Global Accuracy"] is not None]
    global_accuracies = [float(data["Global Accuracy"]) for data in parsed_data if data["Global Accuracy"] is not None]

    # Plotting
    plt.figure(figsize=(12, 6))
    plt.plot(epochs, local_accuracies, label='Local Accuracy', marker='o')
    
    # Only plot global accuracies where they are available
    if global_accuracies:
        plt.plot(global_epochs, global_accuracies, label='Global Accuracy', linestyle='-', marker='x')

    plt.xlabel('Epochs')
    plt.ylabel('Accuracy (%)')
    plt.title('Local and Global Accuracy over Epochs')
    plt.legend()
    plt.grid(True)
    plt.show()

# Read the output from your file
file_path = 'output10epochs.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    output_text = file.read()

# Parse the output
parsed_data = parse_training_output(output_text)
print(parsed_data)
# Plot the graph
plot_data(parsed_data)
