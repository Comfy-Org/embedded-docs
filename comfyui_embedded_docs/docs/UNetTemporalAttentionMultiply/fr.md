# UNetTemporalAttentionMultiply

Le nœud UNetTemporalAttentionMultiply applique des facteurs de multiplication à différents types de mécanismes d'attention dans un modèle UNet temporel. Il modifie le modèle en ajustant les poids des couches d'auto-attention et d'attention croisée, en distinguant les composants structurels et temporels. Cela permet un réglage précis de l'influence de chaque type d'attention sur la sortie du modèle.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle d'entrée à modifier avec les multiplicateurs d'attention | MODEL | Oui | - |
| `self_structural` | Multiplicateur pour les composants structurels de l'auto-attention (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `self_temporal` | Multiplicateur pour les composants temporels de l'auto-attention (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `cross_structural` | Multiplicateur pour les composants structurels de l'attention croisée (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |
| `cross_temporal` | Multiplicateur pour les composants temporels de l'attention croisée (par défaut : 1.0) | FLOAT | Non | 0.0 - 10.0 |


| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec des poids d'attention ajustés | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/fr.md)

---
**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`
