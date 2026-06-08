Le nœud EmptyAceStepLatentAudio crée des échantillons audio latents vides d'une durée spécifiée. Il génère un lot de latents audio silencieux remplis de zéros, dont la longueur est calculée en fonction des secondes d'entrée et des paramètres de traitement audio. Ce nœud est utile pour initialiser des workflows de traitement audio nécessitant des représentations latentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `secondes` | La durée de l'audio en secondes (par défaut : 120.0) | FLOAT | Oui | 1.0 - 1000.0 |
| `taille_du_lot` | Le nombre d'images latentes dans le lot (par défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Renvoie des échantillons audio latents vides avec des zéros. La sortie contient un tenseur `samples` et un champ `type` défini sur "audio". | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
