import numpy as np
import jellyfish

def channel(sent_signal):
    s = np.mean(sent_signal**2)
    if s <= 1:
        s = 1
    noise_power = (10**(-2.65))*s
    shift = np.exp(-2j*np.pi*np.random.rand())
    sent_signal = sent_signal*shift
    noise_std = np.sqrt(noise_power/2)
    rcv_signal = sent_signal + noise_std*np.random.randn(len(sent_signal))
    + 1j*noise_std*np.random.randn(len(sent_signal))
    return rcv_signal

def serialize_complex(complex_vector,file_name):
    complex_vector = complex_vector.reshape(-1)
    np.savetxt(file_name,np.concatenate([np.real(complex_vector),
    np.imag(complex_vector)]))

def deserialize_complex(file_name):
    tx_data = np.loadtxt(file_name)
    N_sample = tx_data.size
    N_sample = N_sample//2
    tx_data = np.clip(tx_data, -1.5,1.5)
    tx_data = tx_data[0:N_sample] + 1j*tx_data[N_sample:(2*N_sample)]
    return tx_data

def read_file(path):
    with open(path, encoding="utf-8") as file:
        content = file.readlines()
    content = [x.strip() for x in content]
    return content

def write_final(text):
    with open("final.txt", "w+", encoding="utf-8") as file:
        file.write(text)

def compare(strings):
    _max = 0.0
    idx = 0
    for i, s in enumerate(strings):
        count = len(np.array([int(ord(c)) for c in s if 97 < int(ord(c)) < 122]))
        bad = len(np.array([int(ord(c)) for c in s if int(ord(c)) < 30]))
        tmp = count/(bad+1)
        if tmp > _max:
            _max = tmp
            idx = i
    return strings[idx]

def compute_score():
    ini = read_file('initial.txt')
    fin = read_file('final.txt')

    print("Result is : ", fin[0])
    print("Number of different characters : ", jellyfish.damerau_levenshtein_distance(ini[0], fin[0]))