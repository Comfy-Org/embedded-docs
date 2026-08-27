# Wan 2.7 Édition Vidéo

Le nœud Wan2VideoEditApi utilise le modèle Wan 2.7 pour éditer une vidéo selon des instructions textuelles, des images de référence ou un transfert de style. Il traite la vidéo d’entrée et génère une nouvelle vidéo en fonction des paramètres spécifiés comme la résolution, la durée et le format d’image.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour l’édition vidéo. | DYNAMIC_COMBO | Oui | `"wan2.7-videoedit"` |
| `vidéo` | La vidéo à éditer. | VIDEO | Oui | - |
| `graine` | Graine à utiliser pour la génération. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `paramètre audio` | 'auto' : le modèle décide s’il doit régénérer l’audio en fonction de la invite. 'origin' : préserver l’audio original de la vidéo d’entrée. (défaut : "auto") | COMBO | Oui | `"auto"`<br>`"origin"` |
| `filigrane` | Indique s’il faut ajouter un filigrane généré par IA au résultat. (défaut : False) | BOOLEAN | Oui | - |

### wan2.7-videoedit Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Instructions d’édition ou exigences de transfert de style. (défaut : chaîne vide) | STRING | Oui | - |
| `resolution` | La résolution de la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `ratio` | Format d’image. S’il n’est pas modifié, se rapproche du format de la vidéo d’entrée. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durée de sortie en secondes. 'auto' correspond à la durée de la vidéo d’entrée. Une valeur spécifique tronque depuis le début de la vidéo. (défaut : "auto") | COMBO | Oui | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `reference_images` | Emplacement extensible : connectez 0 à 4 images (`image1`...`image4`) pour guider l’édition. La limite est de 4 pour le modèle wan2.7-videoedit. | IMAGE | Non | 0 à 4 éléments |

**Contraintes :**
*   La `prompt` doit contenir au moins 1 caractère.
*   La `video` d’entrée doit avoir une durée comprise entre 2 et 10 secondes.
*   L’emplacement extensible `reference_images` accepte un maximum de 4 images.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La vidéo éditée générée par le modèle. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `27283273ee56c90903db103a3e9bc17dc4df0914676c9aedd2a115b07937dc10`
