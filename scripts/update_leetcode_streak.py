import requests
from datetime import datetime, timedelta
from pathlib import Path


USERNAME = "rohon97"


QUERY = """
query userProfileCalendar($username: String!, $year: Int) {
  matchedUser(username: $username) {
    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }
    userCalendar(year: $year) {
      submissionCalendar
    }
  }
}
"""


def get_submission_data():

    year = datetime.now().year

    response = requests.post(
        "https://leetcode.com/graphql",
        json={
            "query": QUERY,
            "variables": {
                "username": USERNAME,
                "year": year
            }
        },
        headers={
            "Content-Type": "application/json"
        }
    )

    return response.json()["data"]["matchedUser"]



def calculate_streak(calendar):

    dates = []

    for timestamp, count in calendar.items():

        if int(count) > 0:

            date = datetime.fromtimestamp(
                int(timestamp)
            ).date()

            dates.append(date)


    dates.sort()


    longest = 0
    current = 0

    today = datetime.today().date()


    date_set = set(dates)


    # Current streak

    day = today

    while day in date_set:

        current += 1
        day -= timedelta(days=1)


    # Longest streak

    temp = 0
    previous = None


    for day in dates:

        if previous and day == previous + timedelta(days=1):

            temp += 1

        else:

            temp = 1


        longest = max(
            longest,
            temp
        )

        previous = day


    return current, longest, len(dates)



def create_svg(
    current,
    longest,
    active,
    solved
):

    svg = f"""
<svg width="500" height="220" 
xmlns="http://www.w3.org/2000/svg">

<rect width="500" height="220"
rx="15"
fill="#161b22"/>


<text x="40" y="50"
fill="white"
font-size="28"
font-family="Arial">
🔥 LeetCode Streak
</text>


<text x="70" y="110"
fill="#58a6ff"
font-size="45"
font-family="Arial">
{current}
</text>


<text x="50" y="145"
fill="white"
font-size="18">
Current Streak
</text>



<text x="240" y="110"
fill="#58a6ff"
font-size="45"
font-family="Arial">
{longest}
</text>


<text x="230" y="145"
fill="white"
font-size="18">
Longest Streak
</text>



<text x="70" y="190"
fill="#3fb950"
font-size="18">
Active Days: {active}
</text>


<text x="280" y="190"
fill="#3fb950"
font-size="18">
Solved: {solved}
</text>


</svg>
"""


    Path(
        "assets"
    ).mkdir(
        exist_ok=True
    )


    with open(
        "assets/leetcode-streak.svg",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(svg)



def main():

    data = get_submission_data()


    calendar = (
        data["userCalendar"]
        ["submissionCalendar"]
    )


    import json

    calendar = json.loads(
        calendar
    )



    current,longest,active = calculate_streak(
        calendar
    )


    solved = sum(
        item["count"]
        for item in
        data["submitStatsGlobal"]["acSubmissionNum"]
    )


    create_svg(
        current,
        longest,
        active,
        solved
    )



if __name__ == "__main__":
    main()
