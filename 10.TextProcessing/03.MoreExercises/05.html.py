def generate_html():
    title = input()
    content = input()
    comments = []

    while True:
        comment = input()
        if comment == "end of comments":
            break
        comments.append(comment)

    html_output = []
    html_output.append(f"<h1>\n    {title}\n</h1>")
    html_output.append(f"<article>\n    {content}\n</article>")

    for comment in comments:
        html_output.append(f"<div>\n    {comment}\n</div>")

    for line in html_output:
        print(line)


generate_html()
