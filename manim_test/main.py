import manim


class CreateCircle(manim.Scene):
    def construct(self):
        logic_form = manim.Tex(r"$x_1 \land \neg x_2$", font_size=100)
        self.play(manim.Create(logic_form))
        self.wait(1.0)