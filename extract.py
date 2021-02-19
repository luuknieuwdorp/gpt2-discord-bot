import json
import os
import re

root = os.path.dirname(__file__)
source = os.path.join(root, "source")
dojo = os.path.join(source, 'dojo')

output = open(os.path.join(root, dojo, "output.txt"), 'w', encoding='utf-8')

if __name__ == '__main__':
    for entry in os.scandir(source):
        if entry.path.endswith(".json"):
            text = json.load(open(entry.path, 'r', encoding='utf-8'))
            for message in text["messages"]:
                if message["author"]["name"] == "Dojobear":
                    text = re.sub("^>.*\\n\\n", "", message["content"])
                    output.write(text + "\n")

output.close()

