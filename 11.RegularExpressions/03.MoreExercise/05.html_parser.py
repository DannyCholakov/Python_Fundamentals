import re

def extract_title(html):
    title_pattern = r'<title>(.*?)</title>'
    match = re.search(title_pattern, html, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""

def extract_content(html):
    body_pattern = r'<body>(.*?)</body>'
    match = re.search(body_pattern, html, re.DOTALL)
    if match:
        body_content = match.group(1)
        content = re.sub(r'<.*?>', '', body_content)
        return re.sub(r'\s+', ' ', content).strip()
    return ""

html_input = input("Enter HTML content: ")

title = extract_title(html_input)
content = extract_content(html_input)

print(f"Title: {title}")
print(f"Content: {content}")
