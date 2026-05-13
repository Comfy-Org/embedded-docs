> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/fr.md)

Le nœud UNetTemporalAttentionMultiply applique des facteurs de multiplication à différents types de mécanismes d'attention dans un modèle UNet temporel. Il modifie le modèle en ajustant les poids des couches d'auto-attention et d'attention croisée, en distinguant les composants structurels et temporels. Cela permet un réglage précis de l'influence de chaque type d'attention sur la sortie du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle d'entrée à modifier avec les multiplicateurs d'attention |
| `self_structural` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composants structurels de l'auto-attention (par défaut : 1.0) |
| `self_temporal` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composants temporels de l'auto-attention (par défaut : 1.0) |
| `cross_structural` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composants structurels de l'attention croisée (par défaut : 1.0) |
| `cross_temporal` | FLOAT | Non | 0.0 - 10.0 | Multiplicateur pour les composants temporels de l'attention croisée (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle modifié avec des poids d'attention ajustés |

---
**Source fingerprint (SHA-256):** `98d62fb28a0cdf62154ae4e0b672b3a7bcb9ed61186a164a43992263c1f9439a`
