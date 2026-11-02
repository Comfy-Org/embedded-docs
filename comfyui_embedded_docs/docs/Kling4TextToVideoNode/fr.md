# Kling 4.0 Text to Video

Génère une vidéo à partir d’un prompt textuel avec le modèle Kling 4.0, y compris l’audio. Ce nœud envoie le prompt et les paramètres de génération à l’API Kling, attend la fin de la tâche et renvoie la vidéo terminée. Utilisez-le lorsqu’un clip doit être créé à partir d’une simple description, sans média de référence.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Sélecteur de modèle. Seul `"kling-4.0"` est disponible ; le sélectionner révèle les entrées ci-dessous. | DYNAMIC_COMBO | Oui | `"kling-4.0"` |

### Entrées kling-4.0

Ces entrées apparaissent lorsque `model` est défini sur `"kling-4.0"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Description textuelle de la vidéo à générer. Doit contenir entre 1 et 26000 caractères. | STRING | Oui | 1 à 26000 caractères |
| `resolution` | Résolution de la vidéo de sortie. Par défaut : `"720p"`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Rapport d’aspect de la vidéo de sortie. Par défaut : `"16:9"`. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `duration` | Durée de la vidéo générée en secondes. Par défaut : 5. | INT | Oui | 3 à 30 |
| `seed` | La graine (`seed`) contrôle si le nœud doit être réexécuté ; les résultats sont non déterministes quelle que soit la graine. Par défaut : 42. | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, téléchargée depuis le fournisseur une fois la tâche terminée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `3835dcb7d83d843ea7f6c5dc691b48759d9c3e7a7baeead3d0f92817e73d6079`
