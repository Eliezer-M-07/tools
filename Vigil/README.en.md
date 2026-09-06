<div align="center">

<img width="401" height="187" alt="Vigil" src="https://github.com/user-attachments/assets/a2d5ce60-e37f-472b-bec2-85d601666eaa" />

Tool developed in Python for checking the availability of websites and network ports.

![Version](https://img.shields.io/badge/version-1.0.0-000000?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-000000?style=for-the-badge\&logo=python\&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP%2FHTTPS-000000?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-000000?style=for-the-badge)

</div>

🇺🇸 English | [🇧🇷 Português](README.md)

---

## Description

Vigil is a command-line tool designed to check the availability and connectivity of hosts and services.

The application allows individual checks for websites and TCP ports, as well as providing a full analysis option for a host.

The information provided includes HTTP status, IPv4 address, request latency, and the state of the analyzed ports.

---

## Features

### Website Check

The website check uses HTTP or HTTPS requests to determine whether the specified address is accessible.

The functionality performs:

* Website availability check.
* HTTP status code identification.
* Request latency measurement.
* Automatic addition of `https://` when no protocol is specified.
* Handling of request-related errors.

### Port Check

The port check uses TCP connections to determine whether a specific port is accessible on the specified host.

The verification result is classified according to the connection behavior:

| State      | Description                                      |
| ---------- | ------------------------------------------------ |
| `OPEN`     | The TCP connection was successfully established. |
| `CLOSED`   | The connection was refused by the host.          |
| `FILTERED` | The connection attempt exceeded the timeout.     |
| `ERROR`    | Another error occurred during the connection.    |

### Full Check

The `Full Check` option performs a complete analysis of the specified host.

The check provides:

* Analyzed host.
* Resolved IPv4 address.
* Website availability status.
* HTTP status code.
* Request latency.
* Status of ports `443`, `80`, and `8080`.

The following ports are checked:

* `443` — HTTPS
* `80` — HTTP
* `8080` — Alternative HTTP

---

## Requirements

To run the project, the following are required:

* Python 3
* pip
* Internet connection for HTTP/HTTPS checks

The only external dependency currently used is the `requests` library.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Eliezer-M-07/tools.git
```

Navigate to the project directory:

```bash
cd vigil
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the main file:

```bash
python main.py
```

After initialization, the program displays the following menu:

```text
[1] Check if the website is online.
[2] Check if the port is open.
[3] Full Check
[0] Exit
```

Each option directs the execution to the corresponding service.

---

## Project Structure

```text
vigil/
├── functions/
│   ├── clear_terminal.py
│   ├── colors.py
│   └── validate_url.py
│
├── services/
│   ├── full_check.py
│   ├── port_up.py
│   └── website_up.py
│
├── main.py
├── requirements.txt
├── README.md
└── README.en.md
```

### `functions/`

Contains helper functions used by the application.

| File                | Description                                             |
| ------------------- | ------------------------------------------------------- |
| `clear_terminal.py` | Responsible for clearing the terminal.                  |
| `colors.py`         | Defines resources related to terminal color formatting. |
| `validate_url.py`   | Validates and processes the URLs provided by the user.  |

### `services/`

Contains the modules responsible for the checks performed by Vigil.

| File            | Description                              |
| --------------- | ---------------------------------------- |
| `website_up.py` | Checks website availability.             |
| `port_up.py`    | Checks TCP port availability.            |
| `full_check.py` | Combines website, IPv4, and port checks. |

---

## Technologies

The project uses the following technologies and resources:

* Python 3
* Requests
* Socket
* urllib.parse

### Requests

Used to perform HTTP and HTTPS requests during website checks.

### Socket

Used to establish TCP connections and resolve host addresses.

### urllib.parse

Used to parse and manipulate URLs provided by the user.

---

## How It Works

The `main.py` file is responsible for displaying the main menu and directing execution to the available services.

### Website Check

The provided address is processed and validated before the request is performed.

When no protocol is specified, Vigil uses `https://` by default.

After the request, the connection status, HTTP status code, and time required to complete the operation are obtained.

### Port Check

Port checks use TCP connections through the `socket` module.

The result is determined based on the behavior of the connection attempt:

```text
Connection established  -> OPEN
Connection refused      -> CLOSED
Timeout exceeded        -> FILTERED
Other error             -> ERROR
```

### Full Check

The `Full Check` combines the available functionalities into a single operation.

The verification flow consists of:

```text
Specified host
    |
    +-- IPv4 Resolution
    |
    +-- Website Check
    |     |
    |     +-- Status
    |     +-- HTTP Code
    |     +-- Latency
    |
    +-- Port Check
          |
          +-- 443
          +-- 80
          +-- 8080
```

---

## Objective

The objective of Vigil is to provide a simple interface for performing basic availability and connectivity checks directly from the terminal.

The tool can be used for connectivity diagnostics, website availability checks, and TCP port analysis on authorized hosts.

---

## Limitations

Vigil performs basic availability and connectivity checks. The results represent the behavior of the host at the time of execution and may vary depending on factors such as firewall configuration, network conditions, service availability, and response time.

The `FILTERED` classification, for example, indicates that the connection was not completed within the configured timeout. It does not necessarily mean that the port is definitively blocked.

---

## Contributing

Contributions to the project are welcome.

To contribute:

1. Fork the repository.
2. Create a branch for your changes.
3. Implement and test your modifications.
4. Commit your changes.
5. Open a Pull Request describing the modifications.

---

## License

Refer to the project's license file for information regarding the terms of use and distribution.
