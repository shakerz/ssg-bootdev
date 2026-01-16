# This is a sample Python script.
from inline_markdown import split_nodes_delimiter
from extract_markdown import extract_markdown_images, extract_markdown_links
from textnode import TextNode,TextType


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
   node = TextNode("This is text with a `code block` word", TextType.TEXT)
   node2 = TextNode("This is text with a **bolded phrase** in the middle", TextType.BOLD)

   new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
   print(f"new_nodes {new_nodes}")

   text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
   print(extract_markdown_images(text))

   text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
   print(extract_markdown_links(text))


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
