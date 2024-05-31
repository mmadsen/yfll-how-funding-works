from manim import *
import time
import numpy as np


from yfll.text import to_text
from yfll.utils import partition_iterable_equal_chunks

BUDGET_FRACTIONS = [0.65, 0.07, 0.04, 0.028, 0.038, 0.167]
BUDGET_LABELS = ["Personnel", "Collections", "Technology", "Programs", "Facilities", "Miscellaneous"]
TOTAL_BOOKS_TO_SHOW = 100
BOOK_COLORS = ["purple", "red", "yellow", "orange", "blue", "campaign-teal"]


class LibraryBudget(Scene):
    def construct(self):
        self.main_title("What Makes Up The Library Budget?")
        self.pie_chart()

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


    def book_test(self):
        # just a test, show an array of book icons
        books = self.get_colored_book_array()
        for group in books:
            self.add(group)
            self.wait(0.2)
        final_group = books[-1]
        first_elem = final_group[0]
        last_elem = final_group[-1]
        line = Line(first_elem.get_center(), last_elem.get_center(), color=GOLD)
        brace = Brace(line, sharpness=0.7)
        b1_text = brace.get_text("2023 Expenses: \$1,860,000").scale(0.5)
        self.add(brace, b1_text)
        self.wait(10)


    def get_colored_book_array(self):
        w = 0.2
        # calculate the number of books of each color
        fractions = np.array(BUDGET_FRACTIONS)
        num_books_each_type = fractions * TOTAL_BOOKS_TO_SHOW
        rounded_each_type = np.round(num_books_each_type, 0)
        books = []
        for num, color in zip(rounded_each_type, BOOK_COLORS):
            print(f"{num} of {color}")
            books.extend([SVGMobject(f"assets/icons8-book-{color}.svg").set(width=w) for i in range(int(num))])

        print(f"books: {books}")

        groups = partition_iterable_equal_chunks(books, 10, return_list=True)
        print(groups)
        final_vgroups = []
        first_row = True
        cur_row = None 

        for g in groups:
            print(g)
            if first_row is True:
                vg = VGroup(*g).arrange(RIGHT, buff=0.2).to_edge(UL, buff=0.25)
                cur_row = vg
                first_row = False
            else:
                vg = VGroup(*g).arrange(RIGHT, buff=0.2).next_to(cur_row, DOWN, buff=0.25)
                cur_row = vg
            final_vgroups.append(vg)
        print(final_vgroups)
        return final_vgroups


    def get_book_array(self, book_color):
        w = 0.2
        result = []
        row1 = (
            VGroup(
                *[
                    SVGMobject(f"assets/icons8-book-{book_color}.svg").set(width=w)
                    for i in range(10)
                ]
            )
            .arrange(RIGHT, buff=0.2)
            .to_edge(UL, buff=0.25)
        )
        result.append(row1)
        prev_row = row1
        for i in range(9):
            row = (
                VGroup(
                    *[
                        SVGMobject(f"assets/icons8-book-{book_color}.svg").set(width=w)
                        for i in range(10)
                    ]
                )
                .arrange(RIGHT, buff=0.2)
                .next_to(prev_row, DOWN, buff=0.25)
            )
            result.append(row)
            prev_row = row
        return result

    def pie_chart(self):
        Sector.set_default(inner_radius=0, outer_radius=3, stroke_width=2, fill_opacity=0.7, stroke_color=GREY_BROWN)

        init_values = [100, 0, 0, 0, 0, 0]
        colors = [ManimColor.from_hex("#138d8c"), BLUE_D, GREEN_D, GOLD_D, MAROON_D, PURPLE_D]
        init_total = sum(init_values)
        init_angles = [360 * value / init_total for value in init_values]
        init_sangles = [sum(init_angles[:i]) for i in range(len(init_angles))]

        final_values = [0.65, 0.07, 0.04, 0.028, 0.038, 0.167]
        final_total = sum(final_values)
        final_angles = [360 * value / final_total for value in final_values]
        final_sangles = [sum(final_angles[:i]) for i in range(len(final_angles))]

        sectors = VGroup()
        for value, init_angle, init_sangle, final_angle, final_sangle, color in zip(init_values, init_angles,
                                                                                    init_sangles, final_angles,
                                                                                    final_sangles, colors):
            sector = Sector(
                start_angle=init_sangle * DEGREES,
                angle=init_angle * DEGREES,
                color=color,
            )
            sector.init_angle = init_angle
            sector.init_sangle = init_sangle
            sector.final_angle = final_angle
            sector.final_sangle = final_sangle
            sectors.add(sector)

        for sector in sectors:
            sector.save_state()

        def update_sector(sector, alpha):
            sector.restore()
            angle = interpolate(sector.init_angle * DEGREES, sector.final_angle * DEGREES, alpha)
            start_angle = interpolate(sector.init_sangle * DEGREES, sector.final_sangle * DEGREES, alpha)
            sector.become(
                Sector(
                    start_angle=start_angle,
                    angle=angle,
                    color=sector.color,
                )
            )

        def get_sector_centers(sectors):
            centers = [sec.get_center() for sec in sectors]
            return centers

        # -------------------- Animation --------------------
        circle = Circle(radius=3, color=GREY_BROWN, stroke_width=5)
        title = Text("Library Budget").scale(0.8).to_edge(UL, buff=0.25)
        self.play(Create(sectors))
        self.add(circle, title)
        self.wait(1)
        self.play(
            UpdateFromAlphaFunc(sectors[0], update_sector),
            UpdateFromAlphaFunc(sectors[1], update_sector),
            UpdateFromAlphaFunc(sectors[2], update_sector),
            UpdateFromAlphaFunc(sectors[3], update_sector),
            UpdateFromAlphaFunc(sectors[4], update_sector),
            UpdateFromAlphaFunc(sectors[5], update_sector)
        )
        self.wait(1)

        # add labels for sectors
        sector_labels = VGroup().arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        sector_arrows = VGroup() 
        sector_centers = get_sector_centers(sectors)
        prev_sector = None
        i = 0
        for sector in sectors:
            start = sector_centers[i]
            if prev_sector is None:
                sector_text = Text(BUDGET_LABELS[i]).scale(0.4).next_to(circle, UR * 1.2, buff = 0.5, aligned_edge=LEFT)
                sector_labels.add(sector_text)
                prev_sector = sector_text
            else:
                sector_text = Text(BUDGET_LABELS[i]).scale(0.4).next_to(prev_sector, DOWN * 4, buff = 0.25, aligned_edge=LEFT)
                sector_labels.add(sector_text)
                prev_sector = sector_text
            end = sector_text.get_edge_center(DL)
            sector_arrow = Line(start=end + (LEFT * 0.2), end=start)
            sector_arrows.add(sector_arrow)
            i += 1

        self.add(sector_labels, sector_arrows)
        self.wait(1)
