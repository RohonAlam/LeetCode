import os
import json
import re


with open(
    "data/problem_topics.json",
    "r",
    encoding="utf-8"
) as file:

    problem_topics = json.load(file)



topic_count = {}


for topic in problem_topics.values():

    topic_count[topic] = 0



solved_problems = []



# Scan repository folders

for item in os.listdir("."):

    if not os.path.isdir(item):
        continue


    # LeetSync folder format:
    # 852-peak-index-in-a-mountain-array

    match = re.match(
        r"^\d+-(.*)",
        item
    )


    if match:

        slug = match.group(1)


        solved_problems.append(
            slug
        )


        if slug in problem_topics:

            topic = problem_topics[slug]

            topic_count[topic] += 1



total = len(solved_problems)



def progress_bar(value):

    if total == 0:
        return "░░░░░░░░░░"


    percentage = int(
        (value / total) * 100
    )


    filled = percentage // 10


    return (
        "█" * filled +
        "░" * (10-filled)
    )



table = """
| Topic | Problems Uploaded | Progress |
|---|---:|---|
"""


for topic, count in topic_count.items():

    percentage = (
        int((count / total) * 100)
        if total else 0
    )


    table += (
        f"| {topic} | {count} | "
        f"{progress_bar(count)} {percentage}% |\n"
    )



table += f"""

### Repository Progress

**{total} Problems Uploaded**

"""



with open(
    "README.md",
    "r",
    encoding="utf-8"
) as file:

    readme = file.read()



updated = re.sub(
    r"<!-- START_PROGRESS -->.*?<!-- END_PROGRESS -->",
    (
        "<!-- START_PROGRESS -->\n\n"
        + table +
        "\n<!-- END_PROGRESS -->"
    ),
    readme,
    flags=re.S
)



with open(
    "README.md",
    "w",
    encoding="utf-8"
) as file:

    file.write(updated)



print(
    "DSA Progress Updated"
)
