import requests
import singer
import time

from requests.auth import HTTPBasicAuth

LOGGER = singer.get_logger()

class TapAppcues:
    def __init__(self, account_id, access_token, secret_token):
        self.account_id = account_id
        self.access_token = access_token
        self.secret_token = secret_token

    def discover(self):
        schema = {
            "properties": {
                "job_id": {"type": "string"},
                "job_url": {"type": "string"},
                "status": {"type": "integer"},
                "title": {"type": "string"}
            }
        }
        singer.write_schema('appcues', schema, 'job_id')

    def get_basic_auth(self):
        return HTTPBasicAuth(self.access_token, self.secret_token)

    def start_sync(self):
        url = f"https://api.appcues.com/v2/accounts/{self.account_id}/bulk_export/jobs"
        body = {}
        response = requests.post(url, headers={'Content-Type': 'application/json'}, auth=self.get_basic_auth())
        if response.status_code != 202:
            raise Exception(f"Failed to initiate bulk export: {response.text}")
        response_data = response.json()
        job_id = response_data["job_id"]
        job_url = response_data["job_url"]
        LOGGER.info(f"Started bulk export with job_id {job_id}")
        return job_url

    def check_job_status(self, job_url):
        response = requests.get(job_url, headers={'Content-Type': 'application/json'}, auth=self.get_basic_auth())
        response_data = response.json()
        status = response_data["status"]
        LOGGER.info(f"Job status is {status}")
        return status

    def sync(self):
        self.discover()
        job_url = self.start_sync()
        status = 202
        while status not in [200, 400, 422]:
            LOGGER.info("Waiting for job to complete...")
            time.sleep(10)
            status = self.check_job_status(job_url)
        if status == 200:
            LOGGER.info("Bulk export job completed successfully")
        else:
            raise Exception(f"Bulk export job failed with status {status}")

if __name__ == '__main__':
    tap = TapAppcues("137053", "ecf7f10a-3ece-4658-9bc9-d592306697ed-02", "f7c6d033-0221-4c7d-bf01-5e28a5c85d27")
    tap.sync()
