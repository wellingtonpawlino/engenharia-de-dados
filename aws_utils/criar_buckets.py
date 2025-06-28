

import boto3
import os
from dotenv import load_dotenv

# 🔐 Carrega variáveis do .env
dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(dotenv_path)

# 🔎 Valida presença das variáveis
required_vars = ["AWS_ACCESS_KEY_ID", "AWS_SECRET_ACCESS_KEY", "AWS_DEFAULT_REGION"]
missing = [var for var in required_vars if os.getenv(var) is None]
if missing:
    raise EnvironmentError(f"Variáveis ausentes no .env: {', '.join(missing)}")

# 🌎 Região AWS
region = os.getenv("AWS_DEFAULT_REGION")

# 🪣 Nomes dos buckets
buckets = [
    "welldata-bronze",
    "welldata-silver",
    "welldata-gold"
]

# 💡 Cria cliente S3
s3 = boto3.client("s3", region_name=region)

# 🚀 Loop para criar buckets
for bucket in buckets:
    try:
        s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration={"LocationConstraint": region}
        )
        print(f"✅ Bucket '{bucket}' criado com sucesso.")
    except Exception as e:
        print(f"❌ Erro ao criar o bucket '{bucket}': {e}")