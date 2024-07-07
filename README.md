# Automated Testing for Gardenscapes

## Requirements

- Python 3.11+
- pip
- npm (Node Package Manager)
- Appium

## Setup

1. **Clone the repository**

   ```sh
   git clone <repository-url>
   cd <repository-directory>

2. **Create a virtual environment**

   ```sh
   python -m venv venv
   
3. **Activate the virtual environment**
  
   * On Windows:

   ```sh
   .\venv\Scripts\activate  
   ```
   * On Mac:
   ```sh
   source venv/bin/activate 
   ```
   
4. **Install the required Python packages**

   ```sh
   pip install -r requirements.txt

5. **Install Appium globally using npm**

   ```sh
   npm install -g appium

6. **Start the Appium server**

   ```sh
   appium

## Running Tests

1. **Set up environment variables in "envs" directory**


2. **Connect your device with the Gardenscapes app or run an emulator**


3. **Run the tests**
   ```sh
   python run_tests.py android
   ```

## Additional Information
- Ensure that the Appium server is running before executing the tests.
- Modify the android.env and ios.env files as needed to match your device configuration.
- There is one single test in this repository that verifies that the Gardenscapes app starts up correctly and logs into the game itself.
- The test only works on the Android platform.
- The test assumes that you are logged in with any Google account and have Gardenscapes app on your device.