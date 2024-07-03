# qr_code_display_service/QRCodeDisplayService.py

import tkinter as tk
import qrcode
from event_manager.EventManager import EventManager

class QRCodeDisplayService:
    def __init__(self, event_manager):
        self.event_manager = event_manager
        self.window = tk.Tk()
        self.window.title("QR Code Display")
        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack()

    def display_qr_code(self, qr_data, position):
        qr = qrcode.make(qr_data)
        qr_image = tk.PhotoImage(data=qr.png_as_base64_str(scale=5))
        self.canvas.create_image(position, image=qr_image)
        self.window.mainloop()

    def remove_qr_code(self, position):
        self.canvas.delete(position)

    def update_qr_code(self, qr_data, position):
        self.remove_qr_code(position)
        self.display_qr_code(qr_data, position)

if __name__ == "__main__":
    event_manager = EventManager()
    qr_service = QRCodeDisplayService(event_manager)
    qr_service.display_qr_code("Hello World", (100, 100))
