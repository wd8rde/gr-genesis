#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2015 Robert Anthoney Bouterse, WD8RDE.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import gr
from genesis_g59 import *

class g59(gr.basic_block):
    def __init__(self,
                 freq,
                 filt,
                 attenuation=False,
                 audiopreamp=False,
                 rfpreamp=False,
                 tx=False,
                 transverterver=False):
        gr.basic_block.__init__(self,
            name="g59",
            in_sig=[numpy.float32],
            out_sig=[numpy.float32])
        self.g59 = g59_cmd()
        self.set_lo_frequency(freq)
        self.set_band_filter(filt)
        self.attenuator(attenuation)
        self.audiopreamp(audiopreamp)
        self.transverterver(transverterver)
        self.rfpreamp(rfpreamp)
        self.tx(tx)

    def forecast(self, noutput_items, ninput_items_required):
        #setup size of input_items[i] for work call
        for i in range(len(ninput_items_required)):
            ninput_items_required[i] = noutput_items

    def general_work(self, input_items, output_items):
        output_items[0][:] = input_items[0]
        consume(0, len(input_items[0]))
        #self.consume_each(len(input_items[0]))
        return len(output_items[0])

    def set_lo_frequency(self,freq):
        self.g59.set_freq(freq)

    def set_band_filter(self,filt):
        self.g59.set_filt(filt)

    def attenuator(self,on_off):
        if (on_off):
            self.g59.att_on()
        else:
            self.g59.att_off()

    def audiopreamp(self,on_off):
        if (on_off):
            self.g59.af_on()
        else:
            self.g59.af_off()

    def rfpreamp(self,on_off):
        if (on_off):
            self.g59.rf_on()
        else:
            self.g59.rf_off()

    def tx(self,on_off):
        if (on_off):
            self.g59.tx_on()
        else:
            self.g59.tx_off()

    def transverterver(self,on_off):
        if (on_off):
            self.g59.trv_on()
        else:
            self.g59.trv_off()

