# Bria Supprimer l'Arrière-plan Vidéo (Transparent)

Ce nœud supprime l'arrière-plan d'une vidéo à l'aide du service d'IA Bria et produit les images détourées ainsi qu'un masque alpha. Connectez les deux sorties à un nœud de composition, ou transmettez-les à un nœud Save WEBM pour écrire une vidéo transparente.

## Entrées

| Paramètre | Description | Type de Données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `vidéo` | La vidéo d'entrée à traiter | VIDEO | Oui | - |
| `graine` | La graine contrôle si le nœud doit se réexécuter ; les résultats sont non déterministes quelle que soit la graine (par défaut : 0) | INT | Oui | 0 à 2147483647 |

## Sorties

| Nom de Sortie | Description | Type de Données |
|---------------|-------------|-----------------|
| `images` | Les images vidéo dont l'arrière-plan a été supprimé | IMAGE |
| `mask` | Le masque alpha pour les images vidéo | MASK |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaTransparentVideoBackground/fr.md)

---
**Source fingerprint (SHA-256):** `45fb3fc185b5c6420d6ac2b87f2403566e1ef6dcdc57791fb833b6ccb2a64cd9`
