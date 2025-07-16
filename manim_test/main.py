
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)) + "/..")

import manim
import manim_automata.src.manim_automata as manim_automata

class Test(manim.MovingCameraScene):
    def construct(self):
        manim_automaton = manim_automata.ManimAutomaton(xml_file="test.jff")

        self.camera.frame_height = manim_automaton.height + 10
        self.camera.frame_width = self.camera.frame_height * 16 / 9
        self.camera.frame.move_to(manim_automaton) 

        self.add(manim_automaton)

        self.wait()
        manim_automaton.set_highlighted_state(0, self)
        self.wait()
        manim_automaton.set_highlighted_state(2, self)
        self.wait()
        manim_automaton.set_highlighted_state(3, self)
        self.wait()
        manim_automaton.set_highlighted_state(2, self)
        self.wait()
        manim_automaton.set_highlighted_state(1, self)

        self.wait(1.0)
