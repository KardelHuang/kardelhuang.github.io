text = " Name: Kardel, Score: 100 \n"
dict = {}
words = text.strip().split(", ")
for word in words:
    dict.update({word.split(": ")[0]: word.split(": ")[1]})

print(dict)

def clean_text(text: str):
    clean_list = [word.strip() for word in text.split(" ") if word]
    return " ".join(clean_list)

print(clean_text("a bb ccc   dd \ne  \nf  g"))
