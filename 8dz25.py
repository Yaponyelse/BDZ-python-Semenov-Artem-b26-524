def read_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return "file not found"
    except PermissionError:
        return "permission denied"
    except OSError as e:
        return f"os error: {e.strerror}"