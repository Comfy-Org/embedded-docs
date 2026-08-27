# Enregistrer la vidéo

Le nœud Save Video enregistre la vidéo d'entrée dans votre répertoire de sortie ComfyUI. Vous pouvez choisir le préfixe du nom de fichier, le format de conteneur, le codec vidéo et les options d'encodage telles que la qualité et l'espace colorimétrique. Le nœud gère automatiquement la dénomination des fichiers avec des incréments de compteur et peut intégrer les métadonnées du workflow dans le fichier enregistré.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | La vidéo à enregistrer. | VIDEO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant de nœuds (par défaut : "video/ComfyUI"). | STRING | Oui | - |
| `format` | Le conteneur de sortie. Auto préserve le conteneur source lorsque c'est possible ; MP4, MKV et WebM sélectionnent un conteneur spécifique (par défaut : "auto"). | DYNAMIC_COMBO | Oui | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Le codec vidéo de sortie. Auto préserve un flux source compatible. Le ré-encodage H.264 et AV1 prend en charge SDR, HDR (HLG) et HDR PQ. Apparaît lorsqu'un format est sélectionné (par défaut : "auto"). | DYNAMIC_COMBO | Non | `"auto"`<br>`"h264"`<br>`"av1"` |

### Entrées H.264

Ces entrées apparaissent lorsque `codec` est `"h264"`. Ce codec est disponible avec les formats `auto`, `mp4` et `mkv`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `encoding` | Le mode automatique préserve les flux H.264 compatibles. Le mode Re-encode applique des options d'encodage personnalisées. | DYNAMIC_COMBO | Non | `"auto"`<br>`"re-encode"` |
| `crf` | Des valeurs plus faibles produisent une qualité supérieure et des fichiers plus volumineux. Apparaît lorsque `encoding` est `"re-encode"` (par défaut : 23.0). | FLOAT | Non | 0.0 à 51.0 |
| `color_space` | Auto utilise sRGB pour les vidéos créées à partir d'images et préserve les couleurs reconnues sur les vidéos chargées. sRGB écrit en SDR BT.709/sRGB. HDR écrit en 10 bits BT.2020/HLG ; HDR PQ écrit en BT.2020/PQ. Les autres pixels d'entrée doivent déjà utiliser l'espace colorimétrique sélectionné. Apparaît lorsque `encoding` est `"re-encode"` (par défaut : "auto"). | COMBO | Non | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

### Entrées AV1

Ces entrées apparaissent lorsque `codec` est `"av1"`. Ce codec est disponible avec les formats `auto`, `mp4`, `mkv` et `webm`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `encoding` | Le mode automatique préserve les flux AV1 compatibles. Le mode Re-encode applique des options d'encodage personnalisées. | DYNAMIC_COMBO | Non | `"auto"`<br>`"re-encode"` |
| `crf` | Des valeurs plus faibles produisent une qualité supérieure et des fichiers plus volumineux. Apparaît lorsque `encoding` est `"re-encode"` (par défaut : 30.0). | FLOAT | Non | 0.0 à 63.0 |
| `color_space` | Auto utilise sRGB pour les vidéos créées à partir d'images et préserve les couleurs reconnues sur les vidéos chargées. sRGB écrit en SDR BT.709/sRGB. HDR écrit en 10 bits BT.2020/HLG ; HDR PQ écrit en BT.2020/PQ. Les autres pixels d'entrée doivent déjà utiliser l'espace colorimétrique sélectionné. Apparaît lorsque `encoding` est `"re-encode"` (par défaut : "auto"). | COMBO | Non | `"auto"`<br>`"sRGB"`<br>`"HDR"`<br>`"HDR PQ"` |

Remarque : Le format `webm` ne prend en charge que les codecs `auto` et `av1`. Lorsque `format` est `"auto"`, le conteneur source est préservé lorsque c'est possible. Lorsque `color_space` est `"auto"`, aucun espace colorimétrique explicite n'est appliqué et l'espace colorimétrique est déterminé automatiquement.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `vidéo` | La vidéo d'entrée, inchangée. | VIDEO |
| `ui` | Un aperçu du fichier vidéo enregistré, comprenant le chemin du fichier et les informations de sous-dossier pour l'affichage dans l'interface. | PREVIEW_VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/fr.md)

---
**Source fingerprint (SHA-256):** `39b168eab2d6798adfec6ace3d4320f26217d893844ba54e62041cfdf0183e6f`
