# Notes for developers.

- We use `miniconda`, `nbdev` and `jupyter lab` for development
- After cloning the repository create a virtual environment from `environment.yml`
- There are two ways of adding code to this repo:

  * If what you are doing involves experimenting with Jupyter Lab, you may want to write your code in a Jupyter Notebook in the folder nbs (make sure you follow the naming convention <number>_<file_name>). This convention helps us track how to follow the logic of the code. In which case use [nbdev](https://nbdev.fast.ai/)
  * If you are just addig code that does not involve experimenting with Jupyter Lab, add said code to the `qgoferutils` folder by following the convention <file_name_> the trailing underscore tells other developers this was not exported from nbs folder using nbdev.

- If you need to add a new library in development use:

  > $ !pip install < library name > - when using jupyter lab in the notebook you are working on.
  > pip install < library name > - at the terminal when adding code directly to the repo

- When done adding the library and you are sure it must be shipped to users add it as either a dev_reuirement, requirement etc based on [Search for requirements section](https://nbdev.fast.ai/tutorials/tutorial.html)

- We encourage testing and unit tests. 

## HAPPY HACKING!!!
