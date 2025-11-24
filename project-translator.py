# (ინგლისური → ქართული)
translit = {
    "a": "ა", "b": "ბ", "c": "ც", "d": "დ", "e": "ე",
    "f": "ფ", "g": "გ", "h": "ჰ", "i": "ი", "j": "ჯ",
    "k": "კ", "l": "ლ", "m": "მ", "n": "ნ", "o": "ო",
    "p": "პ", "q": "ქ", "r": "რ", "s": "ს", "t": "ტ",
    "u": "უ", "v": "ვ", "w": "ვ", "x": "ხ", "y": "ი", "z": "ზ",

    # დამატებითი კომბინაციები
    "sh": "შ",
    "ch": "ჩ",
    "kh": "ხ",
    "ts": "ც",
    "dz": "ძ",
    "tch": "ჭ",
    "zh": "ჟ"
}


def transliterate(text):
    text = text.lower()
    result = ""
    i = 0

    while i < len(text):
        # 3-ასოიანი კომბინაცია
        if i + 2 < len(text) and text[i:i+3] in translit:
            result += translit[text[i:i+3]]
            i += 3
        # 2-ასოიანი კომბინაცია
        elif i + 1 < len(text) and text[i:i+2] in translit:
            result += translit[text[i:i+2]]
            i += 2
        # ერთ ასოიანი
        elif text[i] in translit:
            result += translit[text[i]]
            i += 1
        else:
            result += text[i]  # უცნობი სიმბოლოს 그대로 დატოვება
            i += 1

    return result


word = input("Enter English text: ")
print("Georgian:", transliterate(word))
