import yaml


sample_sheet=config["sample_sheet"]
with open(sample_sheet) as f:
    SAMPLES = yaml.safe_load(f)

OUT = config["out"]

localrules:
    all,


include: "workflow/rules/rule.smk"
include: "workflow/rules/createQfile.smk"


rule all:
    input:
        expand(OUT + "/{sample}_qfile.txt", sample=SAMPLES),
