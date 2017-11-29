# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crutial component, find out what it is and insert it too!

url = "https//www.reddit.com/r/nevertellmethebots"

def url_fixer(an_url):
    new_url = ""
    i = 0
    for c in an_url:
        if i < len(an_url) - 4:
            new_url += an_url[i]
        if i == 4:
            new_url += ":"
        i += 1
    new_url += "odds"
    return new_url
print(url_fixer(url))

url = url.replace("bots", "odds")
l = url.split("//")
l[0] = l[0] + ":"
url = "//".join(l)
print(url)

