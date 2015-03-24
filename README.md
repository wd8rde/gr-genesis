# gr-genesis
GNURadio blocks for Genesis SDR Radios, written by Robert A. Bouoterse, WD8RDE (mailto:wd8rde@gmail.com)

Currently implemented:
  G59, a block for the Genesis G59 SDR Transceiver.

Depends on genesis_g59_py pacakage, https://github.com/wd8rde/genesis_g59_py.git

to build,

1. git clone https://github.com/wd8rde/gr-genesis.git
2. cd to gr-genesis/
3. mkdir build
4. cd build
5. cmake ../
6. make
7. sudo make install

##Running 
On Ubuntu 14.04, using the gnuradio package 3.7.2.1-5, I found I needed to edit the /etc/gnuradio/conf.d/grc.conf file, and add a path to/usr/local/share/gnuradio/grc/blocks. The resulting file looked like:

```
# This file contains system wide configuration data for GNU Radio.
# You may override any setting on a per-user basis by editing
# ~/.gnuradio/config.conf

[grc]
global_blocks_path = /usr/share/gnuradio/grc/blocks:/usr/local/share/gnuradio/grc/blocks
```

If everything works correctly you will see a Genesis category in the blocks list, and a G59 block inside of it.
