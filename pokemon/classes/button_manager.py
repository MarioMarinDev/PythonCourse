
class ButtonManager:
    def __init__(self, buttons, controls):
        self.buttons = buttons
        self.index = 0
        self.controls = controls
        self.last_input = None
        for index, button in enumerate(buttons):
            if button.selected:
                self.index = index

    def control(self):
        for index, button in enumerate(self.buttons):
            if self.controls.move_down and self.last_input != "move_down":
                self.last_input = "move_down"
                self.next_position()
            elif self.controls.move_up and self.last_input != "move_up":
                self.last_input = "move_up"
                self.previous_position()
            elif button.selected and self.controls.accept and self.last_input != "accept":
                self.last_input = "accept"
                return {"action": button.action, "value": button.value}
            elif not self.controls.move_down and not self.controls.move_up and not self.controls.accept:
                self.last_input = None
            button.selected = self.index == index
        return None

    def next_position(self):
        index = self.index + 1
        if index >= len(self.buttons):
            index = 0
        self.index = index

    def previous_position(self):
        index = self.index - 1
        if index < 0:
            index = len(self.buttons) - 1
        self.index = index

    def render(self):
        for button in self.buttons:
            button.render()

