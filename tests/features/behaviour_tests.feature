Feature: automated daybatch creation

  Scenario: no daybatch is created when no instruments are installed in CATI
    Given there are no instruments installed in CATI
    When the automated daybatch process is triggered
    Then no daybatches are created

  Scenario: no baybatch is created when active instruments in CATI do not have a survey day of today
    Given there is an instrument installed in CATI
    And the instrument does not have a survey day of today
    When the automated daybatch process is triggered
    Then a daybatch is not created for the instrument

  Scenario: a daybatch is created when an active instrument in CATI has a survey day of today
    Given there is an instrument installed in CATI
    And the instrument has a survey day of today
    When the automated daybatch process is triggered
    Then a daybatch is created for the instrument

  Scenario: a daybatch is created for OPN2101y when it has a survey day of today
    Given there are two instruments installed in CATI
    And the instrument 'OPN2101x' does not have a survey day of today
    And the instrument 'OPN2101y' has a survey day of today
    When the automated daybatch process is triggered
    Then a daybatch is only created for 'OPN2101y'

  Scenario: a daybatch is created for OPN2101x and OPN2101y when both have a survey day of today
    Given there are two instruments installed in CATI
    And the instrument 'OPN2101x' has a survey day of today
    And the instrument 'OPN2101y' has a survey day of today
    When the automated daybatch process is triggered
    Then a daybatch is only created for 'OPN2101x'
    And a daybatch is only created for 'OPN2101y'