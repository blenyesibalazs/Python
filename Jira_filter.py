from atlassian import Jira

jira = Jira(
    url = 'https://jira.orcsoftware.com/',
    username = 'bblenyesi',
    password = 'Infront22222222!'
)

jql_request = 'project = FOBR AND (assignee = amunlawin OR reporter = amunlawin) AND updatedDate >= startOfMonth(-1) AND updatedDate <= endOfMonth(-1)'
ticket = jira.jql(jql_request)


#delete miscellaneous keys, needs optimization
notNeededKeys = ["expand", "startAt", "maxResults"]

print("Deleting keys: ")
for i in range(len(notNeededKeys)):
    del ticket[notNeededKeys[i]]
    print(notNeededKeys[i])

print('\n\n')
#the types vary depending on depth, there's a ton of nesting ongoing
#print(type(ticket))
#print(type(ticket["issues"]))
#print(type(ticket["issues"][0]))
#print(type(print(ticket["issues"][0]["fields"]))) #this finally contains all custom fields

nrTickets = ticket["total"]
parameters = ticket["issues"][0]["fields"] #new dictionary to house parameters

print(nrTickets)