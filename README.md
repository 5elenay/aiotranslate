# aiotranslate
Free google translate module that uses async/await syntax.

# Example 
```py
from aiotranslate import Translator
import asyncio

async def main():
    translator = Translator() 

    # you can add aiohttp session if you want like -> Translator(session=aiohttp.ClientSession())
    # also you can save the translates like -> Translator(save_translates=True)
    
    translated = await translator.translate("hello", "tr", "en")

    # first argument: the text will be translated
    # second argument: the language will converted
    # last argument: the language that text

    print(translated) # -> Merhaba
    print(translator.history()) # shows all translates that saved.

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
```