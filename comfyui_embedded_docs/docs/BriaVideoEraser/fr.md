# BriaVideoEraser

Efface d’une vidéo, avec Bria, tout ce que couvre un masque image par image, puis comble le vide. Le masque doit être blanc sur ce qui doit être supprimé et noir partout ailleurs. Bria accepte des clips d’au plus 5,1 secondes à 20 à 30 images par seconde avec des dimensions en pixels paires ; l’audio est conservé par défaut. Le clip renvoyé peut être plus court de quelques images que l’entrée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `video` | Clip dans lequel effectuer l’effacement. | VIDEO | Oui | - |
| `mask` | Un masque par image de la vidéo, blanc là où se trouve l’objet à effacer. Fournissez soit un masque, soit une vidéo de masque, pas les deux. | MASK | Non | - |
| `mask_video` | Une vidéo de masque déjà encodée, avec les mêmes dimensions et le même nombre d’images que la vidéo. Fournissez soit un masque, soit une vidéo de masque, pas les deux. | VIDEO | Non | - |
| `preserve_audio` | Conserver la piste audio de l’entrée. Par défaut : true. | BOOLEAN | Non | `true`<br>`false` |

**Remarques sur les contraintes :**

- Exactement l’un des paramètres `mask` ou `mask_video` doit être connecté. Une erreur est levée si aucun n’est fourni, ou si les deux le sont.
- La vidéo doit durer au maximum 5,1 secondes et avoir une fréquence de 20 à 30 images par seconde. Réajustez la temporisation du clip avec Get Video Components et Create Video si nécessaire.
- La vidéo doit avoir des dimensions en pixels paires (largeur et hauteur divisibles par 2). Sinon, recadrez-la ou redimensionnez-la d’abord.
- Lorsque vous utilisez `mask`, il doit contenir une image de masque par image de vidéo, et son rapport d’aspect doit correspondre à celui de la vidéo. Les masques sont binarisés à 50 % : les zones peintes avec une opacité inférieure à la moitié sont ignorées, et un masque vide déclenche une erreur. Si la résolution du masque diffère de celle de la vidéo, elle est redimensionnée aux dimensions de la vidéo.
- Lorsque vous utilisez `mask_video`, celle-ci doit avoir les mêmes dimensions et le même nombre d’images que la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le clip modifié, avec les zones masquées effacées et les vides comblés. La sortie peut être plus courte de quelques images que le clip d’entrée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoEraser/fr.md)

---
**Source fingerprint (SHA-256):** `525b90013b9d9ea4b224caf1f32479493c96f90e28acbf3cf7a4d16a6ca91a45`
