from unittest.mock import patch

from notifications_python_client.notifications import NotificationsAPIClient

from functions.notify_functions import send_email_notification_for_instrument_without_daybatch


@patch.object(NotificationsAPIClient, "send_email_notification")
def test_send_email_notification_for_instrument_without_daybatch(mock_send_email_notification, mock_config):
    print(mock_config)
    assert send_email_notification_for_instrument_without_daybatch(mock_config, "DST2106Z") is None
    mock_send_email_notification.assert_called_once()
