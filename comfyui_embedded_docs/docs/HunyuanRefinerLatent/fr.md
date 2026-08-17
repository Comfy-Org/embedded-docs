# Latent HunyuanRefiner

---

Le nœud HunyuanRefinerLatent traite les entrées de conditionnement et latentes pour les opérations de raffinement. Il applique une augmentation de bruit à la fois au conditionnement positif et négatif tout en incorporant les données d'image latente, et génère une nouvelle sortie latente avec des dimensions spécifiques pour un traitement ultérieur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `positive` | L'entrée de conditionnement positif à traiter | CONDITIONING | Oui | - |
| `negative` | L'entrée de conditionnement négatif à traiter | CONDITIONING | Oui | - |
| `latent` | L'entrée de représentation latente | LATENT | Oui | - |
| `noise_augmentation` | La quantité d'augmentation de bruit à appliquer (défaut : 0.10, pas : 0.01, paramètre avancé) | FLOAT | Oui | 0.0 - 1.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `positive` | Le conditionnement positif traité, avec l'augmentation de bruit appliquée et la concaténation d'image latente | CONDITIONING |
| `negative` | Le conditionnement négatif traité, avec l'augmentation de bruit appliquée et la concaténation d'image latente | CONDITIONING |
| `latent` | Un nouveau latent rempli de zéros, avec la même taille de lot et les mêmes trois dernières dimensions que le `latent` d'entrée, mais avec 32 canaux | LATENT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fr.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
