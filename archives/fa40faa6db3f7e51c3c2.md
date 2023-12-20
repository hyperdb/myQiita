---
title: 【CodeIgniter】クラスを利用してフォームの値を自動で取得する
tags:
  - PHP
  - CodeIgniter
private: false
updated_at: '2016-09-21T17:17:33+09:00'
id: fa40faa6db3f7e51c3c2
organization_url_name: null
slide: false
ignorePublish: false
---
PHPのクラスでは宣言していないプロパティにも値を代入することができます。このことを利用すればフォームで送信した値を自動で取得するような仕組みを作ることが可能になります。

# 宣言を行わないプロパティの利用
## サンプルクラスの定義
librariesフォルダに以下のようなコンストラクタしか持たないクラスを定義してみます。

```php
class Dummy
{
    public function __construct($config = array())
    {
    }
}
```

## クラスを使ってみる
上記をクラスをインスタンス化して適当なプロパティ値を設定してブラウザで確認してみます。

```php
function sample_out()
{
    $_form = new Dummy();
    $_form->id = 12345;

    echo '$_form->id = '.$_form->id.'<br/>';
}
```
代入時点でもエラーになりませんし、ブラウザにも以下のように出力されます。

![2016-08-11_1407.png](https://qiita-image-store.s3.amazonaws.com/0/15750/d9c2aaf3-a297-0438-9c35-059e36139969.png)

先ほどのファンクションで宣言をせずに値も代入していないプロパティを出力するように修正してみると「**A PHP Error was encountered**」が表示されます。

```php
function sample_out()
{
    $_form = new Dummy();
    $_form->id = 12345;

    echo '$_form->id = '.$_form->id.'<br/>';
    echo '$_form->name = '.$_form->name.'<br/>';
}
```

![2016-08-11_1402.png](https://qiita-image-store.s3.amazonaws.com/0/15750/9378f0e8-a791-3967-5ab9-dd8ab7d71518.png)

# クラスを利用してフォームの値を取得する
## フォームの準備
以下のようなフォームを準備します。

```php:sample_form.php
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <title>サンプルフォーム</title>
</head>
<body>
  <div id="container">
    <form name="f" id="f" method="post" action="">
      TEXT_1 : <input type="text" name="_text_1" id="_text_1" value="" /><br/>
      TEXT_2 : <input type="text" name="_text_2" id="_text_2" value="" /><br/>
      TEXT_3 : <input type="text" name="_text_3" id="_text_3" value="" /><br/>
      <br/>
      <input type="submit" value="送信" /><br/>
    </form>
  </div>
</body>
</html>
```

## コントローラで表示
コントローラ内で上記のviewを表示します。

```php
function sample_out()
{
  $this->load->view("sample_form");
}
```

![2016-08-18_1350.png](https://qiita-image-store.s3.amazonaws.com/0/15750/b9452d02-9ef8-7a24-ad1a-baf7dc4e4b48.png)

## クラスを準備
一応フォームが表示されるようになったので、フォーム処理用のクラスを作成し、先ほどのクラスでインスタンス化してみます。

```php:SampleForm.php
class SampleForm
{
  protected $_CI;

  public function __construct($config = array())
  {
    $this->_CI =& get_instance();
    $this->set_post();
  }

  public function set_post()
  {
    $post_param = $this->_CI->input->post();

    if($post_param && count($post_param) > 0)
    {
      foreach($post_param as $key => $value)
      {
        $this->{$key} = $value;
      }
    }
    return $this;
  }
}
```

先ほどのファンクションを修正します。併せて、フォーム上の３つの変数を画面出力してみます。

```php
function sample_out()
{
  class_exists('SampleForm') OR require APPPATH.'libraries/SampleForm.php';

  $_form = new SampleForm();

  if(isset($_form->_text_1))	echo $_form->_text_1.'<br/>';
  if(isset($_form->_text_2))	echo $_form->_text_2.'<br/>';
  if(isset($_form->_text_3))	echo $_form->_text_3.'<br/>';

  $this->load->view("sample_form");
}
```

## フォームを送信

初期表示では先ほどと同じですので、ここで各項目に値を入力して送信ボタンを押下してみます。

![2016-08-18_1422.png](https://qiita-image-store.s3.amazonaws.com/0/15750/970abfda-9d0c-8bee-645c-a9ed8d8f7620.png)


## フォーム送信結果

送信後はプロパティが参照可能になりますので、以下のように表示されるようになります(上３行が取得されたフォーム値)。

![2016-08-18_1423.png](https://qiita-image-store.s3.amazonaws.com/0/15750/077114ed-1c59-71b1-a344-74501ec8802c.png)

# 最後に

このようにフォームの変数用のプロパティを事前に宣言することなく、フォームの値を取得することができました。このクラスのオブジェクトでviewの中の変数を置き換えるようにすれば初期表示やエラー時の再表示なども簡単にできるかもしれません(以下のようなメソッドを用意しておく必要はあるかもしれませんが・・・)。

```php
public function getValue($_key)
{
    return isset($this->{$_key}) ? $this->{$_key} : '';
}
```
