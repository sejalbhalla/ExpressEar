import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.signal as sg
import os
from scipy.signal import butter, lfilter
import scipy
import pickle

aus = ['1','2l','2r','4','5','6','7','9','10','11','12','13',
       '14','15','16','17','18','20','22','23','24','25','26',
       '27','28','41','42','43','44','45','46l','46r']

subjects = ['1','2','3','4','5','6','7','8','9','10','11','12','13',
            '14','15','16','17','18']

selected_subjects = ['2','4','6','7','11','12','13','15','17']

os.chdir('D:\Weave\ESense Project\Experiments\data')

sub_id = '17'

all_windows = []
all_labels = []
all_subs = []
all_types = []
all_sessions = []

# for sub_id in selected_subjects:
sub = 's' + sub_id
path = os.path.join(os.getcwd(),sub)
dirs = os.listdir(path)

for sess in [1,2,3,4,5,6,7]:
    session = 'session{}'.format(sess)
    sess_path = os.path.join(path, session)
    
    files = os.listdir(sess_path)
    
    for file in files:
        file_name = file.split('.')[0]
        au = file_name.split('_')[2]
        
        if file_name.endswith('Left'):
           file_name = file_name[:-4]
           name_l = file_name + 'Left.csv'
           name_r = file_name + 'Right.csv'
           assert name_l in files and name_r in files
           au = file_name.split('_')[2]
        
           windows = []
           labels = []
        
           # Left
           data_l = pd.read_csv(os.path.join(sess_path, name_l))
           idx_l = list(np.where(data_l.Timestamp == -1)[0])
           assert len(idx_l) == 12
           start_l = idx_l[0]
           end_l = idx_l[-1]
           data_l = data_l[start_l: end_l + 1].iloc[:,1:7]
           data_l = data_l.drop(idx_l)
           idx_l = idx_l[1:-1]
        
           windows_l = []
           type_l = []
        
           for n in idx_l:
               start = n + 1
               end = start + 99
               win = data_l.loc[start: end]
               win = np.array(win)
        
               if(win.shape[0] < 100 and win.shape[0] > 85):
                   print('Correcting AU {} Left'.format(au))
                   diff = 100 - win.shape[0]
                   tmp = data_l.loc[end+1: end+diff]
                   win = np.vstack((win, tmp))
        
               windows_l.append(win.T)
               type_l.append('central')
        
               # Post
               for st in [start+10, start+20]:
                   en = st + 99
                   win = data_l.loc[st: en]
                   win = np.array(win)
        
                   if(win.shape[0] < 100 and win.shape[0] > 85):
                       print('Correcting AU {} Left'.format(au))
                       diff = 100 - win.shape[0]
                       tmp = data_l.loc[end+1: end+diff]
                       win = np.vstack((win, tmp))
        
                   windows_l.append(win.T)
                   type_l.append('post')
        
               # Pre
               for st in [start-11, start-21]:
                   en = st + 100
                   win = data_l.loc[st: en]
                   win = np.array(win)
        
                   if(win.shape[0] < 100 and win.shape[0] > 85):
                       print('Correcting AU {} Left'.format(au))
                       diff = 100 - win.shape[0]
                       tmp = data_l.loc[end+1: end+diff]
                       win = np.vstack((win, tmp))
        
                   windows_l.append(win.T)
                   type_l.append('pre')         
           windows_l = np.array(windows_l)
               
           # Right
           data_r = pd.read_csv(os.path.join(sess_path, name_r))
           idx_r = list(np.where(data_r.Timestamp == -1)[0])
           assert len(idx_r) == 12
           start_r = idx_r[0]
           end_r = idx_r[-1]
           data_r = data_r[start_r: end_r + 1].iloc[:,1:7]
           data_r = data_r.drop(idx_r)
           idx_r = idx_r[1:-1]
          
           windows_r = []
           type_r = []
           
           for n in idx_r:
               start = n + 1
               end = start + 99
               win = data_r.loc[start: end]
               win = np.array(win)
               
               if(win.shape[0] < 100 and win.shape[0] > 85):
                   print('Correcting AU {} Right'.format(au))
                   diff = 100 - win.shape[0]
                   tmp = data_l.loc[end+1: end+diff]
                   win = np.vstack((win, tmp))
               
               windows_r.append(win.T)
               type_r.append('central')
               
               # Post
               for st in [start+10, start+20]:
                   en = st + 99
                   win = data_r.loc[st: en]
                   win = np.array(win)
        
                   if(win.shape[0] < 100 and win.shape[0] > 85):
                       print('Correcting AU {} Right'.format(au))
                       diff = 100 - win.shape[0]
                       tmp = data_l.loc[end+1: end+diff]
                       win = np.vstack((win, tmp))
                       
                   windows_r.append(win.T)
                   type_r.append('post')
               
               # Pre
               for st in [start-11, start-21]:
                   en = st + 100
                   win = data_r.loc[st: en]
                   win = np.array(win)
                   
                   if(win.shape[0] < 100 and win.shape[0] > 85):
                       print('Correcting AU {} Right'.format(au))
                       diff = 100 - win.shape[0]
                       tmp = data_l.loc[end+1: end+diff]
                       win = np.vstack((win, tmp))
        
                   windows_r.append(win.T)
                   type_r.append('pre')
           windows_r = np.array(windows_r)
           
           assert windows_l.shape == windows_r.shape
        
           windows = np.hstack((windows_l, windows_r))
           labels = np.array([au] * len(windows))
           subs = np.array([sub_id] * len(windows))
           sessions = np.array([sess] * len(windows))
           assert type_l == type_r
           types = type_l
           all_windows.append(windows)
           all_labels.append(labels)
           all_types.append(types)
           all_subs.append(subs)
           all_sessions.append(sessions)

final_windows = np.concatenate(all_windows, axis=0)
final_labels = np.concatenate(all_labels, axis=0).reshape(-1,1)
final_subs = np.concatenate(all_subs, axis=0).reshape(-1,1)
final_types = np.concatenate(all_types, axis=0).reshape(-1,1)
final_sessions = np.concatenate(all_sessions, axis=0).reshape(-1,1)

final_X = final_windows 
final_y = np.hstack([final_labels, final_subs, final_types, final_sessions])
final_y = pd.DataFrame(final_y, columns=['label', 'subject','window_type','session'])

os.chdir('D:\Weave\ESense Project\Experiments\data')
pickle.dump(final_X, open('pickled_data\{}_X.pkl'.format(sub), 'wb'))
pickle.dump(final_y, open('pickled_data\{}_y.pkl'.format(sub), 'wb'))


# #----------------
# del windows_l[i]
# del type_l[i]

# del windows_r[i]
# del type_r[i]