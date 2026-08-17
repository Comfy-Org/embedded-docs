# Bria Suppression de l’arrière-plan vidéo (Transparent)

Ce nœud supprime l'arrière-plan d'une vidéo à l'aide du service IA de Bria et renvoie les images détourées ainsi qu'un masque alpha. Connectez les deux sorties à un nœud de composition, ou transmettez-les à un nœud Save WEBM pour écrire une vidéo transparente.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | La vidéo d'entrée à traiter. La durée maximale est de 60 secondes. | VIDEO | Oui | - |
| `seed` | Le `seed` contrôle si le nœud doit être exécuté à nouveau ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images de la vidéo dont l'arrière-plan a été supprimé | IMAGE |
| `mask` | Le masque alpha des images vidéo, où 1 signifie transparent | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/fr.md)

---
**Source fingerprint (SHA-256):** `536bd52af29218d2a342086e92799d3d9310da5ae5cbf02d705ba7503a4d73c8`
