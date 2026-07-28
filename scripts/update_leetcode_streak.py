import requests
import json
from datetime import datetime, timedelta
from pathlib import Path


USERNAME = "rohon97"


QUERY = """
query userProfileCalendar($username: String!) {
  matchedUser(username: $username) {

    submitStatsGlobal {
      acSubmissionNum {
        difficulty
        count
      }
    }

    userCalendar {
      submissionCalendar
    }

  }
}
"""


def get_leetcode_data():

    response = requests.post(
        "https://leetcode.com/graphql",
        json={
            "query": QUERY,
            "variables": {
                "username": USERNAME
            }
        },
        headers={
            "Content-Type": "application/json"
        }
    )

    response.raise_for_status()

    data = response.json()

    return data["data"]["matchedUser"]



def calculate_streaks(calendar):

    active_days = []

    for timestamp, count in calendar.items():

        if int(count) > 0:

            date = datetime.fromtimestamp(
                int(timestamp)
            ).date()

            active_days.append(date)


    active_days.sort()

    if not active_days:
        return 0, 0, 0


    active_set = set(active_days)


    # -------------------------
    # Current Streak
    # -------------------------

    current_streak = 0

    day = active_days[-1]


    while day in active_set:

        current_streak += 1

        day -= timedelta(days=1)



    # -------------------------
    # Longest Streak
    # -------------------------

    longest_streak = 1

    temp = 1


    for i in range(1, len(active_days)):

        difference = (
            active_days[i]
            -
            active_days[i-1]
        ).days


        if difference == 1:

            temp += 1

        else:

            temp = 1


        longest_streak = max(
            longest_streak,
            temp
        )


    return (
        current_streak,
        longest_streak,
        len(active_days)
    )


def generate_svg(
        current,
        longest,
        active,
        solved
):


    svg = f"""
<svg width="500" height="220"
xmlns="http://www.w3.org/2000/svg">


<rect width="500"
height="220"
rx="20"
fill="#161b22"/>


<text x="50"
y="55"
fill="white"
font-size="30"
font-family="Arial">
🔥 LeetCode Streak
</text>



<text x="120"
y="110"
fill="#58a6ff"
font-size="50"
font-family="Arial">
{current}
</text>


<text x="80"
y="145"
fill="white"
font-size="18">
Current Streak
</text>



<text x="350"
y="110"
fill="#58a6ff"
font-size="50"
font-family="Arial">
{longest}
</text>


<text x="300"
y="145"
fill="white"
font-size="18">
Longest Streak
</text>



<text x="80"
y="190"
fill="#3fb950"
font-size="18">
Active Days: {active}
</text>



<text x="310"
y="190"
fill="#3fb950"
font-size="18">
Solved: {solved}
</text>


</svg>
"""


    Path("assets").mkdir(
        exist_ok=True
    )


    with open(
        "assets/leetcode-streak.svg",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(svg)



def main():

    user = get_leetcode_data()



    # -------------------------
    # Match LeetCard solved count
    # -------------------------

    solved = (
        user["submitStatsGlobal"]
        ["acSubmissionNum"][0]
        ["count"]
    )



    # -------------------------
    # Full submission calendar
    # -------------------------

    calendar = json.loads(
        user["userCalendar"]
        ["submissionCalendar"]
    )



    current, longest, active = calculate_streaks(
        calendar
    )



    generate_svg(
        current,
        longest,
        active,
        solved
    )


    print(
        "LeetCode streak card updated successfully"
    )



if __name__ == "__main__":
    main()
