
removables = ['[', ']', '"', "\n", "address\n", ' ', "", "Co."]
def normalize_title(title):
    for remove in removables:
        title = title.replace(remove, '')
    title = title.lower()
    return title




counties = ['carlow','cavan','clare','cork',
'donegal','dublin','galway','kerry','kildare','kilkenny',
'laois','leitrim','limerick','longford','louth','mayo','meath','monaghan',
'offaly','roscommon','sligo','tipperary','waterford','westmeath',
'wexford','wicklow']





addresses = []
with open('addresses_for_task.csv', 'r') as f:
    
    for line in f:
        title = normalize_title(line)
        title = title.split(",")
        if len(line) > 10:
            addresses.append(title)