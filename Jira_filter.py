from atlassian import Jira

jira = Jira(
    url = 'https://jira.orcsoftware.com/',
    username = 'bblenyesi',
    password = 'Infront22222222!'
)

jql_request = 'project = FOBR AND (assignee = amunlawin OR reporter = amunlawin) AND updatedDate >= startOfMonth(-1) AND updatedDate <= endOfMonth(-1)'
ticket = jira.jql(jql_request)

print(ticket)