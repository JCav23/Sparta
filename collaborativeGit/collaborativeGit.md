# Collaborative Git

## Review of Git

* Create repo
	- Locally (git init) then Push to GitHub
	- Remotely using GitHub and clone to local environment
* Git Commands
	- (Add, Commit, Push, Pull, Checkout, Merge)

## Scenario

Team of 3 who want to work collectively on a python project, one is the Git Authority responsible for setting up the repository, added the team as collaborators and managing the controls of what is possible within the repo

### Setting up the Repo
The Git Auth must be the one to create the repository. Then invite the team members as collaborators to the GitHub Repo. Once everyone is set up on the remote remote you can clone the repo on to local systems. 
The Idea for Collaborative projects using Git is to use multiple branches in the project. 
You could ould use the Main branch to contain the working usable code to roll out to each of the team to work on their individual Developer branches where they can carry out their work and commit their changes before merging into the main branch at the end of the sprint.
However a more appropriate way of working is to use a Feature branch from the Dev branch to work on seperate features by each team member 

### Key Points
* Only Tested code ready for production is on main
* All dev work takes place on the dev branch
* Feature branches can run in parallel
	* Merged with dev branch ready for integration testing

### Setting Up Branch Protection Rules
* Pull requests can require approval before merging. You can set how many team members must aprove
* Set Branch Protection Rules for each branch
* You can specific a default branch for the team to be working on so everyone is working on Dev branch rather than main branch
