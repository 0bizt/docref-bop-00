def http_error(status):
  match status:
    case 400:
      return "Bad request"
    case 404:
      return "Not Found"
    case 401 | 403:
      return "Not allowed"
    case 418:
      return "I'm a teapot"
    case _:
      return "Something's wrong with the internet"

print(http_error(404))

# Not the last block: the "variable name" _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.
