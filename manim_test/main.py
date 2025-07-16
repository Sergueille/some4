
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)) + "/..")

import manim
import manim_automata.src.manim_automata as manim_automata

class Test(manim.MovingCameraScene):
    def construct(self):
        manim_automaton = manim_automata.ManimAutomaton(
            xml_file="test.jff", 
            background_stroke_color=manim.WHITE, 
            color=manim.WHITE, 
            stroke_color=manim.WHITE,
            fill_color=manim.WHITE,
        )

        self.camera.frame_height = manim_automaton.height + 10
        self.camera.frame_width = self.camera.frame_height * 16 / 9
        self.camera.frame.move_to(manim_automaton) 

        self.add(manim_automaton)

        self.wait(1.0)
