import gradio as gr
import pandas as pd
from ai_assisted_coding_cherry.ai_ass_label import *
from ai_assisted_coding_cherry.overview import *
from ai_assisted_coding_cherry.valid_update import *
from ai_assisted_coding_cherry.chat_on_dataset import *
import os
import openai


def main():
    key_json_path = "api_key.json"
    overview_mardown_path = "README.md"
    instruction_video_path = "video demostration.mp4"
    set_openai_key_default(key_json_path)
    try:
        openai.api_key = os.environ['OPENAI_API_KEY']
    except:
        pass


    with gr.Blocks() as app:
        
        with gr.Tab("Select API Key"):
            gr.Markdown("# Select API Key")
            choice = gr.Radio(
            choices=["Use my own API key", "Use default API key in backend"],
            label="Select your preference: ",
            value="Use my own API key"
            )
            preferece_api_key = gr.Textbox(label="Preference API KEY: ", value="***************************")
            submit = gr.Button("Submit")
            text_output = gr.Textbox(label="Output")
            path_input = gr.Variable(value=key_json_path)
            submit.click(api_key_update, inputs=[choice, path_input, preferece_api_key], outputs=text_output)

        with gr.Tab("Overview"):
            # read in the readme file
            gr.Markdown("# Video demostration")
            try:
                gr.Video(instruction_video_path)
            except:
                gr.Markdown("Video demostration is not available")
            overview = overview_markdown(overview_mardown_path)
            gr.Markdown(overview)
            
            
        with gr.Tab("AI Assisted Labeling Simple"):
            gr.Markdown("# AI-Assisted Labeling (Simple)")

            with gr.Row():
                inputs = gr.components.File(type="file", label="Upload CSV file")
                label_button = gr.Button("Process with AI Labeling")
                download_link = gr.components.File(label='Download AI-Assisted CSV')
            
            with gr.Row():

                html_output = gr.components.HTML(label='Processed Data')
                

                outputs=[
                    html_output,
                    download_link
                ]

                label_button.click(
                    fn=ai_assisted_labeling, 
                    inputs=inputs, 
                    outputs=outputs
                )

        with gr.Tab("Chat about dataset"):
                file_input = gr.File(type="file", label="Upload CSV file")
                chat_interface = gr.ChatInterface(
                    fn=chat_on_dataset,
                    additional_inputs=[file_input],
                    title="Dataset Chatbot"
                )


        with gr.Tab("AI assisted Labeling Advanced"):
            gr.Markdown("# AI-Assisted Labeling (Advanced)")

            with gr.Row():
                with gr.Column():
                    file_input = gr.components.File(type="file", label="Upload CSV file")
                    label_button = gr.Button("Begin to label")
                    file_output = gr.components.File(label='Download AI-Assisted CSV')
                    chunk_count = gr.Variable(value=1)
                    accuracy_log = gr.Variable(value=[])  # Store accuracy log

                with gr.Column():
                    batch_size_input = gr.Number(label="Batch Size", value=10)
                    current_dataframe = gr.Variable(value=pd.DataFrame())
                    dataframe_display = gr.DataFrame(interactive=True)
                    
                    correct_button = gr.Button("Correct")

                with gr.Column():
                    plot_display = gr.Plot(interactive=False)
                    plot_btn = gr.Button("Plot Accuracy")
                    download_link = gr.components.File(label='Download Accuracy Log')
                    # dataframe_parser = gr.components.DataframeParser(label="Corrections")
                label_button.click(fn=start_to_label, inputs=[file_input, batch_size_input, accuracy_log, chunk_count], outputs=[dataframe_display, current_dataframe, accuracy_log, chunk_count])
                correct_button.click(fn=correct_dataframe, inputs=[dataframe_display, file_input, current_dataframe, accuracy_log, batch_size_input, chunk_count], outputs=[dataframe_display, file_output, current_dataframe, accuracy_log, chunk_count])
                plot_btn.click(fn=create_plot, inputs=accuracy_log, outputs=[plot_display, download_link])
    
    app.launch()

if __name__ == "__main__":
    main()
