import gradio as gr
from mylib.calculator import add


def greet(phrase):
    greeting = f"Hello {phrase}!"
    return greeting


with gr.Blocks() as demo:
    name = gr.Textbox(label="Name")
    output = gr.Textbox(label="Output Box")
    greet_btn = gr.Button("Greet")
    greet_btn.click(fn=greet, inputs=name, outputs=output)

    num1 = gr.Number(label="1st Number")
    num2 = gr.Number(label="2nd Number")
    calc_result = gr.Textbox(label="Result")
    calculate_btn = gr.Button("Add")
    calculate_btn.click(fn=add, inputs=[num1, num2], outputs=calc_result)

demo.launch()
