import re
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏 👏 👏 http://example.com"

# Remove mentions, URLs, emojis, and special characters
clean_text = re.sub(r"@\w+|http\S+|[^\w\s]", "", raw_text)
clean_text = clean_text.lower()
print("Tīrs teksts:")
print(clean_text)
