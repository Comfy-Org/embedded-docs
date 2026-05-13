> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/fr.md)

Le nœud HunyuanRefinerLatent traite les entrées de conditionnement et latentes pour les opérations de raffinement. Il applique une augmentation de bruit aux conditionnements positif et négatif tout en intégrant les données d'image latente, et génère une nouvelle sortie latente avec des dimensions spécifiques pour un traitement ultérieur.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `positif` | CONDITIONING | Oui | - | L'entrée de conditionnement positif à traiter |
| `négatif` | CONDITIONING | Oui | - | L'entrée de conditionnement négatif à traiter |
| `latent` | LATENT | Oui | - | L'entrée de représentation latente |
| `augmentation_du_bruit` | FLOAT | Oui | 0,0 - 1,0 | La quantité d'augmentation de bruit à appliquer (par défaut : 0,10) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `négatif` | CONDITIONING | Le conditionnement positif traité avec augmentation de bruit appliquée et concaténation d'image latente |
| `latent` | CONDITIONING | Le conditionnement négatif traité avec augmentation de bruit appliquée et concaténation d'image latente |
| `latent` | LATENT | Une nouvelle sortie latente avec des dimensions [batch_size, 32, hauteur, largeur, canaux] |

---
**Source fingerprint (SHA-256):** `f097b58f1948e5c0801f81b51a5189619695a6afa189368aff4c64b126fc5ce5`
