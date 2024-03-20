"""
An example of extension. It does nothing, but you can add transformations
before the return statements to customize the webui behavior.

Starting from history_modifier and ending in output_modifier, the
functions are declared in the same order that they are called at
generation time.
"""

import gradio as gr
import torch
from transformers import LogitsProcessor
from llm_steer import Steer


from modules import chat, shared
from modules.text_generation import (
    decode,
    encode,
    generate_reply,
)

params = {
    "display_name": "LLM Steer",
    "is_tab": True,
}

class MyLogits(LogitsProcessor):
    """
    Manipulates the probabilities for the next token before it gets sampled.
    Used in the logits_processor_modifier function below.
    """
    def __init__(self):
        pass

    def __call__(self, input_ids, scores):
        # probs = torch.softmax(scores, dim=-1, dtype=torch.float)
        # probs[0] /= probs[0].sum()
        # scores = torch.log(probs / (1 - probs))
        return scores

def history_modifier(history):
    """
    Modifies the chat history.
    Only used in chat mode.
    """
    return history

def state_modifier(state):
    """
    Modifies the state variable, which is a dictionary containing the input
    values in the UI like sliders and checkboxes.
    """
    return state

def chat_input_modifier(text, visible_text, state):
    """
    Modifies the user input string in chat mode (visible_text).
    You can also modify the internal representation of the user
    input (text) to change how it will appear in the prompt.
    """
    return text, visible_text

def input_modifier(string, state, is_chat=False):
    """
    In default/notebook modes, modifies the whole prompt.

    In chat mode, it is the same as chat_input_modifier but only applied
    to "text", here called "string", and not to "visible_text".
    """
    return string

def bot_prefix_modifier(string, state):
    """
    Modifies the prefix for the next bot reply in chat mode.
    By default, the prefix will be something like "Bot Name:".
    """
    return string

def tokenizer_modifier(state, prompt, input_ids, input_embeds):
    """
    Modifies the input ids and embeds.
    Used by the multimodal extension to put image embeddings in the prompt.
    Only used by loaders that use the transformers library for sampling.
    """
    return prompt, input_ids, input_embeds

def logits_processor_modifier(processor_list, input_ids):
    """
    Adds logits processors to the list, allowing you to access and modify
    the next token probabilities.
    Only used by loaders that use the transformers library for sampling.
    """
    processor_list.append(MyLogits())
    return processor_list

def output_modifier(string, state, is_chat=False):
    """
    Modifies the LLM output before it gets presented.

    In chat mode, the modified version goes into history['visible'],
    and the original version goes into history['internal'].
    """
    return string

def custom_generate_chat_prompt(user_input, state, **kwargs):
    """
    Replaces the function that generates the prompt from the chat history.
    Only used in chat mode.
    """

    result = chat.generate_chat_prompt(user_input, state, **kwargs)
    return result

def custom_css():
    """
    Returns a CSS string that gets appended to the CSS for the webui.
    """
    return ''

def custom_js():
    """
    Returns a javascript string that gets appended to the javascript
    for the webui.
    """
    return ''

def setup():
    """
    Gets executed only once, when the extension is imported.
    """
    shared.steered_model = None
    pass

def ui():
    """
    Gets executed when the UI is drawn. Custom gradio elements and
    their corresponding event handlers should be defined here.

    To learn about gradio components, check out the docs:
    https://gradio.app/docs/
    """
    with gr.Row():
        with gr.Column():
            layer_idx = gr.Number(label="Layer Index", value=20)
            coeff = gr.Number(label="Coefficient", value=0.4)
            text = gr.Textbox(label="Steering Text", value="logical")
            add_button = gr.Button("Add Steering Vector")
            add_output = gr.Textbox(label="Add Status")
        with gr.Column():
            reset_button = gr.Button("Reset Steering Vectors")
            get_button = gr.Button("Get Steering Vectors")
            steering_vectors_output = gr.Textbox(label="Steering Vectors")

    def add_steering_vector(layer_idx, coeff, text):
        if shared.steered_model is None:
            shared.steered_model = Steer(shared.model, shared.tokenizer)
        shared.steered_model.add(layer_idx=int(layer_idx), coeff=float(coeff), text=text)
        shared.model = shared.steered_model.model
        return f"Steering vector added: Layer {layer_idx}, Coefficient {coeff}, Text '{text}'"

    def reset_steering_vectors():
        if shared.steered_model is not None:
            shared.steered_model.reset_all()
            shared.steered_model = None

    def get_steering_vectors():
        if shared.steered_model is not None:
            steering_vectors = shared.steered_model.get_all()
            return str(steering_vectors)
        else:
            return "No steering vectors found."

    add_button.click(add_steering_vector, inputs=[layer_idx, coeff, text], outputs=[add_output])
    reset_button.click(reset_steering_vectors)
    get_button.click(get_steering_vectors, outputs=[steering_vectors_output])
    pass
