import subprocess
import re
from datetime import datetime


def get_all_commits():
    """
    Get complete git history
    """

    command = [
        "git",
        "log",
        "--reverse",
        "--name-only",
        "--pretty=format:%ad",
        "--date=format:%d %B %Y"
    ]

    result = subprocess.check_output(
        command
    ).decode("utf-8")

    return result



def extract_problems(log):

    lines = log.split("\n")

    problems = []

    current_date = ""

    solved = {}


    for line in lines:

        line = line.strip()


        if not line:
            continue


        # Date line
        if re.match(
            r"\d{1,2} \w+ \d{4}",
            line
        ):

            current_date = line



        # Detect LeetSync folder
        elif re.search(
            r"^\d+-",
            line
        ):

            folder = line.split("/")[0]


            match = re.match(
                r"(\d+)-(.*)",
                folder
            )


            if match:

                number = match.group(1)

                title = (
                    match.group(2)
                    .replace("-", " ")
                    .title()
                )


                problem = (
                    f"{number}. {title}"
                )


                # Save latest commit date
                solved[problem] = current_date



    # Convert dictionary to list
    for problem, date in solved.items():

        problems.append(
            (
                date,
                problem
            )
        )


    return problems



def sort_by_date(problems):

    def convert(date):

        return datetime.strptime(
            date,
            "%d %B %Y"
        )


    return sorted(
        problems,
        key=lambda x: convert(x[0]),
        reverse=True
    )



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
        encoding="utf-8"
    ) as f:

        readme = f.read()



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
    ) as f:

        f.write(updated)



if __name__ == "__main__":


    history = get_all_commits()


    problems = extract_problems(
        history
    )


    problems = sort_by_date(
        problems
    )


    # Show latest 15
    problems = problems[:15]


    table = create_table(
        problems
    )


    update_readme(
        table
    )


    print(
        "README recent problems updated"
    )
