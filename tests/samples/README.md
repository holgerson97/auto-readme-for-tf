# default_name

&nbsp;

# Table of Contents

- [Requiremets](#requirements)
- [Getting Started](#getting-started)
    - [Basic usage](#basic-usage)
    - [Custom usage](#custom-usage)
- [Variables](#variables)
- [Outputs](#outputs)&nbsp;
- [Contributing](#contributing)

&nbsp;
# Requirements
| Software     |  Version  | Source |
| :--------    | :-------- | :----- |
| random | 3.1.0 | hashicorp/random |
| template | 2.2.0 | hashicorp/template |

&nbsp;
# Resources
| Resource |
| :------- |
| `random_resource1` |
| `random_resource2` |
| `random_resource3` |

&nbsp;
# Variables
| Variable | Type | Default | Description | Sensitive |
| :------- | :--: | :------ | :---------- | :-------- |
| `in_main_file` | string | Value | Just antoher number. |  |
| `empty` |  |  |  |  |
| `oneline1` |  |  | Description |  |
| `multiline1` |  |  | Just antoher number. |  |
| `multiline2` |  | Value | Just antoher number. |  |
| `multiline3` | string | Value | Just antoher number. |  |
| `multiline4` | string | Value | Just antoher number. | true |
| `object` | object({    key   = string    value = number  }) | {    key   = "integer"    value = 1  } | Just an object. | true |

&nbsp;
# Outputs
| Output | Description |
| :----- | :---------- |
| `oneline1` |  |
| `multiline1` |  |
| `multiline2` | Description |
| `multiline3` | Description |
| `multiline4` | Description |&nbsp;
## Contributing
Feel free to create pull requests.