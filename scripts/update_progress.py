
import json
import re

with open("data/dsa_progress.json", encoding="utf-8") as f:
    data = json.load(f)

rows = []
total_done = 0
total_questions = 0

for topic, info in data.items():
    solved = len(info["solved"])
    total = info["total"]
    total_done += solved
    total_questions += total

    percent = int((solved / total) * 100) if total else 0
    filled = percent // 10
    bar = "█" * filled + "░" * (10-filled)

    rows.append(
        f"| {topic} | {solved} | {total} | {bar} {percent}% |"
    )

overall = int((total_done / total_questions) * 100)

table = """| Topic | Completed | Total | Progress |
|---|---:|---:|---|
""" + "\n".join(rows) + f"""

### Overall Progress

**{total_done}/{total_questions} Problems Completed**

`{overall}%`
"""

with open("README.md", encoding="utf-8") as f:
    readme = f.read()

readme = re.sub(
    r"<!-- START_PROGRESS -->.*?<!-- END_PROGRESS -->",
    "<!-- START_PROGRESS -->\n\n" + table + "\n\n<!-- END_PROGRESS -->",
    readme,
    flags=re.S
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme)
