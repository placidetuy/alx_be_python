class Book:
    def __init__(self, title, author, year):
        # Constructor: Initializes the title, author, and year
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor: Prints a message when the object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String Representation: Returns a human-readable string
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official Representation: Returns a string that recreates the object
        return f"Book('{self.title}', '{self.author}', {self.year})"

