import gradio as gr
import pandas as pd
import plotly.express as px

def plot_pie_chart(category1, value1, category2, value2, category3, value3):
    df = pd.DataFrame({
        'category': [category1, category2, category3],
        'values': [value1, value2, value3]
    })
    fig = px.pie(df, values='values', names='category', title="Pie Chart")
    return fig

def clear_data():
    return "", 0, "", 0, "", 0, None

with gr.Blocks() as demo:
    with gr.Row():
        category1 = gr.Textbox(label="Category 1", placeholder="Enter category name")
        value1 = gr.Number(label="Value 1", value=0)
    
    with gr.Row():
        category2 = gr.Textbox(label="Category 2", placeholder="Enter category name")
        value2 = gr.Number(label="Value 2", value=0)

    with gr.Row():
        category3 = gr.Textbox(label="Category 3", placeholder="Enter category name")
        value3 = gr.Number(label="Value 3", value=0)

    with gr.Row():
        submit_btn = gr.Button("Submit")
        clear_btn = gr.Button("Clear")
    
    output = gr.Plot()

    submit_btn.click(plot_pie_chart, inputs=[category1, value1, category2, value2, category3, value3], outputs=output)
    clear_btn.click(clear_data, outputs=[category1, value1, category2, value2, category3, value3, output])

demo.launch()
