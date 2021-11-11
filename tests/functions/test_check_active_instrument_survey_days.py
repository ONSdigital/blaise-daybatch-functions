"""Test suite for the 'check active instrument survey day' module."""
import unittest
from unittest.mock import patch

import tests.helpers

date = "10/11/21"


@patch(tests.helpers.api_call())
def test_no_daybatch_is_created_when_no_active_instruments_are_returned_from_the_api(mock_api_call):
    # arrange
    mock_api_call.return_value = MagicMock()

    # act

    # assert
    pass
