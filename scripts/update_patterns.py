import os
import json
import re


with open(
    "data/problem_patterns.json",
    encoding="utf-8"
) as f:
    patterns = json.load(f)



result = {}



for folder in os.listdir("."):

    if not os.path.isdir(folder):
        continue


    match = re.match(
        r"(\d+)-(.*)",
        folder
    )


    if match:

        problem_id = match.group(1)


        if problem_id in patterns:

            pattern = patterns[problem_id]

            if pattern not in result:
                result[pattern] = []


            result[pattern].append(problem_id)



table = """
| Pattern | Problems |
|---|---|
"""



for pattern, problems in result.items():

    table += (
        f"| {pattern} | "
        f"{', '.join(problems)} |\n"
    )



with open(
    "README.md",
    encoding="utf-8"
) as f:

    readme = f.read()



import re


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



print("Patterns updated")



