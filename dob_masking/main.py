import boto3
from functions.dob_masking import dob_mask


def main():
    # initialize variables for connecting to s3
    access_key_id = 'AKIAVQHTBMWHQHU3CZ7V'
    secret_access_key = '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'
    bucket_name = 'stellar-tht-candidates'

    # create s3 client
    s3 = boto3.client('s3', aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

    # list all objects in case there is more than one log file
    response = s3.list_objects(Bucket=bucket_name)
    for obj in response.get('Contents', []):  # loop through the contents to get all file keys in bucket
        log_response = s3.get_object(Bucket=bucket_name, Key=obj['Key'])
        log_file = log_response['Body'].read().decode('utf-8')
        lines = log_file.splitlines()
        masked_lines = []
        for line in lines:
            masked_line = dob_mask(line)
            masked_lines.append(masked_line)
        masked_log_file = '\n'.join(masked_lines)

    with open('/Users/ijeffries/PyCharmProjects/stellarhealth-take-home/dob_masking/masked_logs.txt', 'w') as file:
        file.write(masked_log_file)


if __name__ == "__main__":
    main()