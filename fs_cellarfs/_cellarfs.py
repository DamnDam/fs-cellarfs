import six
from botocore.client import Config
import boto3
from fs_s3fs import S3FS

__all__ = ['CellarFS']

@six.python_2_unicode_compatible
class CellarFS(S3FS):
	@property
	def s3(self):
		if not hasattr(self._tlocal, 's3'):
			self._tlocal.s3 = boto3.resource(
				's3',
				region_name=self.region,
				aws_access_key_id=self.aws_access_key_id,
				aws_secret_access_key=self.aws_secret_access_key,
				aws_session_token=self.aws_session_token,
				endpoint_url=self.endpoint_url,
				config=Config(s3={'addressing_style': 'path'}, signature_version='s3')
			)
		return self._tlocal.s3

	@property
	def client(self):
		if not hasattr(self._tlocal, 'client'):
			self._tlocal.client = boto3.client(
				's3',
				region_name=self.region,
				aws_access_key_id=self.aws_access_key_id,
				aws_secret_access_key=self.aws_secret_access_key,
				aws_session_token=self.aws_session_token,
				endpoint_url=self.endpoint_url,
				config=Config(s3={'addressing_style': 'path'}, signature_version='s3')
			)
		return self._tlocal.client