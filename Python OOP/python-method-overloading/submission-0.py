class TextProcessor:
    def format_text(self, text1, text2 = None):
        if text2 == None:
            return text1.upper()
        else:
            return text1 + text2


# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
