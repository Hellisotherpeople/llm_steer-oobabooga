# llm_steer-oobabooga
Steer LLM outputs towards a certain topic/subject and enhance response capabilities using activation engineering by adding steering vectors, now integrated within the [oobabooga text generation webui!](https://github.com/oobabooga/text-generation-webui)

[llm_steer](https://github.com/Mihaiii/llm_steer), the underlying codebase utilized for this extension, was created by https://github.com/Mihaiii

Note: This extension only works for models loaded using the "transformers" backend. 

# Installation

1.   ```pip3 install llm_steer``` (Make sure pip3 corresponds to the particular pip used by oobabooga, for me it's the pip3 located at ```/home/(user)/text-generation-webui/installer_files/env/bin/pip3``` - otherwise oobabooga won't pick up the installed package)
  
2. run oobabooga, and navigate to the session page. Copy and paste the github url (https://github.com/Hellisotherpeople/llm_steer-oobabooga) into the install box and press enter.
  ![Screenshot from 2024-03-20 16-29-03.png](https://raw.githubusercontent.com/Hellisotherpeople/llm_steer-oobabooga/main/Screenshot%20from%202024-03-20%2016-29-03.png)


# Usage

There are three values: 

**Layer Index (int)**: 
Which layer should the steering vector be inserted into? 

This is not well understood, but in general, the earlier layers are supposedly more "general" and potentially more "impactful". Results will very

Mistral models usually have at least 24 layers. 


**Coefficient (float)**:
The intensity of the vector. Gives fully granular control over the impact of the vector. Can be negative. 


**Steering Text (string)**: 
The prompt used for creating the vector.

Set these values and click "Add Steering Vector". Any combination of steering vectors can be used at the same time. 

To reset and delete all Steering Vectors, click "Reset Steering Vectors"

To view the currently applied Steering Vectors, click "Get Steering Vectors"


# Why is this a big deal?

Several reasons! 

1. You don't consume any tokens this way, leaving the remaining system prompt tokens to have a stronger impact
2. You can dial the particular intensity/attention of a token up or down, and apply it to any layer or combination of layers that you'd like
3. Supports negative values of coeffecient, which implements effectively faster "negative prompting" behavior than existing classifier free guidance built into oobabooga.
4. Makes it pretty easy to implement personalization, or alignment/unalignment.

Further Background on Steering Vectors:  
1. [Activation Addition: Steering Language Models Without Optimization](https://arxiv.org/abs/2308.10248)
2. [Steering GPT-2-XL by adding an activation vector](https://www.greaterwrong.com/posts/5spBue2z2tw4JuDCx/steering-gpt-2-xl-by-adding-an-activation-vector)

Related ideas/inspiration:

1. [repeng/control vectors](https://github.com/vgel/repeng)
2. [Prompt Fusion (for automatic1111)](https://github.com/ljleb/prompt-fusion-extension)

# Screenshots
(No vector)

![image](https://github.com/Hellisotherpeople/llm_steer-oobabooga/assets/12686966/3c24d58d-aae1-4d55-8560-09a6c294afb2)

(Add Sad Vector) 

![image](https://github.com/Hellisotherpeople/llm_steer-oobabooga/assets/12686966/e7d4d331-e7b2-4390-8e21-a8fa3d97672c)

![image](https://github.com/Hellisotherpeople/llm_steer-oobabooga/assets/12686966/375da759-e059-4168-bec2-d1b25dd9f476)

(Add Tax Preperation Vector)

![image](https://github.com/Hellisotherpeople/llm_steer-oobabooga/assets/12686966/0af98f35-23ed-414a-a1e8-96b8ea0b783b)

![image](https://github.com/Hellisotherpeople/llm_steer-oobabooga/assets/12686966/0d18e73b-8e2c-44c7-8f39-d33f8f154fed)


