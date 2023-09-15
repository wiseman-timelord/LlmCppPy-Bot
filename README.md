# Llama2Robot-GGUF
### STATUS - BETA:
* Outstanding/Current work...
1) There is an issue with the emotions prompt, its supposed to happen when, "model_output_1" and "model_output_2" and "model_output_3", are full, but, something else is going on. As soon as I fix this, I will release as 1.05.
2) Window 2 should start with some ascii art, then mode on to roleplay configuration, and then into the chat screen. After doing the model configuration, window 1 should be in "main loop" display, where the user will be observing the processes, and have "window1.py" just for the engine? Its a plan. Moving some of the messaging code to "window2.py", such as detecting raw output updates, then parsing output in window 2, and then saving to window2 own config file.
3) When all is done, need to update docs.
* Updates done for release v1.05 will be...
1) 2 less scripts, python will now, resize and title, the windows with os dependent code in the, window1, window2, scripts (was main1, main2), utilizing code that will work on most linux setups, before this was done through batch and only available to windows users. (a improvement from the "other" project I have been working on).
2) leftover requirements from attempted transformers/torch/jax implementation have been removed, the program now only installs required requirements. This was possibly the case because no support for GGUF on main llamacpp branch, or otherwise just didnt check this after switching to llama during early development. You can remove the 4 non-required libraries with, 'pip uninstall transformers torch jax jaxlib -y' or 'wsl pip uninstall transformers torch jax jaxlib -y', though this may be used by other applications you use, that utilize transformers/torch.
3) scripts now correctly detect, extension of model files with multiple "." and UPPER/lower case, in the filename, such as "llama-2-7b-chat.Q8_K.gguf"
4) Key names improved, the names for the, human_current and model_current and model_previous1 and model_previous2, have been renamed, to better names.

### DESCRIPTION:
* This is a Llama 2 language model and llama-cpp based chatbot/agent framework. It uses Python scripts, YAML files, and ASCII art to produce context-aware conversations. The framework is designed for the creation of future Llama 2 based projects through forks. Llama2Robot a your own project, can be further developed for, reading and modifying and redacting, files and content, supposedly with multi-line output, furthermore, the second window can be easily, replicated and modified, to add additonal windows for displaying other keys of your choice.

  
### FEATURES:
* Code is optimised yet retains clarity in certain functions, code has been distributed soes each file under 7K GPT4 limit.
* Choice of only GGUF now, gotta stay current, if you want GGML, check out <=v1.03, its to do with llama. 
* Program sounds through a few select samples in .wav format, goes through key to window 2 which is non-WSL.
* Text To Speech for Wndows users through windows native audio, whereby, window 1 is WSL Python and window 2 is Python.
* `.ENV` File Management: Creates a default `.ENV` file if it doesn't exist. Useful for later forks.
* Multi-Window Interface: Runs separate scripts in parallel, bypassing the complexities of curses or tkinter on WSL.
* Context Support: Supports 4K-200K context multi-models with a robust interface for chat or chat+instruct models.
* Dynamic Model Initialization: Optimizes thread settings for the Llama language model.
* Interactive User Loop: Features a continuous loop for real-time user interaction.
* Intelligent Response Generation: Utilizes predefined prompts and ASCII art to generate contextually relevant and coherent responses.
* Model Response Rotation: Enhances character dialogue and can be modified for loop avoidance.
* YAML State Management: Manages session state, user preferences, and more through YAML file operations.
* User-Friendly Chat Interface: Offers a clean and intuitive chat interface, complete with ASCII art and dialogue history.
* Customizable Model Selection: Allows users to select from a list of available Llama 2 GGML models in the `./models` directory.

### INTERFACE:
Images may be from differing versions...
* Window 1 - Starting up, this also involves Wise-Llama's choice of fortune cookie!...
```
==========================================================================================
     .____    .__                        ________ __________     ___.           __
     |    |   |  | _____    _____ _____  \_____  \\______   \____\_ |__   _____/  |_
     |    |   |  | \__  \  /     \\__  \ /  _____/|       __/  _ \| __ \ /  _ \   __\
     |    |___|  |__/ __ \|  Y Y  \/ __ \|       \|    |   (  <_> ) \_\ (  <_> )  |
     |_______ \____(____  /__|_|  (____  Y_______ |____|___ \____/|_____/\____/|__|
             \/         \/      \/     \/        \/        \/           \/
                                Welcome To Llama2Robot!
==========================================================================================
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

   \/
   l'> -=< "I used to be indecisive. Now I'm not so sure! It's a work in progress."
   ll
   ll
   LlamaSay~
   ||    ||
   ''    ''

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Initial Startup Processes:
------------------------------------------------------------------------------------------

 Optimizing for x86_64-T24...
 ...using 20 out of 24 threads.

 Clearing input.log...
 ...input.log cleared.

 Clearing output.log...
 ...output.log cleared.

 Emptying keys...
 ...Keys reset.

 Loading... [==============================================================] Complete.
```
* Window 1 - Robust multi-model support for Llama 2 GGML llms...
```
==========================================================================================
                                       MODEL SELECTION
==========================================================================================
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Model Setup Processes:
------------------------------------------------------------------------------------------

 Search For Models...
 Chat model is llama2_7b_chat_uncensored.ggmlv3.q2_K.bin - CTX 4k
 Instruct model is llama-2-7b-32k-instruct.ggmlv3.q2_K.bin - CTX 32k

 Loading chat model with context length 4096, be patient...
llama.cpp: loading model from ./models/llama2_7b_chat_uncensored.ggmlv3.q2_K.bin
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_ctx      = 4096
llama_model_load_internal: ftype      = 10 (mostly Q2_K)
llama_model_load_internal: model size = 7B
llama_model_load_internal: mem required  = 4525.64 MB (+ 1026.00 MB per state)

 Loading instruct model with context length 4096, be patient...
llama.cpp: loading model from ./models/llama-2-7b-32k-instruct.ggmlv3.q2_K.bin
llama_model_load_internal: format     = ggjt v3 (latest)
llama_model_load_internal: n_ctx      = 4096
llama_model_load_internal: ftype      = 10 (mostly Q2_K)
llama_model_load_internal: model size = 7B
llama_model_load_internal: mem required  = 4525.64 MB (+ 1026.00 MB per state)

 Loading... [==============================================================] Complete.
```
* Window 2 - The ROLEPLAY SUMMARY, values of the relevant keys in a display...
```
==========================================================================================
                                     ROLEPLAY SUMMARY
========================================================================================== =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Human's Input:
------------------------------------------------------------------------------------------

 hello there! i never thought i would see you here on the mountain, do you come here often?!

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Wise-Llama's Response:
------------------------------------------------------------------------------------------

 "Ah, a surprise encounter indeed! I have been meditating here for some time now, seeking solace in the mountain's wisdom.", Wise-Llama says with a gentle nod as he closes his eyes to focus on his inner peace.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Wise-Llama's State:
------------------------------------------------------------------------------------------

 indifferent

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
 Event History:
------------------------------------------------------------------------------------------

 Human approaches Wise-Llama on the mountain, initiating a conversation with surprise and curiosity. Wise-Llama responds with a gentle nod and closed eyes, focusing on inner peace while expressing his presence in the area through meditation. Both parties exhibit nonverbal cues of calmness and serenity, creating a peaceful atmosphere for their interaction.

=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
```

