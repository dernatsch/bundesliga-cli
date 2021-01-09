#! /usr/bin/env python3

import requests
import json

def print_match(match, i):
    t1 = match["Team1"]["ShortName"]
    t2 = match["Team2"]["ShortName"]
    vs = "  vs "

    result = match["MatchResults"]
    if len(result) > 0:
        t1g = result[0]["PointsTeam1"]
        t2g = result[0]["PointsTeam2"]
        print(f"{t1:>15} [{t1g}:{t2g}] {t2:15}", end="")
    else:
        print(f"{t1:>15}   vs  {t2:15}", end="")

    print()

def main():
    r = requests.get("https://openligadb.de/api/getmatchdata/bl1")
    data = r.json()

    for i, match in enumerate(data):
        print_match(match, i)


if __name__=="__main__":
    main()
