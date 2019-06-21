import pyaudio
import numpy as np
from AudioRecorder.readers import MicroPhoneReader


audio_recorder = MicroPhoneReader()


file_name = input('Please enter file name: ')

data_size = int(input('please enter data size: '))

cap_params = {'file_name': file_name + '.txt',
              'data_type': 'time_domain',
              'data_size': data_size,
              'cap_time': None,
              'cap_type': 'size'}

data = audio_recorder.save_data(cap_params)

print('Captured %d samples and saved to %s.txt' % (len(data), file_name))