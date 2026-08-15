# HappyHorse Édition Vidéo

Modifiez une vidéo à l'aide d'instructions textuelles ou d'images de référence avec le modèle HappyHorse. La durée de sortie est de 3 à 15 secondes et correspond à la vidéo d'entrée ; les entrées de plus de 15 secondes sont tronquées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle de montage vidéo HappyHorse à utiliser. Cette sélection détermine les options de prompt, de résolution, de ratio et d'images de référence disponibles. | DICT | Oui | "happyhorse-1.0-video-edit" |
| `vidéo` | La vidéo à modifier. | VIDEO | Oui | 3 à 60 secondes |
| `graine` | Graine (seed) à utiliser pour la génération (par défaut : 0). | INT | Oui | 0 à 2147483647 |
| `filigrane` | Indique s'il faut ajouter un filigrane généré par IA au résultat (par défaut : False). | BOOLEAN | Non | True<br>False |

### happyhorse-1.0-video-edit Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Instructions de montage ou exigences de transfert de style. Doit comporter au moins 1 caractère. | STRING | Oui | - |
| `resolution` | La résolution de sortie. | STRING | Oui | "720P"<br>"1080P" |
| `ratio` | Ratio d'aspect. S'il n'est pas modifié, il se rapproche du ratio de la vidéo d'entrée. | STRING | Oui | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez de 0 à 5 images de référence (`image1`...`image5`) pour guider le montage. | IMAGE | Non | 0 à 5 images |

**Remarque :** La vidéo d'entrée doit durer de 3 à 60 secondes. La durée de sortie est de 3 à 15 secondes et correspond à la vidéo d'entrée ; les vidéos d'entrée de plus de 15 secondes sont tronquées. Le `prompt` doit comporter au moins 1 caractère.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo modifiée en sortie. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`
