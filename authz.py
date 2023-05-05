def authorize(user, resource, action):
    """
    This function takes in a user, a resource, and an action, and returns
 whether or not the user is authorized to perform that action on that resource.
 """
    if user.is_admin:
        return True # Admins can do anything
    elif action == "read" and user.has_read_permission(resource):
        return True # Users with read permission can read the resource
    elif action == "write" and user.has_write_permission(resource):
        return True # Users with write permission can write to the resource
    else:
        return False # User is not authorized to perform the action on the resource