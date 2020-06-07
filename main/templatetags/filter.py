from django import template
import re
register = template.Library()

# 本文中の<h2>から目次を生成
@register.filter
def index(text):
    pattern = r"<h2>(.*)</h2>"
    h2_list = re.findall(pattern, text)
    result = ""
    count = 1

    # <h2></h2>内の文字列を<li></li>で挟むで返す
    for h2 in h2_list:
        result += "<li class=\"bold\"><a href=\"#link"+str(count)+"\" class=\"black\">" + str(count) + ". " + h2 + "</a></li>"
        count += 1
    return result

# 見出しに目次からのリンクをつける
@register.filter
def headline(text):
    sum = text.count("<h2>")
    count = 0

    # <h2>にidをつける
    for i in range(sum):
        count += 1
        replaced_text = "<h2 id=\"link" + str(count) + "\" class=\"blue f1\">"
        text = text.replace("<h2>", replaced_text, 1)
    return text
