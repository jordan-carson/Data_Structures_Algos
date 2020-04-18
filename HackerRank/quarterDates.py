

def quarterDates(arr):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    quarters = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3', 'Q4', 'Q4', 'Q4']
    new = dict(zip(months, quarters))
    new_dates = list()
    for i in arr:
        year = i[:4]
        month = i[5:7]

        new_dates.append(str(year) + new.get(int(month)))

    return new_dates






sampledate = ["2014-03-25", '2018-10-12']
print(quarterDates(sampledate))

new_dates = list()
for i in sampledate:
    # for k in dates.keys():
    #
    #     if k == date

    year = i[:4]
    month = i[5:7]
    day = i[8:10]
    if int(month) in [1,2,3]:
        quarter = 'Q1'
    elif int(month) in [4,5,6]:
        quarter = 'Q2'
    elif int(month) in [7,8,9]:
        quarter = 'Q3'
    elif int(month) in [10,11,12]:
        quarter = 'Q4'

    # new_date = str(year) + quarter
    new_dates.append(str(year) + quarter)

    print(new_dates)


