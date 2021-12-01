Feature: create daybatch

  Scenario: no daybatches are created when no instruments are installed
    Given there are no instruments installed
    When the create daybatch process is triggered
    Then no daybatches are created

  Scenario: no daybatches are created when installed instruments do not have an active survey day of today
    Given 'OPN2101X' is installed
    And 'OPN2101X' does not have an active survey day of today
    And 'OPN2101X' has cases
    When the create daybatch process is triggered
    Then a daybatch is not created for 'OPN2101X'

  Scenario: no daybatches are created when installed instruments do not have cases
    Given 'OPN2101X' is installed
    And 'OPN2101X' has an active survey day of today
    And 'OPN2101X' does not have cases
    When the create daybatch process is triggered
    Then a daybatch is not created for 'OPN2101X'

  Scenario: a daybatch is created when an instrument is installed and has an active survey day of today and has cases
    Given 'OPN2101X' is installed
    And 'OPN2101X' has an active survey day of today
    And 'OPN2101X' has cases
    When the create daybatch process is triggered
    Then a daybatch is created for 'OPN2101X'

  Scenario: daybatches are only created for instruments that have an active survey day of today and has cases
    Given 'OPN2101X' is installed
    And 'OPN2101X' has an active survey day of today
    And 'OPN2101X' has cases
    And 'OPN2101Y' is installed
    And 'OPN2101Y' does not have an active survey day of today
    And 'OPN2101Y' does not have cases
    When the create daybatch process is triggered
    Then a daybatch is created for 'OPN2101X'
    And a daybatch is not created for 'OPN2101Y'

  Scenario: daybatches are created for all instruments that have an active survey day of today and has cases
    Given 'OPN2101X' is installed
    And 'OPN2101X' has an active survey day of today
    And 'OPN2101X' has cases
    And 'OPN2101Y' is installed
    And 'OPN2101Y' has an active survey day of today
    And 'OPN2101Y' has cases
    When the create daybatch process is triggered
    Then a daybatch is created for 'OPN2101X'
    And a daybatch is created for 'OPN2101Y'