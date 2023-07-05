add_library("sound")
# https://processing.org/reference/libraries/sound/index.html

def setup():
    global sampler, synth, data, index
    size(200, 200)
    sampler = SoundFile(this, "airplane_chime_x_.wav")
    synth = SqrOsc(this)  # SinOsc, SawOsc, TriOsc
    synth.play()        
    index = 0
    
    # get real data here
    data = []
    for i in range(1000):        
        data.append({'time': 0, 'value': random(0, 100)})  
        
    frameRate(5)  

def draw():
    global sampler, synth, data, index
        
    amplitude = 1.0
    synth.amp(amplitude)

    value = data[index]['value']
    frequency = map(value, 0, 100, 20.0, 1000.0)
    synth.freq(frequency)    

    index += 1
    index %= len(data)

def mouseClicked():
    global sampler
    sampler.amp(0.5)
    sampler.play()

        
