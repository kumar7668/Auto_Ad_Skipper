# Youtube Ad Skipper

## Description
The Youtube Ad Skipper is a Python script that uses Selenium to automate the skipping of ads on YouTube videos. It opens a web browser, navigates to YouTube, and continuously checks for ad overlays. If an ad overlay is detected, it clicks the skip button to skip the ad.

## Requirements
- Python 3.x
- Selenium
- Chrome web browser
- ChromeDriver (automatically managed by ChromeDriverManager)

## Installation
1. Clone the repository:

- git clone https://github.com/kumar7668/Auto_Ad_Skipper.git

2. Install the required packages:

- pip install -r requirements.txt

## Usage
1. Run the script:

- python youtube_ad_skipper.py

The script will open a web browser and navigate to YouTube.
It will continuously check for ad overlays and skip them automatically.


## Configuration
- You can adjust the timeout for ad detection in the check_ad method.
- Customize the logging level and format in the __init__ method of the YoutubePlayer class.




 ## ##########################################################################################################################

## To Create a Executable File

Note - Inside '/build/exe.win-amd64-3.10/; Dir there is alredy youtube_ad_skipper.exe file which is created by follwoing      steps.
------------------------------------------------------------------------------------------------------------------------------
- Here's how you can use cx_Freeze to create an executable:

1. Install cx_Freeze if you haven't already:

- pip install cx-Freeze

2. Create a setup.py file in the same directory as your Python script (youtube_ad_skipper.py) with the following content:

        from cx_Freeze import setup, Executable

        setup(
            name="YoutubeAdSkipper",
            version="1.0",
            description="Skip YouTube ads automatically",
            executables=[Executable("youtube_ad_skipper.py")]
        )

3. Run cx_Freeze using the setup.py file:

- python setup.py build

After cx_Freeze finishes running, check the build directory for the new youtube_ad_skipper.exe file.
------------------------------------------------------------------------------------------------------------------------
