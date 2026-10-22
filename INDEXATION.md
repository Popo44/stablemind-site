# Indexation Google et contrôle mobile — 22 octobre 2026

## Ce que montre Search Console

Rapport de la propriété `sc-domain:stablemind.fr`, consulté dans Chrome. Ses données de couverture datent du 16 octobre 2026, avant les dernières publications. Il présente 5 anciennes 404, 2 redirections et 1 variante canonique.

| URL signalée | Réponse publique vérifiée le 22 octobre | Traitement |
| --- | --- | --- |
| `http://www.stablemind.fr/` | 301 vers `https://www.stablemind.fr/` | Déjà corrigée ; HTTP ne doit pas être indexé séparément |
| `/mentions-legales` | 200 | Alias accessible ; canonical vers `/mentions-legales.html` |
| `/politique-de-confidentialite` | 200 | Alias accessible ; canonical vers `/politique-de-confidentialite.html` |
| `/conditions-generales-de-vente` | 200 | Alias accessible ; canonical vers `/conditions-generales-de-vente.html` |
| `/old-home-2` | 404 avant la nouvelle publication | Ancien accueil : migration ciblée vers l’accueil actuel préparée |
| `https://stablemind.fr/` | 301 vers `https://www.stablemind.fr/` | Exclusion normale d’une redirection |
| `http://stablemind.fr/` | 301 vers `https://www.stablemind.fr/` | Exclusion normale d’une redirection |
| `/index.html` | 200 avec canonical vers `/` | Doublon correctement exclu ; conserver la canonical |

Les chemins sans domaine dans le tableau utilisent `https://www.stablemind.fr`.

## Actions réalisées dans Google

- Sitemap `https://www.stablemind.fr/sitemap.xml` renvoyé le 22 octobre 2026. Confirmation affichée : **Sitemap envoyé**. Sa dernière soumission datait du 6 août 2024 ; la dernière lecture affichée était le 6 janvier 2026. Quatre URL étaient découvertes.
- `/mentions-legales.html` : demande acceptée, confirmation **Indexation demandée**.
- `/politique-de-confidentialite.html` : demande acceptée, confirmation **Indexation demandée**.
- `/conditions-generales-de-vente.html` : déjà détectée mais pas encore explorée ; demande acceptée, confirmation **Indexation demandée**.

Ces confirmations indiquent une mise en file d’attente, pas une indexation immédiate. Google décidera de l’indexation après exploration. Les données anciennes du rapport ne disparaissent pas instantanément.

## Corrections des fichiers

- Dates des trois pages légales et de leurs alias : **22 octobre 2026**, balisées avec `<time datetime="2026-10-22">`. Leur JSON-LD `dateModified` correspond à cette date de révision. Le texte juridique n’a pas été réécrit.
- Copyright : **2024–2026** ; date de création de l’activité conservée en 2024.
- Raccords de sections : six SVG avec dimensions intrinsèques exactes et ratio CSS réservé. Cela évite une hauteur nulle avant la fin du chargement différé.
- Ancien accueil : `/old-home-2.html` et `/old-home-2/index.html` renvoient immédiatement vers `https://www.stablemind.fr/`. Ils restent hors du sitemap et non indexables. Seul cet ancien chemin connu est concerné ; les URL réellement inexistantes restent des 404.
- GitHub Pages n’exposant pas de configuration de redirection HTTP personnalisée pour ce site, ce renvoi utilise un `meta refresh` de 0 seconde, interprété par Google comme permanent. Ce n’est pas une réponse HTTP 301.
- Le contrôle de déploiement vérifie explicitement ces deux pages de migration et leur cible.

## Contrôle mobile

Les six transitions ont été parcourues et chargées dans le navigateur. Mesures en pixels CSS :

| Largeur du viewport | Largeur de contenu hors scrollbar | Vagues : bord gauche / bord droit | Hauteur de chaque vague |
| --- | --- | --- | --- |
| 320 | 305 | 0 / 305 | 14,67 |
| 390 | 375 | 0 / 375 | 18,05 |
| 600 | 585 | 0 / 585 | 28,16 |
| 767 | 752 | 0 / 752 | 36,20 |

Aucun débordement horizontal. Les dimensions sont aussi réservées quand les images ne sont pas encore chargées. Contrôle réalisé dans une simulation de viewport ; pas sur un téléphone physique.

La demi-rosace derrière la fusée est conservée : elle n’est pas une vague de section et n’a pas à être étirée sur toute la largeur. La fusée reste ancrée au pied de page.

Tests : `python scripts/check-seo.py` — 10 fichiers HTML, 4 canoniques et 444 références locales valides. Les chemins locaux `/old-home-2` et `/old-home-2.html` répondent 200 et portent le renvoi immédiat attendu.

## Publication et validation finale

Les dates, le ratio des SVG et le renvoi de l’ancien accueil doivent être publiés avant de lancer **Valider la correction** sur le groupe des 404. Ne pas demander l’indexation de l’ancien accueil ni des variantes HTTP/sans www ; les destinations canoniques sont les pages à faire indexer.

Après le déploiement, vérifier `/old-home-2` et lancer la validation du groupe des 404 dans Search Console. Les catégories « Page avec redirection » et « Autre page avec balise canonique correcte » peuvent légitimement rester présentes.

Références : [Rapport d’indexation Google](https://support.google.com/webmasters/answer/7440203?hl=fr), [404 et pages supprimées](https://support.google.com/webmasters/answer/2445990?hl=fr), [Redirections permanentes et meta refresh](https://developers.google.com/search/docs/crawling-indexing/301-redirects).
