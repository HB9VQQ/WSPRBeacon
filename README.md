# Intl. WSPR Beacon Project

#### Status: Custom Firmware is finished. Hardware in production
[Beacon Install Guide](https://docs.google.com/document/d/1nfN_jRqq9-nsfkYHM_3KrRoq1a5RWeYCly9_mQI3QVw/edit?usp=sharing)

[Current candidate Map](https://www.google.com/maps/d/u/1/edit?mid=14X0GJ4vSQ7D8piZfuHDs902Y9tINuPqB&usp=sharing)

Custom Arduino Firmware for the [Zachtek WSPR Desktop Transmitter](https://www.zachtek.com/1012).
This Firmware extends the factory functionality by adding a coordinated WSPR Band hopping transmit schedule following the [WSJT-X implementation](https://www.physics.princeton.edu/pulsar/K1JT/wsjtx-doc/wsjtx-main-2.3.0.html#_band_hopping)

![image](https://user-images.githubusercontent.com/75934980/118491568-6cabce00-b71f-11eb-9634-eb7d8e3a8a85.png)

For each enabled Band the scheduler will start to transmit at the corresponding Minute. This enables a global Network of WSPR Beacons to transmit on the same Band at the same time. The exact TX Frequency within the allocated WSPR segment/Band (200 Hz) is picked randomly by the Firmware. Here is a screenshot

![image](https://user-images.githubusercontent.com/75934980/118852891-7bd37d00-b8d3-11eb-9f1d-f38a72d42085.png)


These coordinated Beacon Signals can then be decoded with WSJT-X (automated Band-Hopping) and uploaded to the [WSPRnet.org](https://wsprnet.org/drupal/) Database for further analysis.
 [Link to a Video](https://www.youtube.com/watch?v=vloVXac17Ss) showing the WSPR Beacon with the custom Firmware in Action (showing PC Software just  for demo purpose). Beacon runs headless, no PC needed.

### Why?

To identify and visualize weak Signal Propagation paths to study global Ham Radio HF Propagation for the interested audience by collecting WSPR Data over an extended period of time like years.

### How?

Goal is to establish a global Network of 20-30 permanently installed, standardized, easy to operate, inexpensive and self-contained WSPR Beacons running **24x7x365** at strategic locations sharing the same or a very similar Setup:

- **Omni directional Antenna** (vert. EFHW, Multiband GP etc.)
- RF Power 200 mW
- Same transmission schedule
- Same Band coverage **(at least 80,40,20,15 and 10m)**

### What is required to participate?

- Type 1 Callsign as explained here [WSPR Messages explained](https://www.dxplorer.net/wspr/msgtypes.html) Type 2 or Type 3 won't work
- Vertical omnidirectional Antenna for the 80,40,20,15,10m Band ([Endfed Halfwave](https://www.hyendcompany.nl/antenna/multiband_8040201510m/product/detail/3/HyEndFed_5_Band_Black_Clamp_MK3#prod), [DX Commander](https://www.m0mcx.co.uk/store/products/multi-band-80m-6m-hf-antenna-p-ale-compliant-antenna-survival-prep-sota-kit/), [Butternut HF6V](https://static.dxengineering.com/global/images/instructions/but-hf6v.pdf) or similar Multiband Antenna)
- Beacon needs to be run 24x7x365 (minus maintenance time)
- Our custom built WSPR Beacon Transmitter (incl. LPF's for the 80,40,30,20,15,12 and 10m Band)
- **The Beacon Operator is responsible to follow the local regulations in regards of unattended automatic Transmitters**

Applications from HAM Radio Clubs will be preferred over individuals.

### Cost ?

Ready-to-use self-contained **(No PC/No Internet required)** WSPR Beacon Transmitters covering the 80,40,30,20,15,12 and 10m Band running the special Beacon Firmware should be available by the End of June 2021 (limited quantity). These Transmitters are purpose built devices for the WSPR Beacon Project by Harry @Zachtek and are not available off-the-shelf with the indicated Band coverage. Power output ~200mW. Power usage: 5V (USB) max. 250mA. The cost per Device incl. Beacon Firmware, USB cable and GPS Antenna is 165 Euro (not including postage).

![image](https://user-images.githubusercontent.com/75934980/118846833-665b5480-b8cd-11eb-8c84-0a258b85ec0d.png)


Focus Regions for such Beacons are:

- Alaska (shipping cost 21 USD)
- Australia (shipping cost 26 AUD)
- Canada (shipping cost 25 CAD)
- Central Europe (shipping Cost 9 Euros)
- Hawaii (shipping cost 21 USD)
- Iceland (shipping cost 1250 ISK)
- India
- Japan (shipping cost 2.2 JPY)
- New Zealand (shipping cost 28 NZD)
- Asiatic Russia
- Scandinavia (11 USD)
- South Africa (shipping cost 280 ZAR)
- South America (shipping cost 21 USD)
- UAE (shipping cost 74 AED)
- USA east coast (shipping cost 21 USD)
- USA west coast (sipping cost 21 USD)
- Any other interesting Region

Please [drop me a line](mailto:atomic@gmx.net) if you fully comply with the above mentioned [requirements](https://github.com/HB9VQQ/WSPRBeacon/blob/main/README.md#what-is-required-to-participate) and if you want to participate in the International WSPR Beacon Project. Include the phrase "Beacons are cool" in your email, this way I know you have read this page :-)

#### Project Milestones

- May-17 2021 Project kick off
- May-19 2021 Custom Arduino Firmware finished. PoC successful
- May-20 2021 Placed order for first batch of custom built WSPR Transmitters
- May-22 2021 Started to onboard HAM Radio Clubs and individual WSPRer around the globe. Pls help to spread the Word, TU!

