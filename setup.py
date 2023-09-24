from setuptools import setup

install_reuires=['llama-cpp-python==0.2.6',"tqdm==4.6.61","requests","playsound","sentencepiece","tiktoken","GitPython","transformers==4.31.0"]
setup(
    name='MINIbot_7',
    version='0.0.1',
    packages=install_reuires,
    license='',
    author='Dawood Thouseef',
    author_email='tdawood140@gmail.com',
    description="It's a chatbot made using llama2 model"
)
