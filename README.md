# WSPRBeacon

#### Status: Proof of Concept completed, finalizing custom Firmware. Stay tuned for official Release

Custom Arduino Firmware for the [Zachtek WSPR Desktop Transmitter](https://www.zachtek.com/1012).
This Firmware extends the factory functionality by adding a coordinated WSPR Band hopping transmit schedule following the [WSJT-X implementation](https://www.physics.princeton.edu/pulsar/K1JT/wsjtx-doc/wsjtx-main-2.3.0.html#_band_hopping)

![image](https://user-images.githubusercontent.com/75934980/118491568-6cabce00-b71f-11eb-9634-eb7d8e3a8a85.png)

For each enabled Band the scheduler will start to transmit at the corresponding Minute. This enables a global Network of WSPR Beacons to transmit at the same Time and on the same Band.
The exact TX Frequency within the allocated WSPR segment/Band (200 Hz) is picked randomly by the Firmware. These coordinated Beacon Signals can then be decoded with WSJT-X and uploaded to the [WSPRnet.org](https://wsprnet.org/drupal/) Database for further analysis.

Here is a [Link to a Video](https://www.youtube.com/watch?v=vloVXac17Ss) showing the WSPR Beacon with the custom Firmware in Action.

### Why?

To identify and visualize weak Signal Propagation paths to study global Ham Radio HF Propagation for the interested audience.

### How?

Goal is to establish a global Network of permanently installed, standardized, easy to operate, inexpensive and self-contained WSPR Beacons running 24x7x365, sharing the same or a very similar Setup:

- Omni directional Antenna (vert. EFHW, Multiband GP etc.)
- Same RF Power (200 mW)
- Same transmission schedule
- Same Band coverage --> 80,40,20,15 and 10m

Customized ready-to-use WSPR Transmitters covering the above mentioned Bands will be made available at a later stage of the Project.


Focus Regions for such Beacons are:

- Alaska
- Australia
- Canada
- Central Europe
- Hawaii
- Iceland
- India
- Japan
- New Zealand
- Asiatic Russia
- Scandinavia
- South Africa
- South America
- UAE
- USA east coast
- USA west coast
- Any other interesting Region

Please drop me a line if you are interested to run a permanent WSPR Beacon and want to participate in the International WSPR Beacon Project.
