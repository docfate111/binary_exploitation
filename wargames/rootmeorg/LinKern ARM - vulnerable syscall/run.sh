#!/bin/sh
qemu-system-x86_64 \
    -m 128M \
    -s \
    -cpu kvm64 \
    -kernel vmlinuz \
    -initrd initramfs.cpio.gz \
    -snapshot \
    -nographic \
    -monitor /dev/null \
    -no-reboot \
    -append "console=ttyS0 nopti quiet panic=1"
