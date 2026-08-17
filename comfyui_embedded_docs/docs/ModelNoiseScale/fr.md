# Échelle de bruit du modèle

Ce nœud ajuste l'échelle de bruit utilisée lors de l'échantillonnage du modèle. Il vous permet de définir une valeur d'échelle de bruit spécifique, qui contrôle la quantité de bruit appliquée au processus d'échantillonnage du modèle. Le nœud clone le modèle et met à jour sa configuration d'échantillonnage avec la nouvelle échelle de bruit tout en conservant les paramètres de décalage et de multiplicateur existants.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle auquel appliquer l'ajustement de l'échelle de bruit. | MODEL | Oui | - |
| `noise_scale` | Échelle de bruit d'entraînement absolue. Par exemple HiDream-O1 base : 8.0, dev : 7.5. (par défaut : 1.0) | FLOAT | Oui | 0.0 to 64.0 (step: 0.01) |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `MODEL` | Le modèle modifié avec la nouvelle échelle de bruit appliquée. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelNoiseScale/fr.md)

---
**Source fingerprint (SHA-256):** `75b0b99323fc15ff3cafc23de05a9d6b52d059494fbc229e5fb685d2908dd5d3`
