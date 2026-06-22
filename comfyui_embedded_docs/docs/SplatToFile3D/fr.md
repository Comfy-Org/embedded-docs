# Créer un fichier 3D (à partir d’un Splat)

## Présentation

Le nœud SplatToFile3D convertit un nuage gaussien (gaussian splat) en un objet File3D pouvant être utilisé avec les nœuds Save ou Preview 3D. Il ne prend en charge qu'un seul élément par lot et vous permet de choisir parmi différents formats de fichier de sortie pour les données 3D exportées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Les données du nuage gaussien à sérialiser dans un fichier | SPLAT | Oui | - |
| `format` | Le format de fichier de sortie pour le fichier 3D. ply : nuage gaussien 3D standard avec harmoniques sphériques complètes. ksplat : SplatBuffer mkkellogg (niveau 0, non compressé), couleur de base uniquement. spz : compressé gzip Niantic (~10x plus petit), couleur de base uniquement (par défaut : "ply") | COMBO | Oui | `"ply"`<br>`"ksplat"`<br>`"spz"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `model_3d` | Un objet File3D contenant les données du nuage gaussien sérialisées dans le format sélectionné, prêt à être sauvegardé ou prévisualisé | FILE3D |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/fr.md)

---
**Source fingerprint (SHA-256):** `c04fe04faa8ce81ad699e67c00d047550b0cadbfd037b687331f76944501a9f6`
