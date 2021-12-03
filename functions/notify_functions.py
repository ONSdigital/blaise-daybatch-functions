from notifications_python_client.notifications import NotificationsAPIClient


def send_email_notification(config, instrument_name):
    try:
        print(f"Sending email notification for instrument {instrument_name} to {config.to_notify_email}")
        notifications_client = NotificationsAPIClient(f"{config.notify_api_key}")
        notifications_client.send_email_notification(
            email_address=f"{config.to_notify_email}",
            template_id=f"26ee1592-2de8-4ca7-a833-219595e110cf",
            personalisation={"instrument_name": instrument_name}
        )
    except Exception as error:
        print(f"Error when sending email notification for instrument {instrument_name} via GOV.UK Notify API - ", error)
