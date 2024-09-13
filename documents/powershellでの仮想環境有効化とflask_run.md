
# PowerShellでの仮想環境有効化とFlask起動
- スクリプトを実行するためのポリシー設定
  > powershell set-ExecutionPolicy RemoteSigned CurrentUser

- Falskサーバーのメインディレクトリへ移動
  > cd C:\Users\Yoshiro_Fujimoto\PycharmProjects\pythonProject

- 仮想環境の有効化
  > venv\Scripts\activate.ps1

- 仮想環境の無効化
  > deactivate

- Flaskの起動
  > flask run
  
