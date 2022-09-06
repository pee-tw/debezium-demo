# Debezium Demo
This is a WIP repo to show the capabilities of CDC

# Installing Poetry
```sh
brew install pipx
pipx ensurepath
pipx install poetry
```

# To run the demo stack
`make init-cluster`
Wait until Kafka Connect container becomes ready ~2 minutes. Then, test with `add_connector.http`, if GET requests returns empty array. Then, proceed to POST to register the connector. Get request should now return `"inventory-connector"` now. Proceed to run `python stream.py` and make changes to customers table to see change stream.
