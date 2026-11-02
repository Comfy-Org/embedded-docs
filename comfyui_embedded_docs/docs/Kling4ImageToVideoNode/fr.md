# Kling 4.0 Image to Video

Génère une vidéo à partir d'un ensemble d'images clés avec le modèle Kling 4.0, y compris l'audio. La première image, jusqu'à huit images intermédiaires et la dernière image sont envoyées dans l'ordre ; les images intermédiaires sont réparties uniformément sur le clip et la sortie adopte le rapport d'aspect de la première image clé. Utilisez-le pour animer une image ou pour orienter un plan à travers une séquence de moments clés.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. Seul `"kling-4.0"` est disponible ; le sélectionner révèle les entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`. Au moins une des entrées d'image doit être connectée.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `first_frame` | Image facultative sur laquelle la vidéo commence. | IMAGE | Non | - |
| `middle_frames` | Emplacements extensibles facultatifs pour les images entre la première et la dernière, jusqu'à 8. Elles sont réparties uniformément sur le clip. | AUTOGROW | Non | 0 à 8 images |
| `last_frame` | Image facultative sur laquelle la vidéo se termine. | IMAGE | Non | - |
| `prompt` | Description facultative du mouvement. Référez-vous aux images connectées avec `@Image1`, `@Image2`, etc., dans l'ordre : première image, images intermédiaires, dernière image. Par défaut : chaîne vide. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo générée en secondes. Par défaut : 5. | INT | Oui | 3 à 30 |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* Au plus 10 images peuvent être connectées au total, en comptant la première image, chaque image intermédiaire et la dernière image.
* La vidéo adopte le rapport d'aspect de la première image clé, aucun rapport d'aspect n'est donc nécessaire en entrée.
* Chaque image doit mesurer au moins 300x300 pixels, avec un rapport d'aspect compris entre 2:5 et 5:2.
* Un prompt qui mentionne `@ImageN` génère une erreur lorsque moins de N images sont connectées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche terminée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `762c350abd4a881b96355a7ce5b9e346d5c3ff22e9f11db820584d02aee12885`
