
resource "aws_s3_bucket" "bucket" {
  bucket = "my-cloud-bucket"
  versioning {
    enabled = true
  }

  lifecycle_rule {
    enabled = true
    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }
  }
}
