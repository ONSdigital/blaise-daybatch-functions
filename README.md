# blaise-daybatch-functions

> A day batch is a selection of cases from the entire Blaise data file that will be worked on that day. Since the CATI system cannot work without a day batch, you have to create a day batch per CATI survey for each active day in the survey period.

This repo has functions for creating daybatches and checking that daybatches have been created. Notifications are sent
if daybatches don't exist but should. These functions are deployed to GCP as Cloud Functions and will be triggered via
Cloud Scheduler.

An email will be sent to the users *if* Daybatch creation fails *or* there is no baybatch.

The email template comes from gov.notify portal (see Rich for credentials :eyes).

Email wording changed on 07/04/22 to "Questionnaire {questionnaire} may not have a daybatch".

## Local Setup

Clone the project locally:

```shell
git clone https://github.com/ONSdigital/blaise-daybatch-functions.git
```

### Set up a virtual environment:

If `poetry` is already installed globally, skip virtual environment setup and follow from [Install dependencies](#install-dependencies) step.

macOS:

```shell
python3 -m venv venv
source venv/bin/activate
```

Windows:

```shell
python -m venv venv
venv\Scripts\activate
```

Install poetry:

```shell
pip install poetry
```

### Install dependencies:

```shell
poetry install
```

Authenticate with GCP:

```shell
gcloud auth login
```

Set your GCP project:

```shell
gcloud config set project ons-blaise-v2-dev-sandbox123
```

Open a tunnel to our Blaise RESTful API in your GCP project:

```shell
gcloud compute start-iap-tunnel restapi-1 80 --local-host-port=localhost:90 --zone europe-west2-a
```

Create an .env file in the root of the project and add the following environment variables:

| Variable | Description | Example |
| --- | --- | --- |
| BLAISE_API_URL | The RESTful API URL the application will use to get installed questionnaire data. | localhost:90 |
| BLAISE_SERVER_PARK | The name of the Blaise server park. | gusty |
| NOTIFY_API_KEY | The API key for the GOV.UK Notify service. | blah-blah-blah |
| TO_NOTIFY_EMAIL | The email address to notify when a daybatch doesn't exist but should. | blah@blah.blah |

Example .env file:

```shell
BLAISE_API_URL="localhost:90"
BLAISE_SERVER_PARK="gusty"
NOTIFY_API_KEY="blah-blah-blah"
TO_NOTIFY_EMAIL="blah@blah.blah"
```

The local environment variables aren't necessary if you're only running the unit tests and the behave tests.

Run the "create_daybatches" Cloud Function:

```shell
poetry run python -c "from main import create_daybatches; create_daybatches(None, None)"
```

Run the "check_daybatches" Cloud Function:

```shell
poetry run python -c "from main import check_daybatches; check_daybatches(None, None)"
```

## Linting

- Run `make lint` to run lint checks.
- Run `make lint-fix` to apply auto-fixes and formatting.
```shell
make lint
make lint-fix
```

## Type Checking

- Run `make typecheck` to run static type checks.
- Type checking is powered by Pyright and configured for strict checking in `pyproject.toml`.
- Only `models/config_models.py` has type annotations, so Pyright includes only the `models` directory; configured in `pyproject.toml`.

```shell
make typecheck
```

## Check for unused or missing Python dependencies

- Run `make deptry` to check for unused or missing dependencies
```shell
make deptry
```


## Check for dead (unused) Python code

- Run `make vulture` to check for unused Python code
```shell
make vulture
```



## Unit tests

- Run `make test` to run tests and report coverage.
- The coverage report omits test files.

```shell
make test
```

## Run Behave BDD Tests
- Run `make test-behave` to run the behave tests.
```shell
make test-behave
```
