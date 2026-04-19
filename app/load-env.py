import os


def load_env_file(env_file_path=".env"):
    """Manually loads environment variables from a .env file."""
    if os.path.exists(env_file_path):
        with open(env_file_path, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):  # Ignore comments and empty lines
                    key, value = line.split("=", 1)  # Split at the first '=' only
                    os.environ[key] = value  # Set the environment variable
    pass

def get_all_env_vars() -> dict:
    """
    Reads all environment variables and returns them as a dictionary.

    Returns:
        dict: A dictionary containing all environment variable names and their values.

    Author:
        Ritu
    """
    return dict(os.environ)


def load_env_vars(env_file_path=".env"):
    """
    loads env file, reads all vars and returns as a python dict

    Author:
        Ritu
    """
    load_env_file(env_file_path)
    #print("loading env vars")
    return get_all_env_vars()
