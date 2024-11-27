# -*- coding: utf-8 -*-
# news.py

import feedparser

def get_news():
    url = "http://www.cnnturk.com/feed/rss/news"
    haberler = feedparser.parse(url)

    if not haberler.entries:
        return "Şu anda Türkiye için haber bulunmamaktadır."

    top_articles = haberler.entries[:5]  # İlk 5 haberi al
    news_summary = "İşte en son haberler: "
    for i, haber in enumerate(top_articles, 1):
        news_summary += f"\n{i}. {haber.title} - CNN Türk"
    return news_summary
