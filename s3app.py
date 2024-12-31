import boto3

app = Flask(_name_)
s3 = boto3.client('s3')
BUCKET_NAME = 'list-bucket-content-demo'

@app.route('/list-bucket-content/<path:subpath>', methods=['GET'])
@app.route('/list-bucket-content', defaults={'subpath': ''}, methods=['GET'])
def list_bucket_content(subpath):
  prefix = subpath.strip('/') + '/' if subpath else ''
  response = s3.list_objects_v2(Bucket=BUCKET_NAME, Prefix=prefix, Delimiter='/')

  contents = []
  if 'CommonPrefixes' in response:
      contents.extend([cp['Prefix'].rstrip('/') for cp in response['CommonPrefixes']])
  if 'Contents' in response:
      contents.extend([obj['Key'].replace(prefix, '') for obj in response['Contents'] if obj['Key'] != prefix])

  return jsonify({'content': contents})

if _name_ == '_main_':
  app.run(host='0.0.0.0', port=5000)