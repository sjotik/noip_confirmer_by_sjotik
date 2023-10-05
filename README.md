![License](https://img.shields.io/github/license/sjotik/noip_confirmer_by_sjotik.svg?style=for-the-badge) ![Repo Size](https://img.shields.io/github/languages/code-size/sjotik/noip_confirmer_by_sjotik.svg?style=for-the-badge) ![TOP_LANGUAGE](https://img.shields.io/github/languages/top/sjotik/noip_confirmer_by_sjotik.svg?style=for-the-badge)
    
# NoIP confirmer by [sjotik](https://github.com/sjotik)

## Table of Contents

- [Description](#description)
- [Screenshots](#screenshots)
- [Built With](#built-with)
- [Getting Started](#getting-started)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

NoIP free hosts auto confirmer script. No matter how much free hosts you have - it will confirm every hosts, available for confirm.

## Screenshots

<img src="https://thumb.cloud.mail.ru/weblink/thumb/xw1/gLPj/1TK9UFxEm">

## Built With
<a href="https://www.python.org/"><img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" height="40px" width="40px" /></a>
<a href="https://www.docker.com"><img src="https://www.svgrepo.com/show/373553/docker.svg" height="50px" width="50px"/>

## Getting Started

Python3.10 used for this script and Selenium 4.11.2.



### Installation

Clone repo:

`git@github.com:sjotik/noip_confirmer_by_sjotik.git`

Install reuirements:

`pip install -r requirements.txt`


## Usage

For using script set noip account username to 1st argument position and noip account password to 2nd:

`python3 noip.py username password`

You can scheduling this command for periodic start.

Script filling LOG file in the same directory when file script located. In file writing statuses of job.
After successful job script make screenshot page of hosts list.

Also there is the Dockerfile. You can build docker image and scheduling run docker container for automate job on background.
!!!! For build the Image edit lines with **"ENV UNAME"** and **"ENV PW"**. Set your NoIP account username and password or docker build process will be exited.

Example command for build:

`docker build -t image_name .`

Example command for run container:

`docker run --name container_name image_name`


#### PS: the script start can be long because of the features of the chromedriver




#### P.S. I have docker container (beta, but working) with this script for ARM (i'm using on RPI),
#### if need it, create фт issue and I’ll finish the project.
<img src="https://brandslogos.com/wp-content/uploads/images/arm-logo-vector-1.svg" alt="Logo" width="80" height="80">


## License

<a href="https://choosealicense.com/licenses/mit/"><img src="https://raw.githubusercontent.com/johnturner4004/readme-generator/master/src/components/assets/images/mit.svg" height=40 />MIT License</a>

<!--
## Contacts

<a href="https://www.linkedin.com/in/"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" /></a>  <a href="mailto:"><img src=https://raw.githubusercontent.com/johnturner4004/readme-generator/master/src/components/assets/images/email_me_button_icon_151852.svg /></a>
-->
