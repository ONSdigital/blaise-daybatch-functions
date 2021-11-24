Feature: create daybatch

  Scenario: no daybatches are created when no instruments are installed
    Given there are no instruments installed
    When the create daybatch process is triggered
    Then no daybatches are created

  Scenario: no daybatches are created when installed instruments do not have an active survey day of today
    Given there is an instrument installed
    And the instrument does not have an active survey day of today
    When the create daybatch process is triggered
    Then no daybatches are created

  Scenario: no daybatches are created when installed instruments do not have cases
    Given there is an instrument installed
    And the instrument does not have cases
    When the create daybatch process is triggered
    Then no daybatches are created

  Scenario: a daybatch is created when an instrument is installed and has an active survey day of today and has cases
    Given there is an instrument installed
    And the instrument does have an active survey day of today
    And the instrument does have cases
    When the create daybatch process is triggered
    Then a daybatch is created for the instrument

  Scenario: daybatches are only created for instruments that have an active survey day of today and has cases
    Given there are two instruments installed
    And the instrument 'OPN2101X' does not have an active survey day of today and does not have cases
    And the instrument 'OPN2101Y' has an active survey day of today and has cases
    When the create daybatch process is triggered
    Then a daybatch is not created for 'OPN2101X'
    And a daybatch is created for 'OPN2101Y'

  Scenario: daybatches are created for all instruments that have an active survey day of today and has cases
    Given there are two instruments installed
    And the instrument 'OPN2101Y' has an active survey day of today and has cases
    And the instrument 'OPN2101Z' has an active survey day of today and has cases
    When the create daybatch process is triggered
    Then a daybatch is created for 'OPN2101Y'
    And a daybatch is created for 'OPN2101Z'