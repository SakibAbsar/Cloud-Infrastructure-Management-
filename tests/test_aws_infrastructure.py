
import unittest
from terraform_validate import TerraformTest

class TestAWSInfrastructure(unittest.TestCase):
    def test_ec2_instance(self):
        tf = TerraformTest("../infrastructure/aws")
        tf.plan()
        tf.assert_resource_present("aws_instance", "web_server")

if __name__ == "__main__":
    unittest.main()
