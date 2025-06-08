from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def compare_summaries(summary_a, summary_b):
    emb1 = model.encode(summary_a, convert_to_tensor=True)
    emb2 = model.encode(summary_b, convert_to_tensor=True)
    score = util.pytorch_cos_sim(emb1, emb2)
    return float(score)