### USAGE (windows):
* For Windows WSL:
1) Download the Package: Download the package and extract it to a dedicated folder. Open the folder in Windows Explorer with Admin rights or a shell with Admin privileges.
2) Install Requirements: Double-click `Install Requirements.bat`, this will install all required, packages and libraries, which includes experimental GGUF model support.
3) Download Models: Download the required GGML `*.bin` chat model files and place them in the `./models` folder. Note that the required `config.json` is already present in the `./models` folder.
4) Launch the Application: Double-click `Launch Llama2Robot.bat` to start the program.
* Optional - Window Resizing: Hold down Ctrl and scroll your mouse wheel to resize the window to your liking.
* Optional - Arguments: Edit `Launch Llama2Robot.bat` to include or run Python with relevant arguments like, `--logs` and '--tts'.
* Note - Sounds and TTS and Logging, are enabled by default, this may be altered through the editing of the arguements, --tts and --sound, in the file "Launch Llama2Robot.bat".

### USAGE (linux untested):
* For Linux (Untested):
1) Download the Package: Download the package and extract it to a dedicated folder. Open the folder in a shell with Admin privileges.
2) Install Requirements: Run, `pip install -r ./data/req_wsl.txt` and 'pip install -r ./data/req_win.txt`, in the shell, additionally run, "wsl pip install --upgrade --force-reinstall --no-cache-dir llama-cpp-python" for GGUF and "wsl pip install libncurses5-dev" for something?!.
3) Download Models: Download the required GGML `*.bin` chat model files and place them in the `./models` folder. Note that the required `config.json` is already present in the `./models` folder.
4) Launch the Application: Run `python window1.py` and `python window2.py` in separate shell windows to start the program.
* Optional (Untested) - Window Resizing: Hold down Ctrl and scroll your mouse wheel to resize the window to your liking.
* Optional - Arguments: to run, 'main1.py' and 'main2.py' with relevant arguments like, `--logs` (for window.py), and, '--tts' or '--sound' (for window2.py).

### TEST PROMPTS:
* Designed for the default roleplay settings...
1) Hello there! I never thought I would see you here on the mountain, do you come here often?
2) Wow, you can actually talk? That's super amazing! What brings you to this remote place?
3) You look very wise, are you knowledgeable, do you, know wise things and have wise thoughts?
4) Oh, please do tell about the great mysteries Wise-Llama, what is the purpose of humanity?

### REQUIREMENTS:
* Windows with WSL or Linux (untested), + libraries listed in `./data/req_wsl.txt` + packages libncurses5-dev & xterm + experimental llama-cpp-python (for GGUF).
* Python 3.x + libraries listed in `./data/req_win.txt`.
* Compatible with Llama 2 GGML models, such as [this one](https://huggingface.co/TheBloke/llama2_7b_chat_uncensored-GGML), or otherwise Llama 2 GGUF models, such as [this one](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GGUF).

### DISCLAIMER:
* Using the experimental version of llama-cpp-python will possibly break support for GGML or other applications that use llama-cpp, ensure to, use environment or perform a backup, before running the install process. If you want a GGML version of the program, then consult versions <=1.03 of Llama2Robot. I can tell you that the GGUF is a superior product as shown above, and the prompt syntax is standardaized between, chat and instruct, however, some models designed for roleplay may differ.  
* This program is in no way affiliated with the Llama 2 developers, it merely is a Chatbot that runs through the use of Llama 2 GGUF based. models. The Llama 2 model has been chosen because it is the only local language model that has been reviewed on YouTube to my knowing at the time of, inception and creation, that are able to correctly write a ".json" file. Thus if this were the case with other models beforehand, it would be named after them.
* Llama2Robot is a roleplaying chatbot framework created by Wiseman-Timelord. Users and developers can modify it to create their own AI software for personal interests (see docs), however, they are solely responsible for any changes they make. If you profit significantly from your modified version, consider financially supporting the original author, Wiseman-Timelord, as a gesture of appreciation for his work. Note that using Llama2Robot doesn't grant you any personal, rights or approvals, from the timelord himself.
