rule makeSummaryCsv:
    input:
        OUT + "/results_per_sample/",
    output:
        OUT + "/poppunk_clusters.csv",
    log:
        OUT + "/log/summarize.log"
    message:
        "Merging individual popPUNK output to one csv."
    resources:
        mem_gb=config["mem_gb"]["makeSummaryCsv"],
    params: script = "workflow/scripts/make_summary_csv.py"
    threads: config["threads"]["makeSummaryCsv"]
    shell: """
    python {params.script} -i {input} > {output}
    """
