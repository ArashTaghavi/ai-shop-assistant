from IPython.display import display, HTML


def rtl_print(text, box=False, title: str | None = None):
    styles = ""

    if box:
        styles = "border:1px solid #ccc; padding:10px;"

    title_html = ""

    if title:
        title_html = f"""
        <link href="https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css"
          rel="stylesheet">
        <div style="font-weight:bold; margin-bottom:8px;font-family:'Vazirmatn', sans-serif;">
            {title}
        </div>
        """

    display(HTML(f"""
            <div style="direction:rtl; text-align:right; {styles} font-family:'Vazirmatn', sans-serif;">
                {title_html}
                <div>{text}</div>
            </div>
            """))
