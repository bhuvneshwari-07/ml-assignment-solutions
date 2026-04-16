# Scenario 10: Summarization with Constraints
# Task: Summarize a text into 2 sentences.
# If the summary exceeds 50 words, truncate it to the nearest complete sentence.

def summarize_text(text):
    # Mock summary (replace with real LLM if needed)
    summary = "Python is widely used in data science. It offers powerful libraries and simplicity."

    words = summary.split()

    if len(words) > 50:
        sentences = summary.split('.')
        truncated = ''
        word_count = 0

        for sentence in sentences:
            if word_count + len(sentence.split()) <= 50:
                truncated += sentence + '.'
                word_count += len(sentence.split())
            else:
                break

        return truncated.strip()

    return summary


if __name__ == "__main__":
    print(summarize_text("Some long article text...")) 