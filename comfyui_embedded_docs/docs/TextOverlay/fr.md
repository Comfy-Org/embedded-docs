# Superposer du texte

Ce nœud dessine du texte par-dessus une image ou un lot d’images. Il crée une superposition de texte en utilisant une taille de police, une couleur, une position verticale, un alignement horizontal et un contour noir facultatif configurables, puis combine la superposition avec les pixels de l’image d’origine.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | L’image d’entrée ou le lot d’images sur lequel dessiner le texte | IMAGE | Oui | |
| `texte` | Le texte à superposer sur l’image (par défaut : ""). Prend en charge plusieurs lignes : les séquences d’échappement `\n` et `\t` sont converties en retours à la ligne et tabulations, et les lignes longues sont automatiquement mises à la ligne pour tenir dans la largeur de l’image. | STRING | Oui | |
| `taille_de_police` | Taille de police en pourcentage de la hauteur de l’image (par défaut : 5.0) | FLOAT | Oui | 0.5 à 50.0 (pas de 0.5) |
| `couleur` | Couleur du texte (par défaut : "#ffffff") | COLOR | Oui | |
| `position` | Position verticale du texte sur l’image (par défaut : "top") | COMBO | Oui | "top"<br>"bottom" |
| `alignement` | Alignement horizontal du texte (par défaut : "left") | COMBO | Oui | "left"<br>"center"<br>"right" |
| `contour` | Dessiner un contour noir autour du texte (par défaut : True) | BOOLEAN | Oui | |

Remarque : Si `text` est vide ou ne contient que des espaces, le nœud renvoie les images d’entrée inchangées. La superposition de texte est rendue une seule fois et appliquée à chaque image du lot. Si le bloc de texte rendu est plus haut que la zone d’image disponible, la taille de police est réduite automatiquement jusqu’à ce qu’il tienne ou atteigne une taille minimale.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `images` | Les images d’entrée avec la superposition de texte composée par-dessus | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/fr.md)

---
**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`
