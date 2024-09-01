import boto3
from botocore.exceptions import NoCredentialsError

# Configura tu cliente S3
s3 = boto3.client('s3', aws_access_key_id='AKIAXKPUZMWN5WZNBTE2',
                  aws_secret_access_key='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')

def upload_file_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"Archivo {file_name} subido a {bucket}/{object_name}")
    except NoCredentialsError:
        print("Credenciales no encontradas.")

def generate_presigned_url(bucket, object_name, expiration=3600):
    try:
        response = s3.generate_presigned_url('get_object',
                                             Params={'Bucket': bucket,
                                                     'Key': object_name},
                                             ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return None
    return response

# Ejemplo de uso
fileName= 'test.pdf'
bucketName= 'bim-data-storage'
upload_file_to_s3(fileName, bucketName)
url = generate_presigned_url(bucketName, fileName)
print(f"Enlace de descarga: https://bim-data-storage.s3.us-east-2.amazonaws.com/{fileName}")
