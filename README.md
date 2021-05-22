# Intl. WSPR Beacon Project

#### Status: Custom Firmware is finished. Hardware in production, accepting Pre-orders
#### [Beacon Install Guide](https://docs.google.com/document/d/1nfN_jRqq9-nsfkYHM_3KrRoq1a5RWeYCly9_mQI3QVw/edit?usp=sharing)

Custom Arduino Firmware for the [Zachtek WSPR Desktop Transmitter](https://www.zachtek.com/1012).
This Firmware extends the factory functionality by adding a coordinated WSPR Band hopping transmit schedule following the [WSJT-X implementation](https://www.physics.princeton.edu/pulsar/K1JT/wsjtx-doc/wsjtx-main-2.3.0.html#_band_hopping)

![image](https://user-images.githubusercontent.com/75934980/118491568-6cabce00-b71f-11eb-9634-eb7d8e3a8a85.png)

For each enabled Band the scheduler will start to transmit at the corresponding Minute. This enables a global Network of WSPR Beacons to transmit at the same Time and on the same Band. The exact TX Frequency within the allocated WSPR segment/Band (200 Hz) is picked randomly by the Firmware. Here is a screenshot

![image](https://user-images.githubusercontent.com/75934980/118852891-7bd37d00-b8d3-11eb-9f1d-f38a72d42085.png)


These coordinated Beacon Signals can then be decoded with WSJT-X (automated Band-Hopping) and uploaded to the [WSPRnet.org](https://wsprnet.org/drupal/) Database for further analysis.
 [Link to a Video](https://www.youtube.com/watch?v=vloVXac17Ss) showing the WSPR Beacon with the custom Firmware in Action (showing PC Software just  for demo purpose). Beacon runs headless, no PC needed.

### Why?

To identify and visualize weak Signal Propagation paths to study global Ham Radio HF Propagation for the interested audience.

### How?

Goal is to establish a global Network of 20-30 permanently installed, standardized, easy to operate, inexpensive and self-contained WSPR Beacons running **24x7x365** at strategic locations sharing the same or a very similar Setup:

- **Omni directional Antenna** (vert. EFHW, Multiband GP etc.)
- RF Power 200 mW
- Same transmission schedule
- Same Band coverage **(at least 80,40,20,15 and 10m)**
- **Permission from local authorities to run an unattended Beacon Transmitter** -> We need positive confirmation on that

Applications from HAM Radio Clubs will be preferred over individuals.

### Cost ?

Ready-to-use self-contained **(No PC/No Internet required)** WSPR Beacon Transmitters covering the 80,40,30,20,15,12 and 10m Band running the special Beacon Firmware should be available by the End of June 2021 (limited quantity). These Transmitters are purpose built devices for the WSPR Beacon Project by Harry @Zachtek and are not available off-the-shelf with the indicated Band coverage. Power output ~200mW. Power usage: 5V (USB) max. 250mA. Estimated cost per Device incl. Beacon Firmware, USB cable and GPS Antenna < 200 Euro (not including postage).

![image](https://user-images.githubusercontent.com/75934980/118846833-665b5480-b8cd-11eb-8c84-0a258b85ec0d.png)


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

Please [drop me a line](mailto:atomic@gmx.net) if you are interested to run a permanent WSPR Beacon and want to participate in the International WSPR Beacon Project. Include the phrase "Beacons are cool" in your email, this way I know you have read this page :-)

#### Project Milestones

- May-17 2021 Project kick off
- May-19 2021 Custom Arduino Firmware finished. PoC successful
- May-20 2021 Placed order for first batch of custom built WSPR Transmitters

