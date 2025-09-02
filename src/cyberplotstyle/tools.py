import colorsys
import math

import matplotlib.colors as mcolors
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.typing import ColorType


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

def plot_colormap(cmap):
    fig, ax = plt.subplots(figsize=(6, 1))
    fig.subplots_adjust(bottom=0.5)

    norm = mcolors.Normalize(vmin=0, vmax=1)

    fig.colorbar(
        plt.cm.ScalarMappable(norm=norm, cmap=cmap),
        cax=ax, orientation="horizontal"
    )
    fig.suptitle(cmap.name, y=1.1)

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