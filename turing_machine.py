from manim import *

def str_(val):
    if val in [0, 1]:
        return str(val)
    else:
        return '#'

class TuringMachine(VGroup):
    def __init__(self, nb_shown=9, tape=None, width=0.5, height=1):

        self.nb_shown = nb_shown
        self.scale = 9/nb_shown
        self.wid = width*self.scale
        self.hei = height*self.scale

        if tape is None:
            tape = [0 for i in range(nb_shown)]

        self.tape_content = tape
        self.tape_cells = [Rectangle(width=self.wid, height=self.hei) for i in range(nb_shown)]
        self.tape_text = [Text(str_(self.tape_content[i])) for i in range(nb_shown)]

        self.tape_group = VGroup()

        for i in range(nb_shown):
            self.tape_cells[i].shift(UP*(self.nb_shown//2 -i)*self.scale)
            self.tape_text[i].shift(UP*(self.nb_shown//2-i)*self.scale).scale(0.5*self.scale)


        self.tape_group.add(self.tape_cells)
        self.tape_group.add(self.tape_text)

        self.arrow = Arrow([1.5,0,0], [0.5,0,0], buff=0, stroke_width=4).set_color(YELLOW)
        self.current =  Rectangle(width=self.wid, height=self.hei).set_color(YELLOW)
        self.current_id = nb_shown//2

        self.head = VGroup()
        self.head.add(self.current, self.arrow)

        self.all = VGroup()
        self.all.add(self.tape_group, self.head)

    def write(self, scene, val):

        self.tape_content[self.current_id] = val
        new_text = Text(str_(val)).move_to(self.tape_text[self.current_id]).set_color(RED)

        # scene.play(Transform(self.tape_text[i], new_text))
        scene.play(ReplacementTransform(self.tape_text[self.current_id], new_text), run_time=0.5)
        scene.play(new_text.animate.scale(0.5*self.scale), run_time=0.5)
        new_text.set_color(WHITE)

        self.tape_text[self.current_id] = new_text

    def move_right(self, scene, top_val=0):

        if  self.current_id == self.nb_shown//2:
            new_cell = Rectangle(width=self.wid, height=self.hei).shift(UP*(self.nb_shown//2 + 1)*self.scale)
            new_text = Text(str_(top_val)).shift(UP*(self.nb_shown//2 + 1)*self.scale).scale(0.5*self.scale)
            self.tape_cells.append(new_cell)
            self.tape_content.append(top_val)
            self.tape_text.append(new_text)

            self.tape_cells = self.tape_cells[-1:] + self.tape_cells[:-1]
            self.tape_text = self.tape_text[-1:] + self.tape_text[:-1]

            self.tape_group.add(new_cell, new_text)
        else:
            self.current_id -= 1

        # scene.add(new_cell, new_text)
        scene.play(self.tape_group.animate.shift(DOWN*self.scale))

    def move_left(self, scene, top_val=0):

        if self.current_id == len(self.tape_content) - (self.nb_shown+1)//2:
            new_cell = Rectangle(width=self.wid, height=self.hei).shift(DOWN*(self.nb_shown//2 + 1)*self.scale)
            new_text = Text(str_(top_val)).shift(DOWN*(self.nb_shown//2 + 1)*self.scale).scale(0.5*self.scale)
            self.tape_cells.append(new_cell)
            self.tape_text.append(new_text)

            self.tape_group.add(new_cell, new_text)

        self.current_id += 1

        # scene.add(new_cell, new_text)
        scene.play(self.tape_group.animate.shift(UP*self.scale))


class Test(Scene):
    def construct(self):
        machine = TuringMachine(nb_shown=11)

        # self.play(Create(machine.all), run_time=2)
        self.add(machine.all)
        self.wait()
        machine.write(self, 1)
        machine.move_right(self, 2)
        machine.move_right(self, 2)
        machine.write(self, 1)
        machine.move_left(self, 2)
        machine.write(self, 0)
        machine.move_left(self, 2)
        machine.move_left(self, 1)
        machine.move_right(self, 2)
        machine.move_right(self, 1)
        machine.move_right(self, 1)
        machine.move_right(self, 1)
        machine.move_right(self, 1)
        self.wait(2)
