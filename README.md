# Dialog Smart Button and Amazon Dash Button performance comparison

### Getting Started

#### Setting up the Amazon Dash Button
1. Download the Amazon Shopping app on [Google Play](https://play.google.com/store/apps/details?id=com.amazon.mShop.android.shopping&hl=en) or [iTunes](https://itunes.apple.com/us/app/amazon-app-shop-scan-compare/id297606951?mt=8)
2. Turn on Wi-Fi and Bluetooth on your phone
3. Open the Amazon Shopping app
	1. Tap the **Menu** icon on the top left corner
	2. Select **Your Account**
	3. Under **Dash Services** select **Set up a new device**
4. Sign in to your Amazon Account
5. **Start Setup**. After signing in tap **Agree & Get Started**
6. Connect the Dash Button to your Wi-Fi
	1. On your Dash Button device, press and hold the button until the LED blinks blue, and then release the button.
	2. In the app, select **Connect**. Your Dash Button device searches for available Wi-Fi connections. It also connects to your phone so you can enter Wi-Fi information.
	3. Enter a network password for the selected Wi-Fi network. Then tap **Continue**.
	4. Select **Continue**
7. The nex step requires you to select a product to be ordered when the button is pressed. Since we do not want this, **exit out of the app**. The button should be connected to your Wi-Fi.

#### Setting up project on your machine

##### Setting up on Linux (or RaspberryPi)
1. Connect to the same Wi-Fi network the buttons were configured to. 
2. Open the **terminal**.
3. Install **git** using
	'sudo apt-get install git'
4. Navigate to the filepath where you wish to run the project. For example, if you wish to run the project on your Desktop, use
	'cd ~/Desktop'
5. Clone the project on to your selected filepath using
	'git clone https://github.com/savidude/button-testing.git'

### Now the fun part!

#### Identifying the MAC addresses of your buttons
1. Run the **mac_finder** python script using
	'sudo python mac_finder.py'
2. Press either the Dash Button or the Dialog Smart Button.
3. If your device is connected to the same network the buttons were configured to, you should see something similar to this on the terminal screen where the button's mac address is in place of <BUTTON_MAC_ADDRESS>.
	'Source MAC: <BUTTON_MAC_ADDRESS>'
4. Press the button a few more times to make sure that the shown MAC address belongs to the button, and not any other devices connected to your network.
5. Open 'config.ini' in the project folder using any text editor.
6. Copy the MAC addresses of the Dialog and Amazon buttons, and paste them replacing 'MAC_ADDRESS_OF_DIALOG_BUTTON' and 'MAC_ADDRESS_OF_DASH_BUTTON' respectively.
7. Exit out of the script.
	'crtl + c'

#### Testing network connectivity speeds of the buttons
1. Run the **arpsniffer** python script
	'sudo python arpsniffer.py'
2. Press the buttons. A message should be displayed on the terminal window when the buttons are pressed.