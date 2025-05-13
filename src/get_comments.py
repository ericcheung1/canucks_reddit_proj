def fetch_comments(reddit, submission_id):
    """
    Recreates comment forest from PRAW in memory as a dictionary.

    This function takes a reddit instance and a reddit post id and
    returns a MongoDB-like document in memory as a dictionary.

    Args:
        reddit (praw.Reddit): A authenticated reddit instance.
        submission_id (str): A string representing a reddit submission id.
    
    Returns:
        post_data (dict): A dictionary replicating the comment forest structure.
    """
    submission = reddit.submission(id=submission_id)
    
    # final dictionary to store post information and comments/replies
    post_data = {
            "post_id": submission.id, 
            "title": submission.title,
            "author": str(submission.author),
            "utc_created": submission.created_utc, 
            "comments": []
            }
    
    # temporary storage of comments to check if is reply or not
    comment_map = {}

    print(submission.title)

    # gets comments from "more comments"
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:] # type: ignore

    # looping through each level of comment forest in breath-first search
    while comment_queue:
        comment = comment_queue.pop(0)

        # extract info from current comment in queue as a dictionary
        comment_dict = {    
            "comment_id": comment.id, 
            "author": str(comment.author), 
            "body": comment.body, 
            "utc_created": comment.created_utc, 
            "replies": []
            }
        
        # places current comment into comment_map dict
        # by having comment_id be the key and whole comment_dict as the value
        # makes it easier to look up comment by comment id
        comment_map[comment.id] = comment_dict 

        # if comment exists and is a reply
        # because replies have parent id prefixed with "t1_"
        if comment_dict and comment.parent_id.startswith("t3_"): 
            
            # are top level comments and appending them to post data
            post_data["comments"].append(comment_dict)
        else:

            # strips "t1_" prefix
            # assigns the parent id variable from
            # .parent_id method which is parent submission's id
            # we know these are replies as they don't start with "t3_"
            parent_id = comment.parent_id[3:]

            # if parent comment is in comment map
            # means if parent submission is in comment map
            # connecting child's id to its parent post 
            if parent_id in comment_map:

                # append it as a reply in comment map
                comment_map[parent_id]["replies"].append(comment_dict)

        # adds replies to current comment to back of queue
        comment_queue.extend(comment.replies)
    
    return post_data
            
