from typing import AnyStr, Any
import requests
from PIL import ImageTk


def get_qr_code(qr_code_size: int,
                qr_text: AnyStr = "You did not specify input text!") -> Any:

    request_string = f"https://api.qrserver.com/v1/create-qr-code/?data="\
                     f"{qr_text}"\
                     f"&size=[{qr_code_size}]x[{qr_code_size}]"

    response: requests.Response = requests.get(request_string)

    # qr_code_image = ImageTk.PhotoImage(data=response.content)
    print(response.__str__() + "\n")
    print(request_string)
    print(response.content)
    # print(qr_code_image)

    with open("final_response.png", "wb") as file:
        file.write(response.content)

    return response.content
