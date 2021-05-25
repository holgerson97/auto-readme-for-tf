# Auto README for Terraform

Tool to help you create templated READMEs that contain the actual information from your Terraform Module. Iterates through your module folder and pick up all information needed to make your README look good and provide helpful content.

Take a look at the examples folder to see some READMEs generated by this tool.
&nbsp;

## Requirements
| Software | Version   |
| :------- | :-------- |
| Python   | >= 3.7    |
| Pip3	   | >= 20.0.2 |
| Terraform| >= 0.14.0 |
&nbsp;

**NOTE:** Older versions may work too, but aren't tested.

## Examples
&nbsp;

Creates a README with all features for the Terraform module at given path.
```
python3 main.py --path "terraform-example-module/"
```
&nbsp;

Creates a README excluding contributions for the Terraform module at given path and specifys title name.
```
python3 main.py --path "terraform-exaple-module" --name "Example Module" --contributing False
```
&nbsp;

## Contributing
Feel free to create pull requests.