from dotenv import load_dotenv
import os

# Caminho absoluto do .env na raiz
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
dotenv_path = os.path.join(base_dir, ".env")
load_dotenv(dotenv_path)


print("AWS_ACCESS_KEY_ID =", os.getenv("AWS_ACCESS_KEY_ID"))
print("AWS_SECRET_ACCESS_KEY =", os.getenv("AWS_SECRET_ACCESS_KEY"))
print("AWS_DEFAULT_REGION =", os.getenv("AWS_DEFAULT_REGION"))