import os


def create_external_clustering_flag(external_clustering_flag, db_dir):
    if external_clustering_flag:
        db_dir_name = os.path.basename(os.path.normpath(db_dir))
        return f"--external-clustering {db_dir}/{db_dir_name}_external_clusters.csv"
    return ""


rule assign_popPUNK_cluster:
    input:
        OUT + "/q_files/{sample}_qfile.txt",
    output:
        output_dir=directory(OUT + "/results_per_sample/{sample}_poppunk/"),
        output_csv=OUT
        + "/results_per_sample/{sample}_poppunk/{sample}_poppunk_clusters.csv",
        output_pkl=OUT
        + "/results_per_sample/{sample}_poppunk/{sample}_poppunk.dists.pkl",
        output_npy=OUT
        + "/results_per_sample/{sample}_poppunk/{sample}_poppunk.dists.npy",
        output_h5=OUT + "/results_per_sample/{sample}_poppunk/{sample}_poppunk.h5",
        external_csv=OUT
        + "/results_per_sample/{sample}_poppunk/{sample}_poppunk_external_clusters.csv"
        if config["external_clustering"]
        else [],
    log:
        OUT + "/log/{sample}_poppunk.log",
    conda:
        "../envs/poppunk.yaml"
    message:
        "Running popPUNK clustering"
    params:
        db_dir=config["db_dir"],
        external_clustering=create_external_clustering_flag(
            config["external_clustering"], config["db_dir"]
        ),
    resources:
        mem_gb=config["mem_gb"]["fasta_popPUNK"],
    threads: config["threads"]["fasta_popPUNK"]
    shell:
        """
        poppunk_assign \
            --db {params.db_dir} \
            --threads {threads} --query {input} --output {output.output_dir} {params.external_clustering}\
            2> {log}
        """
