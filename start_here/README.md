# Notes for developers.

- We use `miniconda`, `nbdev` and `jupyter lab` for development

- After cloning the repository create a virtual environment from `environment.yml`

- If you need to add a new library in development use:

  > $ !pip install < library name >
  > In the notebook you are working on.

- All code is written in `nbs folder` and exported using `nbdev` command.

- Very rarely should you export and share your installed env packages but if you must run the bash script `run_export_env.sh` (Ask someone on the project for a windows variant.)

- Finally code is read in the oder of numbering in `nbs folder` i.e notebook 001_name thename notebook 002_name

## HAPPY HACKING!!!
