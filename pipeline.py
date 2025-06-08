from src.summarizer import summarize_user_session
from src.comparator import compare_summaries

def process_log_file(file_name, raw_log_text, ground_truth=None):
    ai_summary = summarize_user_session(raw_log_text)

    if not ground_truth:
        ground_truth = "N/A"
        similarity = 0.0
    else:
        similarity = compare_summaries(ai_summary, ground_truth)

    return {
        "file_name": file_name,
        "summary": ai_summary,
        "ground_truth": ground_truth,
        "similarity": similarity
    }
