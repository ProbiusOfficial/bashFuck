## **关于**

针对Linux终端的无字母命令执行的骚操作x

Idea来源于[CTFshow](https://www.ctf.show/)周末的极限挑战赛

(后面不定期有各种有意思的挑战赛哦~欢迎各位师傅来平台玩呀)

## **Wiki**

整个项目的核心是 Linux终端可以通过 `$'\xxx'` 的方式执行命令，xxx是字符ascii码的八进制形式，通过这一点，我们可以通过位运算符号和Linux终端的其他特性，在没有数字的情况下继续构造这样的形式以实现无字母数字仅用几个字符就实现任意命令执行。

当然本项目也有一定局限性，这取决于linux的系别，因为在debian系操作系统中，sh指向dash；在centos系操作系统中，sh指向bash。

笔者会在后面完善这个wiki，更细致的讲解构造的原理。

## **Usage**

使用python3运行bashFuck.py文件即可，根据提示输入你的命令，程序会自动为你生成从最基本的`$'\xxx'`形式到更复杂的形式。

```Bash
python bashFuck.py
```

![image-20230303214213304](https://nssctf.wdf.ink//img/WDTJ/202303032142258.png)

![image-20230303214251065](https://nssctf.wdf.ink//img/WDTJ/202303032142995.png)

效果展示：

![image-20230303214530937](https://nssctf.wdf.ink//img/WDTJ/202303032145972.png)

