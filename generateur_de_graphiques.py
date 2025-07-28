import plotly.express as px

def generate_chart(df, x_col, y_col, title, chart_type):
    chart_type = chart_type.lower()

    if chart_type == "ligne":
        fig = px.line(df, x=x_col, y=y_col, markers=True, title=title)
    elif chart_type == "barres":
        fig = px.bar(df, x=x_col, y=y_col, title=title)
    elif chart_type == "secteurs (pie)":
        fig = px.pie(df, names=x_col, values=y_col, title=title)
    elif chart_type == "histogramme":
        fig = px.histogram(df, x=y_col, title=title)
    else:
        fig = px.line(df, x=x_col, y=y_col, markers=True, title=title)

    fig.update_layout(template="plotly_white", xaxis_title="Mois", yaxis_title=y_col)
    return fig

