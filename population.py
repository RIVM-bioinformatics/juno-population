import pathlib
from pickle import DUP
import yaml
import argparse
import sys

sys.path.append("./base_juno_pipeline")
from base_juno_pipeline.base_juno_pipeline import (
    PipelineStartup,
    RunSnakemake,
    helper_functions,
)

from database_locations import species_database_locations


class PopulationRun(PipelineStartup, RunSnakemake):
    def __init__(
        self,
        input_dir,
        output_dir,
        species=None,
        db_dir=None,
        input_type="fasta",
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
            pipeline_name="population",
            pipeline_version="0.1.0",
            output_dir=output_dir,
            workdir=pathlib.Path(__file__).parent.resolve(),
            unlock=unlock,
            rerunincomplete=rerunincomplete,
            dryrun=dryrun,
            **kwargs,
        )

        # Specific Juno-Population pipeline attributes
        if not db_dir:
            self.db_dir = species_database_locations.get(species)
            if not self.db_dir:
                raise KeyError(
                    "Cannot determine db_dir: This species is currently not configured AND no db_dir was provided. Manually provide a db_dir via -b/--database, or ask for your species to be configured."
                )

        self.user_parameters = pathlib.Path("config/user_parameters.yaml")

        # Start pipeline
        self.start_juno_pipeline()

        # Create user_parameters.yaml and sample_sheet.yaml files
        self.config_params = {
            "input_dir": str(self.input_dir),
            "out": str(self.output_dir),
            "db_dir": str(self.db_dir),
        }
        with open(self.user_parameters, "w") as f:
            yaml.dump(self.config_params, f, default_flow_style=False)

        with open(self.sample_sheet, "w") as f:
            yaml.dump(self.sample_dict, f, default_flow_style=False)
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
        "-s",
        "--species",
        default=None,
        required=False,
        help="The species name, use an underscore instead of a space (e.g. streptococcus_pneumoniae). Check the publicly available popPUNK databases on www.poppunk.net/pages/databases.html",
    )
    parser.add_argument(
        "-b",
        "--database",
        default=None,
        required=False,
        help="The path to the popPUNK database to use. This overrides information provide with the --species argument.",
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
    PopulationRun(
        input_dir=args.input,
        output_dir=args.output,
        species=args.species,
        db_dir=args.database,
        local=args.local,
        unlock=args.unlock,
        rerunincomplete=args.rerunincomplete,
        dryrun=args.dryrun,
        **args.snakemake_args,
    )
