# Créer un fichier 3D (à partir d’un Splat)

SplatToFile3D convertit un gaussian splat en un objet File3D pouvant être utilisé avec les nœuds Save ou Preview 3D. Vous pouvez choisir le format de fichier de sortie. Le nœud ne prend en charge qu'un seul élément par lot ; s'il reçoit plus d'un élément, il utilise le premier et journalise un avertissement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Les données du gaussian splat à sérialiser dans un fichier. Un seul élément par lot est pris en charge. Si plus d'un élément est fourni, seul le premier est utilisé. | SPLAT | Oui | - |
| `format` | Le format de fichier de sortie pour le fichier 3D. ply : standard 3D Gaussian Splat avec harmoniques sphériques complètes. ksplat : mkkellogg SplatBuffer (niveau 0, non compressé), couleur de base uniquement. spz : Niantic compressé par gzip (~10x plus petit), couleur de base uniquement (par défaut : "ply") | COMBO | Oui | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Un objet File3D contenant les données du gaussian splat sérialisées dans le format sélectionné, prêt à être enregistré ou prévisualisé | FILE3D |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/fr.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
