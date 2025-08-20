
from pathlib import Path

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt

from .colors import cps_colors, tud_colors
from .colors import scale_hls as scale_hls

# Set the CPS sytle
plt.style.use(Path(__file__).parent / "cps.mplstyle")

# Updated the named colors
mcolors.get_named_colors_mapping().update(cps_colors)
mcolors.get_named_colors_mapping().update(tud_colors)