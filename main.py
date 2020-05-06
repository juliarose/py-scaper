from sites.github_com import githubCom

data = githubCom.get_profile('juliarose')

if data is not None:
    print(data.get('name'))