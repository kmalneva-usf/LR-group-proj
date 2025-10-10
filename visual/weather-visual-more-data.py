import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
# Load the CSV file
df = pd.read_csv("y_f9_vals_wide.csv")

# Initialize the figure
fig = go.Figure()

# Plot each sample as a line
for col in df.columns[1:]:
    fig.add_trace(go.Scatter(
        x=df["x"],
        y=df[col],
        mode="lines",
        name=col,
        line=dict(width=1)
    ))

# Customize layout
fig.update_layout(
    title="Weather Prediction Plot",
    xaxis_title="x",
    yaxis_title="Rainfall",
    hovermode="x unified",
    template="plotly_white",
    showlegend=True,
    legend=dict(orientation="h", y=-0.2)
)

# Show the interactive plot
fig.show()
pio.write_html(fig, "in-depth-visual.html")
