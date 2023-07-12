# Changelog

## [0.1.3](https://github.com/RIVM-bioinformatics/juno-population/compare/v0.1.2...v0.1.3) (2023-07-12)


### Dependencies

* removing anaconda and defaults channel and adding no defaults ([efb7784](https://github.com/RIVM-bioinformatics/juno-population/commit/efb7784a718da242ce159f7392954ce11b09637a))

## [0.1.2](https://github.com/RIVM-bioinformatics/juno-population/compare/v0.1.1...v0.1.2) (2023-02-16)


### Bug Fixes

* Pin juno-library version ([18c8584](https://github.com/RIVM-bioinformatics/juno-population/commit/18c8584a42e47d80c1532d317e280f513a6d05f3))

## [0.1.1](https://github.com/RIVM-bioinformatics/juno-population/compare/v0.1.0...v0.1.1) (2023-01-09)


### Features

* Support external clustering flag of popPUNK. ([60a8eb0](https://github.com/RIVM-bioinformatics/juno-population/commit/60a8eb01c67eb537f0b4a1c61c81db52f7db8ca5))


### Bug Fixes

* Add base_juno to master environment ([e8a06a6](https://github.com/RIVM-bioinformatics/juno-population/commit/e8a06a676454a7dda05ec470bb5eca55532f84b3))
* Correct the config lookup in aggregatePoppunkCsv rule ([e3365f8](https://github.com/RIVM-bioinformatics/juno-population/commit/e3365f8c7ffba85a311b5d49935bf6a71b21c998))

## 0.1.0 (2022-11-16)


### Features

* Add --species to run_pipeline.sh. Fix: Correct input type from both to fasta. ([4a2594b](https://github.com/RIVM-bioinformatics/juno-population/commit/4a2594bc611568652ea9fa5e92841ec2a6df3cfc))
* added --species and --database arguments and use these to set correct poppunk db_dir ([6e6c95c](https://github.com/RIVM-bioinformatics/juno-population/commit/6e6c95ce7b6f9e781ef61784ed994b4c98577ed0))
* Create first version of rule for Q-file ([e1a6d4d](https://github.com/RIVM-bioinformatics/juno-population/commit/e1a6d4d3e5ed20e063900e66dfe32d18eff55f7a))
* Create hardcoded version of popPUNK rule ([131de03](https://github.com/RIVM-bioinformatics/juno-population/commit/131de0379f8796c856a035ddc07706ebb14d2843))
* Create summary rule. ([0f3e219](https://github.com/RIVM-bioinformatics/juno-population/commit/0f3e21915f2a82cbe7bb7ec3aa68926b91812b4e))


### Bug Fixes

* Add default species "other" in run_pipeline.sh ([931882c](https://github.com/RIVM-bioinformatics/juno-population/commit/931882c50b3b08ecf61650461305095da3a4ce2f))
* Correctly handle --queue argument. ([7f0833a](https://github.com/RIVM-bioinformatics/juno-population/commit/7f0833a4f333c83230d986f4aa6a44658e3d12f7))
* Specify juno-library version ([5b64764](https://github.com/RIVM-bioinformatics/juno-population/commit/5b647640458a9b488e580f4e70cb9165d16b602c))
