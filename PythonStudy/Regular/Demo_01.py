import re


def test01_verify_account():
    # verify if the input QQ account is valid
    # 要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
    # QQ号是5~12的数字且首位不能为0
    username = input('input username:')
    qq = input('input qq:')

    p1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)
    if not p1:
        print('please input valid username!')

    p2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not p2:
        print('please input valid qq')
    if p1 and p2:
        print('u r right!')


def test02_extract_phonenumber():
    # 从一串文字中提取手机号码
    # 使用前瞻和后顾保证手机号前后不该出现数字
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    # res_list = re.findall(pattern, sentence)
    res_list = pattern.findall(sentence)
    print(res_list)
    print('------------分割线-------------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('------------分割线-------------')
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def test03_substitute():
    sentence = '你是傻逼吗?我操你大爷的.Fuck you.'
    subs = '[操肏艹]|fuck|shit|傻[比逼叉缺吊屌]|煞笔'
    # 用❤代替上面出现的字符, re.IGNORECASE->大小写不敏感
    purified = re.sub(subs, '❤️‍', sentence, flags=re.IGNORECASE)
    print(purified)

def test04_split_longString():
    poem = '床前明月光，疑是地上霜，举头望明月，低头思故乡'
    sentence_list = re.split(r'[，。,.]', poem)
    print(sentence_list)


# test01_verify_account()
# test02_extract_phonenumber()
# test03_substitute()
# test04_split_longString()
