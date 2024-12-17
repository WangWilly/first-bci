# First BCI

## Setup

https://docs.openbci.com/GettingStarted/Boards/CytonGS/

Requirements:
- Cyton Board
- Dongle (Ganglion)

### For GUI (provided by OpenBCI)

Follow [this](https://docs.openbci.com/Software/OpenBCISoftware/GUIDocs/#running-the-openbci-gui-from-the-processing-ide).

> MacOS ⚠️
> The FTDI driver is only necessary for Windows 8, Windows 10, and Mac OS X 10.9 through 10.15. If you are running a Mac that is mid 2015 or newer, you do not need to install the FTDI driver.
>
> https://docs.openbci.com/Troubleshooting/MacOSGanglionBLEWorkaround/

https://docs.openbci.com/Software/OpenBCISoftware/GUIDocs/

### For Python development

[Find the port of Ganglion](https://brainflow.readthedocs.io/en/stable/SupportedBoards.html#ganglion):
```bash
ls /dev/cu.* # to find the port of the device
```

Apply the presetted configuration:
```bash
poetry shell
```

- https://docs.openbci.com/ForDevelopers/SoftwareDevelopment/

