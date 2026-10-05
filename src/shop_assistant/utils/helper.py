from IPython.display import display, Markdown


def rtl_print(text, box=False):
    styles = ""

    if box:
        styles = "border:1px solid #ccc; padding:3px;"
    display(
        Markdown(
            f'<span style="direction: rtl; display: block; text-align: right;{styles}">{text}</span>'
        )
    )
