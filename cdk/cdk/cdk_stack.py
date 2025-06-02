from aws_cdk import (
    # Duration,
    Stack, RemovalPolicy
    # aws_sqs as sqs,
)

from aws_cdk import aws_s3 as s3
from constructs import Construct

class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        # Create an S3 Bucket for storing assets or emails
        bucket = s3.Bucket(self, 
                           "AssetBucket", 
                           versioned=True,
                           removal_policy=RemovalPolicy.DESTROY)
        # example resource
        # queue = sqs.Queue(
        #     self, "CdkQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
    