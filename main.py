import scipy.io.wavfile as wavfile
import scipy
import scipy.fftpack
import matplotlib.pyplot as plt


def processAndShow(file_name):
    """Process a wav file and show the sound spectrum of the sound

    Args:
    -----
    file_name: str
        Name of wav file
    """
    fs_rate, signal = wavfile.read(file_name)
    print ("Frequency sampling", fs_rate)
    l_audio = len(signal.shape)
    print ("Channels", l_audio)
    if l_audio == 2:
        signal = signal.sum(axis=1) / 2
    N = signal.shape[0]
    print ("Complete Samplings N", N)
    secs = N / float(fs_rate)
    print ("secs", secs)
    Ts = 1.0/fs_rate
    print ("Timestep between samples Ts", Ts)
    t = scipy.arange(0, secs, Ts)
    FFT = abs(scipy.fft(signal))
    FFT_side = FFT[range(N/2)]
    freqs = scipy.fftpack.fftfreq(signal.size, t[1]-t[0])
    freqs_side = freqs[range(N//2)]
    plt.title("Doppler Effect")
    plt.plot(freqs_side, abs(FFT_side), "b")
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Count single-sided')
    plt.show()


processAndShow("DataF10440.1Hz.wav")
