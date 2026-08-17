# EmptyAceStepLatentAudio

Le nœud `EmptyAceStepLatentAudio` crée des échantillons audio latents vides d'une durée spécifiée. Il génère un lot de latents audio silencieux remplis de zéros, dont la longueur est calculée en fonction des secondes d'entrée et des paramètres de traitement audio. Ce nœud est utile pour initialiser des workflows de traitement audio nécessitant des représentations latentes.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `seconds` | La durée de l'audio en secondes (défaut : 120.0) | FLOAT | Oui | 1.0 - 1000.0 (pas de 0.1) |
| `batch_size` | Le nombre d'images latentes dans le lot (défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Renvoie des échantillons audio latents vides remplis de zéros. La sortie contient un tenseur `samples` et un champ `type` défini sur « audio ». | LATENT |

Remarque : La longueur du latent est dérivée de la valeur `seconds` en utilisant un taux d'échantillonnage interne de 44100 Hz, calculée comme suit : `int(seconds × 44100 / 512 / 8)` trames. Le tenseur latent résultant est entièrement rempli de zéros.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
