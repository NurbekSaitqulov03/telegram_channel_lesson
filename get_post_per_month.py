from read_data import fromJson


def get_post_per_month(data:dict)->dict:
    """
    Return the number of posts for each month

    Args:
        data (dict): a dictionary of posts
        
    Returns: 
        dict: a dictionary with the number of posts for each month
    """
    a = {}
    x = data['messages']
    for i in x:
        y = i['date'].split('T')[0]
        z = y.split('-')[1]

        a.setdefault(z, 0)
        a[z] += 1
    return a
print(get_post_per_month(fromJson('data/result.json')))