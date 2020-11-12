from scrapy import Selector


class ContentGetter:
    def __init__(self, fields: str, key: str, value: str, titles: list, to_null: list):
        self.fields = fields
        self.key = key
        self.value = value
        self.titles = titles
        self.to_null = to_null

    def get_title(self, content: Selector):
        for title in self.titles:
            response = content.xpath(title).get()
            if response:
                return response.lower().strip().replace(' ', '_')
        return None

    def get_information(self, content: Selector) -> dict:
        """
        Функция собирает все ключи и знанчение по заданному селектору
        :param content:
        :return:
        """
        response = {}

        for field in content.xpath(self.fields):
            key = self._get_key(field)
            value = self._get_value(field)
            response[key] = value

        return response

    def _get_key(self, field: Selector) -> str:
        """
        Из filed селектора возвращает ключ по заданному self.key пути
        :param field:
        :return:
        """
        return field.xpath(self.key).get().lower().strip().replace(' ', '_').replace(':', '')

    def _get_value(self, field: Selector):
        """
        Из filed селектора возвращает значение по заданному self.value пути
        :param field:
        :return:
        """
        value = field.xpath(self.value).getall()
        value = self.format_list(value)

        if len(value) == 1:
            return value[0]
        return value if len(value) > 1 else None


    def format_list(self, ls: list) -> list:
        """
        Функция удаляет лидирующие и замыкающие пробелы, а так-же строки, которые находяся в to_null превращает в None
        во всем списке
        :param ls:
        :return:
        """
        for i in range(len(ls)):
            try:
                ls[i] = ls[i].strip()
            except AttributeError:
                # Текущий элемент списка не строка
                continue
            if ls[i] in self.to_null:
                ls[i] = None
        return ls
