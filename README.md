# ISENSIT multi sensor
Multisensor integration on Home Assistant

# Guide
## Setup install
 1. Ensure the version of Home Assistant. It should be supervised version or OS version.
 2. Enter the 'Settings' section. 
 3. Search and install 'Mosquitto broker' from add-ons.
 4. Start the broker and ensure the Home Assistant and Multisensor are under same internet.

## Plugin install
 1. Download HACS from Home Assistant. Check the website if there is any problem. https://hacs.xyz/docs/setup/download/
 2. Choose 'HACS' on the left bar and enter 'integration'.
 3. Find the 'integration' and 'frontend' at the top bar and then click three dots at the top right corner.
 4. Select 'custom repositories'.
 5. Copy the URL (the website address) of this page and then paste it in the 'Repository' line and select 'integration'.
 6. Click 'Add' and then click '+ Explore & Download' at bottom right corner and search for 'isensit' or 'multisensor'.
 7. Click 'install' and restart Home Assistant after installation.
 8. You can restart the Home Assistant by clicking 'Developer tools' on the left side bar and choose 'restart home assistant' in 'restart'.
 9. Enter 'Settings' and select 'Devices & Services'.
 10. Click 'Add integration' at bottom and search for 'isensit' or 'multisensor'.
 11. All the settings are done. Device and entities will jump out when topics are received.