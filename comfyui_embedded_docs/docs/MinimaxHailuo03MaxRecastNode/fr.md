# MiniMax H3 Max Recast

Recast remplace les personnes d’une vidéo par celles de photos de référence tout en conservant le mouvement, la caméra, les coupes et le son du clip source. La vidéo est téléversée, la tâche Hailuo 03 Max est interrogée, et la vidéo recast est renvoyée à la résolution choisie.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | "MiniMax H3 Max" |

### Entrées MiniMax H3 Max

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `video` | Vidéo source, d’une durée de 5 à 30 secondes ; chaque plan doit durer 15 secondes ou moins. Le rapport d’aspect doit être compris entre 0,4 et 2,5. | VIDEO | Oui | 5 à 30 secondes |
| `reference_images` | Emplacement extensible : connectez 1 à 4 photos (`image_1`...`image_4`), une par nouvelle personne, d’au moins 256x256 pixels. Par défaut, elles remplacent les personnes principales de la vidéo de gauche à droite. | IMAGE | Oui | 1 à 4 images |
| `prompt` | Facultatif. Qui devient qui, ou quoi d’autre conserver ou modifier. Faites référence aux photos avec `@Image1`..`@Image4`, par exemple « l’homme devient @Image2 ». | STRING | Oui | 0 à 2000 caractères |
| `resolution` | Résolution de la vidéo de sortie (par défaut : "768P"). | COMBO | Oui | "768P"<br>"1080P" |
| `enhance_realism` | Textures de peau plus naturelles et meilleure intégration des nouvelles personnes dans la scène (par défaut : false). | BOOLEAN | Non | true<br>false |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo recast avec les nouvelles personnes en place. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxRecastNode/fr.md)

---
**Source fingerprint (SHA-256):** `a9e6f9edf12653f9f361992a097d1d57e7ba14b3e7dd20008b0e022cabc14c1b`
