import pathlib
import yaml
import argparse
import sys

sys.path.append("./base_juno_pipeline")
from base_juno_pipeline.base_juno_pipeline import (
    PipelineStartup,
    RunSnakemake,
    helper_functions,
)


class TemplateRun(PipelineStartup, RunSnakemake):
    def __init__(
        self,
        input_dir,
        output_dir,
        input_type="fastq",
        unlock=False,
        rerunincomplete=False,
        dryrun=False,
        **kwargs
    ):
        PipelineStartup.__init__(
            self,
            input_dir,
            input_type=input_type,
        )
        RunSnakemake.__init__(
            self,
            pipeline_name="template",
            pipeline_version="0.1.0",
            output_dir=output_dir,
            workdir=pathlib.Path(__file__).parent.resolve(),
            unlock=unlock,
            rerunincomplete=rerunincomplete,
            dryrun=dryrun,
            **kwargs,
        )
        self.start_juno_pipeline()
        self.config_params = {
            "input_dir": str(self.input_dir),
            "out": str(self.output_dir),
        }
        with open(self.user_parameters, "w") as f:
            yaml.dump(self.config_params, f, default_flow_style=False)
        self.run_snakemake()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Template juno pipeline. If you see this message please change it to something appropriate"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=pathlib.Path,
        required=True,
        metavar="DIR",
        help="Relative or absolute path to the input directory. It must either be the output directory of the Juno-assembly pipeline or it must contain all the raw reads (fastq) and assemblies (fasta) files for all samples to be processed.",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=pathlib.Path,
        metavar="DIR",
        default="output",
        help="Relative or absolute path to the output directory. If non is given, an 'output' directory will be created in the current directory.",
    )
    parser.add_argument(
        "-l",
        "--local",
        action="store_true",
        help="Running pipeline locally (instead of in a computer cluster). Default is running it in a cluster.",
    )
    # Snakemake arguments
    parser.add_argument(
        "-u",
        "--unlock",
        action="store_true",
        help="Unlock output directory (passed to snakemake).",
    )
    parser.add_argument(
        "-n",
        "--dryrun",
        action="store_true",
        help="Dry run printing steps to be taken in the pipeline without actually running it (passed to snakemake).",
    )
    parser.add_argument(
        "--rerunincomplete",
        action="store_true",
        help="Re-run jobs if they are marked as incomplete (passed to snakemake).",
    )
    parser.add_argument(
        "--snakemake-args",
        nargs="*",
        default={},
        action=helper_functions.SnakemakeKwargsAction,
        help="Extra arguments to be passed to snakemake API (https://snakemake.readthedocs.io/en/stable/api_reference/snakemake.html).",
    )
    args = parser.parse_args()
    TemplateRun(
        input_dir=args.input,
        output_dir=args.output,
        local=args.local,
        unlock=args.unlock,
        rerunincomplete=args.rerunincomplete,
        dryrun=args.dryrun,
        **args.snakemake_args,
    )
