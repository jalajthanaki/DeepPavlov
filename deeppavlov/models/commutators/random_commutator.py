"""
Copyright 2017 Neural Networks and Deep Learning lab, MIPT

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from random import choice

from deeppavlov.core.common.registry import register
from deeppavlov.core.models.inferable import Inferable


@register("random")
class RandomCommutator(Inferable):
    def __init__(self):
        pass

    def _commutate(self, predictions, history):
        idx = choice(range(len(predictions)))
        winner = predictions[idx]
        name = list(winner.keys())[0]
        prediction = list(winner.values())[0]
        return idx, name, prediction

    def infer(self, predictions, history):
        return self._commutate(predictions,  history)
