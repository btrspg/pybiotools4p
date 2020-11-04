# AUTOGENERATED! DO NOT EDIT! File to edit: 09_bitk.ipynb (unless otherwise specified).

__all__ = ['Bitk']

# Cell

import os
from ..base import Base, modify_cmd


# Cell


class Bitk(Base):
    def __init__(self, software, fd):
        super(Bitk, self).__init__(software)
        self._default = fd
        if '/' in software:
            bin = os.path.dirname(software) + '/'
        else:
            bin = ''
        self._software = bin + 'pybitk'



    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;{software} --version'.format(
            repr=self.__repr__(),
            software=self._software
        )

    @modify_cmd
    def cmd_dedim(self, count,prefix,clinical,size,style,title):
        '''
        '''
        return r'''
{software} {dedim_para} {count} {prefix} \
            --annotation {clinical} \
            --size {size} \
            --style {style} \
            -t {title} \

        '''.format(
            software=self._software,
            dedim_para=self._default['dedim'],
            **locals()
        )

    @modify_cmd
    def cmd_fc_rename(self, fc,clinical,prefix,sample_title,bam_title,count_title):
        '''
        '''
        return r'''
{software} {fc_rename} {fc} {clinical} {prefix} \
        -s {sample_title} \
        -b {bam_title} \
        -c {count_title}
        '''.format(
            software=self._software,
            fc_rename=self._default['fc_rename'],
            **locals()
        )

    @modify_cmd
    def cmd_merge_fc_deseq2(self,featurecounts_file,deseq2_file,output,key_in_fc,key_in_deseq2):
        return r'''
 {software} {merge_fc_deseq2} \
    --key-in-fc '{key_in_fc}' \
    --key-in-deseq2 '{key_in_deseq2}' \
    {featurecounts_file} {deseq2_file} {output}
        '''.format(
            software=self._software,
            merge_fc_deseq2=self._default['merge_fc_deseq2'],
            **locals()
        )

    def __repr__(self):
        return 'inhouse python package:' + self._software

    def __str__(self):
        return '''
In-house python package, https://github.com/btrspg/bitk.git
        '''