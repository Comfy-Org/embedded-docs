# MiniMax H3 Max Insert Video

Ce nœud remplace la partie d’une vidéo entre les instants de début et de reprise par une scène nouvellement générée, guidée par un prompt et des images et vidéos de référence facultatives. La vidéo source est coupée à `start_time` et reprend à `resume_time` ; l’intervalle supprimé est régénéré et réinséré. Utilisez-le pour corriger un plan, remplacer une action ou faire le lien entre deux parties d’un clip.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | "MiniMax H3 Max" |

### Entrées MiniMax H3 Max

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo source, jusqu’à 60 secondes. Le rapport d’aspect doit être compris entre 0.4 et 2.5. | VIDEO | Oui | 0 à 60 secondes |
| `reference_images` | Emplacement extensible : connectez jusqu’à 9 images de référence facultatives (`image_1`...`image_9`) pour la nouvelle scène, d’au moins 256x256 pixels. Elles sont référencées dans le prompt sous la forme `@Image1`..`@Image9` dans l’ordre de connexion. | IMAGE | Non | 0 à 9 images |
| `reference_videos` | Emplacement extensible : connectez jusqu’à 3 vidéos de référence facultatives (`video_1`...`video_3`) pour la nouvelle scène, de 2 à 15 secondes chacune et 15 secondes au total. Elles sont référencées dans le prompt sous la forme `@Video1`..`@Video3` dans l’ordre de connexion. | VIDEO | Non | 0 à 3 vidéos |
| `prompt` | La nouvelle scène. Un prompt ou au moins une référence est requis ; les références sans prompt sont souvent ignorées. | STRING | Oui | 0 à 50000 caractères |
| `start_time` | Seconde où la vidéo source s’arrête et où la nouvelle scène commence (par défaut : 2.0). | FLOAT | Oui | 1.625 à 60.0 |
| `resume_time` | Seconde où la vidéo source reprend après la nouvelle scène (par défaut : 3.0). Doit être postérieure à `start_time` et au moins 1.375 seconde avant la fin de la vidéo. La partie de la source entre `start_time` et `resume_time` est supprimée. | FLOAT | Oui | 1.625 à 60.0 |
| `duration` | Durée de la nouvelle scène en secondes (par défaut : 5). | INT | Oui | 5 à 13 |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "768P"). | COMBO | Oui | "480P"<br>"768P" |
| `color_match` | Faire correspondre les couleurs de la nouvelle scène à celles de la vidéo source (par défaut : true). | BOOLEAN | Non | true<br>false |
| `prompt_expansion` | Réécrire le prompt à l’aide de la vidéo source. Désactivez cette option pour obtenir des résultats reproductibles pour la même graine (par défaut : true). | BOOLEAN | Non | true<br>false |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 2147483647 |

### Contraintes des paramètres

- `resume_time` doit être postérieur à `start_time` et au moins 1.375 seconde avant la fin de la vidéo ; sinon, la requête est rejetée.
- Chaque vidéo de référence doit durer entre 2 et 15 secondes, et leur durée totale ne peut pas dépasser 15 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo source avec la nouvelle scène insérée entre les instants de début et de reprise. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxInsertVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `623ad0b37f51ce4640c0058676e008697e31563c2a77a3da79ba7936af2d3f99`
