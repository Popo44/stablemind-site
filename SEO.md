# Référencement Stable Mind — 18 octobre 2026

## Cible et intentions

Entrepreneurs et PME à Nantes, avec des prestations accessibles à distance en France. L’établissement indiqué dans les mentions légales est à Sainte-Luce-sur-Loire ; aucune adresse à Nantes n’a été inventée.

| Intention | Contenu actuel |
| --- | --- |
| Création de site web à Nantes | Titre SEO, H1, introduction et section Services |
| Refonte de site web à Nantes | Accueil, offres et exemples de réalisations |
| Identité visuelle à Nantes | Introduction, section Services et portfolio |
| Stable Mind / Pauline Genestier | Présentation, coordonnées et données structurées |

## Corrections réalisées localement

- Titre d’accueil : « Création et refonte de sites web à Nantes | Stable Mind » (55 caractères). Description : 158 caractères, ciblée entrepreneurs et PME.
- Titre principal et introduction explicites ; titres des réalisations, des services et de la FAQ plus descriptifs. Les références au parcours et à la spécialisation humaine de Pauline sont conservées.
- Un seul H1 et un seul repère `main` par document. Le contenu principal de l’accueil comprend désormais toutes les sections, et non uniquement le portfolio.
- Métadonnées uniques pour l’accueil, les trois pages légales et la page 404. Les alias des pages légales désignent leur URL préférée en `.html`.
- Canoniques, liens internes et sitemap concordants. Les anciennes variantes d’URL restent accessibles pour préserver les liens entrants ; une canonical est un signal, pas une redirection HTTP.
- Page 404 en français, avec H1 et `noindex, follow`, exclue du sitemap. Les URL inexistantes renvoient déjà un vrai statut 404 sur le site public.
- Balise `google-site-verification` corrigée : son contenu est uniquement le jeton existant. Cela ne confirme pas à lui seul la propriété Search Console.
- Graphe JSON-LD : entreprise de services, site et page ; fil d’Ariane sur les pages légales. Coordonnées reprises du site, profils LinkedIn et Behance existants, zone desservie Nantes/France. Horaires génériques retirés faute de confirmation.
- Aucun avis chiffré, récompense ou résultat enrichi fictif ajouté. Le balisage FAQ n’a pas été ajouté pour promettre un affichage enrichi : Google le réserve aux sites gouvernementaux et de santé faisant autorité.
- Open Graph et cartes sociales complets, avec image locale de 1 200 × 630 px, URL, langue et textes alternatifs.
- Textes alternatifs incorrects corrigés pour Vincent Garçon, Muriel Attar et Guillaume Escarieux. Libellés accessibles ajoutés aux liens sociaux.
- Chargement immédiat des visuels du premier écran ; chargement différé et décodage asynchrone des images du portfolio. Les scripts externes de mesure présents dans l’export sont différés sans modifier leurs identifiants.
- Quatorze images de projets déclinées en WebP jusqu’à 480, 800 et 1 200 px selon la taille d’origine. Les `srcset` déclarent leurs vraies largeurs, avec `sizes` correspondant aux cartes existantes : 40 vw sur mobile, 27 vw sur ordinateur. Le ratio d’affichage 4:3 et les deux rangées animées sont conservés.
- Pour ces 14 images uniques, somme des fichiers sources : 1 272 104 octets. Somme des variantes 480 px : 368 426 octets, soit environ 71 % de moins. Somme des variantes les plus grandes : 1 067 486 octets, soit environ 16 % de moins. Ce sont des comparaisons de fichiers, pas une mesure du trafic réseau réel : le navigateur choisit les variantes selon l’écran et sa densité.
- Contrôle `scripts/check-seo.py` ajouté avant publication dans GitHub Actions : métadonnées, H1, repères, JSON-LD, canoniques, sitemap, ressources et ancres internes, avec contrôle de casse.

## Correction visuelle prioritaire

