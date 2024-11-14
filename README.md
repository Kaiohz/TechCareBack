# TechCare API

API de gestion des produits et fournisseurs pour TechCare.

## Fonctionnalités

### Gestion des Fournisseurs
- **Ajouter un fournisseur** (`POST /rest/v1/library/supplier/add`)
  - Permet d'ajouter un nouveau fournisseur avec :
    - Nom de l'entreprise
    - Numéro SIRET
    - Adresse
    - Contact

- **Lister les fournisseurs** (`GET /rest/v1/library/suppliers/get`)
  - Récupère la liste de tous les fournisseurs enregistrés

### Gestion des Familles de Produits
- **Ajouter une famille de produits** (`POST /rest/v1/library/familyproduct/add`)
  - Permet de créer une nouvelle catégorie de produits avec :
    - Nom de la famille
    - Spécifications générales

- **Lister les familles de produits** (`GET /rest/v1/library/familyproducts/get`)
  - Récupère toutes les familles de produits disponibles

### Gestion des Produits
- **Ajouter un produit** (`POST /rest/v1/library/product/add`)
  - Permet d'ajouter un nouveau produit avec :
    - Nom du produit
    - Code douanier
    - Statut kit (oui/non)
    - Référence
    - Numéro de série
    - Image
    - Description
    - Prix public
    - Prix d'achat
    - TVA
    - Date du prix
    - Unités
    - Commentaires
    - Spécifications
    - ID de la famille de produits
    - Liste des fournisseurs associés

- **Lister les produits** (`GET /rest/v1/library/products/get`)
  - Récupère tous les produits avec leurs informations complètes
  - Inclut la liste des fournisseurs pour chaque produit

## Sécurité
- Toutes les routes sont protégées par une clé API
- La clé API doit être fournie dans le header `api_key`

## Base de données
- Utilise SQLite comme base de données
- Gère les relations entre :
  - Produits et Fournisseurs (relation many-to-many)
  - Produits et Familles de produits (relation one-to-many)

## Installation et Configuration
1. Copier `.env.example` vers `.env` et compléter les valeurs
2. Installer les dépendances : `pipenv install`

## Démarrage
Lancer l'application : `pipenv run python -m techcareback.main`

## Tests
Exécuter les tests avec couverture :
```bash
pipenv run coverage run --source=techcareback -m pytest tests
pipenv run coverage report
```