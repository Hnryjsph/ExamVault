"""
Get all hosts for your organization returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi

configuration = Configuration()
configuration.api_key["apiKeyAuth"] = "671065161b04913c5b49a5f1c2ce8fc1"
configuration.api_key["appKeyAuth"] = "c3718836eb5f993d0173d3c0848baaea140a0cad"
configuration.server_variables["site"] = "datadoghq.com"

with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)


