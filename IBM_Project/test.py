from transformers import BartTokenizer, BartForConditionalGeneration, pipeline
from rouge_score import rouge_scorer

# Load pre-trained model and tokenizer
model_name = 'facebook/bart-large-cnn'
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)


# Function to summarize text
def summarize_text(text, max_length=250, min_length=100):
    summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)
    summary = summarizer(text, max_length=max_length, min_length=min_length, truncation=True)
    return summary[0]['summary_text']


# Sample text for summarization
sample_text = """
Types of Animals
First of all, all kinds of living organisms which are eukaryotes and compose of numerous cells and can sexually reproduce are known as animals. All animals have a unique role to play in maintaining the balance of nature.
A lot of animal species exist in both, land and water. As a result, each of them has a purpose for their existence. The animals divide into specific groups in biology. Amphibians are those which can live on both, land and water.
Reptiles are cold-blooded animals which have scales on their body. Further, mammals are ones which give birth to their offspring in the womb and have mammary glands. Birds are animals whose forelimbs evolve into wings and their body is covered with feather.
They lay eggs to give birth. Fishes have fins and not limbs. They breathe through gills in water. Further, insects are mostly six-legged or more. Thus, these are the kinds of animals present on earth.
Importance of Animal
Animals play an essential role in human life and planet earth. Ever since an early time, humans have been using animals for their benefit. Earlier, they came in use for transportation purposes.
Further, they also come in use for food, hunting and protection. Humans use oxen for farming. Animals also come in use as companions to humans. For instance, dogs come in use to guide the physically challenged people as well as old people.
In research laboratories, animals come in use for drug testing. Rats and rabbits are mostly tested upon. These researches are useful in predicting any future diseases outbreaks. Thus, we can protect us from possible harm.
Astronomers also use animals to do their research. They also come in use for other purposes. Animals have use in various sports like racing, polo and more. In addition, they also have use in other fields.
They also come in use in recreational activities. For instance, there are circuses and then people also come door to door to display the tricks by animals to entertain children. Further, they also come in use for police forces like detection dogs.
Similarly, we also ride on them for a joyride. Horses, elephants, camels and more come in use for this purpose. Thus, they have a lot of importance in our lives.
"""

# Summarize the sample text
summary = summarize_text(sample_text)
print("Summary:")
print(summary)


# Function to evaluate the summary using ROUGE
def evaluate_summary(reference_text, generated_summary):
    scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
    scores = scorer.score(reference_text, generated_summary)
    return scores


# Evaluate the generated summary
rouge_scores = evaluate_summary(sample_text, summary)
print("\nROUGE Scores:")
print(rouge_scores)
