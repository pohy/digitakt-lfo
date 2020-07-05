import math

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.clock import Clock

from funcs import send_cc


FILTER_CHANNEL = 74


class ValueSlider(Widget):
    slider = ObjectProperty()


class Lfo(BoxLayout):
    value_slider = ObjectProperty()
    textinput = ObjectProperty()
    timer = 0
    destination = FILTER_CHANNEL

    def __init__(self):
        super(Lfo, self).__init__()

        self.textinput.text = str(FILTER_CHANNEL)
        self.textinput.bind(text=self.on_destination)
        Clock.schedule_interval(self.tick, 1.0 / 60.0)

    def tick(self, dt):
        self.timer += dt
        value = math.sin(self.timer) / 2 + 0.5
        self.value_slider.slider.value = value
        if self.destination == None:
            return
        send_cc(self.destination, math.floor(value * 127))

    def on_destination(self, instance, value):
        try:
            destination = int(value)
            self.destination = destination
            print('Destination: {}'.format(destination))
        except ValueError:
            print('Error: cannot parse {} as an integer'.format(value))


class Lfos(BoxLayout):
    lfos = ObjectProperty()

    def add_lfo(self):
        self.lfos.add_widget(Lfo())


class DigitaktLfoApp(App):
    def build(self):
        lfos = Lfos()
        lfos.add_lfo()
        return lfos


DigitaktLfoApp().run()
