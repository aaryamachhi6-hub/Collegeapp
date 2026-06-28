from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class CollegeApp(App):

    def build(self):
        self.layout = BoxLayout(
            orientation='vertical',
            padding=10,
            spacing=10
        )

        title = Label(
            text="College AI Assistant",
            font_size=28
        )

        self.output = Label(
            text="Welcome!",
            size_hint_y=0.5
        )

        self.input = TextInput(
            hint_text="Ask about library, fees, exam...",
            multiline=False
        )

        btn = Button(
            text="Send"
        )

        btn.bind(on_press=self.chatbot)

        self.layout.add_widget(title)
        self.layout.add_widget(self.input)
        self.layout.add_widget(btn)
        self.layout.add_widget(self.output)

        return self.layout

    def chatbot(self, instance):
        msg = self.input.text.lower()

        if "library" in msg:
            reply = "Library Timing: 9 AM - 5 PM"

        elif "fees" in msg:
            reply = "Contact Accounts Department"

        elif "exam" in msg:
            reply = "Exam starts from 10 July"

        elif "attendance" in msg:
            reply = "Minimum attendance required is 75%"

        elif "placement" in msg:
            reply = "Placement Cell is in Block B"

        else:
            reply = "Information not available"

        self.output.text = reply
        self.input.text = ""

CollegeApp().run()
