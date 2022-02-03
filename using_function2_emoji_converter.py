print("Welcome To The Emoji Converter")
def emoji_converter(a):
    emoji={
        "happy":"😄",
        "blushing":"😊",
        "sad":"😔"
    }

    print(emoji[a])
a= (input("enter your mood:")).lower()
emoji_converter(a)