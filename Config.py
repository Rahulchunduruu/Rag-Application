import os
from dotenv import load_dotenv


load_dotenv()
class config:
        Grok_api=os.getenv('grok_api')
        Hugging_face_api=os.getenv('hugging_face_api')
        OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
        vector_store_path=os.getenv('vector_store_path')