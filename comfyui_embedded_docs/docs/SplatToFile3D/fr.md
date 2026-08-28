# Créer un fichier 3D (à partir d’un Splat)

Le nœud SplatToFile3D convertit un splat gaussien en un objet File3D pouvant être utilisé avec les nœuds Save ou Preview 3D. Il ne prend en charge qu’un seul élément par lot et vous permet de choisir parmi différents formats de fichiers de sortie pour les données 3D exportées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `splat` | Les données du splat gaussien à sérialiser dans un fichier | SPLAT | Oui | - |
| `format` | Le format de fichier de sortie pour le fichier 3D. ply : splat gaussien 3D standard avec harmoniques sphériques complètes. ksplat : SplatBuffer mkkellogg (niveau 0, non compressé), couleur de base uniquement. spz : compressé gzip par Niantic (~10x plus petit), couleur de base uniquement (par défaut : « ply ») | COMBO | Oui | « ply »<br>« ksplat »<br>« spz » |

Remarque : Ce nœud ne prend en charge qu’un seul élément par lot. Si le splat d’entrée contient plus d’un élément dans le lot, le nœud enregistre un avertissement et utilise le premier élément. Si un format non pris en charge est fourni, le nœud génère une erreur.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `modèle_3d` | Un objet File3D contenant les données du splat gaussien sérialisées dans le format sélectionné, prêt à être enregistré ou prévisualisé | FILE3D |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplatToFile3D/fr.md)

---
**Source fingerprint (SHA-256):** `4bb49f417a66f25fce577894a67f39bae6157c4eb88ccf8fad77d74141a50409`
