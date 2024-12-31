# httpservice -terraform

Directories: In Amazon S3, directories are represented as prefixes in object keys. For example, an object with the key dir1/ represents a directory named dir1. When listing objects with a delimiter (typically /), S3 groups objects that share the same prefix up to the first occurrence of the delimiter, effectively simulating a directory structure.
    AWS Documentation

Files: Files are represented by their object keys without a trailing delimiter. For instance, file1.txt is a file at the top level of the bucket.
 
 # How the Service Works:

    Listing Top-Level Contents: When the endpoint /list-bucket-content is accessed without a specified path, the service lists all objects at the top level of the S3 bucket. It uses the delimiter / to group objects by their prefixes, identifying directories and files.
    Listing Contents of a Specific Directory: When a path is specified (e.g., /list-bucket-content/dir1), the service lists all objects under that prefix. It again uses the delimiter / to group objects, effectively listing the contents of the specified directory.



1. Launch an EC2 Instance
    Create an EC2 instance with a suitable AMI (e.g., Ubuntu 20.04).
    Ensure it has an appropriate security group with necessary inbound and outbound rules.
    install sudo apt install python3-pip -y
    pip install flask boto3
    create s3-app.py file
 
 2. Attach an IAM Role to EC2

    Create an IAM Role with the AmazonS3FullAccess policy.
    Attach this role to the EC2 instance.

3. Configure AWS CLI
Log in to the EC2 instance via SSH.
Run the following command to configure AWS CLI:
aws configure

4. Create S3 bucket And give Policy

    "Version": "2012-10-17",
    "Id": "Policy1735567338835",
    "Statement": [
        {
            "Sid": "Stmt1735567337153",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::taskwalibucket/*"
        }
    ]
}
