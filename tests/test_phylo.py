from vcfkit import phylo
from subprocess import Popen, PIPE
import hashlib
from tests.test_utilities import Capturing


def test_phylo_fasta():
    with Capturing() as out:
        phylo.main(["phylo", "fasta", "test_data/test.vcf.gz"])
    last_line = out[-1]
    assert 2958 == len(last_line)
    assert last_line.startswith("AANNCTC")


def test_phylo_nj():
    with Capturing() as out:
        phylo.main(["phylo", "tree", "nj", "test_data/test.vcf.gz"])
    line = out[24]
    assert line == "DL200:0.132458"


def test_phylo_upgma():
    with Capturing() as out:
        comm = ["phylo", "tree", "upgma", "test_data/test.vcf.gz"]
        phylo.main(comm)
    line = out[25]
    assert line == "RC301:0.0854988"
