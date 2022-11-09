rule aggregate_poppunk_csv:
    input:
        expand(OUT + "/results_per_sample/{sample}_poppunk/{sample}_poppunk_clusters.csv", sample=SAMPLES),
    output:
        OUT + "/poppunk_clusters.csv",
    log:
        OUT + "/log/summarize.log",
    message:
        "Merging individual popPUNK output to one csv."
    resources:
        mem_gb=config["mem_gb"]["aggregatePoppunkCsv"],
    threads: config["threads"]["aggregatePoppunkCsv"]
    run:
        import pandas as pd
                        
        aggregated_csv = pd.concat([pd.read_csv(f) for f in input], ignore_index=True)
        aggregated_csv.to_csv(output[0])

