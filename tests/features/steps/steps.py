from behave import *

use_step_matcher("re")

no_instruments_installed = []


@given("there are no instruments installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    mock_get_installed_instrument_data = no_instruments_installed
    raise NotImplementedError(u'STEP: Given there are no instruments installed')


@when("the create daybatch process is triggered")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When the create daybatch process is triggered')


@then("no daybatches are created")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then no daybatches are created')


@given("there is an instrument installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given there is an instrument installed')


@step("the instrument does not have an active survey day of today")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the instrument does not have an active survey day of today')


@step("the instrument does not have cases")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the instrument does not have cases')


@step("the instrument does have an active survey day of today")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the instrument does have an active survey day of today')


@step("the instrument does have cases")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the instrument does have cases')


@then("a daybatch is created for the instrument")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then a daybatch is created for the instrument')


@given("there are two instruments installed")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given there are two instruments installed')


@step("the instrument 'OPN2101X' does not have an active survey day of today and does not have cases")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: And the instrument \'OPN2101X\' does not have an active survey day of today and does not have cases')


@step("the instrument 'OPN2101Y' has an active survey day of today and has cases")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the instrument \'OPN2101Y\' has an active survey day of today and has cases')


@then("a daybatch is not created for 'OPN2101X'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then a daybatch is not created for \'OPN2101X\'')


@step("a daybatch is created for 'OPN2101Y'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a daybatch is created for \'OPN2101Y\'')


@step("the instrument 'OPN2101Z' has an active survey day of today and has cases")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And the instrument \'OPN2101Z\' has an active survey day of today and has cases')


@step("a daybatch is created for 'OPN2101Z'")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: And a daybatch is created for \'OPN2101Z\'')
