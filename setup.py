from setuptools import setup

install_reuires=['llama-cpp-python==0.2.6',"tqdm==4.6.61","requests","playsound","sentencepiece","tiktoken","speechbrain","sounddevice","holidays","GitPython","transformers==4.31.0","botocore","pyAudioAnalysis==0.3.5","soundfile","torch==1.12.1","huggingsound","numpy==1.24","pydub","torchaudio==0.12.1","Pyaudio","textblob","pvporcupine"]
setup(
    name='MINIbot_7',
    version='0.0.1',
    packages=install_reuires,
    license='',
    author='Dawood Thouseef',
    author_email='tdawood140@gmail.com',
    description="It's a chatbot made using llama2 model"
)
