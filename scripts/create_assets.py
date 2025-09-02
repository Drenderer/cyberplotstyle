"""Generates the color tables for the documentation."""

from pathlib import Path

from matplotlib import pyplot as plt

import cyberplotstyle
from cyberplotstyle.tools import plot_colormap, plot_colortable

# plt.style.use("cyberplotstyle.presentation")

ASSET_PATH = Path(__file__).parent.parent / "assets"

fig = plot_colortable(cyberplotstyle.tud_colors, sort_colors=False)
fig.savefig(ASSET_PATH / "tud_colors.png")

fig = plot_colortable(cyberplotstyle.cps_colors, sort_colors=False)
fig.savefig(ASSET_PATH / "cps_colors.png")

fig = plot_colormap(cyberplotstyle.colormaps["cps:seismic"])
fig.savefig(ASSET_PATH / "cps_seismic.png", bbox_inches="tight")