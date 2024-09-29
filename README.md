# README

This README file provides instructions on how to launch the app and run tests.

## Launching the App

To launch the app, follow these steps:

1. Clone the project and submodules `git clone https://github.com/Marketoi/lpe_3cl.git`
2. Init Submodule `git submodule init`
3. Update the project `git pull --recurse-submodules`
4. copy .env.example to .env and change to your open3cl path if needed
5. Go to your/open3cl/path/engine.js, replace line 45 by `const package_version = '0.1.0';`
6. Install the required dependencies by running `npm install`.
7. Start the app by running `npm run start`.
8. Open your web browser and visit `http://localhost:3000/api` to access the swagger.

## Launching the App Docker
1. Follow step 1 to step 5
2. `docker build -t le-dpe-api .`
3. `docker run -d -p 3000:3000 --name le-dpe-api le-dpe-api`

## Running Tests

To run tests for the app, follow these steps:

1. Run the command `npm run test` to execute the unit tests.
2. Run the command `npm run test:e2e` to execute the end to end tests.2