
def merge_ranges(meetings):

    # sort by start time
    sorted_meetings = sorted(meetings)

    # initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, max(last_merged_meeting_end, current_meeting_end))
        else:
            # add the current meeting since it doesn't overlap
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings


if __name__ == '__main__':
    INPUT_ARRAY = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    SOLUTION = [(0, 1), (3, 8), (9, 12)]

    sol = merge_ranges(INPUT_ARRAY)

    print('Pass' if sol == SOLUTION else 'Fail')