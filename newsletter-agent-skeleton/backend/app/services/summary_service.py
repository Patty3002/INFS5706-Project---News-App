def prep_summary(articles):
    res = list()
    for article in articles:
        res.append({
            "title": article["title"],
            "description": article["description"],
            "content": article["content"],
            "url": article["url"]
        })
    return res

