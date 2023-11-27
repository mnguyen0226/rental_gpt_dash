def read_file_as_str(filename):
    """Return input markdown file as string

    Args:
        filename: markdown file

    Returns:
        data string
    """
    with open(filename, "r") as file:
        data = file.read()
    return data
