> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/fr.md)

Le nœud **VideoTriangleCFGGuidance** applique un motif d'échelle de guidage CFG triangulaire aux modèles vidéo. Il modifie l'échelle de conditionnement dans le temps en utilisant une fonction d'onde triangulaire qui oscille entre la valeur CFG minimale et l'échelle de conditionnement d'origine. Cela crée un motif de guidage dynamique qui peut contribuer à améliorer la cohérence et la qualité de la génération vidéo.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle vidéo auquel appliquer le guidage CFG triangulaire |
| `min_cfg` | FLOAT | Oui | 0.0 - 100.0 | La valeur d'échelle CFG minimale pour le motif triangulaire (par défaut : 1.0) |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle modifié avec le guidage CFG triangulaire appliqué |

---
**Source fingerprint (SHA-256):** `0b854d78f32e265b1a4322cb11b231df33e6072611142537e0c8cff4e93db49a`
