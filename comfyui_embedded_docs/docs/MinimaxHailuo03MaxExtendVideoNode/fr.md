# MiniMax H3 Max Extend Video

Ce nœud poursuit une vidéo avec de nouvelles séquences guidées par un prompt et des références audio optionnelles. La vidéo source est téléversée, la suite est générée, et le résultat est renvoyé soit sous la forme de la vidéo entière re-rendue, soit uniquement sous la forme des nouvelles séquences. Deux modèles sont disponibles : « MiniMax H3 Max » et « MiniMax H3 Max Turbo », ce dernier étant moins cher par unité.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour poursuivre la vidéo. Les deux modèles exposent les mêmes entrées ci-dessous. | DYNAMIC_COMBO | Oui | "MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |

### Entrées du modèle

Ces entrées s'appliquent aux deux modèles.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo à étendre, d'une durée de 1,625 à 60 secondes, jusqu'à 50 Mo. Le rapport d'aspect doit être compris entre 0,4 et 2,5. | VIDEO | Oui | 1.625 à 60 secondes |
| `prompt` | Ce qui se passe ensuite. Décrivez la suite, pas la source. Référez-vous aux audios de référence sous la forme `@Audio1`..`@Audio3`, par exemple « @Audio1 pour la voix ». | STRING | Oui | 1 à 50000 caractères |
| `reference_audios` | Emplacement extensible : connectez jusqu'à 3 clips audio (`audio_1`...`audio_3`) pour les nouvelles séquences, d'au moins 2 secondes chacun et 14,5 secondes au total. | AUDIO | Non | 0 à 3 clips |
| `duration` | Secondes de nouvelles séquences à ajouter (par défaut : 5). | INT | Oui | 1 à 15 |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "768P"). | COMBO | Oui | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `aspect_ratio` | Rapport d'aspect de la sortie. "auto" suit la vidéo source ; les autres valeurs recadrent la vidéo au rapport sélectionné (par défaut : "auto"). | COMBO | Oui | "auto"<br>"21:9"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16" |
| `output` | "extended" renvoie la vidéo entière, re-rendue à la résolution sélectionnée, avec les nouvelles séquences. "continuation" renvoie uniquement les nouvelles séquences, en commençant par une répétition de 1,6 seconde de la fin de la source (par défaut : "extended"). | COMBO | Oui | "extended"<br>"continuation" |
| `prompt_expansion` | Réécrit le prompt à l'aide de la vidéo source pour maintenir la cohérence de la suite. Désactivez-le pour obtenir des résultats reproductibles pour la même valeur de `seed` (par défaut : true). | BOOLEAN | Non | true<br>false |
| `seed` | Graine aléatoire. Une même requête avec la même seed produit des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |

### Contraintes des paramètres

- En résolution 2K, la sortie "extended" est limitée à 45 secondes au total, vidéo source plus nouvelles séquences. Utilisez "continuation" ou une résolution inférieure pour des clips plus longs.
- Chaque clip audio de référence doit durer au moins 2 secondes, et leur ensemble ne peut pas dépasser 14,5 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo étendue ou uniquement les nouvelles séquences, selon le réglage `output`. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxExtendVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `db41a14db392fa450689c8d0d73d38b4ce9ea59ee30cfe4d6d2b0501cf0fc9a8`
