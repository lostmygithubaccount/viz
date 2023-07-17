# imports
from eda import *
import streamlit as st

# get data
t = ibis.examples.penguins.fetch()

# visualize
alt_chart = (
    alt.Chart(t)
    .mark_point()
    .encode(x="bill_length_mm:Q", y="bill_depth_mm:Q", color="species:N")
    .interactive()
    .properties(width=800, height=400)
)

st.altair_chart(alt_chart)

pypl_chart = px.scatter(
    t,
    x="bill_length_mm",
    y="bill_depth_mm",
    color="species",
    width=800,
    height=400,
    title="Bill Length vs Bill Depth",
)
st.plotly_chart(pypl_chart)

alt_bar_chart = (
    alt.Chart(t.group_by("species").agg(ibis._.count().name("count")))
    .mark_bar()
    .encode(
        x="species:N",
        y="count:Q",
    )
    .properties(width=800, height=400)
)
st.altair_chart(alt_bar_chart)

pypl_bar_chart = px.bar(
    t.group_by("species").agg(ibis._.count().name("count")),
    x="species",
    y="count",
)
st.plotly_chart(pypl_bar_chart)


# sns_chart = sns.scatterplot(
#    data=t.to_pandas(),
#    x="bill_length_mm",
#    y="bill_depth_mm",
#    hue="species",
#    legend="full",
# )
# st.pyplot(sns_chart.figure)
