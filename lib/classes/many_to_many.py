class Article:
    # Initializing an empty list to store all article instances.
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
    # Appending the new article instance to the all list.
        Article.all.append(self)
    # Defining the title property to return the title of the article.
    @property
    def title(self):
        return self._title
# Assigning of a new title value with constraints.
    @title.setter
    def title(self, new_title):
        if hasattr(self, 'title'):
            AttributeError('Title cannot be changed')
        if isinstance(new_title, str) and 5 <= len(new_title) <= 50:
            self._title = new_title
        else:
            ValueError('Title must be a string between 5 and 50 characters')
# Defining the author property to return the author of the article.
    @property
    def author(self):
        return self._author
# Assigning of a new author value with constraints.
    @author.setter
    def author(self, new_author):
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            raise TypeError("Author must be an instance of Author")
# Defining the magazine property to return the magazine of the article.
    @property
    def magazine(self):
        return self._magazine
# Allowing assignment of a new magazine value with constraints.    
    @magazine.setter
    def magazine(self, new_magazine):
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            raise TypeError("Magazine must be an instance of Magazine")


class Author:
    def __init__(self, name):
# Initializing the author with a name.
        self.name = name
# Defining the name property to return the author's name.
    @property
    def name(self):
        return self._name
# Allowing assignment of a new name value with constraints.
    @name.setter
    def name(self, new_name):
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    ValueError("Name must be longer than 0 characters")
            else:
                TypeError("Name must be a string")

    def articles(self):
        return [article for article in Article.all if self == article.author]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = list({magazine.category for magazine in self.magazines()})
        return areas if areas else None


class Magazine:
    def __init__(self, name, category):
    # Initializing the magazine with a name and a category. 
        self.name = name
        self.category = category
# Defining the name property to return the magazine's name.
    @property
    def name(self):
        return self._name
# Allowing assignment of a new name value with constraints.
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            ValueError("Name must be a string between 2 and 16 characters")
# Defining the category property to return the magazine's category.
    @property
    def category(self):
        return self._category
# Allowing assignment of a new category value with constraints.
    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            ValueError("Category must be a non-empty string")

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        article_titles = [article.title for article in self.articles()]
        return article_titles if article_titles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author_counts[article.author] = author_counts.get(article.author, 0) + 1

        return [author for author, count in author_counts.items() if count >= 2] or None
