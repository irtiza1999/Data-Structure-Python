# Given N number of activities with their start and end times. We nee d to select the maximum number og activities that can be performed by a single person, assumming that a person can only work on a single activity at a time.

activities = [["A1", 0, 6],
              ["A2", 3, 4],
              ["A3", 1, 2],
              ["A4", 5, 8],
              ["A5", 5, 7],
              ["A6", 8, 9]
              ]


def printMaxActivitices(activities):
    activities.sort(key=lambda x: x[2])
    i = 0
    firstA = activities[i][0]
    print(firstA)
    for j in range(len(activities)):
        if activities[j][1] > activities[i][2]:
            print(activities[j][0])
            i = j
            
printMaxActivitices(activities)
