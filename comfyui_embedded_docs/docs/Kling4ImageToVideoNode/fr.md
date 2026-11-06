# Kling 4.0 — image vers vidéo

Génère une vidéo à partir d’un ensemble d’images clés avec le modèle Kling 4.0, incluant l’audio. La première image, jusqu’à huit images intermédiaires et la dernière image sont envoyées dans l’ordre, les images intermédiaires sont réparties uniformément sur le clip, et la sortie reprend le rapport d’aspect de la première image clé. Utilisez-le pour animer une image ou orienter un plan à travers une séquence de moments clés.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. `"kling-4.0"` prend en charge jusqu’à 1080p et 30 secondes ; `"kling-4.0-flash"` est limité à 720p, 20 secondes et une seule première image. La sélection d’un modèle révèle ses entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`. Au moins une des entrées d’image doit être connectée.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `first_frame` | Image facultative sur laquelle la vidéo commence. | IMAGE | Non | - |
| `middle_frames` | Emplacements extensibles facultatifs pour les images entre la première et la dernière, jusqu’à 8. Elles sont réparties uniformément sur le clip. | AUTOGROW | Non | 0 à 8 images |
| `last_frame` | Image facultative sur laquelle la vidéo se termine. | IMAGE | Non | - |
| `prompt` | Description facultative du mouvement. Faites référence aux images connectées via `@Image1`, `@Image2`, etc., dans l’ordre première image, images intermédiaires, dernière image. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo générée en secondes. Par défaut : 5. | INT | Oui | 3 à 30 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

### Entrées kling-4.0-flash

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0-flash"`. Flash anime une seule première image.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `first_frame` | Image sur laquelle la vidéo commence. | IMAGE | Oui | - |
| `prompt` | Description facultative du mouvement. Faites référence à la première image via `@Image1`. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Flash ne rend qu’en 720p. Par défaut : `"720p"`. | COMBO | Oui | `"720p"` |
| `duration` | Durée de la vidéo générée en secondes. Par défaut : 5. | INT | Oui | 3 à 20 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Au plus 10 images peuvent être connectées au total, en comptant la première image, chaque image intermédiaire et la dernière image.
* La vidéo reprend le rapport d’aspect de la première image clé ; aucune entrée de rapport d’aspect n’est donc nécessaire.
* Chaque image doit mesurer au moins 300x300 pixels avec un rapport d’aspect compris entre 2:5 et 5:2.
* Un prompt qui mentionne `@ImageN` déclenche une erreur lorsque moins de N images sont connectées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche terminée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `248ab33bf7a50afbc08baf1e64e5b1908a38905cda2a87d1303eeeb2755b5a6d`
