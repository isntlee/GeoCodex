
removables = ['[', ']', '"', "\n", "address\n", ' ', "", "Co."]
def normalize_title(title):
    for remove in removables:
        title = title.replace(remove, '')
    title = title.lower()
    return title




counties = ['antrim','armagh','carlow','cavan','clare','cork','derry',
'donegal','down','dublin','fermanagh','galway','kerry','kildare','kilkenny',
'laois','leitrim','limerick','longford','louth','mayo','meath','monaghan',
'offaly','roscommon','sligo','tipperary','tyrone','waterford','westmeath',
'wexford','wicklow']





addresses = []
with open('addresses_for_task.csv', 'r') as f:
    
    for line in f:
        title = normalize_title(line)
        title = title.split(",")
        if len(line) > 10:
            addresses.append(title)