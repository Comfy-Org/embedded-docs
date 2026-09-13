# Wan 2.7 Édition Vidéo

Le nœud Wan 2.7 Video Edit édite une vidéo à l'aide d'instructions textuelles, d'images de référence ou d'un transfert de style. Il envoie la vidéo d'entrée (ainsi que toute image de référence) au service d'édition vidéo Wan 2.7 et renvoie une vidéo nouvellement générée selon les paramètres de résolution, de rapport d'aspect et de durée choisis.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle à utiliser pour l'édition vidéo. Chaque option expose son propre ensemble de sous-paramètres. | DYNAMIC_COMBO | Oui | `"wan2.7-videoedit"` |
| `video` | La vidéo à éditer. | VIDEO | Oui | - |
| `seed` | Graine à utiliser pour la génération. (par défaut : 0) | INT | Oui | 0 à 2147483647 |
| `audio_setting` | 'auto' : le modèle décide s'il faut régénérer l'audio en fonction du prompt. 'origin' : conserver l'audio d'origine de la vidéo d'entrée. (par défaut : "auto") | COMBO | Oui | `"auto"`<br>`"origin"` |
| `watermark` | Indique s'il faut ajouter un filigrane généré par IA au résultat. (par défaut : False) | BOOLEAN | Oui | - |

### Entrées wan2.7-videoedit

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Instructions d'édition ou exigences de transfert de style. (par défaut : chaîne vide) | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Rapport d'aspect. S'il n'est pas modifié, il s'approche du rapport de la vidéo d'entrée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durée de sortie en secondes. 'auto' correspond à la durée de la vidéo d'entrée. Une valeur spécifique tronque à partir du début de la vidéo. (par défaut : "auto") | COMBO | Oui | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez de 0 à 4 images (`image1`...`image4`) pour guider l'édition. La limite du nombre est de 4 pour le modèle wan2.7-videoedit. | IMAGE | Non | 0 à 4 items |

**Contraintes :**
*   `audio_setting` et `watermark` sont des options avancées.
*   Le `prompt` doit contenir au moins 1 caractère.
*   La `video` d'entrée doit avoir une durée comprise entre 2 et 10 secondes.
*   L'emplacement extensible `reference_images` accepte un maximum de 4 images.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo éditée générée par le modèle. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
