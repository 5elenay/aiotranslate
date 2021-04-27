import aiohttp, time
from bs4 import BeautifulSoup

class Translator:
    def __init__(self, session = aiohttp.ClientSession(), save_translates: bool = False):
        self.__memory = []
        self.__session = session
        self.__add_to_memory = save_translates

    def __raise_error(value: str, argument_name: str, check: type):
        if not isinstance(value, check):
            raise TypeError(f"Argument '{argument_name}' type must be {type(check).__name__}, not {type(value).__name__}.")

    async def translate(self, text: str, language_to: str, language_from: str):
        Translator.__raise_error(text, "text", str)
        Translator.__raise_error(language_to, "to", str)
        Translator.__raise_error(language_from, "from", str)

        async with self.__session as session:
            async with session.get(f'https://translate.google.com/m?tl={language_to}&sl={language_from}&q={text}') as response:
                result = await response.text()
                source = BeautifulSoup(result, "html.parser")
                
                translated = source.find("div", attrs={ "class": "result-container" }).text
                
                if self.__add_to_memory:
                    self.__memory.append({
                        "time": time.time(),
                        "to": language_to,
                        "from": language_from,
                        "text": text,
                        "translated": translated,
                    })

                return translated

    def history(self):
        return self.__memory
