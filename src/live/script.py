import re

def parse_training_output(text):
    # Define a regex pattern to capture the relevant information
    pattern = re.compile(
        r"Train Epoch: (\d+\(\d+%\))\s+"
        r"Local-Loss: ([\d.]+)\s+"
        r"Local-Accuracy: ([\d.]+)\s+"
        r"ID: \d+\(\d+/\d+\)\s+"
        r"Learning rate: ([\d.]+)\s+"
        r"Rate: [\d.]+\s+"
        r"Epoch Finished Time: [^ ]+\s+"
        r"Experiment Finished Time: [^ ]+(?:\s+"
        r"Global-Loss: ([\d.]+)\s+"
        r"Global-Accuracy: ([\d.]+))?"
    )

    # Find all matches in the text
    matches = pattern.findall(text)

    # Process matches to get the desired output
    results = []
    for match in matches:
        epoch, local_loss, local_accuracy, learning_rate, global_loss, global_accuracy = match
        result = {
            "Epoch": epoch,
            "Local Loss": local_loss,
            "Local Accuracy": local_accuracy,
            "Learning Rate": learning_rate,
            "Global Loss": global_loss or "N/A",  # Default to "N/A" if not present
            "Global Accuracy": global_accuracy or "N/A"
        }
        results.append(result)

    return results

# Read the output from a file
file_path = 'output.txt'  # Replace with your file path
with open(file_path, 'r') as file:
    output_text = file.read()

# Parse the output
parsed_data = parse_training_output(output_text)
for data in parsed_data:
    print(data)
