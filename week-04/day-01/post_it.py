class PostIt():
    def __init__(self, bg_color, text, text_color):
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color

    def __str__(self):
        return "Background color: {}, text: {}, text color: {}".format(self.bg_color, self.text, self.text_color)

print(PostIt("orange", "Idea 1", "blue"))

awesome = PostIt("pink", "Awesome", "black")
print(awesome)

superb = PostIt("yellow", "Superb!", "green")
print(superb)

