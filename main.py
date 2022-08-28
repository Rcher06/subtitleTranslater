from deep_translator import GoogleTranslator

name = input("Subtitle File Name: ")
target = input("Target Language: ")
colorCode = input("Hex Color Code(default=yellow[#ffff54]): ")
if len(colorCode) == 0:
    colorCode = "#ffff54"
string = ""
translator = GoogleTranslator(source="auto", target=target)

def progressBar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.0f}% {progress}/{total}", end="\r")

def setQuote(str:str) -> str:
    l = str.split("\n\n")
    lenght = len(l)
    for index,i in enumerate(l):
        try:
            a = i.split("\n")
            fst = a.pop(0)
            sec = a.pop(0)
            for ind,k in enumerate(a):
                a[ind] = k + "\n" + f'<font color={colorCode}>' + translator.translate(k) + "</font>"
            b = [fst, sec]
            b += a
            b = "\n".join(b)
            l[index] = b
        except Exception as e:
            print(e)
        
        #print(index)
        progressBar(index, lenght)
    res = "\n\n".join(l)
    return res

with open("./" + name, "r") as f:
    string = f.read()
    string = setQuote(string)

with open("./" + f"translatedTo({target})_" + name, "w", encoding="utf-8") as f:
    f.write(string)
