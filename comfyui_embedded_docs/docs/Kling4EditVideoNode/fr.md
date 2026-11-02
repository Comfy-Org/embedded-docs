# Kling 4.0 Edit Video

Modifie une vidéo existante avec une invite textuelle à l'aide du modèle Kling 4.0, éventuellement guidé par des vidéos de référence et des images de référence. Le résultat conserve la longueur de la vidéo d'entrée. Utilisez-le pour modifier ce qui se passe dans un clip, le restyler ou remplacer des éléments tout en conservant la synchronisation d'origine.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. Seul `"kling-4.0"` est disponible ; le sélectionner révèle les entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video_1` | La vidéo à modifier, d'une durée de 3 à 30 secondes. La sortie conserve sa longueur. | VIDEO | Oui | 3 à 30 secondes |
| `reference_videos` | Emplacements extensibles pour les vidéos de référence, jusqu'à 4. Faites-y référence dans l'invite sous la forme `@Video2`, etc. Chaque vidéo et toutes les vidéos ensemble doivent durer de 3 à 30 secondes. | AUTOGROW | Non | 0 à 4 vidéos |
| `reference_images` | Emplacements extensibles pour les images de référence, jusqu'à 10. Faites-y référence dans l'invite sous la forme `@Image1`, `@Image2`, etc. | AUTOGROW | Non | 0 à 10 images |
| `prompt` | Description de ce qu'il faut modifier et de ce qu'il faut conserver. Faites référence à la vidéo en cours de modification sous la forme `@Video1`, aux vidéos de référence sous la forme `@Video2`, etc., et aux images sous la forme `@Image1`, etc. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Format d'image de la vidéo de sortie. `"adaptive"` conserve le format d'image de la vidéo d'entrée. Par défaut : `"adaptive"`. | COMBO | Oui | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | La graine contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

**Contraintes et comportement :**

* La vidéo d'entrée et chaque vidéo de référence doivent durer de 3 à 30 secondes, avoir au moins 700x700 et au plus 4553x4553 pixels, pas plus de 8 294 400 pixels au total, avec un format d'image compris entre 2:5 et 5:2 et une fréquence d'images d'au moins 24 ips. Toutes les vidéos ensemble ne doivent pas dépasser 30 secondes.
* Chaque image de référence doit faire au moins 300x300 pixels avec un format d'image compris entre 2:5 et 5:2, et au plus 10 images peuvent être connectées.
* Une invite qui mentionne `@VideoN` ou `@ImageN` génère une erreur lorsque moins de N entrées de ce type sont connectées.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo modifiée, téléchargée depuis le fournisseur une fois la tâche terminée. Elle a la même longueur que la vidéo d'entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `00e8de2529df9be6bc1fae5f2c2beda01f151143448e91b79f9cfb27436064ff`
