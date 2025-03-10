try:
    from book_search import BookSearch
except ImportError:
    import sys
    sys.path.insert(0, './path_to_book_search_directory')
    from book_search import BookSearch

if __name__ == "__main__":
    bot = BookSearch()
    bot.search_book("Git Pocket Guide")
    bot.close_browser()
