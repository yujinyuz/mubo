import time


def make_key(args, kwargs):
    # Create a unique key using args and kwargs
    key = args + tuple(sorted(kwargs.items()))
    return key


def cachet(ttl):
    """Simple caching function that stores the results inside the `cache` dictionary"""
    cache = {}

    def decorate(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            key = make_key(args, kwargs)

            if key in cache:
                result, timestamp = cache[key]

                if current_time - timestamp < timeout:
                    print(f"Returning cached result for {key}")
                    return result
                else:
                    print(f"Cache expired for {key}, recalculating")

            result = func(*args, **kwargs)
            cache[args] = (result, current_time)
            print(f"Caching result for {key}")

            return result

        return wrapper

    return decorate


@cachet(ttl=10)
def fetch_github_user(username):
    time.sleep(3)
    return {"username": username, "followers": 50}


print(fetch_github_user("yujinyuz"))
print(fetch_github_user("yujinyuz"))
