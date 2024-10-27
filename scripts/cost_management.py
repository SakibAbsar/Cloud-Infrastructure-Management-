
import boto3

def get_costs():
    client = boto3.client("ce", region_name="us-east-1")
    response = client.get_cost_and_usage(
        TimePeriod={"Start": "2023-01-01", "End": "2023-01-31"},
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )
    print(response["ResultsByTime"])

if __name__ == "__main__":
    get_costs()
