# VideoCrop

Ce nœud recadre une vidéo sur une zone rectangulaire sélectionnée, en ne conservant que la partie située à l'intérieur de ce rectangle. Il crée également un aperçu de la vidéo recadrée afin que vous puissiez visualiser le résultat. Si la largeur et la hauteur de recadrage sont nulles, la vidéo entière est conservée sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | La vidéo source qui sera recadrée. | VIDEO | Oui | Toute vidéo |
| `crop` | Zone de recadrage en pixels. Une largeur ou une hauteur nulle conserve l'image complète. Le rectangle de recadrage fournit les valeurs `x`, `y`, `width` et `height`, toutes avec une valeur par défaut de 0. | VIDEO_EDIT | Oui | `x` ≥ 0<br>`y` ≥ 0<br>`width` ≥ 0<br>`height` ≥ 0<br>Toutes les valeurs ont 0 pour valeur par défaut |

Remarque : La zone de recadrage est décrite en coordonnées de pixels. Lorsque la largeur et la hauteur sont à 0, aucun recadrage n'est appliqué et le nœud renvoie la vidéo d'entrée complète.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo recadrée sur la zone rectangulaire sélectionnée. Lorsque la largeur et la hauteur de recadrage sont à 0, la sortie est la vidéo d'entrée complète. Le résultat recadré est également enregistré sous forme de fichier MP4 temporaire et affiché comme aperçu vidéo. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoCrop/fr.md)

---
**Source fingerprint (SHA-256):** `0c4ebd51027669fc232fe42a5e8840b5e4e95083b6794cd7b4c43123ddc0341b`
