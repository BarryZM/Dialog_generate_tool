# Copyright (c) 2021, NVIDIA CORPORATION.  All rights reserved.
# Copyright 2015 and onwards Google, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from asr_model.text_processing.vi.verbalizers.address import AddressFst
from asr_model.text_processing.vi.verbalizers.cardinal import CardinalFst
from asr_model.text_processing.vi.verbalizers.date import DateFst
from asr_model.text_processing.vi.verbalizers.decimal import DecimalFst
from asr_model.text_processing.vi.verbalizers.fraction import FractionFst
from asr_model.text_processing.vi.verbalizers.electronic import ElectronicFst
from asr_model.text_processing.vi.verbalizers.math import MathFst
from asr_model.text_processing.vi.verbalizers.measure import MeasureFst
from asr_model.text_processing.vi.verbalizers.money import MoneyFst
from asr_model.text_processing.vi.verbalizers.ordinal import OrdinalFst
from asr_model.text_processing.vi.verbalizers.telephone import TelephoneFst
from asr_model.text_processing.vi.verbalizers.time import TimeFst
from asr_model.text_processing.vi.verbalizers.whitelist import WhiteListFst
from asr_model.text_processing.vi.graph_utils import GraphFst


class VerbalizeFst(GraphFst):
    """
    Composes other verbalizer grammars.
    For deployment, this grammar will be compiled and exported to OpenFst Finate State Archiv (FAR) File.
    More details to deployment at NeMo/tools/text_processing_deployment.
    """

    def __init__(self):
        super().__init__(name="verbalize", kind="verbalize")
        cardinal = CardinalFst()
        cardinal_graph = cardinal.fst
        ordinal_graph = OrdinalFst().fst
        decimal = DecimalFst()
        decimal_graph = decimal.fst
        fraction = FractionFst()
        fraction_graph = fraction.fst
        address_graph = AddressFst().fst
        math_graph = MathFst().fst
        measure_graph = MeasureFst(decimal=decimal, cardinal=cardinal).fst
        money_graph = MoneyFst(decimal=decimal).fst
        time_graph = TimeFst().fst
        date_graph = DateFst().fst
        whitelist_graph = WhiteListFst().fst
        telephone_graph = TelephoneFst().fst
        electronic_graph = ElectronicFst().fst
        graph = (
            time_graph
            | date_graph
            | money_graph
            | measure_graph
            | ordinal_graph
            | fraction_graph
            | math_graph
            | address_graph
            | decimal_graph
            | cardinal_graph
            | whitelist_graph
            | telephone_graph
            | electronic_graph
        )
        self.fst = graph
