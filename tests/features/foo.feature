Scenario 1 Automate daybatch creation using 'Active Survey Days'

Given a survey is deployed in Blaise 5 environment (questionnaire and sample)
When there is an 'active survey day' that matches today's date associated with the survey
Then a daybatch for that survey will be automatically created in CATI

Scenario 2 Timing of automated daybatch process

Given a survey with an 'active survey day' that matches today's date
When it is 05:00
Then the automated daybatch process begins
And the daybatch will be available for TO interviewers to start work no later than 09:00

Scenario 3 Include all cases in daybatch

Given a survey with an 'active survey day' that matches today's date
When the automated daybatch process is run
Then all cases associated with that survey will be included