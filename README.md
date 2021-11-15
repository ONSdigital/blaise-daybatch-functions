# blaise-daybatch-functions

blah blah blah

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

```shell
BLAISE_API_URL="localhost:90"
```

Run the "create_daybatches" Cloud Function:

python -c "from main import create_daybatches; create_daybatches(None, None)"