import subprocess
import re


def get_recent_commits(limit=20):
    """
    Get recent git commits with changed file names
    """

    command = [
        "git",
        "log",
        f"-{limit}",
        "--name-only",
        "--pretty=format:%ad",
        "--date=format:%d %B %Y"
    ]

    result = subprocess.check_output(command).decode("utf-8")

    return result



def extract_problems(log):
    """
    Extract LeetCode problem folders from git history
    """

    lines = log.split("\n")

    problems = []

    current_date = ""

    seen = set()


    for line in lines:

        line = line.strip()


        if not line:
            continue


        # Detect date
        if re.match(r"\d{1,2} \w+ \d{4}", line):

            current_date = line


        # Detect LeetSync folder
        elif re.search(r"\d+-", line):

            folder = line.split("/")[0]


            match = re.match(
                r"(\d+)-(.*)",
                folder
            )


            if match:

                number = match.group(1)

                title = match.group(2)

                title = (
                    title
                    .replace("-", " ")
                    .title()
                )


                problem = (
                    f"{number}. {title}"
                )


                # Remove duplicates
                if problem not in seen:

                    problems.append(
                        (
                            current_date,
                            problem
                        )
                    )

                    seen.add(problem)



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



def update_readme(table):

    with open(
        "README.md",
        "r",
        encoding="utf-8"
    ) as file:

        readme = file.read()



    updated = re.sub(
        r"<!-- START_RECENT -->.*?<!-- END_RECENT -->",
        (
            "<!-- START_RECENT -->\n\n"
            + table +
            "\n<!-- END_RECENT -->"
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



if __name__ == "__main__":

    log = get_recent_commits()

    problems = extract_problems(log)


    if problems:

        table = create_table(problems)

    else:

        table = """
| Date | Problem |
|---|---|
| - | No recent problems found |
"""


    update_readme(table)


    print(
        "Recently solved problems updated successfully!"
    )
