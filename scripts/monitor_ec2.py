
import boto3
from datetime import datetime, timedelta

def monitor_ec2(instance_id):
    cloudwatch = boto3.client("cloudwatch", region_name="us-west-2")
    response = cloudwatch.get_metric_statistics(
        Namespace="AWS/EC2",
        MetricName="CPUUtilization",
        Dimensions=[{"Name": "InstanceId", "Value": instance_id}],
        StartTime=datetime.utcnow() - timedelta(minutes=10),
        EndTime=datetime.utcnow(),
        Period=60,
        Statistics=["Average"]
    )
    print("CPU Utilization:", response["Datapoints"])

if __name__ == "__main__":
    monitor_ec2("i-0abcd1234efgh5678")
