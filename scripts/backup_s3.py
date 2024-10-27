
import boto3

def backup_s3_bucket(source_bucket, destination_bucket):
    s3 = boto3.resource("s3")
    copy_source = {"Bucket": source_bucket, "Key": "file.txt"}
    bucket = s3.Bucket(destination_bucket)
    bucket.copy(copy_source, "file_backup.txt")
    print("Backup complete.")

if __name__ == "__main__":
    backup_s3_bucket("source-bucket", "backup-bucket")
