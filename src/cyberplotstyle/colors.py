import colorsys
import math

import matplotlib.colors as mcolors
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.typing import ColorType

cps_colors = {
    "cps:darkblue": "#435384",
    "cps:red": "#c24c4c",
    "cps:lightblue": "#688fc6",
    "cps:orange": "#f6a315",
    "cps:green": "#16a48a",
    "cps:grey": "#cccccc",
    "cps:black": "#000000",
}

# TU Darmstadt colors from "https://www.intern.tu-darmstadt.de/media/medien_stabsstelle_km/services/medien_cd/das_bild_der_tu_darmstadt.pdf"
tud_colors = {
    "tud:1a": "#5D85C3",
    "tud:2a": "#009CDA",
    "tud:3a": "#50B695",
    "tud:4a": "#AFCC50",
    "tud:5a": "#DDDF48",
    "tud:6a": "#FFE05C",
    "tud:7a": "#F8BA3C",
    "tud:8a": "#EE7A34",
    "tud:9a": "#E9503E",
    "tud:10a": "#C9308E",
    "tud:11a": "#804597",
    "tud:1b": "#005AA9",
    "tud:2b": "#0083CC",
    "tud:3b": "#009D81",
    "tud:4b": "#99C000",
    "tud:5b": "#C9D400",
    "tud:6b": "#FDCA00",
    "tud:7b": "#F5A300",
    "tud:8b": "#EC6500",
    "tud:9b": "#E6001A",
    "tud:10b": "#A60084",
    "tud:11b": "#721085",
    "tud:1c": "#004E8A",
    "tud:2c": "#00689D",
    "tud:3c": "#008877",
    "tud:4c": "#7FAB16",
    "tud:5c": "#B1BD00",
    "tud:6c": "#D7AC00",
    "tud:7c": "#D28700",
    "tud:8c": "#CC4C03",
    "tud:9c": "#B90F22",
    "tud:10c": "#951169",
    "tud:11c": "#611C73",
    "tud:1d": "#243572",
    "tud:2d": "#004E73",
    "tud:3d": "#00715E",
    "tud:4d": "#6A8B22",
    "tud:5d": "#99A604",
    "tud:6d": "#AE8E00",
    "tud:7d": "#BE6F00",
    "tud:8d": "#A94913",
    "tud:9d": "#961C26",
    "tud:10d": "#732054",
    "tud:11d": "#4C226A",
}

# Copied from matplotlib docs: https://matplotlib.org/stable/gallery/color/named_colors.html
def plot_colortable(colors, *, ncols=4, sort_colors=True):
    """Plot a table listing the colors with their names.

    Args:
        colors: `Dict` of colors.
        ncols: Number of columns in the colortable. Defaults to 4.
        sort_colors: If true sorts the colors by their HSV values. Defaults to True.

    Returns:
        Figure.

    """
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by hue, saturation, value and name.
    if sort_colors is True:
        names = sorted(
            colors, key=lambda c: tuple(mcolors.rgb_to_hsv(mcolors.to_rgb(c)))
        )
    else:
        names = list(colors)

    n = len(names)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(
        margin / width,
        margin / height,
        (width - margin) / width,
        (height - margin) / height,
    )
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.0)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, name in enumerate(names):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(
            text_pos_x,
            y,
            name,
            fontsize=14,
            horizontalalignment="left",
            verticalalignment="center",
        )

        ax.add_patch(
            Rectangle(
                xy=(swatch_start_x, y - 9),
                width=swatch_width,
                height=18,
                facecolor=colors[name],
                edgecolor="0.7",
            )
        )

    return fig

def scale_hls(
    color: ColorType, hue: float = 1.0, lightness: float = 1.0, saturation: float = 1.0
) -> tuple[float, float, float, float]:
    """Return a color with rescaled hue, lightness and/or saturation.

    Args:
        color: Matplotlib color.
        hue: Factor the hue is scaled with.
            Defaults to `1.0`.
        lightness: Factor the lightness is sacaled with.
            Defaults to `1.0`.
        saturation: Factor the saturation is scaled with.
            Defaults to `1.0`.

    Returns:
        Adjusted color, as RGBA tuple.

    """
    r, g, b, a = mcolors.to_rgba(color)
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    h = max(0, min(1, h * hue))
    l = max(0, min(1, l * lightness))
    s = max(0, min(1, s * saturation))
    return colorsys.hls_to_rgb(h, l, s) + (a,)
