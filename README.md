# GrindCoffee

![alt text](Images/readme_banner.png)

GrindCoffee is a simple coffee brewing companion that helps you track and manage your coffee brewing process. Whether you're a beginner to coffee, an enthusiast or a home barista, GrindCoffee provides the tools you need to brew the perfect cup of coffee.

The idea for GrindCoffee came from a problem that my coffee-nerd friend was facing. He had just bought some fancy brewing equipment and coffee grinder. But, the assistance app for the grinder was broken and no longer being developed. He came to me with this issue and after reverse engineering the grind size formula with him, I got to working on this project. 

I set out to build an uncomplicated web-app which solved the above problem and more, becoming a one stop coffee assistant to guide you throughout the brewing process.  

## Features

**<ins>Grind Size Optimizer</ins>**: 
- Helps in determining the optimal values for your coffee grinder's inner and outer rings, to give you a perfect grind.
- Provides granular adjustements.
- Tells you the miniumum adjustments you need to make to get to your desired grind size.

**<ins>Brew Timer</ins>**: 
- Keeps track of your brewing time across the bloom, brew and stir stages.
- Allows users to adjust and customize the duration of each stage seperately

## Installation & Usage

To install and use GrindCoffee locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yashaswat/GrindCoffee.git
    cd GrindCoffee
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the following command:
    ```bash
    streamlit run app.py
    ```

## Contributions

We welcome contributions for fixes and features! To contribute, clone the repository like mentioned above and follow these steps:

1. Create a branch for your changes:
    ```bash
    git checkout -b your-feature-branch
    ```
2. Make your changes to the code.

3. Commit the changes
    ```bash
    git add .
    git commit -m "Description of changes"
    ```
4. Create a pull request:
    - Go to the original repo
    - Click on "Compare & pull request" button
    - Add a title and description of PR
    - Click "Create pull request"

## Contact

If you have any questions or feedback, feel free to reach out at vyashaswat@gmail.com.

Enjoy brewing with GrindCoffee! ☕️