# Kling 4.0 — référence vers vidéo

Génère une vidéo à partir d’images de référence et de vidéos de référence avec le modèle Kling 4.0, y compris l’audio. Les références déterminent le sujet, le style et le mouvement, et une première et une dernière image facultatives fixent le début et la fin du clip. Utilisez-le pour conserver la cohérence d’un personnage ou d’une scène tout au long d’un plan tout en décrivant l’action dans le prompt.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Sélecteur de modèle. `"kling-4.0"` prend en charge jusqu’à la 4K HDR, des clips de 30 secondes et une dernière image ; `"kling-4.0-flash"` est limité à 720p et 20 secondes et n’a pas d’entrée `last_frame`. La sélection d’un modèle révèle ses entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `reference_images` | Emplacements extensibles pour les images de référence, jusqu’à 10. Référencez-les dans le prompt sous la forme `@Image1`, `@Image2`, etc., dans l’ordre de connexion. | AUTOGROW | Non | 0 à 10 images |
| `reference_videos` | Emplacements extensibles pour les vidéos de référence, jusqu’à 5. Référencez-les dans le prompt sous la forme `@Video1`, `@Video2`, etc. Chaque vidéo, ainsi que l’ensemble des vidéos, doit durer de 3 à 30 secondes. | AUTOGROW | Non | 0 à 5 vidéos |
| `first_frame` | Image facultative sur laquelle la vidéo commence. Compte dans la limite de 10 images avec les images de référence. | IMAGE | Non | - |
| `last_frame` | Image facultative sur laquelle la vidéo se termine. Compte dans la limite de 10 images avec les images de référence. | IMAGE | Non | - |
| `prompt` | Description de la vidéo à générer. Référencez les entrées sous la forme `@Image1`, `@Image2`, etc., et `@Video1`, `@Video2`, etc. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie ; une option dont le nom contient `HDR` renvoie une vidéo HDR. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Rapport d’aspect de la vidéo de sortie. `"adaptive"` suit le prompt, puis la première image ou les vidéos de référence, et sinon revient à 16:9. Par défaut : `"adaptive"`. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durée de la vidéo générée, en secondes. Par défaut : 5. | INT | Oui | 3 à 30 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quel que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

### Entrées kling-4.0-flash

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0-flash"`.

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `reference_images` | Emplacements extensibles pour les images de référence, jusqu’à 10. Référencez-les dans le prompt sous la forme `@Image1`, `@Image2`, etc., dans l’ordre de connexion. | AUTOGROW | Non | 0 à 10 images |
| `reference_videos` | Emplacements extensibles pour les vidéos de référence, jusqu’à 5. Référencez-les dans le prompt sous la forme `@Video1`, `@Video2`, etc. Chaque vidéo, ainsi que l’ensemble des vidéos, doit durer de 3 à 20 secondes. | AUTOGROW | Non | 0 à 5 vidéos |
| `first_frame` | Image facultative sur laquelle la vidéo commence. Compte dans la limite de 10 images avec les images de référence. | IMAGE | Non | - |
| `prompt` | Description de la vidéo à générer. Référencez les entrées sous la forme `@Image1`, `@Image2`, etc., et `@Video1`, `@Video2`, etc. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Flash ne génère qu’en 720p. Par défaut : `"720p"`. | COMBO | Oui | `"720p"` |
| `aspect_ratio` | Rapport d’aspect de la vidéo de sortie. `"adaptive"` suit le prompt, puis la première image ou les vidéos de référence, et sinon revient à 16:9. Par défaut : `"adaptive"`. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durée de la vidéo générée, en secondes. Par défaut : 5. | INT | Oui | 3 à 20 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quel que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Les images sont limitées à 10 au total, en comptant les images de référence, la première image et la dernière image.
* Chaque image doit faire au moins 300x300 pixels, avec un rapport d’aspect compris entre 2:5 et 5:2.
* Chaque vidéo de référence doit durer de 3 à 30 secondes (de 3 à 20 avec `kling-4.0-flash`), mesurer au moins 700x700 pixels et au plus 4553x4553 pixels, ne pas dépasser 8,294,400 pixels au total, avoir un rapport d’aspect compris entre 2:5 et 5:2 et une fréquence d’images d’au moins 24 fps. L’ensemble des vidéos de référence ne doit pas dépasser la même limite.
* Un prompt qui mentionne `@ImageN` ou `@VideoN` génère une erreur lorsque moins de N entrées de ce type sont connectées.
* Lorsqu’une première ou une dernière image est connectée, le nœud ajoute une instruction indiquant que la vidéo commence ou se termine exactement sur cette image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche terminée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `d1048c637074d79fa41da1f903a1f4b2c895563dde4c5ee761c20460a8d2e383`
