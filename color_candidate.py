import random
import pyray as pr
from utils import wes_anderson


class Cell:
    """
    - this class describes a given color choice from a color ("R", "G", "B") component
    - it has a collision detection with the mouse
    - once collision + mouse pressed, the cell is locked, meaning is not not clickable anymore
    """

    def __init__(
        self,
        id: int,
        position: pr.Vector2,
        size: pr.Vector2,
        offset_x: int,
        offset_y: int,
        color: pr.Color,
    ) -> None:
        self.id = id
        self.position = position
        self.size = size
        self.color = color
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.state_changed: bool = False
        self.is_clicked: bool = False
        self.is_highlighted: bool = False
        self.is_disable: bool = False
        self.rect = pr.Rectangle(
            self.position.x + self.offset_x,
            self.position.y + self.offset_y,
            self.size.x,
            self.size.y,
        )

    def get_colored_clicked(self) -> None:
        if self.is_clicked:
            return self.color

    def update(self) -> None:
        # print(f"{pr.check_collision_point_rec(pr.get_mouse_position(), self.rect)}, {pr.is_mouse_button_pressed(0)}")
        if not self.is_disable:
            if pr.check_collision_point_rec(pr.get_mouse_position(), self.rect):
                self.is_highlighted = True
                if pr.is_mouse_button_pressed(0):
                    self.state_changed = not self.state_changed
                    self.is_clicked = True
                    self.is_disable = True
            else:
                self.is_highlighted = False

    def draw(self):
        pr.draw_rectangle_rec(self.rect, self.color)
        if self.is_highlighted:
            pr.draw_rectangle_lines_ex(self.rect, 2, pr.RAYWHITE)
        if self.is_clicked:
            pr.draw_text(
                f"{self.color.r},{self.color.g},{self.color.b}",
                int(self.rect.x) + 5,
                int(self.rect.y) + 5,
                10,
                pr.BLACK,
            )
            # pr.draw_text(
            #     f"id={self.id}",
            #     int(self.rect.x) + 5,
            #     int(self.rect.y) + 20,
            #     10,
            #     pr.BLACK,
            # )


class ColorContainer:
    """
    - this class describes a set of 4 color component
    - one of the cell has the real color componet, while the others are fake
        - initially I was thinking to add the same color compoenent, i.e shades of red, blue, etc .. but after testing it made the choice more difficult
    - the real color compoenent is located randomly inside the 4 choices
    """

    def __init__(
        self,
        position: pr.Vector2,
        value: int,
        outline_color: pr.Color,
        base_color: pr.Color,
        color_target: str,
    ) -> None:
        self.position = position
        self.value = value
        self.outline_color = outline_color
        self.base_color = base_color
        self.color_target = color_target
        self.interactive_area: list[Cell] = []  # make_cells()
        self.is_picked: bool = False
        self.colored_picked: pr.Color = None
        self.id_picked: int = None

    def make_cells(self) -> list[Cell]:
        # randomize the position of the true value
        indices: list[int] = [0, 1, 2, 3]
        true_pos = random.choice(indices)
        indices.remove(true_pos)
        print(f"{true_pos=}, {indices=}")
        cells_position_offset = [
            [20, 20],
            [20 + 80, 20],
            [20, 20 + 80],
            [20 + 80, 20 + 80],
        ]

        # add true cell
        self.interactive_area.append(
            Cell(
                id=true_pos,
                position=pr.Vector2(self.position.x, self.position.y),
                size=pr.Vector2(80, 80),
                offset_x=cells_position_offset[true_pos][0],
                offset_y=cells_position_offset[true_pos][1],
                color=self.base_color,
            )
        )
        # add fake cells
        for i in indices:
            self.interactive_area.append(
                Cell(
                    id=i,
                    position=pr.Vector2(self.position.x, self.position.y),
                    size=pr.Vector2(80, 80),
                    offset_x=cells_position_offset[i][0],
                    offset_y=cells_position_offset[i][1],
                    color=random.choice(wes_anderson),
                )
            )

    def get_colored_picked(self) -> pr.Color:
        if self.is_picked:
            return self.colored_picked

    def update(self) -> None:
        # check if any cell has been clicked
        if not any([c.is_disable for c in self.interactive_area]):
            _ = [c.update() for c in self.interactive_area]

            # find the id and color of the cell that has been clicked
            clicked_vals = [c.is_disable for c in self.interactive_area]
            current_index = clicked_vals.index(any(clicked_vals))
            current_col = self.interactive_area[current_index].get_colored_clicked()

            self.id_picked = current_index
            self.colored_picked = current_col
        else:
            pass
            # if a choice has been made, we display it
            self.is_picked = True
            # print(f"ColorContainer -> id picked: {self.id_picked}, colored picked: {self.colored_picked}")

    def draw(self) -> None:
        # outline
        # rect = pr.Rectangle(self.position.x, self.position.y, 200, 200)
        # pr.draw_rectangle_lines_ex(rect, 1, self.outline_color)
        pr.draw_text(
            f"Choose the {self.color_target}\n component",
            int(self.position.x) + 40,
            int(self.position.y) + 200,
            20,
            pr.RAYWHITE,
        )
        _ = [c.draw() for c in self.interactive_area]
