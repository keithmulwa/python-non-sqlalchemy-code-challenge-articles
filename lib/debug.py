#!/usr/bin/env python3
import ipdb
from classes.many_to_many import Article, Author, Magazine

if name == 'main':
    print("HELLO! :slightly_smiling_face: let's debug :vibing_potato:")

# Create authors
a1 = Author("Alice")
a2 = Author("Bob")

# Create magazines
m1 = Magazine("Tech Today", "Technology")
m2 = Magazine("Health Weekly", "Health")

# Add articles
a1.add_article(m1, "AI in 2025")
a1.add_article(m2, "Healthy Living")
a2.add_article(m1, "The Future of Python")
a2.add_article(m1, "AI Ethics")
a2.add_article(m1, "Data Science Trends")

print("\n--- Demo Data Loaded ---")
print("Alice's Articles:", [a.title for a in a1.articles()])
print("Alice's Magazines:", [m.name for m in a1.magazines()])
print("Alice's Topics:", a1.topic_areas())
print("Tech Today Articles:", [a.title for a in m1.articles()])
print("Tech Today Contributors:", [au.name for au in m1.contributors()])
print("Tech Today Article Titles:", m1.article_titles())
print("Tech Today Contributing Authors:", [au.name for au in m1.contributing_authors()])

# stay in debugger
ipdb.set_trace()