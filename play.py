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
    device_idx = 0

    print('-' * 60)
    print('Playing wav for {}s on device {}'.format(sec, device_idx))

    wav_file = wave.open('audio-recording.wav')

    stream_out = pa.open(
        rate=wav_file.getframerate(),      # sampling rate
        channels=wav_file.getnchannels(),  # number of output channels
        format=pa.get_format_from_width(
            wav_file.getsampwidth()),      # sample format and length
        output=True,                       # output stream flag
        output_device_index=device_idx,    # output device index
        frames_per_buffer=1024,            # buffer length
    )

    output_audio = wav_file.readframes(5 * wav_file.getframerate())
    stream_out.write(output_audio)
