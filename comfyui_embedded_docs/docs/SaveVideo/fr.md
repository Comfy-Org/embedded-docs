# Enregistrer la vidéo

Le nœud SaveVideo enregistre une vidéo d’entrée dans votre répertoire de sortie ComfyUI. Il permet de choisir le préfixe du nom de fichier, le format vidéo et le codec, et il crée automatiquement un nom de fichier unique en ajoutant un compteur. Par défaut, le nœud stocke également les métadonnées du workflow dans la vidéo enregistrée.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `codec` | Le codec à utiliser pour la vidéo. Sélectionner `h264` révèle des options d’encodage supplémentaires (défaut : « auto »). | DYNAMIC_COMBO | Oui | "auto"<br>"h264" |
| `video` | La vidéo à enregistrer. | VIDEO | Oui | - |
| `filename_prefix` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (défaut : « video/ComfyUI »). | STRING | Oui | - |
| `format` | Le format d’enregistrement de la vidéo. Il détermine l’extension de fichier de la vidéo enregistrée (défaut : « auto »). | COMBO | Oui | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### Entrées h264

Ces entrées apparaissent lorsque `codec` est défini sur `h264`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `encoding` | Le mode d’encodage pour H.264. Le mode automatique préserve les flux H.264 compatibles. Le mode ré-encodage applique un CRF personnalisé (défaut : « auto »). | DYNAMIC_COMBO | Non | "auto"<br>"re-encode" |
| `crf` | Des valeurs plus faibles produisent une qualité supérieure et des fichiers plus volumineux. Disponible uniquement lorsque `encoding` est défini sur `re-encode` (défaut : 23.0). | FLOAT | Oui (uniquement lorsque `encoding` est `re-encode`) | 0.0 à 51.0 (pas : 1.0) |

Remarque : Si le `filename_prefix` inclut des dossiers, par exemple `video/ComfyUI`, la vidéo est enregistrée dans ce sous-dossier du répertoire de sortie. Le nom de fichier est créé à partir du préfixe avec un compteur ajouté, par exemple `ComfyUI_00001_.mp4`, afin que les fichiers existants ne soient pas écrasés.

Remarque : Lorsque les métadonnées sont activées, le nœud intègre le prompt du workflow et des métadonnées supplémentaires dans la vidéo enregistrée. Les métadonnées peuvent être désactivées en démarrant ComfyUI avec l’argument `--disable-metadata`.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo qui a été enregistrée, transmise depuis l’entrée. | VIDEO |
| `ui` | Un aperçu du fichier vidéo enregistré, y compris le chemin d’accès et les informations de sous-dossier pour l’affichage dans l’interface utilisateur. | PREVIEW_VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/fr.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
