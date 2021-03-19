import pyaudio
import wave


if __name__ == '__main__':

    pa = pyaudio.PyAudio()

    print('\n' + '-' * 60)

    info = pa.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    for i in range(0, numdevices):
        if (pa.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print("Input Device id ", i, " - ",
                  pa.get_device_info_by_host_api_device_index(0, i).get('name'))

    sec = 5
    channel = 1
    rate = 48000
    device_idx = 0

    print('-' * 60)
    print('\nStart recording for {}s on device {}\n'.format(sec, device_idx))

    stream_in = pa.open(
        rate=rate,
        channels=channel,
        format=pyaudio.paInt16,
        input=True,
        input_device_index=device_idx,
        frames_per_buffer=1024
    )

    # read 5 seconds of the input stream
    input_audio = stream_in.read(sec * rate)

    output_filename = 'audio-recording.wav'
    wav_file = wave.open(output_filename, 'wb')

    # define audio stream properties
    wav_file.setsampwidth(2)          # sample width in bytes
    wav_file.setnchannels(channel)    # number of channels
    wav_file.setframerate(rate)       # sampling rate in Hz

    # write samples to the file
    wav_file.writeframes(input_audio)
