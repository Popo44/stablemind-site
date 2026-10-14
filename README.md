# Stable Mind

Site statique issu de Webflow, publié avec GitHub Pages pour [www.stablemind.fr](https://www.stablemind.fr/). Le domaine et sa zone DNS sont gérés chez OVHcloud.

## Publication

Le fichier `stablemind-github-pages.zip` contient les pages HTML, les styles, les scripts, les images et les polices. Le workflow `.github/workflows/deploy-pages.yml` décompresse cette archive puis publie son contenu. La source Pages du dépôt est configurée sur **GitHub Actions**.

## Mettre le site à jour

1. Décompresser le ZIP et modifier les fichiers souhaités, ou préparer un nouvel export Webflow.
2. Vérifier les liens et ressources. Conserver `index.html`, `404.html`, les pages légales, les dossiers de ressources et la configuration de référencement.
3. Recréer le ZIP avec les fichiers du site directement à la racine, sans dossier parent supplémentaire.
4. Remplacer `stablemind-github-pages.zip` sur la branche `main`.
5. Vérifier la réussite de **Publish Stable Mind** dans Actions.

Le domaine personnalisé doit rester `www.stablemind.fr` dans Settings → Pages. Le fichier CNAME contenu dans le ZIP ne configure pas le domaine pour un déploiement par GitHub Actions.

## DNS web

- Racine `stablemind.fr` : quatre entrées A vers `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
- `www` : CNAME vers `popo44.github.io.`.
- Les entrées de messagerie sont indépendantes de ces réglages.

## Services externes

Les liens Google Forms, Tally et Zcal ainsi que les scripts externes présents dans l’export sont conservés. Il n’y a aucun formulaire Webflow natif sur les pages publiques.

Les anciens accueils, le guide de style et la page 401 sont exclus de cette version de production.
