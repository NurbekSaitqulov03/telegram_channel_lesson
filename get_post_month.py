from read_data import fromJson


def get_post_month(data:dict,month:int)->int:
    """
    Return the number of posts for a given month

    Args:
        data (dict): a dictionary of posts
        month (int): as number between 1 and 12

    Returns: 
        int: the number of posts for the given month
    """
    x = 0
    a = data['messages']
    for i in a:
        oy = i['date'].split('T')[0]
        oy1 = oy.split('-')[1]
        if int(oy1) == month:
            x += 1
    return x
print(get_post_month(fromJson('data/result.json'), 8))