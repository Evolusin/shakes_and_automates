import textract

from settings import Settings

config = Settings()
text = textract.process(f"misja_koniec.png")
print(text)
