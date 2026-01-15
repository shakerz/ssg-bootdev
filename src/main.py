# This is a sample Python script.
from textnode import TextNode,TextType


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
   node =  TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
   print(node)


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
