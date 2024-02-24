# ███ AUTHENTICATION ███████████████████████████████████████████████████████████████████████████████████████████████████
# └──▶ This submodule defines WFM's "Auth" endpoints.


# ███ DEPENDENCIES █████████████████████████████████████████████████████████████████████████████████████████████████████
import requests
from src.wfm import __WFM_API_BASE_URL__


# ███ FUNCTIONS ████████████████████████████████████████████████████████████████████████████████████████████████████████
def sign_in(email: str,
            password: str
            ):
    # └──▶ Authenticate via header

    endpoint = "/auth/signin"  # ───▶ API endpoint

    body = {  # ───▶ POST body
        "auth_type": "header",  # ───▶ Specify header-based auth
        "email": email,  # ───▶ Email field for auth
        "password": password,  # ───▶ Password field for auth
        "device_id": ""  # ───▶ TODO figure out wtf this is
    }

    # ┌──▶ Perform request
    response = requests.post(url=__WFM_API_BASE_URL__ + endpoint,
                             json=body)

    print(response.text)  # TODO finish


def sign_up(email: str,  # ───▶ Email field for auth
            password: str,  # ───▶ password field for auth
            region: str = "en",  # ───▶ Region field for auth
            device_id="",  # ───▶ TODO figure out wtf this is
            recaptcha=""  # ───▶ TODO figure out how to use this
            ):
    # └──▶ Sign up via header

    endpoint = "/auth/registration"  # ───▶ API endpoint

    body = {  # ───▶ POST body
        "auth_type": "header",  # ───▶ Specify header-based auth
        "email": email,  # ───▶ Email field for auth
        "password": password,  # ───▶ Password field for auth
        "password_second": password,    # ───▶ Second password field for validation
        "region": region,
        "device_id": device_id,  # ───▶ TODO figure out wtf this is
        "recaptcha": recaptcha  # ───▶ TODO figure out how to use this
    }

    # ┌──▶ Perform request
    response = requests.post(url=__WFM_API_BASE_URL__ + endpoint,
                             json=body)

    print(response.text)  # TODO finish
    print(response.headers)
