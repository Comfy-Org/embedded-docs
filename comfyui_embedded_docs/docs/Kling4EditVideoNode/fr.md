# Kling 4.0 — modifier une vidéo

Modifie une vidéo existante à l’aide d’un prompt textuel en utilisant le modèle Kling 4.0, éventuellement guidé par des vidéos de référence et des images de référence. Le résultat conserve la durée de la vidéo d’entrée. Utilisez-le pour modifier ce qui se passe dans un clip, en changer le style ou remplacer des éléments tout en conservant le minutage d’origine.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. `"kling-4.0"` prend en charge les modifications jusqu’à la 4K HDR et 30 secondes ; `"kling-4.0-flash"` est limité à la 720p et 20 secondes. La sélection d’un modèle révèle ses entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video_1` | La vidéo à modifier, d’une durée de 3 à 30 secondes. La sortie conserve sa durée. | VIDEO | Oui | 3 à 30 secondes |
| `reference_videos` | Emplacements extensibles pour vidéos de référence, jusqu’à 4. Faites-y référence dans le prompt sous la forme `@Video2`, etc. Chaque vidéo, ainsi que toutes les vidéos ensemble, doit durer de 3 à 30 secondes. | AUTOGROW | Non | 0 à 4 vidéos |
| `reference_images` | Emplacements extensibles pour images de référence, jusqu’à 10. Faites-y référence dans le prompt sous la forme `@Image1`, `@Image2`, etc. | AUTOGROW | Non | 0 à 10 images |
| `prompt` | Description de ce qui doit être modifié et de ce qui doit être conservé. Faites référence à la vidéo en cours de modification sous la forme `@Video1`, aux vidéos de référence sous la forme `@Video2`, etc., et aux images sous la forme `@Image1`, etc. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie ; une option dont le nom contient `HDR` renvoie une vidéo HDR. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Rapport d’aspect de la vidéo de sortie. `"adaptive"` conserve le rapport d’aspect de la vidéo d’entrée. Par défaut : `"adaptive"`. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats restent non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `audio` | `"native"` génère un nouvel audio pour la vidéo modifiée, `"original"` conserve l’audio de la vidéo d’entrée. Par défaut : `"native"`. | COMBO | Non | `"native"`<br>`"original"` |

### Entrées kling-4.0-flash

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0-flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video_1` | La vidéo à modifier, d’une durée de 3 à 20 secondes. La sortie conserve sa durée. | VIDEO | Oui | 3 à 20 secondes |
| `reference_videos` | Emplacements extensibles pour vidéos de référence, jusqu’à 4. Faites-y référence dans le prompt sous la forme `@Video2`, etc. Chaque vidéo, ainsi que toutes les vidéos ensemble, doit durer de 3 à 20 secondes. | AUTOGROW | Non | 0 à 4 vidéos |
| `reference_images` | Emplacements extensibles pour images de référence, jusqu’à 10. Faites-y référence dans le prompt sous la forme `@Image1`, `@Image2`, etc. | AUTOGROW | Non | 0 à 10 images |
| `prompt` | Description de ce qui doit être modifié et de ce qui doit être conservé. Faites référence à la vidéo en cours de modification sous la forme `@Video1`, aux vidéos de référence sous la forme `@Video2`, etc., et aux images sous la forme `@Image1`, etc. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Flash ne rend qu’en 720p. Par défaut : `"720p"`. | COMBO | Oui | `"720p"` |
| `aspect_ratio` | Rapport d’aspect de la vidéo de sortie. `"adaptive"` conserve le rapport d’aspect de la vidéo d’entrée. Par défaut : `"adaptive"`. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats restent non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |
| `audio` | `"native"` génère un nouvel audio pour la vidéo modifiée, `"original"` conserve l’audio de la vidéo d’entrée. Par défaut : `"native"`. | COMBO | Non | `"native"`<br>`"original"` |

**Contraintes et comportement :**

* La vidéo d’entrée et chaque vidéo de référence doivent durer de 3 à 30 secondes (3 à 20 avec `kling-4.0-flash`), mesurer au moins 700x700 et au plus 4553x4553 pixels, ne pas dépasser 8 294 400 pixels au total, avoir un rapport d’aspect compris entre 2:5 et 5:2 et une fréquence d’images d’au moins 24 fps. L’ensemble des vidéos ne doit pas dépasser la même limite.
* Chaque image de référence doit mesurer au moins 300x300 pixels, avec un rapport d’aspect compris entre 2:5 et 5:2, et au maximum 10 images peuvent être connectées.
* Un prompt qui mentionne `@VideoN` ou `@ImageN` provoque une erreur lorsque moins de N entrées de ce type sont connectées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo modifiée, téléchargée depuis le fournisseur une fois la tâche terminée. Elle a la même durée que la vidéo d’entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `7b7f48c3292a0c380f5fceecca2291dc74d99d5d73e4049bd67d33822cd0696e`
