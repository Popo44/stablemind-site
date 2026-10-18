# Stable Mind

Site statique issu de Webflow, publié avec GitHub Pages sur [www.stablemind.fr](https://www.stablemind.fr/). Le domaine et ses DNS sont gérés chez OVHcloud.

## Fichiers du projet

- `site/` : tous les fichiers publiés, dont les pages HTML, `css/`, `js/`, `images/` et `fonts/`.
- `scripts/preview.cjs` et `preview.cmd` : aperçu local.
- `.github/workflows/deploy-pages.yml` : publication automatique de `site/` après un push sur `main`.

Les fichiers sont directement versionnés : aucune archive ZIP à reconstruire. Modifiez les fichiers dans `site/` pour que SourceGit affiche les changements.

## Tester avant un commit

1. Ouvrez le dossier de ce dépôt et double-cliquez sur **preview.cmd**.
2. Gardez la fenêtre du serveur ouverte, puis ouvrez **http://127.0.0.1:4190/**.
3. Modifiez les fichiers dans `site/`, puis rechargez avec **Ctrl+F5**.
4. Vérifiez les projets (dont les deux images Ensol), le défilement du carrousel, les avis, les offres, la FAQ, le menu et les pages légales.
5. Dans Chrome, utilisez **F12**, puis **Ctrl+Maj+M**, pour contrôler aussi les largeurs de 390 et 768 px.
6. Arrêtez le serveur avec **Ctrl+C** lorsque vous avez terminé.

Le lanceur utilise Node.js installé sur le PC, ou le runtime fourni avec Codex. Sur un autre ordinateur, installez Node.js si nécessaire. Sur macOS/Linux, lancez `node scripts/preview.cjs` depuis ce dépôt.

Si le port est déjà utilisé, fermez le précédent aperçu avant de relancer. Le serveur indique le dossier réellement affiché : il doit se terminer par `stablemind-site/site`.

## Enregistrer et publier avec SourceGit

Ouvrez ce dépôt dans SourceGit, puis consultez **Local Changes** pour examiner les fichiers modifiés. Les changements HTML/CSS/JS sont lisibles ligne par ligne ; les images restent des fichiers binaires.

- **Commit** : enregistre les modifications dans l’historique local. Le site public ne change pas.
- **Push** sur `main` : envoie les commits vers GitHub et déclenche la publication.

Après votre validation locale, sélectionnez les fichiers souhaités, créez le commit, puis cliquez sur Push si vous souhaitez publier. Vérifiez la réussite de **Publish Stable Mind** dans l’onglet Actions de GitHub avant de contrôler le site public avec Ctrl+F5.

Ne modifiez pas uniquement une ancienne copie située dans `outputs` : la version de référence est désormais `site/` dans ce dépôt. Une nouvelle exportation Webflow doit être comparée à ces fichiers pour conserver les corrections déjà apportées.

## Configuration GitHub Pages et OVH

La source Pages du dépôt reste **GitHub Actions**. Le workflow publie uniquement le dossier `site/`, sans inclure la documentation ni le serveur d’aperçu.

Le domaine personnalisé doit rester `www.stablemind.fr` dans Settings → Pages. Conservez aussi `site/CNAME` ; ce fichier ne configure pas à lui seul le domaine d’un déploiement par Actions.

- Racine `stablemind.fr` : quatre entrées A vers `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
- `www` : CNAME vers `popo44.github.io.`.
- Les entrées de messagerie restent indépendantes de ces réglages.

## Services externes

Les liens Google Forms, Tally et Zcal ainsi que les scripts externes de l’export sont conservés. Depuis l’aperçu, leurs liens ouvrent les vrais services. Il n’y a aucun formulaire Webflow natif sur les pages publiques.

Les anciens accueils, le guide de style et la page 401 sont exclus de la production. Vérifiez les majuscules/minuscules des chemins : GitHub Pages les distingue même si Windows les tolère.
