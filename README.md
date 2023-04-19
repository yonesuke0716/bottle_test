# bottle_test

## 仮想環境の構築手順
### pyenv, pyenv-virtualenvのインストール
```
brew install pyenv pyenv-virtualenv
```
パスを通す
```
echo 'export PYENV_ROOT="${HOME}/.pyenv"' >> ~/.bash_profile
echo 'export PATH="${PYENV_ROOT}/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
source ~/.bash_profile
```

### 仮想環境の構築
```
pyenv install 3.11.3
```
できたか確認(3.11.3があればOK)
```
pyenv versions
```
Python3.11.3の下にvirtualenvを作成
```
pyenv virtualenv 3.11.3 bottle_test
```
仮想環境を切り替える
```
pyenv global bottle_test
```
先頭に(bottle_test)と出ればOK

仮想環境を終了するとき
```
pyenv global system
```

仮想環境を削除するとき
```
pyenv uninstall hoge
```

## ライブラリのインストール
```
pip3 install --no-cache-dir -r requirements.txt
```

## 実行方法
python3 app.py
