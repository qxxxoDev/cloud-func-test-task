from dotenv import load_dotenv

def main():
    """ Точка входа в приложение """
    load_dotenv()

    from api import call_api

    call_api()
