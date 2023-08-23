import socket
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class ProjectorControl(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        
        self.ip_input = TextInput(hint_text="Enter Projector IP")
        self.port_input = TextInput(hint_text="Enter Port")
        
        self.connect_button = Button(text="Conectar proyector")
        self.connect_button.bind(on_press=self.connect_to_projector)
        
        self.on_button = Button(text="ON")
        self.on_button.bind(on_press=self.turn_on_projector)
        
        self.off_button = Button(text="OFF")
        self.off_button.bind(on_press=self.turn_off_projector)
        
        self.menu_button = Button(text="Abrir Menu")
        self.menu_button.bind(on_press=self.open_menu)
        
        self.left_button = Button(text="Izquierda")
        self.left_button.bind(on_press=self.navigate_left)
        
        self.right_button = Button(text="Derecha")
        self.right_button.bind(on_press=self.navigate_right)
        
        self.layout.add_widget(self.ip_input)
        self.layout.add_widget(self.port_input)
        self.layout.add_widget(self.connect_button)
        self.layout.add_widget(self.on_button)
        self.layout.add_widget(self.off_button)
        self.layout.add_widget(self.menu_button)
        self.layout.add_widget(self.left_button)
        self.layout.add_widget(self.right_button)
        
        self.projector_socket = None
        
        return self.layout
    
    def connect_to_projector(self, instance):
            proyector_ip = self.ip_input.text
            puerto = int(self.port_input.text)
                        
            self.projector_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.projector_socket.connect((proyector_ip, puerto))

    def turn_on_projector(self, instance):
            if self.projector_socket:
                self.projector_socket.send(b'TURN_ON')
    
    def turn_off_projector(self, instance):
            if self.projector_socket:
                self.projector_socket.send(b'TURN_OFF')

    def on_stop(self):
            if self.projector_socket:
                self.projector_socket.close()
            
    def open_menu(self, instance):
            if self.projector_socket:
                self.projector_socket.send(b'OPEN_MENU')

    def navigate_left(self, instance):
            if self.projector_socket:
                self.projector_socket.send(b'NAVIGATE_LEFT')

    def navigate_right(self, instance):
            if self.projector_socket:
                self.projector_socket.send(b'NAVIGATE_RIGHT')


if __name__ == '__main__':
    ProjectorControl().run()
