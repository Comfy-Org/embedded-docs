# Recadrer la vidéo

Ce nœud recadre une vidéo sur une région rectangulaire définie en pixels, en conservant uniquement la zone située à l'intérieur de ce rectangle. Il enregistre un aperçu MP4 temporaire du résultat recadré et produit la vidéo recadrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | La vidéo source qui sera recadrée. | VIDEO | Oui | Toute vidéo |
| `crop` | Région de recadrage en pixels. Une largeur/hauteur nulle conserve l'image complète. Le rectangle de recadrage fournit les valeurs `x`, `y`, `width` et `height`, toutes avec une valeur par défaut de 0. | VIDEO_EDIT | Oui | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Toutes les valeurs ont 0 par défaut |

Remarque : La région de recadrage est décrite en coordonnées de pixels. Lorsque la largeur et la hauteur sont 0, aucun recadrage n'est appliqué et le nœud produit la vidéo d'entrée complète.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo recadrée sur la région rectangulaire sélectionnée. Lorsque la largeur et la hauteur de recadrage sont 0, la sortie correspond à la vidéo d'entrée complète. Le résultat recadré est également enregistré dans un fichier MP4 temporaire et affiché sous forme d'aperçu vidéo. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/fr.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
