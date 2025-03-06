# Content Generator 

## Overview

**Content Generator** is a web application built with [Streamlit](https://streamlit.io) that dynamically generates a Content on any given topic. Leveraging the power of the LLama2 model from Hugging Face, the application crafts content based on user-defined topics and word limits while providing feedback on generation time.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Dependencies](#dependencies)
  - [Download Model](#download-model)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Repository](#repository)
- [License](#license)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **Dynamic Content Generation:** Accepts user input for a topic and word count, then uses the LLama2 model to generate a Content.
- **Time Tracking:** Displays the duration taken to generate the response.
- **Streamlit Integration:** Provides an interactive and user-friendly web interface.

## Installation

### Prerequisites

- Python 3.7 or higher
- Git (for cloning the repository)

### Dependencies

Install the required Python packages using `pip`:

```sh
pip install streamlit ctransformers langchain
```

### Download Model

Download the LLama2 model file directly from Hugging Face and place it in the `llama_models/` directory:

```sh
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q2_K.gguf -P llama_models/
```

> **Note:** Ensure that the model file is correctly located in the `llama_models/` folder before running the application.

## Usage

1. **Launch the App:**

   In your terminal, navigate to the project directory and run:

   ```sh
   streamlit run app.py
   ```

2. **Generate a Content:**

   - Enter a topic in the provided text input field.
   - Specify the desired number of words for the Content.
   - Click the **Generate** button.
   - The generated Content and the time taken for generation will be displayed on the screen.

## File Structure

```
├── app.py                 # Main Streamlit application file
├── llama_models/          # Directory containing the LLama2 model file
└── README.md              # Project documentation
```

## Repository

The source code for this project is hosted on GitHub. For more details, visit the repository:

[Content Generator Repository](https://github.com/shib1111111/Content-Generator.git)


## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for improvements or bug fixes. For major changes, open an issue first to discuss your ideas.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Thank you for using this software ! Feel free to reach out with any questions or feedback.

<em style="color: #ff66b2; font-weight: bold;">✨ --- Designed & made  by Shib Kumar Saraf ✨</em>