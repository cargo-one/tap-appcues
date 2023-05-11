# tap-appcues

ecf7f10a-3ece-4658-9bc9-d592306697ed-02

f7c6d033-0221-4c7d-bf01-5e28a5c85d27

137053


curl https://api.appcues.com/v2/accounts/137053/export/events \
  -u ecf7f10a-3ece-4658-9bc9-d592306697ed-02:f7c6d033-0221-4c7d-bf01-5e28a5c85d27 \
  -H 'content-type: application/json' \
  -d '
  {
    "email": "mr@cargo.one",
    "format": "csv",
    "conditions": [
      ["name", "like", "appcues%"]
    ],
    "start_time": "2023-04-19T00:00:00",
    "end_time": "2023-04-19T06:00:00",
    "time_zone": "00:00"
  }
  '