def domain_name(url):
    new_url = url.replace('https://www.','')
    new_url = new_url.replace('http://www.','')
    new_url = new_url.replace('http://','')
    new_url = new_url.replace('https://','')
    new_url = new_url.replace('www.','')
    l = new_url.split('.')
    return l[0]

# domain_name("http://github.com/carbonfive/raygun") == "github" 
# domain_name("http://www.zombie-bites.com") == "zombie-bites"
# domain_name("https://www.cnet.com") == "cnet"