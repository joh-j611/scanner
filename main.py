import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.utils import platform
from plyer import call


class AirtimeScanner(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=15)

        self.info_label = Label(text="Scan or Enter Scratch Card PIN")
        self.add_widget(self.info_label)

        self.pin_input = TextInput(hint_text="e.g. 1234567890123456", multiline=False)
        self.add_widget(self.pin_input)

        self.scan_btn = Button(text="Scan Camera (Simulated OCR)")
        self.scan_btn.bind(on_press=self.scan_card)
        self.add_widget(self.scan_btn)

        self.saf_btn = Button(text="Top Up Safaricom (*141*)", background_color=(0.2, 0.8, 0.2, 1))
        self.saf_btn.bind(on_press=self.topup_safaricom)
        self.add_widget(self.saf_btn)

        self.airtel_btn = Button(text="Top Up Airtel (*130*)", background_color=(0.9, 0.1, 0.1, 1))
        self.airtel_btn.bind(on_press=self.topup_airtel)
        self.add_widget(self.airtel_btn)

    def scan_card(self, instance):
        # Simulated OCR output.
        # In a full build, this passes a camera frame to pytesseract.image_to_string(image)
        simulated_camera_text = "Airtime scratch card num: 5382059517415871"

        # Regex to find a continuous string of 14 to 16 digits
        match = re.search(r'\d{14,16}', simulated_camera_text)
        if match:
            self.pin_input.text = match.group()
            self.info_label.text = "PIN Extracted Successfully!"
        else:
            self.info_label.text = "No valid PIN found. Try again."

    def dial_ussd(self, prefix, pin):
        pin = pin.strip()
        if not pin:
            self.info_label.text = "Please enter or scan a PIN first."
            return

        if not pin.isdigit():
            self.info_label.text = "PIN must contain digits only."
            return

        # The trailing '#' must be encoded as '%23' for Android dialer intents
        ussd = f"{prefix}{pin}%23"
        try:
            call.makecall(tel=ussd)
            self.info_label.text = "Dialing..."
        except NotImplementedError:
            self.info_label.text = "Dialing isn't supported on this platform."
        except Exception as e:
            self.info_label.text = f"Dialer Error: {e}"

    def topup_safaricom(self, instance):
        self.dial_ussd("*141*", self.pin_input.text)

    def topup_airtel(self, instance):
        self.dial_ussd("*130*", self.pin_input.text)


class ScannerApp(App):
    def build(self):
        if platform == "android":
            self.request_android_permissions()
        return AirtimeScanner()

    def request_android_permissions(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.CALL_PHONE, Permission.CAMERA])
        except ImportError:
            # android module only exists inside a built APK, not in dev environments
            pass


if __name__ == '__main__':
    ScannerApp().run()