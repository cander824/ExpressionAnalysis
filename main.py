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

import DataPreprocessing
import LayerOptimizer
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
file = 'proteindata.csv'


def main():
    pseqs, scaled_values = DataPreprocessing.run(file)
    opt_model, split = LayerOptimizer.run(pseqs, scaled_values)
    train_x, test_x, train_y, test_y = split
    opt_model.evaluate(test_x, test_y)
    print("Done")


if __name__ == "__main__":
    main()


