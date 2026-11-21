# the-joke-the-reviewer-laughs-at-20261121-0329: one joke about AI coding agents, written to entry.txt.
import os

dir_path = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
os.makedirs(dir_path, exist_ok=True)
file_path = os.path.join(dir_path, 'entry.txt')

joke = "When the bot asked me to explain the inheritance tree, I realized I was just the senior developer reviewer for an intern who never sleeps."

with open(file_path, 'w', encoding='utf-8', newline='') as f:
    f.write(joke)
