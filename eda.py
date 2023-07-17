# imports
import ibis

import seaborn as sns

import altair as alt
import plotly.io as pio
import plotly.express as px
import ibis.selectors as s
import matplotlib.pyplot as plt

from datetime import datetime, timedelta

# options
## ibis config
ibis.options.interactive = True

## matplotlib config
plt.style.use("dark_background")

## seaborn config
sns.set(style="darkgrid")
sns.set(rc={"figure.figsize": (12, 10)})

## plotly config
pio.templates.default = "plotly_dark"

## altair config
alt.renderers.set_embed_options(theme="dark")
