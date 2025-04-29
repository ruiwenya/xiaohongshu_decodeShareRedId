import base64

def decode_share_red_id(encoded_str):
    # Step 1: Base64 解码
    decoded_bytes = base64.b64decode(encoded_str)
    decoded_str = decoded_bytes.decode('utf-8')

    # Step 2: 自定义字符减法
    key = "262035496752980663974569"
    result = []
    for i, char in enumerate(decoded_str):
        offset = int(key[i % len(key)])
        result.append(chr(ord(char) - offset))

    # Step 3: 转换为小写
    return ''.join(result).lower()

def encode_share_red_id(original):
    if not original:
        return ""

    key = "262035496752980663974569"
    key_len = len(key)

    # Step 1: 转化为大写
    original_upper = original.upper()

    # Step 2: 自定义字符加法
    added_chars = []
    for i, ch in enumerate(original_upper):
        digit = int(key[i % key_len])
        added = chr(ord(ch) + digit)
        added_chars.append(added)

    added_str = ''.join(added_chars)

    # Step 3: Base64编码
    encoded_bytes = base64.b64encode(added_str.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')

    # Replace '+' -> '-', '/' -> '_' and strip padding '='
    encoded_url_safe = encoded_str.replace('+', '-').replace('/', '_').rstrip('=')

    return encoded_url_safe

# test
encodedid = "ODs0MDQ5Rjw2NzUyOTgwNjg3OTg5S0hO"
rawid = "652014b30000000024015fbe"
print(encode_share_red_id(rawid))
print(decode_share_red_id(encodedid))