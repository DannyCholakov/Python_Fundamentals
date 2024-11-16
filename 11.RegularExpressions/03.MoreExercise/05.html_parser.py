import re

def html_parser():
    html_input = input()

    title_pattern = r"<title>(.*?)</title>"
    title_match = re.search(title_pattern, html_input)
    title = title_match.group(1) if title_match else "No title"

    body_pattern = r"<body>(.*?)</body>"
    body_match = re.search(body_pattern, html_input, re.DOTALL)
    body_content = body_match.group(1) if body_match else ""

    content = re.sub(r"<.*?>", "", body_content)
    content = re.sub(r"\s+", " ", content).strip()

    print(f"Title: {title}")
    print(f"Content: {content}")

html_parser()
