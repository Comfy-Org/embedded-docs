> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/fr.md)

Le nœud CLIPAttentionMultiply permet d'ajuster le mécanisme d'attention dans les modèles CLIP en appliquant des facteurs de multiplication à différents composants des couches d'auto-attention. Il fonctionne en modifiant les poids et les biais des projections de requête, de clé, de valeur et de sortie dans le mécanisme d'attention du modèle CLIP. Ce nœud expérimental crée une copie modifiée du modèle CLIP d'entrée avec les facteurs d'échelle spécifiés appliqués.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `clip` | CLIP | Oui | - | Le modèle CLIP à modifier |
| `q` | FLOAT | Oui | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection de requête (par défaut : 1.0) |
| `k` | FLOAT | Oui | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection de clé (par défaut : 1.0) |
| `v` | FLOAT | Oui | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection de valeur (par défaut : 1.0) |
| `sortie` | FLOAT | Oui | 0.0 - 10.0 | Facteur de multiplication pour les poids et biais de projection de sortie (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CLIP` | CLIP | Renvoie un modèle CLIP modifié avec les facteurs d'échelle d'attention spécifiés appliqués |

---
**Source fingerprint (SHA-256):** `43dab83ecfc928f3359eb7560658f43235bf3faa62c81084a2b4f482e3a4638f`
