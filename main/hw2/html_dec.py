def italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


def bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"

    return wrapped
