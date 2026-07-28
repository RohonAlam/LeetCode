import subprocess
import re
from datetime import datetime


def get_recent_commits(limit=10):

    command = [
        "git",
        "log",
        f"-{limit}",
        "--name-only",
        "--pretty=format:%ad",
        "--date=format:%d %B %Y"
    ]

    result = subprocess.check_output(command).decode()

    return result



def extract_problems(log):

    lines = log.split("\n")

    problems = []

    current_date = ""

    for line in lines:

        line = line.strip()

        if not line:
            continue


        # Date line
        if re.match(r"\d{1,2} \w+ \d{4}", line):
            current_date = line


        # Folder containing LeetCode problem
        elif re.match(r"\d+-", line):

            folder = line.split("/")[0]

            name = folder.replace("-", " ")

            problems.append(
                (current_date, name.title())
            )


    return problems[:10]



def create_table(problems):

    table = """
| Date | Problem |
|---|---|
"""

    for date, problem in problems:

        table += (
            f"| {date} | {problem} |\n"
        )

    return table



log = get_recent_commits()

problems = extract_problems(log)

table = create_table(problems)



with open("README.md", encoding="utf-8") as f:
    readme = f.read()


readme = re.sub(
    r"<!-- START_RECENT -->.*?<!-- END_RECENT -->",
    f"<!-- START_RECENT -->\n\n{table}\n<!-- END_RECENT -->",
    readme,
    flags=re.S
)


with open("README.md","w",encoding="utf-8") as f:
    f.write(readme)


print("Recent problems updated")
