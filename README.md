# Dockerized_API
Advanced REST API with Python, Django REST Framework and Docker using Test Driven Development (TDD)

## GIthub Actions

- WIll use github actions in order to run some automated tasks whenever we push changes to our project.
- A tool similar to Travis-CI, GitLab CI/CD, Jenkins...
- Allows you ro run jobs whenever your code changes..

### Common uses :
- Deployment
- Code linting
- Unit tests

### How it works
- Start by setting up a trigger (you set up which event you want)
- When the trigger occurs, you you run the jobs you have defined (For example, running unit tests).

### Configuring
- Create a config file at ```.github/workflows/checks.yml```
  - Set trigerr
  - Add steps for running testing and linting
  
## Docker hub

- Where you pull docker base images from to your local machine..
