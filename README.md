<p align="center">
  <h3 align="center">Lotus Notes to MongoDB Migration</h3>

  <p align="center">
    This open source utility can migrate Lotus Notes Database(NSF) data to MongoDB
    <br />
    <a href="https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration">Scope</a>
    ·
    <a href="https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration/issues">Report Bug</a>
    ·
    <a href="https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration/issues">Request Feature</a>
  </p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

With the divestiture of IBM Notes to HCL, it’s a need of this moment to move existing IBM Notes applications to some other platform. There are several options to choose from, but MEAN (MongoDB-Express-Angular-NodeJs) stack is the most appropriate choice because of following reasons,
1.	MongoDB is the most popular NoSql database which offers several benefits like scalability, indexing, faster processing, Compass and Atlas etc.
2.	NodeJS is JavaScript runtime which runs on Chrome V8 engine which is fast and secure. 
3.	Angular is full featured JavaScript framework to design feature rich UI.
In every rewrite or redesign project, the most critical part is the existing Data. Data retention, processing and migration are the steps which are critical and required for every application. IBM Notes (Lotus Notes) being a legacy tool with very small community, there are no or very less options available (as per my knowledge and R&D) to migrate data to MongoDB. There are 3rd party tools available, but that is costly and there is a risk of exposing confidential data to some 3rd party which is not secure. 
We are redesigning our existing IBM Notes applications to MEAN stack and we faced these challenges during Data migrations. To overcome this, I have developed this solution that can easily migrate data from IBM Notes to MongoDB. This solution offers several benefits,
1.	It’s easy to implement and it can be used with any IBM Notes database.
2.	It’s based-on HTTP and REST, so its fast and secure.
3.	Its written in Python which has excellent set of libraries to work with Data (Data Cleaning, Data Processing etc).
4.	We are getting and processing data in JSON and its suitable for Python and MongoDB.
5.	Most importantly, once you are out of IBM Notes it will give you lot of options and opportunities to scale your application using modern tools. You can implement DevOps, TDD, AI and many others (Opportunities are endless).

### Built With

* [Python](https://www.python.org/downloads/)
* [Domino Access Service API](https://ds_infolib.hcltechsw.com/ldd/ddwiki.nsf/xpAPIViewer.xsp?lookupName=IBM+Domino+Access+Services+9.0.1#action=openDocument&content=catcontent&ct=api)
* [MongoDB](https://www.mongodb.com/try/download/community)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

You need to install following Python packages
* pip
```sh
pip install pymongo
pip install csv
pip install requests
pip install traceback
```
You need to configure Domino Access Service API on your Domino server and database. Here are the instruction to setup and enable that, <br />
[Instructions to setup and enable Domino Access Service API][documentation-file]
### Installation

1. Clone the repo
```sh
git clone https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration.git
```
2. Install Python packages
```sh
pip install
```



<!-- USAGE EXAMPLES -->
## Usage

please refer to the [Documentation][documentation-file]



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

This code pattern is licensed under the Apache Software License, Version 2.  Separate third party code objects invoked within this code pattern are licensed by their respective providers pursuant to their own separate licenses. Contributions are subject to the [Developer Certificate of Origin, Version 1.1 (DCO)](https://developercertificate.org/) and the [Apache Software License, Version 2](https://www.apache.org/licenses/LICENSE-2.0.txt).

[Apache Software License (ASL) FAQ](https://www.apache.org/foundation/license-faq.html#WhatDoesItMEAN)



<!-- CONTACT -->
## Contact

Kirti Jha - kirtijha@in.ibm.com

Project Link: [https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration](https://github.com/IBM/Lotus-Notes-to-MongoDB-Migration)







<!-- MARKDOWN LINKS & IMAGES -->
[documentation-file]: documentation/IBM%20Notes%20to%20MongoDB%20Migration.docx