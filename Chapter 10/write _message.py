#Writing Multiple Lines
from pathlib import Path

contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('C:/Users/lesed/OneDrive/Documents/Code College/WEB BOOTCAMP/Python/MyWork/Source_Code/Chapter 10/programming.txt')
path.write_text(contents)

