#!/bin/bash

echo $@

POSITIONAL=()
while [[ $# -gt 0 ]]
do
key="$1"

echo $key

case $key in
    -p|--path)
    TF_PATH="$2"
    shift # past argument
    shift # past value
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters

if [[ -z $TF_PATH ]]
then
    echo "--path not set. Abort."
    exit 1
fi

cd $TF_PATH
terraform fmt -recursive || echo "Terraform not installed. Please ensure Terraform is installed before running this script."