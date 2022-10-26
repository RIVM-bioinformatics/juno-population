rule fasta_popPUNK:
    input:
        expand(OUT + "/{sample}_qfile.txt", sample=SAMPLES)
    output:
        output_dir = directory(OUT + "/{sample}_poppunk/"),
    log:
        OUT + "/log/{sample}_poppunk.log"
    conda:
        "../../envs/poppunk.yaml"
    message:
        "Running popPUNK clustering"
    resources:
        mem_gb=config["mem_gb"]["fasta_popPUNK"],
    threads: config["threads"]["fasta_popPUNK"]
    shell: """
    poppunk_assign --db /mnt/db/juno/poppunk/streptococcus/GPS_v4_references --threads {threads} --query {input} --output {output.output_dir} 2> {log}
    """
