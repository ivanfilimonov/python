def raises(a):
    def wrapped(b):
        try:
            if (callable(b)):
                return b()
            else:
                return b
        except Exception:
            return a

    return wrapped
