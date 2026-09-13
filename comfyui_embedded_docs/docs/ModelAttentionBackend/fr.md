# Backend d’attention du modèle

Ce nœud sélectionne l'implémentation d'attention dense pour un modèle, clone le modèle, applique le backend choisi et renvoie le clone patché. Lorsqu'il est utilisé avec Block Sparse Attention, ce backend est utilisé chaque fois que l'attention sparse est inactive ou non prise en charge. Si le backend sélectionné n'est pas disponible, le nœud revient automatiquement à l'attention PyTorch.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à patcher. | MODEL | Oui |  |
| `attention` | Le backend d'attention dense à appliquer. L'attention Comfy Kitchen utilise une attention INT8 quantifiée et n'est disponible que sur les GPU Nvidia et AMD. Par défaut : "pytorch attention". Si le backend sélectionné n'est pas disponible, l'attention PyTorch est utilisée comme solution de repli. | COMBO | Oui | "pytorch attention"<br>"comfy kitchen attention" |

Remarque : l'option "comfy kitchen attention" n'est listée que lorsque le module d'attention INT8 Comfy Kitchen est disponible dans l'environnement actuel.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model` | Un clone du modèle d'entrée avec le backend d'attention sélectionné appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/fr.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
