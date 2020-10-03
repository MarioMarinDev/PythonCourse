from classes.text import Text


class Button(Text):
    def __init__(self, text, font, color, position,
                 selected=False, selected_color=(255, 0, 0), action=None, value=None):
        super().__init__(text, font, color, position)
        self.selected = selected
        self.selected_color = selected_color
        self.action = action
        self.value = value

    @property
    def text_render(self):
        c = self.color
        if self.selected:
            c = self.selected_color
        return self.font.render(self.text, True, c)
