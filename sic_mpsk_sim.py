#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: sic_mpsk_sim
# Author: Rafik Zitouni
# Description: Flow Graph
# Generated: Tue Apr 10 17:27:48 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.qtgui import Range, RangeWidget
from grc_gnuradio import blks2 as grc_blks2
from optparse import OptionParser
import math
import numpy
import sip
import sys
from gnuradio import qtgui


class sic_mpsk_sim(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "sic_mpsk_sim")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("sic_mpsk_sim")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "sic_mpsk_sim")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.snr_db = snr_db = 10
        self.const_type = const_type = 1
        self.variable_qtgui_label_0 = variable_qtgui_label_0 = {0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[const_type] + " - Change const_type for different constellation types!"
        self.noisevar = noisevar = 10**(-snr_db/10)
        self.const = const = (digital.constellation_bpsk(), digital.constellation_qpsk(), digital.constellation_8psk())
        self.block = block = 1000
        self.alpha = alpha = .1
        self.R = R = 100e3

        ##################################################
        # Blocks
        ##################################################
        self._alpha_range = Range(0, 1, .01, .1, 200)
        self._alpha_win = RangeWidget(self._alpha_range, self.set_alpha, 'Alpha (P1/P)', "counter_slider", float)
        self.top_layout.addWidget(self._alpha_win)
        self._variable_qtgui_label_0_tool_bar = Qt.QToolBar(self)

        if None:
          self._variable_qtgui_label_0_formatter = None
        else:
          self._variable_qtgui_label_0_formatter = lambda x: x

        self._variable_qtgui_label_0_tool_bar.addWidget(Qt.QLabel('Constellation Type'+": "))
        self._variable_qtgui_label_0_label = Qt.QLabel(str(self._variable_qtgui_label_0_formatter(self.variable_qtgui_label_0)))
        self._variable_qtgui_label_0_tool_bar.addWidget(self._variable_qtgui_label_0_label)
        self.top_layout.addWidget(self._variable_qtgui_label_0_tool_bar)

        self._snr_db_range = Range(0, 20, 1, 10, 200)
        self._snr_db_win = RangeWidget(self._snr_db_range, self.set_snr_db, 'P/sigma^2 (dB)', "counter_slider", float)
        self.top_layout.addWidget(self._snr_db_win)
        self.qtgui_number_sink_0_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0_0.set_title('BER 1 (after cancelling user 2)')

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_0_win, 1,0,1,1)
        self.qtgui_number_sink_0_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0_0.set_title("BER 2 (after cancelling user 1)")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_0_win, 1,1,1,1)
        self.qtgui_number_sink_0_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0_0.set_update_time(0.10)
        self.qtgui_number_sink_0_0.set_title("BER 2 (Without Cancellation)")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0_0.set_min(i, 0)
            self.qtgui_number_sink_0_0.set_max(i, 1)
            self.qtgui_number_sink_0_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0_0.set_label(i, labels[i])
            self.qtgui_number_sink_0_0.set_unit(i, units[i])
            self.qtgui_number_sink_0_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0_0.enable_autoscale(False)
        self._qtgui_number_sink_0_0_win = sip.wrapinstance(self.qtgui_number_sink_0_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_0_win, 0,1,1,1)
        self.qtgui_number_sink_0 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_0.set_update_time(0.10)
        self.qtgui_number_sink_0.set_title("BER1 (Without Cancellation)")

        labels = ['BER', '', '', '', '',
                  '', '', '', '', '']
        units = ['', '', '', '', '',
                 '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
                  ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        for i in xrange(1):
            self.qtgui_number_sink_0.set_min(i, 0)
            self.qtgui_number_sink_0.set_max(i, 1)
            self.qtgui_number_sink_0.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_0.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_0.set_label(i, labels[i])
            self.qtgui_number_sink_0.set_unit(i, units[i])
            self.qtgui_number_sink_0.set_factor(i, factor[i])

        self.qtgui_number_sink_0.enable_autoscale(False)
        self._qtgui_number_sink_0_win = sip.wrapinstance(self.qtgui_number_sink_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_number_sink_0_win, 0,0,1,1)
        self.qtgui_const_sink_x_0_0 = qtgui.const_sink_c(
        	1024, #size
        	"Constellation", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0_0.enable_grid(False)
        self.qtgui_const_sink_x_0_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0_0.disable_legend()

        labels = ["Constellation: "+str(const[const_type].arity()) + "-PSK", '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [0.6, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_0_win)
        self.digital_constellation_decoder_cb_0_0_0_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_constellation_decoder_cb_0_0_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_constellation_decoder_cb_0_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(const[const_type].base())
        self.digital_chunks_to_symbols_xx_2 = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.digital_chunks_to_symbols_xx_1_0 = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.digital_chunks_to_symbols_xx_1 = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.digital_chunks_to_symbols_xx = digital.chunks_to_symbols_bc((const[const_type].points()), 1)
        self.blocks_throttle_0_1 = blocks.throttle(gr.sizeof_char*1, R,True)
        self.blocks_sub_xx_2_0 = blocks.sub_cc(1)
        self.blocks_sub_xx_2 = blocks.sub_cc(1)
        self.blocks_multiply_const_vxx_2_0 = blocks.multiply_const_vcc(((1-alpha)**0.5, ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vcc((alpha**0.5, ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vcc(((1-alpha)**0.5, ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((alpha**0.5, ))
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.blks2_error_rate_0_0_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.blks2_error_rate_0_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.blks2_error_rate_0_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.blks2_error_rate_0 = grc_blks2.error_rate(
        	type='BER',
        	win_size=block*100,
        	bits_per_symbol=2,
        )
        self.analog_random_source_x_1 = blocks.vector_source_b(map(int, numpy.random.randint(0, const[const_type].arity(), block)), True)
        self.analog_random_source_x_0 = blocks.vector_source_b(map(int, numpy.random.randint(0, const[const_type].arity(), block)), True)
        self.analog_noise_source_x_0 = analog.noise_source_c(analog.GR_GAUSSIAN, noisevar, -42)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_noise_source_x_0, 0), (self.blocks_add_xx_0, 2))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blks2_error_rate_0_0_0_0, 0))
        self.connect((self.analog_random_source_x_0, 0), (self.blocks_throttle_0_1, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.blks2_error_rate_0_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.blks2_error_rate_0_0_0, 0))
        self.connect((self.analog_random_source_x_1, 0), (self.digital_chunks_to_symbols_xx_2, 0))
        self.connect((self.blks2_error_rate_0, 0), (self.qtgui_number_sink_0, 0))
        self.connect((self.blks2_error_rate_0_0, 0), (self.qtgui_number_sink_0_0, 0))
        self.connect((self.blks2_error_rate_0_0_0, 0), (self.qtgui_number_sink_0_0_0, 0))
        self.connect((self.blks2_error_rate_0_0_0_0, 0), (self.qtgui_number_sink_0_0_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_sub_xx_2, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_sub_xx_2_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.digital_constellation_decoder_cb_0_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.qtgui_const_sink_x_0_0, 0))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_sub_xx_2, 1))
        self.connect((self.blocks_multiply_const_vxx_2_0, 0), (self.blocks_sub_xx_2_0, 1))
        self.connect((self.blocks_sub_xx_2, 0), (self.digital_constellation_decoder_cb_0_0_0, 0))
        self.connect((self.blocks_sub_xx_2_0, 0), (self.digital_constellation_decoder_cb_0_0_0_0, 0))
        self.connect((self.blocks_throttle_0_1, 0), (self.digital_chunks_to_symbols_xx, 0))
        self.connect((self.digital_chunks_to_symbols_xx, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_1, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.digital_chunks_to_symbols_xx_1_0, 0), (self.blocks_multiply_const_vxx_2_0, 0))
        self.connect((self.digital_chunks_to_symbols_xx_2, 0), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.blks2_error_rate_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_chunks_to_symbols_xx_1, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.blks2_error_rate_0_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0_0, 0), (self.digital_chunks_to_symbols_xx_1_0, 0))
        self.connect((self.digital_constellation_decoder_cb_0_0_0, 0), (self.blks2_error_rate_0_0_0, 1))
        self.connect((self.digital_constellation_decoder_cb_0_0_0_0, 0), (self.blks2_error_rate_0_0_0_0, 1))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "sic_mpsk_sim")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_snr_db(self):
        return self.snr_db

    def set_snr_db(self, snr_db):
        self.snr_db = snr_db
        self.set_noisevar(10**(-self.snr_db/10))

    def get_const_type(self):
        return self.const_type

    def set_const_type(self, const_type):
        self.const_type = const_type
        self.set_variable_qtgui_label_0(self._variable_qtgui_label_0_formatter({0: 'BPSK', 1: 'QPSK', 2: '8-PSK'}[self.const_type] + " - Change const_type for different constellation types!"))
        self.digital_chunks_to_symbols_xx_2.set_symbol_table((self.const[self.const_type].points()))
        self.digital_chunks_to_symbols_xx_1_0.set_symbol_table((self.const[self.const_type].points()))
        self.digital_chunks_to_symbols_xx_1.set_symbol_table((self.const[self.const_type].points()))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[self.const_type].points()))

    def get_variable_qtgui_label_0(self):
        return self.variable_qtgui_label_0

    def set_variable_qtgui_label_0(self, variable_qtgui_label_0):
        self.variable_qtgui_label_0 = variable_qtgui_label_0
        Qt.QMetaObject.invokeMethod(self._variable_qtgui_label_0_label, "setText", Qt.Q_ARG("QString", str(self.variable_qtgui_label_0)))

    def get_noisevar(self):
        return self.noisevar

    def set_noisevar(self, noisevar):
        self.noisevar = noisevar
        self.analog_noise_source_x_0.set_amplitude(self.noisevar)

    def get_const(self):
        return self.const

    def set_const(self, const):
        self.const = const
        self.digital_chunks_to_symbols_xx_2.set_symbol_table((self.const[self.const_type].points()))
        self.digital_chunks_to_symbols_xx_1_0.set_symbol_table((self.const[self.const_type].points()))
        self.digital_chunks_to_symbols_xx_1.set_symbol_table((self.const[self.const_type].points()))
        self.digital_chunks_to_symbols_xx.set_symbol_table((self.const[self.const_type].points()))

    def get_block(self):
        return self.block

    def set_block(self, block):
        self.block = block

    def get_alpha(self):
        return self.alpha

    def set_alpha(self, alpha):
        self.alpha = alpha
        self.blocks_multiply_const_vxx_2_0.set_k(((1-self.alpha)**0.5, ))
        self.blocks_multiply_const_vxx_2.set_k((self.alpha**0.5, ))
        self.blocks_multiply_const_vxx_1.set_k(((1-self.alpha)**0.5, ))
        self.blocks_multiply_const_vxx_0.set_k((self.alpha**0.5, ))

    def get_R(self):
        return self.R

    def set_R(self, R):
        self.R = R
        self.blocks_throttle_0_1.set_sample_rate(self.R)


def main(top_block_cls=sic_mpsk_sim, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
