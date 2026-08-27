# CLIPTextEncodePixArtAlpha

Encode le texte et définit le conditionnement de résolution pour PixArt Alpha. Ce nœud traite l'entrée texte et ajoute les informations de largeur et de hauteur pour créer des données de conditionnement spécifiquement pour les modèles PixArt Alpha. Il ne s'applique pas aux modèles PixArt Sigma.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `width` | La dimension de largeur pour le conditionnement de résolution (par défaut : 1024) | INT | Oui | 0 à MAX_RESOLUTION |
| `height` | La dimension de hauteur pour le conditionnement de résolution (par défaut : 1024) | INT | Oui | 0 à MAX_RESOLUTION |
| `text` | Entrée de texte à encoder. Prend en charge les entrées multilignes et les invites dynamiques. | STRING | Oui | - |
| `clip` | Modèle CLIP utilisé pour la tokenisation et l'encodage | CLIP | Oui | - |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `CONDITIONING` | Données de conditionnement encodées avec des jetons de texte et des informations de résolution | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/fr.md)

---
**Source fingerprint (SHA-256):** `d25a4117d39e3528cd0f64bc34462cd7b4076c67cb4e454c77fcc66490f89be6`
