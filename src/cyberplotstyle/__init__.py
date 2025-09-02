
from pathlib import Path
from warnings import warn

import matplotlib as mpl
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

from .colormaps import colormaps
from .colors import cps_colors as cps_colors
from .colors import tud_colors as tud_colors
from .tools import scale_hls as scale_hls

# Activate CPS sytle
plt.style.use(Path(__file__).parent / "cps.mplstyle")

# Register named colors
mcolors.get_named_colors_mapping().update(cps_colors)
mcolors.get_named_colors_mapping().update(tud_colors)

# Register colormaps
for name, cmap in colormaps.items():
    try:
        mpl.colormaps.register(cmap, name=name, force=False)
    except ValueError as e:
        warn(f"A colormap with name '{name}' is already registered: {e}")