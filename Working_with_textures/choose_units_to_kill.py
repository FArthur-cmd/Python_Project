import pygame

from Working_with_textures.draw_button2 import draw_button2

from Working_with_textures.draw_some_buttons import draw_some_buttons
from Working_with_textures.NewField import create_window_of_Field


def choose_units_to_kill(window, fullscreen, units, length=800, height=600,
                         k=1):
    window = create_window_of_Field(window, fullscreen, "Field", length,
                                    height)
    pygame.display.update()
    size_of_cell = (height * 5 // 6) // 10
    size = (length - size_of_cell * 12) // 2
    if len(units) > 4:
        buttons = draw_some_buttons(window, 4,
                                    [units[0].base.name, units[1].base.name,
                                     units[2].base.name, units[3].base.name],
                                    (-15, 0, size + 23, size_of_cell * 4),
                                    255, 215, 0, 85, 107, 47, int(12 * k))
        names = []
        for i in units[4:]:
            names += [i.base.name]
        if len(units) == 5:
            buttons += draw_some_buttons(window, len(names), names,
                                         (length - size - 15, 0, size + 23,
                                             size_of_cell + 20),
                                         255, 215, 0, 85, 107, 47, int(12 * k))
        else:
            buttons += draw_some_buttons(window, len(names), names,
                                         (length - size - 15, 0, size + 23,
                                             size_of_cell * len(names)),
                                         255, 215, 0, 85, 107, 47, int(12 * k))
    else:
        names = []
        for i in units:
            names += [i.base.name]
        buttons = draw_some_buttons(window, len(names),
                                    names,
                                    (-15, 0, size + 23, size_of_cell * len(units)),
                                    255, 215, 0, 85, 107, 47, int(12 * k))

    buttons += draw_some_buttons(window, 1, ["End"],
                                 (length - size, size_of_cell * 4 + 10, size,
                                  int(75 * k)),
                                 255, 215, 0, 85, 107, 47,
                                 int(15 * k))

    buttons += draw_button2(window, fullscreen,
                            (length - size, height - int(75 * k), size,
                             int(75 * k)),
                            "EXIT")
    pygame.display.update()
    return buttons
