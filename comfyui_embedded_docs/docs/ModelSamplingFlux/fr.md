> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/fr.md)

Le nœud ModelSamplingFlux applique un échantillonnage Flux à un modèle donné en calculant un paramètre de décalage basé sur les dimensions de l'image. Il crée une configuration d'échantillonnage spécialisée qui ajuste le comportement du modèle en fonction des paramètres de largeur, hauteur et décalage spécifiés, puis renvoie le modèle modifié avec les nouveaux paramètres d'échantillonnage appliqués.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | MODEL | Oui | - | Le modèle auquel appliquer l'échantillonnage Flux |
| `décalage_max` | FLOAT | Oui | 0,0 - 100,0 | Valeur de décalage maximale pour le calcul d'échantillonnage (par défaut : 1,15) |
| `décalage_base` | FLOAT | Oui | 0,0 - 100,0 | Valeur de décalage de base pour le calcul d'échantillonnage (par défaut : 0,5) |
| `largeur` | INT | Oui | 16 - MAX_RESOLUTION | Largeur de l'image cible en pixels (par défaut : 1024) |
| `hauteur` | INT | Oui | 16 - MAX_RESOLUTION | Hauteur de l'image cible en pixels (par défaut : 1024) |

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `modèle` | MODEL | Le modèle modifié avec la configuration d'échantillonnage Flux appliquée |

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`
