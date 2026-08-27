# Échelle de bruit du modèle

## Vue d'ensemble

Ce nœud ajuste l'échelle de bruit utilisée lors de l'échantillonnage du modèle. Il permet de définir une valeur spécifique d'échelle de bruit, qui contrôle la quantité de bruit appliquée au processus d'échantillonnage du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle auquel appliquer l'ajustement de l'échelle de bruit. | MODEL | Oui | - |
| `échelle_bruit` | Échelle de bruit d'entraînement absolue. Par exemple, HiDream-O1 base : 8.0, dev : 7.5. (défaut : 1.0) | FLOAT | Oui | 0.0 à 64.0 (pas : 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle modifié avec la nouvelle échelle de bruit appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/fr.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
