import os
import mne
from mne.preprocessing import (ICA, create_eog_epochs, create_ecg_epochs, corrmap)
from mne import Epochs, pick_types, events_from_annotations
from mne.channels import make_standard_montage
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci
import numpy as np
from exportICAcsv import loadData
from exportICAcsv import makeIca

loadData()

''' 
raws = list()
icas = list()

epoch_set = []
label_set = []
raw_set = []
picks_set = []


mapping = {
    'Fc5.': 'FC5', 'Fc3.': 'FC3', 'Fc1.': 'FC1', 'Fcz.': 'FCz', 'Fc2.': 'FC2',
    'Fc4.': 'FC4', 'Fc6.': 'FC6', 'C5..': 'C5', 'C3..': 'C3', 'C1..': 'C1',
    'Cz..': 'Cz', 'C2..': 'C2', 'C4..': 'C4', 'C6..': 'C6', 'Cp5.': 'CP5',
    'Cp3.': 'CP3', 'Cp1.': 'CP1', 'Cpz.': 'CPz', 'Cp2.': 'CP2', 'Cp4.': 'CP4',
    'Cp6.': 'CP6', 'Fp1.': 'Fp1', 'Fpz.': 'Fpz', 'Fp2.': 'Fp2', 'Af7.': 'AF7',
    'Af3.': 'AF3', 'Afz.': 'AFz', 'Af4.': 'AF4', 'Af8.': 'AF8', 'F7..': 'F7',
    'F5..': 'F5', 'F3..': 'F3', 'F1..': 'F1', 'Fz..': 'Fz', 'F2..': 'F2',
    'F4..': 'F4', 'F6..': 'F6', 'F8..': 'F8', 'Ft7.': 'FT7', 'Ft8.': 'FT8',
    'T7..': 'T7', 'T8..': 'T8', 'T9..': 'T9', 'T10.': 'T10', 'Tp7.': 'TP7',
    'Tp8.': 'TP8', 'P7..': 'P7', 'P5..': 'P5', 'P3..': 'P3', 'P1..': 'P1',
    'Pz..': 'Pz', 'P2..': 'P2', 'P4..': 'P4', 'P6..': 'P6', 'P8..': 'P8',
    'Po7.': 'PO7', 'Po3.': 'PO3', 'Poz.': 'POz', 'Po4.': 'PO4', 'Po8.': 'PO8',
    'O1..': 'O1', 'Oz..': 'Oz', 'O2..': 'O2', 'Iz..': 'Iz'
}


tmin, tmax = -1., 4.
event_id = dict(hands=2, feet=3)
subject = 1
runs = [3]  # motor imagery: hands vs feet

raw_fnames = eegbci.load_data(subject, runs)
raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
raw.rename_channels(mapping)
#eegbci.standardize(raw)
montage = make_standard_montage('standard_1005')
raw.set_montage(montage)
#raw.rename_channels(lambda x: x.strip('.'))


raw.crop(tmax=60.)
raw.filter(14., 30.)

picks = pick_types(raw.info, eeg=True)
events, _ = events_from_annotations(raw, event_id=dict(T1=2, T2=3))
#7
epochs = Epochs(raw, events, event_id, tmin, tmax, picks=picks, preload=True)
labels = epochs.events[:, -1] - 2;

epoch_set.append(epochs)
label_set.append(labels)
raw_set.append(raw)
picks_set.append(picks)

print(label_set)


##epochs = mne.Epochs(raw, event_id, tmin, tmax, picks=picks, verbose = False)


#raw.rename_channels(mapping)

#random bc the ica is not determining, sign flips
ica = ICA(n_components=15, random_state=97)
ica.fit(raw)
icaArray = ica.get_components()

raws.append(raw)
icas.append(ica)
print(icas)





#ica.apply()

#raw.load_data()
#ica.plot_sources(raw, show_scrollbars=False)

#ica.plot_properties(raw, picks=[0, 1])

#ica.plot_scores()


icaArray = ica.get_components()

#features = ica.get_sources()
#print(features)

print(icaArray)




#print(mixed)
#print(unmixed)
#print(features)
#sIcaArray = base64.b64encode(icaArray)
#bIcaArray = icaArray.tobytes()

''' 
