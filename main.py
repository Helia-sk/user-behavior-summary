import os
from src.pipeline import process_log_file

log_folder = "data/logs"
output_path = "output/results.txt"
os.makedirs("output", exist_ok=True)

# (Optional) Load manually written ground truths from a file
ground_truths = []
try:
    with open("data/ground_truths.txt", encoding="utf-8") as f:
        ground_truths = [line.strip() for line in f.readlines()]
except FileNotFoundError:
    pass

with open(output_path, "w", encoding="utf-8") as out_file:
    for i, file_name in enumerate(os.listdir(log_folder)):
        file_path = os.path.join(log_folder, file_name)
        with open(file_path, encoding="utf-8") as f:
            log_content = f.read()

        ground_truth = ground_truths[i] if i < len(ground_truths) else None
        result = process_log_file(file_name, log_content, ground_truth)

        out_file.write(f"In this session, {result['summary']}\n\n")
        out_file.write(f"Ground Truth:\n{result['ground_truth']}\n\n")
        out_file.write(f"Similarity Score: {result['similarity']:.2f}\n\n")
        out_file.write("-" * 60 + "\n\n")

print("✅ Formatted summaries saved to output/results.txt")
