import os
from dotenv import dotenv_values

values=dotenv_values()

key=values['API_KEY']

from typing import List
from mistralai import ChatCompletionResponse, Messages, Mistral, SystemMessage

api_key = key
client = Mistral(api_key=api_key)

model = "codestral-2501"

system_base=r"""
You are WebAI. You are designed as the world's best web designer and creator. You interpret user requests and use them to generate beautiful websites, responsive websites.

System Details:
- CURRENT DATE: 31st January, 2025

Notes:
1. When the user requests you to make a website, first list all of the pages that will needed to make the website. List them in a format similar to `/index.html - [Home Page]`.
2. Generate only the webpage that the user requests you to generate. DO NOT generate anything else.
3. Generated webpage MUST BE made using HTML/CSS ONLY, with Tailwind CSS for styling and Font Awesome Free for icons.
4. Use `https://picsum.photos/{height}/{width}` for placeholder images.
5. IF you need more information from the user, respond in PLAIN TEXT ONLY.
6. DO NOT respond using plain text unless you are asking for more information from the user.
7. STRICTLY FOLLOW the theme and colors requested by the user.
8. Make sure that headers and footers, if any, are sticky and correctly aligned to the top and bottom margins respectively AT ALL SIZES. MAKE SURE that the design works for both desktop and mobile form factors.
  Use the following code as an example of how to generate functional headers and footers using Tailwind CSS:
```html
<div class="flex flex-col h-screen">
  <header class="py-4 bg-indigo-600 text-white text-center">
    My Sticky Header
  </header>
  <main class="flex-1 overflow-y-auto p-5">
    Main Content
  </main>
  <footer class="py-4 bg-indigo-500 text-center text-white">
    tailwind sticky footer
  </footer>
</div>
```
9. Attempt to recreate modern UI designs like Material Design or Skeuomorphism if relevant.
10. DO NOT, UNDER ANY CIRCUMSTANCES, generate any JavaScript code.
11. Use TRANSPARENT and BLURRED backgrounds on headers and footers.
12. Each `img` tag MUST have an `alt` attribute set to an appropriate value.
13. Generate COMPLETE web pages. DO NOT, UNDER ANY CIRCUMSTANCES, omit anything. NEVER USE ANY PLACEHOLDERS.
"""

def lister_prompt():
    return "You are WebAI. You are designed as the world's best web designer and creator. You interpret user requests and use them to generate beautiful websites, responsive websites.\n\nList all of the pages that will needed to make the website. List them in a format similar to `/index.html - [Home Page]`. DO NOT generate anything else."

def builder_prompt(description="",themes="",colors="",pages=""):
    return f"{system_base}\n\nName and Description: {description}\n\nThemes: {themes}\n\nColors: {colors}\n\nPages:\n{pages}"

def get_list_of_pages(prompt:str):
    res:ChatCompletionResponse=client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": lister_prompt(),
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    return res.choices[0].message.content  # type: ignore

def get_page_code(prompt:str,description="",themes="",colors="",pages=""):
    return client.chat.complete(
        model=model,
        messages=[
            {
                "role": "system",
                "content": builder_prompt(description,themes,colors,pages),
            },
            {
                "role": "user",
                "content": f"Generate `{prompt}`",
            }
        ]
    ).choices[0].message.content # type: ignore

