from manimlib import *
import numpy as np

class CongruenceOfArcs(Scene):
    def construct(self):
        # Scene 1: Introduction to Arcs
        self.scene_1_introduction_to_arcs()
        
        # Scene 2: Defining Congruent Arcs
        self.scene_2_defining_congruent_arcs()
        
        # Scene 3: Degrees and Length of Arcs
        self.scene_3_degrees_and_length()
        
        # Scene 4: Examples of Congruent and Non-congruent Arcs
        self.scene_4_examples()
        
        # Scene 5: Exercise – Identifying Congruent Arcs
        self.scene_5_exercise()
        
        # Scene 6: Recap and Key Points
        self.scene_6_recap()
        
        # Scene 7: Closing Remarks
        self.scene_7_closing()

    def scene_1_introduction_to_arcs(self):
        # Title
        title = Text("Congruence of Arcs", font_size=48, color=BLUE)
        title.to_edge(UP)
        
        self.play(Write(title))
        self.wait(1)
        
        # Scene 1 title
        scene_title = Text("Scene 1: Introduction to Arcs", font_size=36, color=GREEN)
        scene_title.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Create a neat circle
        circle = Circle(radius=2, color=WHITE, stroke_width=3)
        circle.move_to(ORIGIN)
        
        self.play(ShowCreation(circle))
        self.wait(1)
        
        # Create points A and B on the circle
        angle_a = PI/6
        angle_b = 5*PI/6
        point_a = circle.point_at_angle(angle_a)
        point_b = circle.point_at_angle(angle_b)
        
        dot_a = Dot(point_a, color=RED, radius=0.08)
        dot_b = Dot(point_b, color=RED, radius=0.08)
        label_a = Text("A", font_size=24, color=RED).next_to(dot_a, UR, buff=0.1)
        label_b = Text("B", font_size=24, color=RED).next_to(dot_b, UL, buff=0.1)
        
        self.play(
            ShowCreation(dot_a),
            ShowCreation(dot_b),
            Write(label_a),
            Write(label_b)
        )
        self.wait(1)
        
        # Highlight the arc AB
        arc_ab = Arc(
            start_angle=angle_a,
            angle=angle_b - angle_a,
            radius=2,
            color=YELLOW,
            stroke_width=6
        )
        
        self.play(ShowCreation(arc_ab))
        self.wait(1)
        
        # Add definition text
        definition = Text(
            "Arc: Part of a circle between two points",
            font_size=32,
            color=WHITE
        )
        definition.to_edge(DOWN)
        
        self.play(Write(definition))
        self.wait(2)
        
        # Clear scene
        self.play(
            FadeOut(VGroup(title, scene_title, circle, dot_a, dot_b, label_a, label_b, arc_ab, definition))
        )
        self.wait(1)

    def scene_2_defining_congruent_arcs(self):
        # Scene 2 title
        scene_title = Text("Scene 2: Defining Congruent Arcs", font_size=36, color=GREEN)
        scene_title.to_edge(UP)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Create two identical circles side by side
        circle1 = Circle(radius=1.5, color=WHITE, stroke_width=3)
        circle1.move_to(LEFT * 3)
        
        circle2 = Circle(radius=1.5, color=WHITE, stroke_width=3)
        circle2.move_to(RIGHT * 3)
        
        self.play(ShowCreation(circle1), ShowCreation(circle2))
        self.wait(1)
        
        # Create identical arcs on both circles
        arc_angle = PI/3
        start_angle = PI/6
        
        # Arc PQ on first circle
        arc_pq = Arc(
            start_angle=start_angle,
            angle=arc_angle,
            radius=1.5,
            color=BLUE,
            stroke_width=6
        ).move_to(LEFT * 3)
        
        # Points P and Q
        point_p = circle1.point_at_angle(start_angle)
        point_q = circle1.point_at_angle(start_angle + arc_angle)
        dot_p = Dot(point_p, color=BLUE, radius=0.06)
        dot_q = Dot(point_q, color=BLUE, radius=0.06)
        label_p = Text("P", font_size=20, color=BLUE).next_to(dot_p, DR, buff=0.1)
        label_q = Text("Q", font_size=20, color=BLUE).next_to(dot_q, UL, buff=0.1)
        
        # Arc RS on second circle (identical)
        arc_rs = Arc(
            start_angle=start_angle,
            angle=arc_angle,
            radius=1.5,
            color=RED,
            stroke_width=6
        ).move_to(RIGHT * 3)
        
        # Points R and S
        point_r = circle2.point_at_angle(start_angle) + RIGHT * 3
        point_s = circle2.point_at_angle(start_angle + arc_angle) + RIGHT * 3
        dot_r = Dot(point_r, color=RED, radius=0.06)
        dot_s = Dot(point_s, color=RED, radius=0.06)
        label_r = Text("R", font_size=20, color=RED).next_to(dot_r, DR, buff=0.1)
        label_s = Text("S", font_size=20, color=RED).next_to(dot_s, UL, buff=0.1)
        
        # Show arcs and labels
        self.play(
            ShowCreation(arc_pq),
            ShowCreation(arc_rs),
            ShowCreation(dot_p), ShowCreation(dot_q),
            ShowCreation(dot_r), ShowCreation(dot_s),
            Write(label_p), Write(label_q),
            Write(label_r), Write(label_s)
        )
        self.wait(1)
        
        # Add arc labels
        arc_pq_label = Text("Arc PQ", font_size=20, color=BLUE)
        arc_pq_label.next_to(circle1, DOWN, buff=0.3)
        
        arc_rs_label = Text("Arc RS", font_size=20, color=RED)
        arc_rs_label.next_to(circle2, DOWN, buff=0.3)
        
        self.play(Write(arc_pq_label), Write(arc_rs_label))
        self.wait(1)
        
        # Definition of congruent arcs
        definition = Text(
            "Congruent Arcs: Arcs with equal measure (length or degrees)",
            font_size=28,
            color=WHITE
        )
        definition.to_edge(DOWN)
        
        self.play(Write(definition))
        self.wait(1)
        
        # Show measurements
        degrees_text = Text("60°", font_size=20, color=YELLOW)
        degrees_text1 = degrees_text.copy().next_to(arc_pq, UP, buff=0.2)
        degrees_text2 = degrees_text.copy().next_to(arc_rs, UP, buff=0.2)
        
        length_text = Text("π units", font_size=20, color=YELLOW)
        length_text1 = length_text.copy().next_to(arc_pq_label, DOWN, buff=0.1)
        length_text2 = length_text.copy().next_to(arc_rs_label, DOWN, buff=0.1)
        
        self.play(
            Write(degrees_text1), Write(degrees_text2),
            Write(length_text1), Write(length_text2)
        )
        self.wait(2)
        
        # Clear scene
        self.play(
            FadeOut(VGroup(
                scene_title, circle1, circle2, arc_pq, arc_rs,
                dot_p, dot_q, dot_r, dot_s,
                label_p, label_q, label_r, label_s,
                arc_pq_label, arc_rs_label,
                degrees_text1, degrees_text2,
                length_text1, length_text2,
                definition
            ))
        )
        self.wait(1)

    def scene_3_degrees_and_length(self):
        # Scene 3 title
        scene_title = Text("Scene 3: Degrees and Length of Arcs", font_size=36, color=GREEN)
        scene_title.to_edge(UP)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Create a single circle
        circle = Circle(radius=2, color=WHITE, stroke_width=3)
        circle.move_to(ORIGIN)
        
        self.play(ShowCreation(circle))
        self.wait(1)
        
        # Create center point
        center = Dot(ORIGIN, color=WHITE, radius=0.05)
        center_label = Text("O", font_size=20, color=WHITE).next_to(center, DL, buff=0.1)
        
        self.play(ShowCreation(center), Write(center_label))
        self.wait(1)
        
        # Create an arc with central angle
        start_angle = PI/4
        arc_angle = PI/2
        
        arc = Arc(
            start_angle=start_angle,
            angle=arc_angle,
            radius=2,
            color=BLUE,
            stroke_width=6
        )
        
        # Points on the arc
        point_c = circle.point_at_angle(start_angle)
        point_d = circle.point_at_angle(start_angle + arc_angle)
        dot_c = Dot(point_c, color=BLUE, radius=0.08)
        dot_d = Dot(point_d, color=BLUE, radius=0.08)
        label_c = Text("C", font_size=24, color=BLUE).next_to(dot_c, UR, buff=0.1)
        label_d = Text("D", font_size=24, color=BLUE).next_to(dot_d, UL, buff=0.1)
        
        self.play(
            ShowCreation(arc),
            ShowCreation(dot_c), ShowCreation(dot_d),
            Write(label_c), Write(label_d)
        )
        self.wait(1)
        
        # Draw radii to show central angle
        radius_oc = Line(ORIGIN, point_c, color=GREEN, stroke_width=3)
        radius_od = Line(ORIGIN, point_d, color=GREEN, stroke_width=3)
        
        self.play(ShowCreation(radius_oc), ShowCreation(radius_od))
        self.wait(1)
        
        # Mark the central angle
        angle_arc = Arc(
            start_angle=start_angle,
            angle=arc_angle,
            radius=0.5,
            color=YELLOW,
            stroke_width=4
        )
        
        angle_label = Text("90°", font_size=20, color=YELLOW)
        angle_label.move_to(ORIGIN + 0.7 * (UP + RIGHT) / np.sqrt(2))
        
        self.play(ShowCreation(angle_arc), Write(angle_label))
        self.wait(1)
        
        # Text about relationship
        relationship_text = Text(
            "Congruent arcs have equal central angles",
            font_size=28,
            color=WHITE
        )
        relationship_text.to_edge(DOWN, buff=1.5)
        
        self.play(Write(relationship_text))
        self.wait(2)
        
        # Show formula
        formula = MathTex(
            r"\text{Arc length} = \frac{\text{central angle}}{360°} \times \text{circumference}",
            font_size=24,
            color=YELLOW
        )
        formula.to_edge(DOWN)
        
        self.play(
            FadeOut(relationship_text),
            Write(formula)
        )
        self.wait(2)
        
        # Clear scene
        self.play(
            FadeOut(VGroup(
                scene_title, circle, center, center_label,
                arc, dot_c, dot_d, label_c, label_d,
                radius_oc, radius_od, angle_arc, angle_label,
                formula
            ))
        )
        self.wait(1)

    def scene_4_examples(self):
        # Scene 4 title
        scene_title = Text("Scene 4: Examples of Congruent and Non-congruent Arcs", font_size=32, color=GREEN)
        scene_title.to_edge(UP)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Create two circles
        circle1 = Circle(radius=1.2, color=WHITE, stroke_width=3)
        circle1.move_to(LEFT * 3 + UP * 1)
        
        circle2 = Circle(radius=1.2, color=WHITE, stroke_width=3)
        circle2.move_to(RIGHT * 3 + UP * 1)
        
        circle3 = Circle(radius=1.2, color=WHITE, stroke_width=3)
        circle3.move_to(LEFT * 3 + DOWN * 1.5)
        
        circle4 = Circle(radius=1.2, color=WHITE, stroke_width=3)
        circle4.move_to(RIGHT * 3 + DOWN * 1.5)
        
        self.play(
            ShowCreation(circle1), ShowCreation(circle2),
            ShowCreation(circle3), ShowCreation(circle4)
        )
        self.wait(1)
        
        # First pair: Congruent arcs (same central angle)
        arc_angle1 = PI/3
        
        arc1 = Arc(
            start_angle=0,
            angle=arc_angle1,
            radius=1.2,
            color=GREEN,
            stroke_width=5
        ).move_to(LEFT * 3 + UP * 1)
        
        arc2 = Arc(
            start_angle=PI/6,
            angle=arc_angle1,
            radius=1.2,
            color=GREEN,
            stroke_width=5
        ).move_to(RIGHT * 3 + UP * 1)
        
        # Second pair: Non-congruent arcs (different central angles)
        arc_angle2 = PI/6
        arc_angle3 = PI/2
        
        arc3 = Arc(
            start_angle=0,
            angle=arc_angle2,
            radius=1.2,
            color=RED,
            stroke_width=5
        ).move_to(LEFT * 3 + DOWN * 1.5)
        
        arc4 = Arc(
            start_angle=0,
            angle=arc_angle3,
            radius=1.2,
            color=RED,
            stroke_width=5
        ).move_to(RIGHT * 3 + DOWN * 1.5)
        
        self.play(
            ShowCreation(arc1), ShowCreation(arc2),
            ShowCreation(arc3), ShowCreation(arc4)
        )
        self.wait(1)
        
        # Add angle measurements
        angle1_text = Text("60°", font_size=16, color=GREEN)
        angle1_text1 = angle1_text.copy().next_to(circle1, DOWN, buff=0.1)
        angle1_text2 = angle1_text.copy().next_to(circle2, DOWN, buff=0.1)
        
        angle2_text = Text("30°", font_size=16, color=RED)
        angle2_text1 = angle2_text.copy().next_to(circle3, DOWN, buff=0.1)
        
        angle3_text = Text("90°", font_size=16, color=RED)
        angle3_text2 = angle3_text.copy().next_to(circle4, DOWN, buff=0.1)
        
        self.play(
            Write(angle1_text1), Write(angle1_text2),
            Write(angle2_text1), Write(angle3_text2)
        )
        self.wait(1)
        
        # Add labels
        congruent_label = Text("Congruent", font_size=24, color=GREEN)
        congruent_label.move_to(UP * 2.5)
        
        not_congruent_label = Text("Not Congruent", font_size=24, color=RED)
        not_congruent_label.move_to(DOWN * 3)
        
        self.play(Write(congruent_label), Write(not_congruent_label))
        self.wait(2)
        
        # Clear scene
        self.play(
            FadeOut(VGroup(
                scene_title, circle1, circle2, circle3, circle4,
                arc1, arc2, arc3, arc4,
                angle1_text1, angle1_text2, angle2_text1, angle3_text2,
                congruent_label, not_congruent_label
            ))
        )
        self.wait(1)

    def scene_5_exercise(self):
        # Scene 5 title
        scene_title = Text("Scene 5: Exercise – Identifying Congruent Arcs", font_size=32, color=GREEN)
        scene_title.to_edge(UP)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Exercise prompt
        prompt = Text("Are these arcs congruent?", font_size=28, color=WHITE)
        prompt.next_to(scene_title, DOWN, buff=0.5)
        
        self.play(Write(prompt))
        self.wait(1)
        
        # Exercise 1: Congruent arcs
        self.exercise_pair(1, True, PI/4, PI/4, LEFT * 4 + DOWN * 0.5, RIGHT * 4 + DOWN * 0.5)
        
        # Exercise 2: Non-congruent arcs
        self.exercise_pair(2, False, PI/6, PI/3, LEFT * 4 + DOWN * 0.5, RIGHT * 4 + DOWN * 0.5)
        
        # Exercise 3: Congruent arcs (different positions)
        self.exercise_pair(3, True, PI/3, PI/3, LEFT * 4 + DOWN * 0.5, RIGHT * 4 + DOWN * 0.5)
        
        self.play(FadeOut(scene_title), FadeOut(prompt))
        self.wait(1)

    def exercise_pair(self, pair_number, is_congruent, angle1, angle2, pos1, pos2):
        # Create circles for exercise
        circle1 = Circle(radius=1.5, color=WHITE, stroke_width=3).move_to(pos1)
        circle2 = Circle(radius=1.5, color=WHITE, stroke_width=3).move_to(pos2)
        
        # Create arcs
        arc1 = Arc(start_angle=0, angle=angle1, radius=1.5, color=BLUE, stroke_width=5).move_to(pos1)
        arc2 = Arc(start_angle=PI/6, angle=angle2, radius=1.5, color=YELLOW, stroke_width=5).move_to(pos2)
        
        # Pair label
        pair_label = Text(f"Pair {pair_number}", font_size=24, color=WHITE)
        pair_label.move_to((pos1 + pos2) / 2 + UP * 2)
        
        self.play(
            ShowCreation(circle1), ShowCreation(circle2),
            ShowCreation(arc1), ShowCreation(arc2),
            Write(pair_label)
        )
        self.wait(1)
        
        # Show angle measurements as hints
        angle1_deg = int(np.degrees(angle1))
        angle2_deg = int(np.degrees(angle2))
        
        hint1 = Text(f"{angle1_deg}°", font_size=20, color=BLUE)
        hint1.next_to(circle1, DOWN, buff=0.2)
        
        hint2 = Text(f"{angle2_deg}°", font_size=20, color=YELLOW)
        hint2.next_to(circle2, DOWN, buff=0.2)
        
        self.play(Write(hint1), Write(hint2))
        self.wait(2)
        
        # Reveal answer
        if is_congruent:
            answer = Text("CONGRUENT", font_size=32, color=GREEN)
            checkmark = Text("✓", font_size=40, color=GREEN)
        else:
            answer = Text("NOT CONGRUENT", font_size=32, color=RED)
            checkmark = Text("✗", font_size=40, color=RED)
        
        answer.move_to((pos1 + pos2) / 2 + DOWN * 2)
        checkmark.next_to(answer, LEFT, buff=0.3)
        
        self.play(Write(answer), Write(checkmark))
        self.wait(2)
        
        # Clear exercise
        self.play(
            FadeOut(VGroup(circle1, circle2, arc1, arc2, pair_label, hint1, hint2, answer, checkmark))
        )
        self.wait(0.5)

    def scene_6_recap(self):
        # Scene 6 title
        scene_title = Text("Scene 6: Recap and Key Points", font_size=36, color=GREEN)
        scene_title.to_edge(UP)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Key points
        key_points = VGroup(
            Text("• Arc: Part of a circle between two points", font_size=24, color=WHITE),
            Text("• Congruent arcs have equal central angles", font_size=24, color=WHITE),
            Text("• Congruent arcs have equal lengths", font_size=24, color=WHITE),
            Text("• Arc length = (central angle/360°) × circumference", font_size=24, color=WHITE)
        )
        
        key_points.arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        key_points.move_to(ORIGIN)
        
        # Animate each point
        for point in key_points:
            self.play(Write(point))
            self.wait(1)
        
        self.wait(2)
        
        # Clear scene
        self.play(FadeOut(VGroup(scene_title, key_points)))
        self.wait(1)

    def scene_7_closing(self):
        # Scene 7 title
        scene_title = Text("Scene 7: Closing Remarks", font_size=36, color=GREEN)
        scene_title.to_edge(UP)
        
        self.play(Write(scene_title))
        self.wait(1)
        
        # Final message
        final_message = VGroup(
            Text("Remember:", font_size=32, color=YELLOW),
            Text("Congruent arcs must have", font_size=28, color=WHITE),
            Text("equal central angles and equal lengths", font_size=28, color=WHITE)
        )
        
        final_message.arrange(DOWN, buff=0.5)
        final_message.move_to(ORIGIN)
        
        self.play(Write(final_message))
        self.wait(3)
        
        # Thank you message
        thank_you = Text("Thank you for learning with us!", font_size=32, color=BLUE)
        thank_you.move_to(DOWN * 2)
        
        self.play(Write(thank_you))
        self.wait(2)
        
        # Gentle fade out
        self.play(
            FadeOut(VGroup(scene_title, final_message, thank_you)),
            run_time=3
        )
        self.wait(1)


# Additional scene class for modular use
class Scene1IntroductionToArcs(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_1_introduction_to_arcs()


class Scene2DefiningCongruentArcs(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_2_defining_congruent_arcs()


class Scene3DegreesAndLength(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_3_degrees_and_length()


class Scene4Examples(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_4_examples()


class Scene5Exercise(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_5_exercise()


class Scene6Recap(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_6_recap()


class Scene7Closing(Scene):
    def construct(self):
        animation = CongruenceOfArcs()
        animation.scene_7_closing()