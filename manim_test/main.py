import manim
import manim_automata


class Test(manim.MovingCameraScene):
    def construct(self):
        manim_automaton = manim_automata.ManimAutomaton(
            xml_file="test.jff", 
            background_stroke_color=manim.WHITE, 
            color=manim.WHITE, 
            stroke_color=manim.WHITE,
            fill_color=manim.WHITE,
        )

        self.camera.frame_width = manim_automaton.width + 10
        self.camera.frame_height = manim_automaton.height + 10
        self.camera.frame.move_to(manim_automaton) 

        self.play(
            manim.DrawBorderThenFill(manim_automaton)
        )
