# Guidance VideoTriangleCFG

Le nœud VideoTriangleCFGGuidance applique un motif de mise à l'échelle de guidage sans classificateur triangulaire aux modèles vidéo. Il modifie l'échelle de conditionnement au fil du temps à l'aide d'une fonction en onde triangulaire qui oscille entre la valeur CFG minimale et l'échelle de conditionnement d'origine. Cela crée un motif de guidage dynamique qui peut contribuer à améliorer la cohérence et la qualité de la génération vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Le modèle vidéo auquel appliquer le guidage CFG triangulaire | MODEL | Oui | - |
| `min_cfg` | La valeur CFG minimale pour le motif triangulaire (par défaut : 1.0) | FLOAT | Oui | 0.0 - 100.0 |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `model` | Le modèle modifié avec le guidage CFG triangulaire appliqué | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/fr.md)

---
**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`
