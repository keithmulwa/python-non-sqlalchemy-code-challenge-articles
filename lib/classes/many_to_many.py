# classes/many_to_many.py

class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        pass  # immutable

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        mags = [article.magazine for article in self.articles()]
        return list(dict.fromkeys(mags))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        topics = [article.magazine.category for article in self.articles()]
        if not topics:
            return None
        return list(dict.fromkeys(topics))


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be string of length 2-16")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        authors = [article.author for article in self.articles()]
        return list(dict.fromkeys(authors)) if authors else []

    def article_titles(self):
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        authors = self.contributors()
        result = [
            author
            for author in authors
            if len([a for a in Article.all if a.author == author and a.magazine == self]) > 2
        ]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not cls.all or not Article.all:
            return None
        counts = {mag: len(mag.articles()) for mag in cls.all}
        top = max(counts, key=counts.get)
        return top


class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be string 5-50 chars")
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise ValueError("Author and Magazine must be proper instances")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        pass  # immutable
