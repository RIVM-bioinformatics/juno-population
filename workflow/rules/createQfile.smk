rule createQfile:
    """Create popPUNKs required query file, a textfile containing sampleID and location of fasta"""
    # TODO: popPUNK can also work from fastqs. This approach completely ignores this.
    input:
        lambda wc: SAMPLES[wc.sample]["assembly"]
    output:
        OUT + "/{sample}_qfile.txt"
    resources:
        mem_gb=config["mem_gb"]["template_rule"],
    threads: config["threads"]["template_rule"]
    shell:"""
    printf "$(basename {input} .fasta)\t$(realpath {input})\n" > {output}
    """