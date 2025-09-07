## 相关配置
* ### package.json
```javascript
{
  "dependencies": {
    "jsdom": "^26.1.0",
    "node-fetch": "^3.3.2",
    "xmlhttprequest": "^1.8.0"
  },
  "type": "commonjs" //必须设置
}
```
* ### cookie  st  rsa_key 这三个变量的值需要替换
![](https://raw.githubusercontent.com/truefalsehello/jd_captcha_auto/refs/heads/main/1.jpg)
![](https://raw.githubusercontent.com/truefalsehello/jd_captcha_auto/refs/heads/main/3.jpg)
![](https://raw.githubusercontent.com/truefalsehello/jd_captcha_auto/refs/heads/main/4.jpg)
* #### https://curlconverter.com/node-fetch/
![](https://raw.githubusercontent.com/truefalsehello/jd_captcha_auto/refs/heads/main/5.jpg)
![](https://raw.githubusercontent.com/truefalsehello/jd_captcha_auto/refs/heads/main/2.jpg)
* ### 先执行
```bash
python .\jd.py
```

* #### 然后执行
```bash
node .\jingdong.js
