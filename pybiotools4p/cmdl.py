# AUTOGENERATED! DO NOT EDIT! File to edit: u00_main_run.ipynb (unless otherwise specified).

__all__ = ['main']

# Cell

import defopt

from .cmdutils.cmdkallisto import kallisto_quant_merge
from .cmdutils.cmdgffcompare import gffcompare_multiple_gtf_tracking

# Cell

def main():
    cmdlfs = [
        kallisto_quant_merge,
        gffcompare_multiple_gtf_tracking,
    ]
    defopt.run(cmdlfs)