La demi-rosace festonnée d’origine est rétablie derrière la fusée, centrée et sans déformation, sur ordinateur comme sur mobile. La fusée est positionnée au bas de la section ; son animation de déplacement a été retirée pour que son ancrage reste stable. L’espace du bouton est préservé. La vague n’hérite plus des coins arrondis appliqués aux images ordinaires.

## Vérifications

Commande : `python scripts/check-seo.py` depuis le dépôt.

- 8 fichiers HTML, dont les alias existants, contrôlés ; 4 URL canoniques indexables.
- 412 références locales contrôlées : fichiers, ancres et ressources CSS.
- JSON-LD analysable, sitemap XML valide et cohérent, 404 non indexable.
- Vérifications navigateur du rendu et des cartes sur mobile et ordinateur. Fusée : écart de 0 px avec le bas de sa section aux largeurs 320, 390, 600, 767, 1 024 et 1 440 px ; proportions naturelles de la demi-rosace et pas de débordement horizontal.
- Le site public actuel redirige la racine du domaine vers `www` et répond en HTTPS ; les variantes historiques des pages légales répondent 200. Les nouveaux fichiers restent locaux tant qu’ils ne sont pas publiés.

## Suite après publication

1. **Search Console** : ouvrir la propriété existante de `https://www.stablemind.fr/`, vérifier son accès, envoyer `sitemap.xml`, inspecter l’accueil et demander son indexation. Contrôler ensuite les URL choisies comme canoniques par Google et les éventuelles erreurs de couverture. Aucun accès Search Console ni historique d’impressions n’a été consulté dans cette intervention.
2. **Google Business Profile** : vérifier la fiche reliée depuis le site, l’activité réelle, la zone desservie, les services, l’URL et la cohérence du nom et des coordonnées. Ne publier que l’adresse que l’entreprise souhaite rendre publique. La fiche n’a pas été modifiée.
3. **Mesure** : contrôler les conteneurs de mesure existants dans leurs comptes, éviter les événements en double et suivre les clics vers la prise de rendez-vous et la demande de devis. Aucune configuration de compte ni collecte supplémentaire n’a été activée.
4. **Performances après déploiement** : lancer PageSpeed Insights mobile et bureau puis consulter les Core Web Vitals lorsqu’il existe assez de données réelles. Aucun score Lighthouse ou gain de classement n’est annoncé ici ; les contrôles locaux ne remplacent pas une mesure en conditions réelles.
5. **Contenus** : développer ensuite des pages distinctes de création/refonte et d’identité visuelle si elles apportent réellement des informations propres : approche, livrables, délais, exemples, questions et accès aux offres. Prioriser aussi une étude de cas Ensol avec contexte, démarche et résultats vérifiables. Les projets restent actuellement détaillés sur Behance. Éviter des pages dupliquées par ville.
6. **Notoriété** : obtenir des liens pertinents depuis les réalisations clientes, partenaires et réseaux professionnels locaux, puis suivre les requêtes et demandes commerciales sur plusieurs semaines.

Les chiffres commerciaux déjà présents dans le site (par exemple +35 % de rendez-vous) ont été conservés ; leurs justificatifs et leur actualité restent à vérifier côté entreprise. Cette intervention ne constitue pas une étude de volumes de recherche ou un audit de backlinks, faute de données de comptes et d’outils dédiés.

## Références

- [Google : consolider les URL en double](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls)
- [Google : règles générales des données structurées](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
- [Google : conditions des résultats FAQ](https://developers.google.com/search/blog/2023/08/howto-faq-changes)
- [web.dev : chargement différé des images](https://web.dev/articles/browser-level-image-lazy-loading)

## Tester avant commit

Double-cliquer sur `preview.cmd` dans le dépôt, puis ouvrir `http://127.0.0.1:4190/`. Recharger avec Ctrl+F5. Vérifier en particulier les nouveaux textes, le carrousel, les offres et le raccord de la fusée. Les fichiers ne sont ni committés ni poussés par cette intervention.
