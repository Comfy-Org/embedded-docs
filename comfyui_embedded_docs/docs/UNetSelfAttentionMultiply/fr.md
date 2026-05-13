> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/fr.md)

Le nœud UNetSelfAttentionMultiply applique des facteurs de multiplication aux composants requête, clé, valeur et sortie du mécanisme d'auto-attention dans un modèle UNet. Il permet de pondérer différentes parties du calcul d'attention afin d'expérimenter l'impact des poids d'attention sur le comportement du modèle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | MODEL | Oui | - | Le modèle UNet à modifier avec des facteurs d'échelle d'attention |
| `q` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour le composant requête (par défaut : 1.0) |
| `k` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour le composant clé (par défaut : 1.0) |
| `v` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour le composant valeur (par défaut : 1.0) |
| `out` | FLOAT | Non | 0.0 - 10.0 | Facteur de multiplication pour le composant de sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `MODEL` | MODEL | Le modèle UNet modifié avec des composants d'attention mis à l'échelle |

---
**Source fingerprint (SHA-256):** `ee6328c6cba44d30d2e219a2af04bb3d3d9adeaabb959a46f87b3b299dfe2f43`
