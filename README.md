# reverse-proxy-sample

NGINXのリバースプロキシ機能を試しました。
ホスト上にNGINXサーバーと転送先であるFlaskサーバーとPythonのWEBサーバーの3サーバーが起動している構成です。
確認手順は以下のとおりです。
- ```docker-compose up --build```で起動します。
- WEBブラウザから[http://localhost/](http://localhost/)にアクセスするとNGINXのトップページが表示されます。
- WEBブラウザから[http://flask.localhost/](http://flask.localhost/)にアクセスするとFlaskのトップページが表示されます。
- WEBブラウザから[http://foo.localhost/](http://foo.localhost/)にアクセスするとPythonWEBサーバーのトップページが表示されます。なお、fooは任意の文字列です。
