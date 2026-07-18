# Superposer du texte

Ce nœud dessine du texte par-dessus une image ou un lot d'images. Il prend en charge le texte personnalisé, la taille de police, la couleur, la position, l'alignement et un contour optionnel, en composant le texte sur l'image d'origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L'image d'entrée ou le lot d'images sur lequel dessiner le texte. | IMAGE | Oui | |
| `texte` | La chaîne de texte à superposer. Prend en charge les caractères de saut de ligne (`\n`) et de tabulation (`\t`). Par défaut : "" | STRING | Oui | |
| `taille_de_police` | Taille de police en pourcentage de la hauteur de l'image. Par défaut : 5.0 | FLOAT | Oui | 0.5 à 50.0 |
| `couleur` | Couleur du texte. Par défaut : "#ffffff" (blanc) | STRING | Oui | |
| `position` | Position verticale du texte sur l'image. Par défaut : "top" | COMBO | Oui | "top"<br>"bottom" |
| `alignement` | Alignement horizontal du texte. Par défaut : "left" | COMBO | Oui | "left"<br>"center"<br>"right" |
| `contour` | Dessine un contour noir autour du texte. Par défaut : Vrai | BOOLEAN | Oui | |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | L'image ou le lot d'images avec la superposition de texte composée par-dessus. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/fr.md)

---
**Source fingerprint (SHA-256):** `baffaa4ec9d3565e3533673658399271234def8c49e2e4a5f16767ec3f98cb22`
