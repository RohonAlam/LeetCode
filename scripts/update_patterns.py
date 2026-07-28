import os
import json
import re


with open(
    "data/problem_patterns.json",
    "r",
    encoding="utf-8"
) as f:
    patterns = json.load(f)


pattern_problems = {}


for folder in os.listdir("."):

    if not os.path.isdir(folder):
        continue


    # LeetSync format:
    # 852-peak-index-in-a-mountain-array

    match = re.match(
        r"^\d+-(.*)",
        folder
    )


    if match:

        slug = match.group(1)


        if slug in patterns:

            pattern = patterns[slug]


            if pattern not in pattern_problems:
                pattern_problems[pattern] = []


            number = folder.split("-")[0]


            pattern_problems[pattern].append(number)



table = """
| Pattern | Problems |
|---|---|
"""


for pattern, problems in pattern_problems.items():

    table += (
        f"| {pattern} | "
        f"{', '.join(problems)} |\n"
    )



with open(
    "README.md",
    "r",
    encoding="utf-8"
) as f:

    readme = f.read()



readme = re.sub(
    r"<!-- START_PATTERNS -->.*?<!-- END_PATTERNS -->",
    (
        "<!-- START_PATTERNS -->\n\n"
        + table +
        "\n<!-- END_PATTERNS -->"
    ),
    readme,
    flags=re.S
)



with open(
    "README.md",
    "w",
    encoding="utf-8"
) as f:

    f.write(readme)


print("Problem patterns updated")
