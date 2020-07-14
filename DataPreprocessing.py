#     Copyright 2020 Connnor Anderson
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler

aminoacids = ['G', 'A', 'L', 'M', 'F', 'W', 'K', 'Q', 'E', 'S', 'P', 'V', 'I', 'C', 'Y', 'H', 'R', 'N', 'D', 'T']
label_encoder = LabelEncoder().fit(np.array(aminoacids))
onehot_encoder = OneHotEncoder(sparse=False, dtype=int)


def string_to_array(my_string):
    my_string = my_string.upper()
    my_array = np.array(list(my_string))
    return my_array


def one_hot_encoder(pepseq_array):
    integer_encoded = label_encoder.transform(pepseq_array)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    return onehot_encoded


def run(filepath):
    csvdata = pd.read_csv(filepath)

    df = pd.DataFrame(csvdata, columns=['Sequence', 'Data'])

    data = df.to_numpy()
    pseqs_list = []
    vals_list = []
    for entry in data:
        pseqs_list.append(entry[0])
        vals_list.append(entry[1])

    print("Encoding protein sequences")
    pseqs = []
    for pseq in pseqs_list:
        pseqs.append(one_hot_encoder(string_to_array(pseq)))
    pseqs = np.array(pseqs)

    print("Scaling data")
    unscaled_vals = np.array(vals_list).reshape(-1, 1)
    scaler = StandardScaler()
    scaler.fit(unscaled_vals)
    scaled_vals = scaler.transform(unscaled_vals)

    return pseqs, scaled_vals
