from util.readfile import read_file

type Report = list[int]
reports = []

with read_file("input.txt") as file:
    for line in file:
        reps = map(int, line.split())
        reports.append(list(reps))


def is_ok(report: Report) -> bool:
    ascending = descending = True
    for i in range(len(report) - 1):
        is_larger = report[i] < report[i + 1]
        diff = abs(report[i] - report[i + 1])
        acceptable = 1 <= diff <= 3

        if is_larger and acceptable:
            descending = False
        elif not is_larger and acceptable:
            ascending = False
        else:
            return False

    return ascending or descending


def is_ok_with_remove(report: Report) -> bool:
    if is_ok(report):
        return True

    for i in range(len(report)):
        temp = report[:i] + report[i + 1:]
        if is_ok(temp):
            return True

    return False


valid_reports_p1 = 0
valid_reports_p2 = 0
for report in reports:
    if is_ok(report):
        valid_reports_p1 += 1
    if is_ok_with_remove(report):
        valid_reports_p2 += 1
print(valid_reports_p1)
print(valid_reports_p2)
