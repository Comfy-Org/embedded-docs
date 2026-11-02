# Kling 4.0 Reference to Video

Génère une vidéo à partir d'images de référence et de vidéos de référence avec le modèle Kling 4.0, y compris l'audio. Les références déterminent le sujet, le style et le mouvement, et une première et une dernière image facultatives fixent le début et la fin du clip. Utilisez-le pour maintenir la cohérence d'un personnage ou d'une scène sur un plan tout en décrivant l'action dans le prompt.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. Seul `"kling-4.0"` est disponible ; le sélectionner révèle les entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacements extensibles pour les images de référence, jusqu'à 10. Faites-y référence dans le prompt sous la forme `@Image1`, `@Image2`, etc., dans l'ordre de connexion. | AUTOGROW | Non | 0 à 10 images |
| `reference_videos` | Emplacements extensibles pour les vidéos de référence, jusqu'à 5. Faites-y référence dans le prompt sous la forme `@Video1`, `@Video2`, etc. Chaque vidéo et l'ensemble des vidéos doivent durer entre 3 et 30 secondes. | AUTOGROW | Non | 0 à 5 vidéos |
| `first_frame` | Image facultative sur laquelle la vidéo commence. Compte dans la limite de 10 images avec les images de référence. | IMAGE | Non | - |
| `last_frame` | Image facultative sur laquelle la vidéo se termine. Compte dans la limite de 10 images avec les images de référence. | IMAGE | Non | - |
| `prompt` | Description de la vidéo à générer. Faites référence aux entrées sous la forme `@Image1`, `@Image2`, etc., et `@Video1`, `@Video2`, etc. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Rapport d'aspect de la vidéo de sortie. `"adaptive"` suit le prompt, puis la première image ou les vidéos de référence, et sinon revient à 16:9. Par défaut : `"adaptive"`. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durée de la vidéo générée en secondes. Par défaut : 5. | INT | Oui | 3 à 30 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quel que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Les images sont limitées à 10 au total, en comptant les images de référence, la première image et la dernière image.
* Chaque image doit être d'au moins 300x300 pixels avec un rapport d'aspect compris entre 2:5 et 5:2.
* Chaque vidéo de référence doit durer de 3 à 30 secondes, avoir au moins 700x700 et au plus 4553x4553 pixels, ne pas dépasser 8 294 400 pixels au total, avec un rapport d'aspect compris entre 2:5 et 5:2 et une fréquence d'images d'au moins 24 ips. L'ensemble des vidéos de référence ne doit pas dépasser 30 secondes.
* Un prompt qui mentionne `@ImageN` ou `@VideoN` génère une erreur lorsque moins de N entrées de ce type sont connectées.
* Lorsqu'une première ou une dernière image est connectée, le nœud ajoute une instruction indiquant que la vidéo commence ou se termine exactement sur cette image.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche terminée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `bda2298ed6ed06db04a8f342ec6ad0d5a0494e09bfadee72fce4420ebe4eaf6a`
