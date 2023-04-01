

text2 = "This is some other text."
text1 = "This is some other text.\r\nThis is a sample text.\r\nbbbbbbb\r\n"

# text1 = "This is some other aaa text.\r\nThis is a sample text.\r\nbbbbbbb\r\n"

def set_last_update_comment(self, before_text, after_text):
    import difflib
    d = difflib.Differ()
    diff = d.compare(text2.splitlines(), text1.splitlines())

    a = '\n'.join(diff)
    b = a.split('\n')

    res = []
    for data in b:
        print(data)
        if data[0:1] not in ['+', '-', '?']:
            res.append(data.replace('  ',''))
        elif data[0:1] in ['+','?']:
            res.append(data.replace('+ ','').replace('? ',''))
        else:
            pass
    res = '\n'.join(res)
    return res
