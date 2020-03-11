[![pipeline status](https://code.falcon.lab/kestrel-dev/python-utils/boilersson/badges/dev/pipeline.svg)](https://code.falcon.lab/kestrel-dev/python-utils/boilersson/commits/dev)
[![coverage report](https://code.falcon.lab/kestrel-dev/python-utils/boilersson/badges/dev/coverage.svg)](https://code.falcon.lab/kestrel-dev/python-utils/boilersson/commits/dev)

# BOILERSSON
A minimum boilerplate for new Falcon's projects serving a python package.

### To use it:
(remember to set new project name)

```bash
export NEW_PROJECT_NAME="enter_the_project_name"

## checkout the boilersson project:
git clone git@code.falcon.lab:kestrel-dev/python-utils/boilersson.git ${NEW_PROJECT_NAME}

## If you have problems with ssh heys, use https:
## git clone https://code.falcon.lab/kestrel-dev/python-utils/boilersson.git

cd ${NEW_PROJECT_NAME}

## remove git directory:
rm -rf .git

## replace each occurence of boilersson word into ${NEW_PROJECT_NAME}
find ./ -type f -exec sed -i 's/boilersson/${NEW_PROJECT_NAME}/gI' {} \;

## Note that if the project has to be placed out of kestrel-dev/python-utils group also 
## python-utils/boilerplate string should be replaced

## create new repository:
git init
git add .
git commit -m'Initial commit (project created out of our boiler-plate)'

## register new remote:
git push --set-upstream git@code.falcon.lab:kestrel-dev/python-utils/boilersson.git master

## If use of HTTPS is requred:
# git push --set-upstream https://code.falcon.lab/kestrel-dev/python-utils/boilersson.git master

## To configure the remote, run
git remote add origin https://code.falcon.lab/kestrel-dev/python-utils/boilersson.git

```
I believe I have not missed too much. In that case, please supplement this readme.
