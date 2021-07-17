# Intl. WSPR Beacon Project

#### Status: Global Beacon deployment in Progress

[Beacon Map](https://www.google.com/maps/d/u/1/edit?mid=14X0GJ4vSQ7D8piZfuHDs902Y9tINuPqB&usp=sharing)

[Beacon Install Guide](https://docs.google.com/document/d/1nfN_jRqq9-nsfkYHM_3KrRoq1a5RWeYCly9_mQI3QVw/edit?usp=sharing)

Custom Arduino Firmware for the [Zachtek WSPR Desktop Transmitter](https://www.zachtek.com/1012).
This Firmware extends the factory functionality by adding a coordinated WSPR Band hopping transmit schedule following the [WSJT-X implementation](https://www.physics.princeton.edu/pulsar/K1JT/wsjtx-doc/wsjtx-main-2.3.0.html#_band_hopping)

![image](https://user-images.githubusercontent.com/75934980/118491568-6cabce00-b71f-11eb-9634-eb7d8e3a8a85.png)

For each enabled Band the scheduler will start to transmit at the corresponding Minute. This enables a global Network of WSPR Beacons to transmit on the same Band at the same time. The exact TX Frequency within the allocated WSPR segment/Band (200 Hz) is picked randomly by the Firmware. Here is a screenshot

![image](https://user-images.githubusercontent.com/75934980/118852891-7bd37d00-b8d3-11eb-9f1d-f38a72d42085.png)


These coordinated Beacon Signals can then be decoded with WSJT-X (automated Band-Hopping) and uploaded to the [WSPRnet.org](https://wsprnet.org/drupal/) Database for further analysis.
 [Link to a Video](https://www.youtube.com/watch?v=vloVXac17Ss) showing the WSPR Beacon with the custom Firmware in Action (showing PC Software just  for demo purpose). Beacon runs headless, no PC needed.

### Why?

To identify and visualize weak Signal Propagation paths to study global Ham Radio HF Propagation for the interested audience by collecting WSPR Data from standardized Beacon Transmitters over an extended period of time like years. Inspired by the NCDXF CW Beacon Project.

### How?

Goal is to establish a global Network of 30-40 permanently installed, standardized, easy to operate, inexpensive and self-contained WSPR Beacons running **24x7x365** at strategic locations around the globe sharing the same or a very similar Setup:

- **Omni directional Antenna** (vert. EFHW, Multiband GP etc.)
- RF Power 200 mW
- Same transmission schedule (following WSJT-X Band-hopping)
- Same Band coverage **(at least 80,40,20,15 and 10m)**

### What is required to participate?

- Type 1 Callsign like HB9VQQ (max. 6 characters) as explained here [WSPR Messages explained](https://www.dxplorer.net/wspr/msgtypes.html) Type 2 or Type 3 won't work
- Vertical omnidirectional Antenna covering at least 80,40,20,15,10m Band ([Endfed Halfwave](https://www.hyendcompany.nl/antenna/multiband_8040201510m/product/detail/3/HyEndFed_5_Band_Black_Clamp_MK3#prod), [DX Commander](https://www.m0mcx.co.uk/store/products/multi-band-80m-6m-hf-antenna-p-ale-compliant-antenna-survival-prep-sota-kit/), [GAP DX Titan](http://gapantenna.com/shop/antennas/titan-dx/), [Butternut HF6V](https://static.dxengineering.com/global/images/instructions/but-hf6v.pdf) or similar Multiband Antenna)
- Willingness to run the Beacon 24x7x365 (Best effort)
- Our custom built WSPR Beacon Transmitter with LPFs for the 80,40,30,20,17,15,12 and 10m Band
- **The Beacon Operator is responsible to follow the local regulations in regards of unattended automatic Transmitters**

Applications from HAM Radio Clubs will be preferred over individuals.

### Cost ?

Ready-to-use self-contained **(No PC/No Internet required)** WSPR Beacon Transmitters covering the 80,40,30,20,17,15,12 and 10m Band running our special Beacon Firmware will be provided by the Project (limited quantity). These Transmitters are purpose built devices for the WSPR Beacon Project by Harry @Zachtek and are not available off-the-shelf with the indicated Band coverage. Power output ~200mW. Power usage: 5V (USB) max. 250mA. The cost of the Beacon Transmitter Hardware is sponsored by the Project, you just need to cover the postage fee and your local custom duties if any. **Potential candidates will be selected very carefully to achieve the best possible global coverage.**

![image](https://user-images.githubusercontent.com/75934980/118846833-665b5480-b8cd-11eb-8c84-0a258b85ec0d.png)
![image](https://user-images.githubusercontent.com/75934980/124916888-74874080-dff3-11eb-968b-ab4a81847612.png)
![image](https://user-images.githubusercontent.com/75934980/124916917-7e10a880-dff3-11eb-83cc-a77a34de6b59.png)


#### Apply for participation

Please [drop me a line](mailto:atomic@gmx.net) if you fully comply with the above mentioned [requirements](https://github.com/HB9VQQ/WSPRBeacon/blob/main/README.md#what-is-required-to-participate) and if you want to participate in the Intl. WSPR Beacon Project. Please answer these seven questions in your email:

1. What is the Beacon callsign you'll be using?
2. What is the planned Beacon location?
3. What Antenna will be used for the Beacon?
4. Is the Antenna installed as a vertical omni directional?
5. Will the Antenna cover at least 80,40,20,15 and 10m Band with an SWR < 2:1?
6. Do you agree to run the Beacon 24x7x365 (Best effort)?
7. HAM Radio Club or individual?

#### Project Milestones

- May-17 2021 Project kick off
- May-19 2021 Custom Arduino Firmware finished. PoC successful
- May-20 2021 Placed order for first batch of custom built WSPR Transmitters
- May-22 2021 Started to onboard HAM Radio Clubs and individual WSPRer around the globe
- June-19 2021 Beacon #1 shipped to Milan, Italy IU2PJI Politecnico Milano - Pilot installation
- June-28 2021 Beacon #1 IU2PJI ON AIR !
- July-17 2021 18 Beacons shipped, 4 operational

