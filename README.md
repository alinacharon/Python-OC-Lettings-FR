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

## Déploiement

### Vue d'ensemble

Le déploiement de l'application OC-Lettings est géré via la plateforme Render. La pipeline CI/CD est configurée pour automatiser le processus de build et de déploiement chaque fois que des modifications sont poussées vers le repository ou qu'un déclencheur manuel est initié.

### Prérequis

Pour garantir un déploiement réussi, les configurations suivantes sont requises :

- Un compte Render avec accès à créer et gérer des services web.
- Docker doit être installé et configuré sur votre machine locale pour construire des images.
- Les variables d'environnement telles que `SENTRY_DSN` et `SECRET_KEY_DJANGO` doivent être définies dans le tableau de bord Render.

### Étapes de déploiement

1. **Se connecter à Render** : Assurez-vous que votre compte GitHub est lié à votre compte Render.
2. **Créer un nouveau service web** : Si ce n'est déjà fait, configurez un nouveau service web dans le tableau de bord Render.
3. **Configurer les paramètres de déploiement** :
   - Définir la commande de build sur `docker build -t alinacharon/lettings .`
   - Définir la commande de démarrage sur `docker run alinacharon/lettings`.
4. **Définir les variables d'environnement** : Dans le tableau de bord Render, naviguez vers la section "Environment" et ajoutez les variables d'environnement nécessaires :
   - `SENTRY_DSN`
   - `SECRET_KEY_DJANGO`
5. **Déclencher le déploiement** :
   - Si vous poussez des modifications vers le repository GitHub, Render reconstruira automatiquement et redéploiera l'application.
   - Alternativement, vous pouvez déclencher un déploiement manuel via le tableau de bord Render en sélectionnant votre service et en cliquant sur "Deploy".

Le site est actuellement accessible à l'adresse : [https://python-oc-lettings-fr-o8k3.onrender.com](https://python-oc-lettings-fr-o8k3.onrender.com).
