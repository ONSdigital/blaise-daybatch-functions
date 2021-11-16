# blaise-daybatch-functions

> A day batch is a selection of cases from the entire Blaise data file that will be worked on that day. Since the CATI system cannot work without a day batch, you have to create a day batch per CATI survey for each active day in the survey period.

This repo has functions for creating daybatches and checking that daybatches have been created. Notifications are sent
if daybatches don't exist but should. These functions are deployed to GCP as Cloud Functions and will be triggered via
Cloud Scheduler.

### Local Setup

Clone the project locally:

```shell
git clone https://github.com/ONSdigital/blaise-daybatch-functions.git
```

Setup a virtual environment:

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

Install dependencies:

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

```shell
BLAISE_API_URL="localhost:90"
BLAISE_SERVER_PARK="gusty"
```

Run the "create_daybatches" Cloud Function:

```
python -c "from main import create_daybatches; create_daybatches(None, None)"
```

Run the "check_daybatches" Cloud Function:

```
python -c "from main import check_daybatches; check_daybatches(None, None)"
```