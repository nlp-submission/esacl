"""
Generate 100 examples for human evaluation
"""

import numpy as np
import pandas as pd

# generated summary
generated_summary = []
with open("./output/ri-rs/test_generations.txt", "r") as f:
    for line in f:
        generated_summary.append(line)

# clean up the spaces
generated_summary = [x.strip() for x in generated_summary]

# input articles
articles = []
with open('./data/xsum/test.source', "r") as f:
    for line in f:
        articles.append(line.strip())

# target summary
target_summary = []
with open('./data/xsum/test.target', "r") as f:
    for line in f:
        target_summary.append(line.strip())

# bart summary
bart_summary = []
with open('./output/finetune-distilbart-xsum/test_generations.txt', "r") as f:
    for line in f:
        bart_summary.append(line.strip())

df = pd.DataFrame({'article': articles[:100], 'target_summary': target_summary[:100], 'generated_summary': generated_summary[:100], 'bart_summary': bart_summary[:100]})
df.to_excel('./data/human-evaluation.xlsx', index=None)