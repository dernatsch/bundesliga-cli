#! /usr/bin/env python3

import argparse

import requests
import json
from datetime import datetime

def print_goals(goals):
    for goal in goals:
        t = goal["MatchMinute"]
        scorer = goal["GoalGetterName"]

        print(f"                    {t}' {scorer}")

    print()

def print_match(match, i, printgoals=False):
    t1 = match["Team1"]["ShortName"]
    t2 = match["Team2"]["ShortName"]
    vs = "  vs "

    print(f"{i}) ", end="")

    # If the game already started display the score instead of vs
    # If the game is in the future show the date after the teams
    result = match["MatchResults"]
    if len(result) > 0:
        t1g = result[0]["PointsTeam1"]
        t2g = result[0]["PointsTeam2"]
        print(f"{t1:>15} [{t1g}:{t2g}] {t2:15}", end="")
    else:
        dt = datetime.fromisoformat(match["MatchDateTime"])
        print(f"{t1:>15}   vs  {t2:15}", end="")
        print(dt.strftime("%a %H:%M"), end="")

    print()

    if printgoals:
        print_goals(match["Goals"])

def main():
    parser = argparse.ArgumentParser(
        description="Show Bundesliga scores on the command line."
    )

    parser.add_argument("--goals", dest="goals", action="store_true",
            help="print the goals of each game")
    args = parser.parse_args()

    r = requests.get("https://openligadb.de/api/getmatchdata/bl1")
    data = r.json()

    for i, match in enumerate(data):
        print_match(match, i, printgoals=args.goals)


if __name__=="__main__":
    main()
