> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/fr.md)

Voici la traduction en français de la documentation technique du nœud ComfyUI `CLIPTextEncodePixArtAlpha` :

---

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodePixArtAlpha/en.md)

Encode le texte et définit le conditionnement de résolution pour PixArt Alpha. Ce nœud traite les entrées textuelles et ajoute les informations de largeur et de hauteur pour créer des données de conditionnement spécifiquement destinées aux modèles PixArt Alpha. Il ne s'applique pas aux modèles PixArt Sigma.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `width` | INT | Oui | 0 à MAX_RESOLUTION | La dimension de largeur pour le conditionnement de résolution (par défaut : 1024) |
| `height` | INT | Oui | 0 à MAX_RESOLUTION | La dimension de hauteur pour le conditionnement de résolution (par défaut : 1024) |
| `text` | STRING | Oui | - | Texte à encoder, prend en charge les entrées multilignes et les invites dynamiques |
| `clip` | CLIP | Oui | - | Modèle CLIP utilisé pour la tokenisation et l'encodage |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CONDITIONING` | CONDITIONING | Données de conditionnement encodées avec les tokens de texte et les informations de résolution |

---
**Source fingerprint (SHA-256):** `d15df3c7bcca10ec85f0689d6631a6b89aa89e609193c36b658b1bc97f90ee9a`
