# llm_steer-oobabooga
Steer LLM outputs towards a certain topic/subject and enhance response capabilities using activation engineering by adding steering vectors, now integrated within the [oobabooga text generation webui!](https://github.com/oobabooga/text-generation-webui)

[llm_steer](https://github.com/Mihaiii/llm_steer), the underlying codebased utilized for this extension, was created by https://github.com/Mihaiii



# Installation

1.   ```pip3 install llm_steer``` (Make sure pip3 corresponds to the particular pip used by oobabooga, for me it's the pip3 /home/(user)/text-generation-webui/installer_files/env/bin/pip3)
  
3. run oobabooga, and navigate to the session page. Copy and paste the github url (https://github.com/Hellisotherpeople/llm_steer-oobabooga) into the install box and press enter.
  ![Screenshot from 2024-03-20 16-29-03.png](https://raw.githubusercontent.com/Hellisotherpeople/llm_steer-oobabooga/main/Screenshot%20from%202024-03-20%2016-29-03.png)
4. enable the extension 

# Why is this a big deal?

Several reasons! 

1. You don't consume any tokens this way, leaving the remaining system prompt tokens to have a stronger impact
2. You can dial the particular intensity/attention of a token up or down, and apply it to any layer or combination of layers that you'd like
3. Supports negative values of coeffecient, which implements effectively faster "negative prompting" behavior than existing classifier free guidance built into oobabooga.
4. Makes it pretty easy to implement personalization, or alignment/unalignment.

Further Background on Steering Vectors:  
1. [Activation Addition: Steering Language Models Without Optimization](https://arxiv.org/abs/2308.10248)
2. [Steering GPT-2-XL by adding an activation vector](https://www.greaterwrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector)

# Related ideas/inspiration:

1. [repeng/control vectors](https://github.com/vgel/repeng)
2. [Prompt Fusion (for automatic1111)](https://github.com/ljleb/prompt-fusion-extension)

# Screemshots
