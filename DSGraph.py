from manim import *


class SupplyDemandGraph(Scene):
    def construct(self):
        # Set background color to white
        self.camera.background_color = "#f1f2f3"

        axes = Axes(
            x_range=[0, 15, 1],
            y_range=[0, 10, 1],
            axis_config={"include_tip": False, "color": BLACK},
        )

        labels = axes.get_axis_labels(
            x_label="Quantity", y_label="Price"
        ).set_color(BLACK)  # Set label color to black

        # Demand curve
        demand_curve = axes.plot(lambda x: 10 - x,x_range=[0,10], color=BLUE)
        demand_label = axes.get_graph_label(
            demand_curve, label="Demand", x_val=6, direction=RIGHT
        ).set_color(BLACK)  # Set label color to black
        demand_label.shift(RIGHT * 0.5)

        # Original Supply curve
        supply_curve = axes.plot(lambda x: x,x_range=[0,10], color=RED)
        supply_label = axes.get_graph_label(
            supply_curve, label="Supply", x_val=4, direction=UR*10
        ).set_color(BLACK)  # Set label color to black
        supply_label.shift(DOWN * 0.5)

        # Shifted Supply curve (parallel to the original supply curve)
        shifted_supply_curve = axes.plot(lambda x: x + 2,x_range=[0,9], color=RED_E)  # Shifted 2 units to the left
        shifted_supply_label = axes.get_graph_label(
            shifted_supply_curve, label="Supply '", x_val=6,direction=UL*2
        ).set_color(BLACK)
        shifted_supply_label.shift(DOWN * 0.5)

        # Equilibrium dot for original supply-demand curve
        equilibrium1 = Dot(axes.coords_to_point(5, 5), color=YELLOW)
        equilibrium_label1 = MathTex("E").set_color(BLACK)  # Set label color to black
        equilibrium_label1.next_to(equilibrium1,LEFT*0.25)
        equilibrium_label1.shift(UR * 0.25)

        equilibrium2 = Dot(axes.coords_to_point(4, 6), color=YELLOW_A)
        equilibrium_label2 = MathTex("E '").set_color(BLACK)  # Set label color to black
        equilibrium_label2.next_to(equilibrium2,LEFT*0.25)
        equilibrium_label2.shift(UR * 0.25)

        # Dashed lines from equilibrium to axes (Q, P)
        dashed_line_to_x1 = DashedLine(
            start=equilibrium1.get_center(), 
            end=axes.coords_to_point(5, 0),  # Project to x-axis
            color=BLACK
        )
        dashed_line_to_y1 = DashedLine(
            start=equilibrium1.get_center(), 
            end=axes.coords_to_point(0, 5),  # Project to y-axis
            color=BLACK
        )

        dashed_line_to_x2 = DashedLine(
            start=equilibrium2.get_center(), 
            end=axes.coords_to_point(4, 0),  # Project to x-axis
            color=BLACK
        )
        dashed_line_to_y2 = DashedLine(
            start=equilibrium2.get_center(), 
            end=axes.coords_to_point(0, 6),  # Project to y-axis
            color=BLACK
        )

        # Labels for Q and P
        q_label1 = MathTex("Q_1").next_to(axes.coords_to_point(5, 0), DOWN).set_color(BLACK)
        p_label1 = MathTex("P_1").next_to(axes.coords_to_point(0, 5), LEFT).set_color(BLACK)
        q_label2 = MathTex("Q_2").next_to(axes.coords_to_point(4, 0), DOWN).set_color(BLACK)
        p_label2 = MathTex("P_2").next_to(axes.coords_to_point(0, 6), LEFT).set_color(BLACK)
        
        # Play all animations
        self.play(Create(axes), Write(labels),run_time=1)
        self.play(Create(demand_curve), Write(demand_label),run_time=1)
        self.play(Create(supply_curve), Write(supply_label),run_time=1)
        self.play(Create(shifted_supply_curve), Write(shifted_supply_label),run_time=1)
        self.play(FadeIn(equilibrium1, equilibrium_label1),run_time=0.5)
        self.play(FadeIn(equilibrium2, equilibrium_label2),run_time=0.5)

        # Show dashed lines and labels
        self.play(Create(dashed_line_to_x1), Create(dashed_line_to_y1),run_time=1)
        self.play(Write(q_label1), Write(p_label1),run_time=1)
        self.play(Create(dashed_line_to_x2), Create(dashed_line_to_y2),run_time=1)
        self.play(Write(q_label2), Write(p_label2),run_time=1)
        self.wait(2)
