## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


# DEPLOYMENT

Here we will see how you can deploy your app on DockerHub and Heroku via GitHub and CircleCI
we will also add Sentry, an 'error viewing' tool.

Step by step:
### Github 

- before anything you need to set up the repository in your github account
- create a github account or login
- git clone the current repo into your computer locally (via zip or http)
- open the project in vscode and login into github with vscode (or through the terminal)
- initialize the repository : git init .
- add repository : git add .
- commit repository: git commit -m "first commit"
- push repository: git push
- head to github.com/your_github/your_project_name(maxcicd)
- you now have the repository linked to your github account
### Circle CI:

- head to the circle ci website and connect via your github account
- then go to projects and press 'set up project' on the right project (maxcicd by default)
- select the branch master of the project to fetch the .circleci/config.yml

### Docker Hub

We will use DockerHub to register our image (application)
- to link the project to docker hub you will need to add environment_variables
- go to your project settings in CircleCI -> "Environment Variables"
- here you will need to add your:
    - DOCKER_HUB_PASSWORD
    - DOCKER_HUB_USER_ID
- Now everytime you push a commit you will also push a docker image of your application on docker hub
- a docker image is a copy of our application's code and requirements which is defined in the dockerfile
- This will allow you to further pull that Docker image from the docker hub registry 
- And publish our application (docker image) inside a docker container on any Server or Virtual Machine
- a docker container only runs your application on a machine's operating system.
  It defers from a virtual machine as it is much lighter.
  Only the strict minimum to run your application is installed.
  While a virtual machine will simulate a whole machine's hardware. 
- to test the docker image locally:
    pre-existing docker image:
      - docker login
      - docker pull {image_name}
      - docker run {image_name}
    new docker image:
      - cd project_directory
      - docker login
      - docker build --tag {app_name} .
      - docker run {app_name}


### Heroku

- first create an account on heroku
- then you will need to generate a [Heroku API Key](https://dashboard.heroku.com/account)
- next create an app ( for example: orange-lettings-maxcicd )
- to deploy on Heroku you will need to add new environment_variables in CircleCI:
    - HEROKU_API_KEY
    - HEROKU_APP_NAME



You are all set !

Now Whenever you commit and push your code on the master/main branch
You will launch Github -> CircleCI -> pip install -> pytest -> flake8 
                                   -> Build and push Docker Image to Docker Hub Registry 
                                   -> Copy docker image from Docker Hub to Heroku registry
                                   -> Deploy image/application to Heroku

You can also re-run a pipeline workflow in CircleCI.
