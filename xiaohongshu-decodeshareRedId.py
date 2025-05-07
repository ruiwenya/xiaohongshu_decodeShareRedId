import base64

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

def decode_share_red_id(encoded_str):
    if not encoded_str:
        return ""

    # Step 1: URL Safe 字符还原
    padded_str = encoded_str.replace('-', '+').replace('_', '/')
    # 补全 Base64 填充符
    padding = '=' * ((4 - (len(padded_str) % 4)) % 4)
    padded_str += padding

    try:
        # Step 2: Base64 解码
        decoded_bytes = base64.b64decode(padded_str)
        decoded_str = decoded_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Base64解码失败: {e}")

    # Step 3: 自定义字符减法
    key = "262035496752980663974569"
    result_chars = []
    
    for i, char in enumerate(decoded_str):
        key_digit = int(key[i % len(key)])
        subtracted = ord(char) - key_digit
        
        # 防止负值导致非法字符
        if subtracted < 0:
            raise ValueError(f"字符减法溢出: {char}({ord(char)}) - {key_digit} < 0")
            
        result_chars.append(chr(subtracted))

    # Step 4: 转换为小写输出
    return ''.join(result_chars).lower()

# test
encodedid = "ODs0MDQ5Rjw2NzUyOTgwNjg3OTg5S0hO"
rawid = "652014b30000000024015fbe"
print(encode_share_red_id(rawid))
print(decode_share_red_id(encodedid))
