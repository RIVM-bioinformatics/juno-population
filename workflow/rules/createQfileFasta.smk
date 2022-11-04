rule create_Qfile_fasta:
    """Create popPUNKs required query file, a textfile containing sampleID and location of fasta"""
    # TODO: popPUNK can also work from fastqs. This approach completely ignores this.
    input:
        lambda wc: SAMPLES[wc.sample]["assembly"]
    output:
        OUT + "/q_files/{sample}_qfile.txt"
    resources:
        mem_gb=config["mem_gb"]["create_Qfile"],
    threads: config["threads"]["create_Qfile"]
    shell:"""
    printf "$(basename {input} .fasta)\t$(realpath {input})\n" > {output}
    """