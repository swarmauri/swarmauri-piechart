
import gradio as gr
from gradio_mycomponent import MyComponent


example = MyComponent().example_value()

demo = gr.Interface(
    lambda x:x,
    MyComponent(),  # interactive version of your component
    MyComponent(),  # static version of your component
    # examples=[[example]],  # uncomment this line to view the "example version" of your component
)


if __name__ == "__main__":
    demo.launch()
