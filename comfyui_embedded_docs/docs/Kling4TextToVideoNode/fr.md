# Kling 4.0 Texte vers vidéo

Génère une vidéo à partir d'un prompt texte avec le modèle Kling 4.0, audio inclus. Ce nœud envoie le prompt et les paramètres de génération à l'API Kling, attend la fin de la tâche et renvoie la vidéo terminée. Utilisez-le lorsqu'un clip doit être créé à partir d'une simple description, sans média de référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Sélecteur de modèle. `"kling-4.0"` prend en charge jusqu'à 1080p et 30 secondes ; `"kling-4.0-flash"` est limité à 720p et 20 secondes. La sélection d'un modèle révèle ses entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle de la vidéo à générer. Doit comporter entre 1 et 26000 caractères. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Format d'image de la vidéo de sortie. Par défaut : `"16:9"`. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durée de la vidéo générée, en secondes. Par défaut : 5. | INT | Oui | 3 à 30 |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

### Entrées kling-4.0-flash

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0-flash"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle de la vidéo à générer. Doit comporter entre 1 et 26000 caractères. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Flash ne génère qu'en 720p. Par défaut : `"720p"`. | COMBO | Oui | `"720p"` |
| `aspect_ratio` | Format d'image de la vidéo de sortie. Par défaut : `"16:9"`. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durée de la vidéo générée, en secondes. Par défaut : 5. | INT | Oui | 3 à 20 |
| `seed` | La graine détermine si le nœud doit être réexécuté ; les résultats ne sont pas déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche terminée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `3e37f976f48488c3accb4efb0d876d12c316796023eb9c28b9209cb2188249e2`
