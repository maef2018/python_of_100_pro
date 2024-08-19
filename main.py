# day 82 使用所学知识创建一个基于文本（命令行）的程序，该**程序接受任何字符串输入并将其转换为摩尔斯电码**

# 将用户输入的数据转换为Morse code 摩尔斯电码

# Define a dictionary for Morse code representation
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
    '(': '-.--.', ')': '-.--.-', ' ': '/'
}


def text_to_code(text):
    """接受字符串并将字符串转换为摩尔斯电码，返回值是摩尔斯电码"""
    text = text.upper()

    # 将字符转换为摩尔斯码
    text_to_morse_code = [MORSE_CODE_DICT.get(char, '') for char in text]

    # 返回一个字符串，所以用到字符串拼接,字符之间用空格分隔
    return ' '.join(text_to_morse_code)


def main():
    """将用户输入字符串转换为摩尔斯码并作为返回值返回"""
    # 接收用户输入字符串
    user_input = input("Please input a string to convert to Morse code: ")

    # 将输入转换为摩尔斯码
    morse_code_output = text_to_code(user_input)

    # 将摩尔斯码作为返回值返回
    return morse_code_output


if __name__ == "__main__":
    morse_code = main()
    print(f"Morse Code is: {morse_code}")
