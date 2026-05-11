import re
import requests

README = "README.md"

# Fetch a random quote
q = requests.get("https://zenquotes.io/api/random").json()[0]
quote = q["q"]
author = q["a"]

new_line = f'- 🥅 **Favorite Quote:** _"{quote}" — {author}_\n'

with open(README, "r", encoding="utf-8") as f:
    content = f.readlines()

pattern = re.compile(r'^- 🥅 \*\*Favorite Quote:\*\* .*')

replaced = False
for i, line in enumerate(content):
    if pattern.match(line):
        content[i] = new_line
        replaced = True
        break

if not replaced:
    # Insert quote after "Mobile Engineer 🌱"
    for i, line in enumerate(content):
        if line.strip().startswith('### Mobile Engineer'):
            content.insert(i + 2, new_line)
            break

with open(README, "w", encoding="utf-8") as f:
    f.writelines(content)

print(f'Quote updated: "{quote}" — {author}')
