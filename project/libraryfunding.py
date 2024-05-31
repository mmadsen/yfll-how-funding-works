from manim import *
import time
import numpy as np


from yfll.text import to_text


class LibraryFunding(Scene):
    def construct(self):
        self.main_title("How Library Funding Works")
        self.introduction()
        self.construct_abstract_scenario_graph()
        self.conclusion()

    def main_title(self, title_text, draft_mode=False):
        colophon = (
            to_text(
                "Produced by Yes For Library Levy, P.O. Box 2083, Friday Harbor WA 98250"
            )
            .scale(0.2)
            .move_to((2.75, -3.5, 0))
        )
        DRAFT = (
            to_text("DRAFT ONLY", color=RED, slant=ITALIC)
            .scale(0.7)
            .move_to((-5, 3.5, 0))
        )
        logo = (
            ImageMobject("assets/YesLibraryWeb3.png")
            .scale(0.2)
            .move_to((6.25, -3.5, 0))
        )

        # Main title
        title = Text(title_text, weight=BOLD).scale(1.2)
        self.add(title)
        self.add(colophon)
        self.add(logo)
        if draft_mode is True:
            self.add(DRAFT)
        self.wait(4)
        self.play(FadeOut(title, shift=DOWN * 2, scale=1.5))
        self.remove(*self.mobjects)

    def introduction(self):
        # Orientation
        l1 = to_text("Our library is funded by property taxes.").scale(0.5)
        l2 = to_text("Each year, by law, the Library levy amount equals").scale(0.5)
        l3 = to_text("the previous year's revenue plus 1%, and a small amount").scale(
            0.5
        )
        l4 = to_text(
            "that covers new construction.  This is independent of property values."
        ).scale(0.5)

        first_group = (
            VGroup(l1, l2, l3, l4)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, 2.1, 0), aligned_edge=LEFT)
        )

        l5 = to_text(
            "Unfortunately, actual expenses increase by more than 1% each year."
        ).scale(0.5)
        l6 = to_text("Some expenses are discretionary, but most are not.").scale(0.5)
        l7 = to_text("Expenses tend to grow by 5-7% annually.").scale(0.5)

        second_group = (
            VGroup(l5, l6, l7)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, -0.25, 0), aligned_edge=LEFT)
        )

        l8 = to_text("Over time, the Library must either consume its reserves").scale(
            0.5
        )
        l9 = to_text(
            "or cut services, staff, or hours.  When those reserves are gone, the"
        ).scale(0.5)
        l10 = to_text(
            "Library must return to the voters to increase its property tax levy."
        ).scale(0.5)
        l12 = to_text("This last occurred in 2011.").scale(0.5)

        third_group = (
            VGroup(l8, l9, l10, l12)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, -2.5, 0), aligned_edge=LEFT)
        )

        l11 = (
            to_text(
                "Now, let's see an example of how this works over time...", w=SEMIBOLD
            )
            .scale(0.6)
            .move_to((0, 0, 0))
        )

        self.add(first_group)
        self.wait(15)
        first_group.color = GREY
        self.add(second_group)
        self.wait(15)
        second_group.color = GREY
        self.add(third_group)
        self.wait(15)
        self.remove(first_group, second_group, third_group)
        self.add(l11)
        self.wait(6)

        self.remove(*self.mobjects)

    def construct_abstract_scenario_graph(self):
        # Orientation
        l1 = to_text(
            "This scenario shows how the balance between revenue and expenses"
        ).scale(0.5)
        l12 = to_text(
            "leads to a cycle where the Library comes to voters every 10-15 years."
        ).scale(0.5)

        first_group = (
            VGroup(l1, l12)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, 2.5, 0), aligned_edge=LEFT)
        )

        l8 = to_text("-  The scenario begins right after a levy adjustment").scale(0.5)
        l2 = to_text("-  Reserves at the beginning are down to $200,000").scale(0.5)
        l3 = to_text("-  Revenue from property taxes grows at 1% per year").scale(0.5)
        l4 = to_text("-  Expenses grow at 5%").scale(0.5)

        assumptions_group = (
            VGroup(l8, l2, l3, l4)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.3)
            .move_to((-5.5, 0, 0), aligned_edge=LEFT)
        )

        l5 = to_text(
            "Watch how reserves grow for the first few years.  But then, as expenses"
        ).scale(0.5)
        l6 = to_text(
            "exceed revenue, reserves are used for operations and eventually"
        ).scale(0.5)
        l7 = to_text(
            "the Library needs to come back to voters in order to maintain services."
        ).scale(0.5)

        second_group = (
            VGroup(l5, l6, l7)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, -2.5, 0), aligned_edge=LEFT)
        )

        self.add(first_group)
        self.add(assumptions_group)
        self.add(second_group)
        self.wait(15)
        self.remove(*self.mobjects)

        # ============ Revenue and Expense In the Abstract =====================
        # Axes
        ax = Axes(
            x_range=[1, 16, 2],
            y_range=[1000000, 2500000, 250000],
            x_length=9,
            y_length=6,
            x_axis_config={
                "numbers_to_include": np.arange(1, 18, 2),
                "decimal_number_config": {
                    "group_with_commas": False,
                    "num_decimal_places": 0,
                },
            },
            y_axis_config={"numbers_to_include": np.arange(1000000, 2500000, 250000)},
            tips=False,
        )

        # LEGEND
        revenue_legend = to_text("Revenue", color=GREEN).scale(0.5)
        expense_legend = to_text("Expense", color=YELLOW).scale(0.5)
        legend_group = (
            VGroup(revenue_legend, expense_legend)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-3.4, 0.25, 0))
        )
        year_axis_label = to_text("Years").scale(0.7).move_to((5.75, -3, 0))

        # RESERVE BALANCE
        starting_reserves = 200000
        tracker = ValueTracker(starting_reserves)

        bar_color = GREEN

        bar_chart = always_redraw(
            lambda: BarChart(
                values=[tracker.get_value()],
                bar_names=["Reserve \$"],
                bar_colors=[bar_color],
                y_range=[0, 1600000, 200000],
            ).move_to((5.6, 1, 0))
        )
        bar_labels = bar_chart.get_bar_labels()

        # Revenue Data
        starting_revenue = 1600000
        starting_expense = 1300000
        reserves_tracking = [starting_reserves]
        rev_x_vals = [1]
        rev_y_vals = [starting_revenue]
        exp_x_vals = [1]
        exp_y_vals = [starting_expense]

        cur_year = rev_x_vals[0]
        cur_rev = starting_revenue
        cur_exp = starting_expense
        cur_reserves = starting_reserves

        while cur_year < 13:
            cur_year += 1
            new_rev = int(cur_rev + (cur_rev * 0.015))
            new_exp = int(cur_exp + (cur_exp * 0.05))
            new_res = cur_reserves + (new_rev - new_exp)
            print(f"new res: {new_res} cur_reserves: {cur_reserves}")

            rev_x_vals.append(cur_year)
            rev_y_vals.append(new_rev)
            exp_x_vals.append(cur_year)
            exp_y_vals.append(new_exp)
            reserves_tracking.append(new_res)
            cur_reserves = new_res
            cur_rev = new_rev
            cur_exp = new_exp
        print("REVENUE MODEL")
        print(rev_x_vals)
        print(rev_y_vals)
        print("EXPENSE MODEL")
        print(exp_x_vals)
        print(exp_y_vals)
        print("RESERVES MODEL")
        print(reserves_tracking)

        # Plot over time
        self.add(ax)
        self.add(year_axis_label)
        self.add(legend_group)
        self.add(bar_chart)

        cur_year = 0
        first_pos_flag = False
        first_neg_flag = False

        add_reserves_text = (
            to_text(
                "At first, revenue is greater than expenses, adding to reserves",
                w=SEMIBOLD,
                color=GREEN,
            )
            .scale(0.3)
            .move_to((-0.75, -2.5, 0))
        )
        drain_reserves_text = (
            to_text(
                "Later, reserves are used to cover expenses", w=SEMIBOLD, color=YELLOW
            )
            .scale(0.3)
            .move_to((1.25, -1.5, 0))
        )
        next_levy_adj = to_text(
            "When reserves are almost gone, a levy adjustment is needed",
            w=SEMIBOLD,
            color=RED,
        ).scale(0.3)
        next_levy_adj_2 = to_text(
            "to replenish reserves, and start the cycle over again",
            w=SEMIBOLD,
            color=RED,
        ).scale(0.3)
        next_levy_vgroup = (
            VGroup(next_levy_adj, next_levy_adj_2)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((1.25, -1.5, 0))
        )

        for cur_year in rev_x_vals:
            rev_line = ax.plot_line_graph(
                x_values=rev_x_vals[0:cur_year],
                y_values=rev_y_vals[0:cur_year],
                line_color=GREEN,
            )
            exp_line = ax.plot_line_graph(
                x_values=exp_x_vals[0:cur_year],
                y_values=exp_y_vals[0:cur_year],
                line_color=YELLOW,
            )
            self.add(ax, rev_line, exp_line)

            reserve_impact = rev_y_vals[cur_year - 1] - exp_y_vals[cur_year - 1]
            self.play(tracker.animate.set_value(reserves_tracking[cur_year - 1]))
            if reserve_impact > 0:
                if first_pos_flag is False:
                    first_pos_flag = True
                    self.add(add_reserves_text)
            if reserve_impact < 0:
                if first_neg_flag is False:
                    first_neg_flag = True
                    self.remove(add_reserves_text)
                    self.add(drain_reserves_text)
                    bar_color = RED
            if tracker.get_value() < 200000:
                break
            cur_year += 1
            self.wait(1)

        self.remove(drain_reserves_text)
        self.add(next_levy_vgroup)
        self.wait(12)
        self.remove(*self.mobjects)

    def conclusion(self):
        logo = (
            ImageMobject("assets/YesLibraryWeb3.png")
            .scale(0.3)
            .move_to((-1.5, -3.3, 0))
        )

        l1 = to_text(
            "The Library last came to voters in 2011, and that levy adjustment"
        ).scale(0.5)
        l2 = to_text("created reserves that were intended to last through 2018.").scale(
            0.5
        )

        first_group = (
            VGroup(l1, l2)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, 2.75, 0), aligned_edge=LEFT)
        )

        l5 = to_text(
            "With careful budgeting the reserves have lasted much longer."
        ).scale(0.5)
        l7 = to_text("But reserves will be exhausted by next year.").scale(0.5)
        l4 = to_text(
            "The Library is asking voters to approve a levy adjustment on August 6th."
        ).scale(0.5)

        second_group = (
            VGroup(l5, l7, l4)
            .arrange(DOWN, aligned_edge=LEFT, buff=0.2)
            .move_to((-6.5, 0.5, 0), aligned_edge=LEFT)
        )

        l8 = to_text(
            "Learn more at the Library's website: sjlib.org/levylidlift"
        ).scale(0.5)
        l9 = to_text(
            "VOTE YES on August 6th", w=SEMIBOLD, color=ManimColor.from_hex("#138d8c")
        ).scale(0.8)

        third_group = VGroup(l8, l9).arrange(DOWN, buff=0.4).move_to((0, -1.75, 0))

        l10 = (
            to_text("yesforlibrarylevy.org", color=ManimColor.from_hex("#138d8c"))
            .scale(0.5)
            .move_to((1.5, -3.3, 0))
        )

        self.add(first_group)
        self.add(second_group)
        self.add(third_group)
        self.add(logo)
        self.add(l10)
        self.wait(10)
