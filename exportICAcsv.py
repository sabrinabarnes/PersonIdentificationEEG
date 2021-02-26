import csv
import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs, corrmap)
from mne import Epochs, pick_types, events_from_annotations
from mne.channels import make_standard_montage
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci
import numpy as np

#file name is S003.csv 
def makeIca(fileName, raw):
  ica = ICA(n_components=15, random_state=97)
  ica.fit(raw)
  icaArray = ica.get_components()

  with open(fileName, 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(icaArray)

def loadData():
  for i in range(3, 4):
    tmin, tmax = -1., 4.
    event_id = dict(hands=2, feet=3)
    subject = i 
    for j in range (1,2):
      runs = j
      raw_fnames = eegbci.load_data(subject, runs)
      raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
      eegbci.standardize(raw)
      montage = make_standard_montage('standard_1005')
      raw.set_montage(montage)
      raw.rename_channels(lambda x: x.strip('.'))
      raw.crop(tmax=60.)
      raw.filter(14., 30.)
      picks = pick_types(raw.info, eeg=True)
      #events, _ = events_from_annotations(raw, event_id=dict(T1=2, T2=3))
      #7
      #epochs = Epochs(raw, events, event_id, tmin, tmax, picks=picks, preload=True)
      #labels = epochs.events[:, -1] - 2;

      filename = "eeg" + str(i) + "-"+ str(j) +".csv"
      makeIca(filename, raw)
