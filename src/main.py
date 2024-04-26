from api_request import get_qr_code
import tkinter
from PIL import ImageTk  # ,Image
# from io import BytesIO

qr_code_size: int = 512
qr_code_pos: float = qr_code_size / 2

# define TkInter window and its attributes
main_window: tkinter.Tk = tkinter.Tk()

main_window.title("QRCODED")
main_window.geometry(f"{qr_code_size}x{qr_code_size}")

main_window.grid_rowconfigure(0, weight=1)
main_window.grid_columnconfigure(0, weight=1)

# make a prompt label, and positon it in the window
prompt = tkinter.Label(main_window, text="Specify text from which to generate QR code of")
prompt.grid(row=0, column=0)
prompt.grid_rowconfigure(0, weight=1)
prompt.grid_columnconfigure(0, weight=1)

# make an input box
qr_code_input = tkinter.Entry(main_window, width=qr_code_size)
qr_code_input.grid(row=1, column=0)
qr_code_input.rowconfigure(0, weight=1)
qr_code_input.columnconfigure(0, weight=1)


# image box
qr_code_canvas = tkinter.Canvas(main_window, width=512, height=512)
qr_code_canvas.grid(row=3, column=0)


# helper function to generate qr code with value from input box
def get_value_return_qr_code():
    value = qr_code_input.get()
    if value == "":
        value = "Wrong input string"

    get_qr_code(qr_code_size, value)

    updated_qr_code_image = ImageTk.PhotoImage(file="final_response.png")
    qr_code_canvas.delete("all")
    qr_code_canvas.create_image(qr_code_pos, qr_code_pos, anchor="center", image=updated_qr_code_image)

    # return output


# make a button for that input
generate_qr_code = tkinter.Button(main_window, text="Generate", command=get_value_return_qr_code)
generate_qr_code.grid(row=2, column=0)


shown_qr_code_image = ImageTk.PhotoImage(file="example_response.png")
qr_code_canvas.create_image(qr_code_pos, qr_code_pos, anchor="center", image=shown_qr_code_image)
# shown_qr_code_image = tkinter.PhotoImage(data=b64decode(generate_qr_code.invoke()))

main_window.mainloop()
