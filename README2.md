# pyenv 3.7.9 #################################################################
```
pyenv install --list
pyenv install 3.7.9 (3.6.8)
pyenv versions
pyenv local 3.7.9 (3.6.8)
```

## Venv
python -m venv .rugpt3xl_env

.\.rugpt3xl_env\Scripts\activate.bat
-- vs
source ./.rugpt3xl_env/bin/activate

python -m pip install --upgrade pip

# Python packages

```
pip install torch==1.7.1+cu101 -f https://download.pytorch.org/whl/torch_stable.html
pip install torchvision==0.8.2+cu101 -f https://download.pytorch.org/whl/torch_stable.html
```

## apex for windows
```
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" git+https://github.com/xbodx/apex.git
```
## apex for linux
```
pip install -v --disable-pip-version-check --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" git+https://github.com/NVIDIA/apex.git
```
```
pip install nltk==3.5
pip install pandas==1.1.3
pip install sentencepiece==0.1.91
pip install tensorflow-gpu==2.3.0
pip install transformers==3.5.1
pip install deepspeed==0.3.11
```

# Python packages torch==1.5 (not work)
```
pip install torch==1.5.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
fix: copy \libs\pytorch_fix\1.5\*
```

# Python packages torch==1.6 (not work)
```
pip install torch==1.6.0+cu101 -f https://download.pytorch.org/whl/torch_stable.html
fix: copy \libs\pytorch_fix\1.6\*
```
