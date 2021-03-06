# AUTOGENERATED! DO NOT EDIT! File to edit: 14_kallisto.ipynb (unless otherwise specified).

__all__ = ['Kallisto']

# Cell

from ..base import Base, modify_cmd


# Cell

class Kallisto(Base):
    def __init__(self, software, fd):
        super(Kallisto, self).__init__(software)
        self._default = fd

    def cmd_version(self):
        '''
        :return:
        '''
        return 'echo {repr} ;echo $({software} version)'.format(
            repr=self.__repr__(),
            software=self._software
        )


    #TODO:
    @modify_cmd
    def cmd_inspect():
        '''
Inspects and gives information about an index

        '''
        pass


    #TODO:
    @modify_cmd
    def cmd_h5dump():
        '''
Converts HDF5-formatted results to plaintext
        '''
        pass



    #TODO:
    @modify_cmd
    def cmd_merge():
        '''
Merges several batch runs
        '''
        pass

    #TODO:
    @modify_cmd
    def cmd_pseudo():
        '''
Runs the pseudoalignment step
        '''
        pass


    #TODO:
    @modify_cmd
    def cmd_bus():
        '''
Generate BUS files for single-cell data
        '''
        pass



    @modify_cmd
    def cmd_quant(self, fastq,index,outdir,gtf):
        '''
Runs the quantification algorithm
        '''
        return r'''
{software} {quant_para} \
        --gtf {gtf} \
        --output-dir {outdir} \
        --index {index} \
        {fastq}
        '''.format(
            software=self._software,
            quant_para=self._default['quant'],
            **locals()
        )

    @modify_cmd
    def cmd_index(self, fasta, index):
        '''
Builds a kallisto index
        '''
        return r'''
{software} {index_para} \
        --index {index} \
        {fasta}
        '''.format(
            software=self._software,
            index_para=self._default['index'],
            **locals()
        )




    def __repr__(self):
        return 'kallisto:' + self._software

    def __str__(self):
        return '''
kallisto is a program for quantifying abundances of transcripts from bulk and single-cell RNA-Seq data,
or more generally of target sequences using high-throughput sequencing reads.

When using this program in your research, please cite

  Bray, N. L., Pimentel, H., Melsted, P. & Pachter, L.
  Near-optimal probabilistic RNA-seq quantification,
  Nature Biotechnology 34, 525-527(2016), doi:10.1038/nbt.3519
        '''