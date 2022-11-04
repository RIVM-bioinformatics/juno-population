rule fasta_popPUNK:
    input:
        expand(OUT + "/{sample}_qfile.txt", sample=SAMPLES)
    output:
        output_dir = directory(OUT + "/{sample}_poppunk/"),
        output_csv = OUT + "/{sample}_poppunk/{sample}_poppunk_clusters.csv",
        output_pkl = OUT + "/{sample}_poppunk/{sample}_poppunk.dists.pkl",
        output_npy = OUT + "/{sample}_poppunk/{sample}_poppunk.dists.npy",
        output_h5 = OUT + "/{sample}_poppunk/{sample}_poppunk.h5",
    log:
        OUT + "/log/{sample}_poppunk.log"
    conda:
        "../../envs/poppunk.yaml"
    message:
        "Running popPUNK clustering"
    params:
        db_dir = config["db_dir"],
    resources:
        mem_gb=config["mem_gb"]["fasta_popPUNK"],
    threads: config["threads"]["fasta_popPUNK"]
    shell: """
    poppunk_assign \
        --db {params.db_dir} \
        --threads {threads} --query {input} --output {output.output_dir} 2> {log}
    """
