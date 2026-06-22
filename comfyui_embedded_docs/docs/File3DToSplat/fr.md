# Obtenir Splat

Ce nœud convertit un fichier 3D contenant des données de splat gaussien en un format de splat gaussien utilisable dans le graphe de nœuds. Il prend en charge les formats de fichier PLY, SPLAT, KSPLAT et SPZ, le format étant automatiquement détecté à partir du contenu du fichier.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model_3d` | Un fichier 3D de splat gaussien | FILE3D | Oui | - |

Le fichier d'entrée doit être dans l'un des formats pris en charge : PLY, SPLAT, KSPLAT ou SPZ. Les fichiers PLY contiennent des données complètes d'harmoniques sphériques, tandis que les autres formats ne contiennent que des informations de couleur de base. Le format est automatiquement détecté à partir du contenu du fichier.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `splat` | Un splat gaussien contenant les données de position, d'échelle, de rotation, d'opacité et d'harmoniques sphériques | SPLAT |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/fr.md)

---
**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`
