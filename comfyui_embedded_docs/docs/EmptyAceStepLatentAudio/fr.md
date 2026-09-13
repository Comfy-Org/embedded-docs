# EmptyAceStepLatentAudio

Le nœud Empty Ace Step 1.0 Latent Audio crée des échantillons latents audio vides pour une durée choisie. Il remplit un lot de latents audio silencieux (tous à zéro), dont la longueur est calculée à partir de l'entrée `seconds` à l'aide des paramètres de traitement audio. Il est généralement utilisé pour initialiser des workflows audio qui nécessitent une représentation latente comme point de départ.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
| --- | --- | --- | --- | --- |
| `seconds` | Durée de l'audio en secondes (par défaut : 120.0, pas : 0.1) | FLOAT | Oui | 1.0 - 1000.0 |
| `batch_size` | Nombre d'images latentes dans le lot (par défaut : 1) | INT | Oui | 1 - 4096 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | Renvoie des échantillons latents audio vides remplis de zéros. La sortie contient un tenseur `samples` et un champ `type` défini sur "audio". | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/fr.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
