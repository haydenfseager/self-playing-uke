# 🎸 Self-Playing-Uke
This is a Python project that allowed me to **automatically play a ukulele** by using the Python library [Mido](https://mido.readthedocs.io/en/latest/)

*Note:* This is merely the code for the project. This took months to manufacture a mechanical working product to accompany it.

## ✔️ Project Components
* [Python](https://www.python.org/doc/essays/blurb/)
* [Raspberry Pi](https://www.raspberrypi.org/)
* [Mido Library](https://mido.readthedocs.io/en/latest/)
* [MIDI Note Chart](https://computermusicresource.com/midikeys.html)
* [Time Library](https://docs.python.org/3/library/time.html)
* [Adafruit Servo Kit Library](https://docs.circuitpython.org/projects/servokit/en/latest/)
* [Design Drawings](https://github.com/key50/Senior-Project)
* [Servo Motors](https://www.amazon.com/Micro-Helicopter-Airplane-Remote-Control/dp/B072V529YD)

## 📜 Project Description:
The **motivation** behind this project is that I needed to create a final project for my Electrical Engineering degree program. Open-ended projects in general are difficult to organize and execute, but I had been thinking over creating a **self-playing** instrument for a while. 

My *initial* thought was to create a self-playing trumpet; an instrument with which I am very familiar due to my many years performing. The problem is: I'm assuming you must use some sort of **pneumatics** system, something with which I *really* didn't want to mess around.

There are 3 main categories of instruments which aren't percussion:
* [Brass](https://en.wikipedia.org/wiki/Brass_instrument)
* [Woodwind](https://en.wikipedia.org/wiki/Woodwind_instrument)
* [String](https://en.wikipedia.org/wiki/String_instrument)

Although both brass and woodwind instruments would be relatively easy to design software play them, they both run into the problem of designing a pneumatic device to "power" the instrument. String instruments only require two individual components: one mechanism to *strum* the strings, and one mechanism to *press* down on the strings. 

You could potentially use *any* string instrument (e.g. violin, viola, cello) but I think the most practical are guitar and ukulele. I decided to go with the ukulele because it is relatively small and light as compared to other string instruments. Additionally, the method we used to strum and press the strings involved rotating a small servo motor back and forth. We were unsure if the 9g motor we used would have enough torque to press the heavy steel stringsof a guitar (Yes, I know we can change the strings, but saving money was also the goal here).

Once you've finally created the **strumming** and **pressing** hardware mechanisms, and finally figured out how to move servos in conjunction to play individual notes, the final step is to create some way of playing a song. You could just hard-code a song, but music is very difficult to hard-code. You need tempo, note-pitch, note-duration, Oh, and don't forget that the note duration depends on the tempo, so make sure you include that in there. This would take forever if you did it this way. Luckily, a language called **MIDI** is here to save the day!

From what I understand, MIDI is just another form of binary that is used to represent music and its components.

The basic **function** of this project is 

For this **implementation**, I used **Python** 

***TLDR***: This is my senior design project from college. The main components are:
1. A string instrument (Ukulele)
2. A mechanism to strum and press on the strings
3. Software to convert servo motor motions to notes by way of combining the strumming and pressing motions
4. A MIDI file parser to extract song information from any song

## 💻 How to Install and Run the Project

## How to Use the Project

## Challenges
* Adjusting the software to fit the hardward
* Raspberry Pi shortage
* Finding the right MIDI file for the job

## Appendix
Here is an explantation of each file individually to explain how the entire system fits together.

# servo-main.py
# midi-file-parse.py
# print-midi-file.py
# note-mapping.py
# servo-test-adafruit.py
# servo-test2.py

