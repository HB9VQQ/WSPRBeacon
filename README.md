# WSPRBeacon

Custom Arduino Firmware for the [Zachteck WSPR Desktop Transmitter](https://www.zachtek.com/1012).
This Firmware extends the functionality by adding a coordinated WSPR Band hopping transmit schedule following the [WSJT-X implementation](https://www.physics.princeton.edu/pulsar/K1JT/wsjtx-doc/wsjtx-main-2.3.0.html)

![image](https://user-images.githubusercontent.com/75934980/118491568-6cabce00-b71f-11eb-9634-eb7d8e3a8a85.png)

For every enabled Band the scheduler will start to transmit on the defined Minute. This enables a global Network of WSPR Beacons to transmit on the same Time and on the same Band.
The exact TX Frequency within the allocated WSPR segment/Band (200 Hz) is picked randomly by the Firmware. The WSPR signal Bandwidth is 5.9 Hz. TX cycle is 2 minutes.

Goal is to establish a global Network of standardized WSPR Beacons sharing the same or very similar Setup:

- Omni directional Antenna (vert. EFHW, Multiband GP etc.)
- Same RF Power (200 mW)
- Same transmission schedule
- Same Band coverage --> 80,40,20,15 and 10m





