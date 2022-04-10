# 牛弟弟
<img src="https://cdn.discordapp.com/attachments/858984158620286998/959774538902695956/unknown.png"/>

> :copyright: Cow Didi By CowTeam 2022

目前進度： **`25%`**

牛弟弟 - 簡易，輕鬆，免費。

## 作者們
- AWeirdScratcher (Python)
- CharlieMoomoo (Javscript)
- Apple Inc. (Javascript)


## 該從哪裡著手？
我們使用的語言為 [Python](https://python.org/)，記得先安裝~
接著，`git clone https://github.com/LittleCow-moo/didi.git` 這個專案。
```py
>>> git clone https://github.com/LittleCow-moo/didi.git

# Cloning into 'didi'...
[remote]: Enumerating objects: 23, done.
[remote]: Counting objects: 100% (23/23), done.
[remote]: Compressing objects: 100% (20/20), done.
[remote]: Total 23 (delta 2), reused 0 (delta 0), pack-reused 0
# Receiving objects: 100% (23/23), 11.36 KiB | 1.62 MiB/s, done.
# Resolving deltas: 100% (2/2), done.
[Sucess] 100%
```
然後，你就可以開始編輯了！

## 甚麼是 `os.environ`？
我們使用 `os.environ` 來隱藏重要的資訊。例如：
```py
client.run(os.environ['token']) # 看不見 token
```

若直接執行程式，會顯示 `KeyError`。

```py
KeyError # 代表裡面沒有此值!
```
請將 `os.environ...` 移掉，改成你想要的 `String` 值。

```py
client.run("My Var")
```

這樣就好了!

<div align="center">
  <blockquote>下一篇： 使用 Javascript 畫龍點睛</blockquote>
</div>
