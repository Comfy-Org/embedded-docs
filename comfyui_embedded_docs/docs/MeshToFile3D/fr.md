# MeshToFile3D

Ce nœud sérialise un maillage en un objet de fichier GLB pouvant être transmis aux nœuds Save 3D ou Preview 3D. Il transporte toutes les données du maillage, y compris les UV, les couleurs, les normales, la texture, les cartes de normale/occlusion/émissive et les paramètres de matériau. Seul le premier élément d’un lot multi-éléments est utilisé.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `mesh` | Le maillage à convertir en fichier GLB, y compris les UV, les couleurs, les normales, la texture, les cartes de normale/occlusion/émissive et le matériau. Un seul élément par lot est pris en charge ; si un lot contient plusieurs éléments, le premier est utilisé. | MESH | Oui | Maillage unique |

Remarque : Le nœud ne prend en charge qu'un seul élément par lot. Si le maillage d'entrée contient plus d'un élément dans son lot, un avertissement est consigné et le premier élément est utilisé. Le maillage doit contenir au moins un sommet et une face ; un maillage vide génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Un objet de fichier GLB (glTF binaire) contenant le maillage sérialisé, prêt à être enregistré ou prévisualisé par d'autres nœuds 3D. | FILE3D |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/fr.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`
