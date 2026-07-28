import os
import re


# Define topic keywords
topics = {
    "Arrays": [
        "array",
        "sum",
        "maximum",
        "merge",
        "sort",
        "product",
        "duplicate"
    ],

    "Binary Search": [
        "search",
        "peak",
        "single-element",
        "rotated"
    ],

    "Hashing": [
        "majority",
        "anagram",
        "hash",
        "frequency"
    ],

    "Sliding Window": [
        "substring",
        "window"
    ],

    "Two Pointer": [
        "3sum",
        "4sum",
        "container"
    ],

    "Matrix": [
        "matrix",
        "2d"
    ],

    "Linked List": [
        "linked",
        "list"
    ],

    "Trees": [
        "tree",
        "binary-tree"
    ],

    "Graphs": [
        "graph",
        "dfs",
        "bfs"
    ],

    "Dynamic Programming": [
        "dp",
        "dynamic"
    ]
}


counts = {topic:0 for topic in topics}


folders = [
    f for f in os.listdir(".")
    if os.path.isdir(f)
]


total = 0


for folder in folders:

    if re.match(r"^\d+-", folder):

        total += 1

        folder_name = folder.lower()

        matched = False

        for topic, keywords in topics.items():

            for keyword in keywords:

                if keyword in folder_name:
                    counts[topic] += 1
                    matched = True
                    break

            if matched:
                break



def progress_bar(value):

    total_problems = max(total,1)

    percentage = int((value / total_problems) * 100)

    filled = percentage // 10

    return (
        "█" * filled +
        "░" * (10-filled)
    )


output = []

output.append(
    f"### Total Problems Solved: **{total}**\n"
)


for topic,count in counts.items():

    percentage = int((count/max(total,1))*100)

    output.append(
        f"| {topic} | {count} | {progress_bar(count)} {percentage}% |\n\n"
    )


table = """
| Topic | Problems | Progress |
|---|---|---|
""" + "".join(output)


with open("README.md","r") as file:
    readme=file.read()



new_readme = re.sub(
    r"<!-- START_PROGRESS -->.*?<!-- END_PROGRESS -->",
    f"<!-- START_PROGRESS -->\n\n{table}\n<!-- END_PROGRESS -->",
    readme,
    flags=re.S
)


with open("README.md","w") as file:
    file.write(new_readme)


print("README Updated Successfully")
