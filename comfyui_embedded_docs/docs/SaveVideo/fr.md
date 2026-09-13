# Enregistrer la vidéo

Le nœud Save Video enregistre la vidéo d'entrée dans votre répertoire de sortie de ComfyUI. Vous pouvez choisir le préfixe du nom de fichier, le format de conteneur, le codec vidéo et les options d'encodage telles que la qualité. Le nœud génère automatiquement un nom de fichier unique à l'aide d'un compteur et peut intégrer les métadonnées du workflow dans le fichier enregistré.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `vidéo` | La vidéo à enregistrer. | VIDEO | Oui | - |
| `préfixe_nom_fichier` | Le préfixe du fichier à enregistrer. Il peut inclure des informations de formatage telles que `%date:yyyy-MM-dd%` ou `%Empty Latent Image.width%` pour inclure des valeurs provenant des nœuds (par défaut : `video/ComfyUI`). | STRING | Oui | - |
| `format` | Le conteneur de sortie. Auto utilise MP4 pour Auto/H.264 et WebM pour AV1. MP4, MKV et WebM sélectionnent un conteneur spécifique. La sélection d'un format détermine également quelles options de codec sont disponibles (par défaut : `auto`). | DYNAMIC_COMBO | Oui | `"auto"`<br>`"mp4"`<br>`"mkv"`<br>`"webm"` |
| `codec` | Le codec vidéo de sortie. Auto préserve un flux source compatible. Le réencodage H.264 et AV1 prend en charge SDR, HDR (HLG) et HDR PQ. Ce sélecteur est imbriqué sous le format choisi (par défaut : `auto`). | DYNAMIC_COMBO | Non | `"auto"`<br>`"h264"`<br>`"av1"` (non disponible avec le format `webm`) |

### Entrées H.264

Ces entrées apparaissent lorsque `codec` vaut `"h264"` et sont disponibles avec les formats `auto`, `mp4` et `mkv`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `encoding` | Le mode automatique préserve les flux H.264 compatibles. Re-encode applique des options d'encodage personnalisées. | DYNAMIC_COMBO | Non | `"auto"`<br>`"re-encode"` |
| `crf` | Des valeurs plus faibles produisent une qualité plus élevée et des fichiers plus volumineux. Apparaît lorsque `encoding` vaut `"re-encode"` (par défaut : 23.0). | FLOAT | Non | 0.0 à 51.0 |

### Entrées AV1

Ces entrées apparaissent lorsque `codec` vaut `"av1"` et sont disponibles avec les formats `auto`, `mp4`, `mkv` et `webm`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `encoding` | Le mode automatique préserve les flux AV1 compatibles. Re-encode applique des options d'encodage personnalisées. | DYNAMIC_COMBO | Non | `"auto"`<br>`"re-encode"` |
| `crf` | Des valeurs plus faibles produisent une qualité plus élevée et des fichiers plus volumineux. Apparaît lorsque `encoding` vaut `"re-encode"` (par défaut : 30.0). | FLOAT | Non | 0.0 à 63.0 |

Remarque : lorsque `format` vaut `"auto"`, le conteneur enregistré est choisi automatiquement : `av1` produit WebM, tandis que `auto` et `h264` produisent MP4. Le format `webm` n'autorise que les codecs `auto` et `av1`. Lorsque `codec` vaut `"auto"`, le flux vidéo source est préservé plutôt que réencodé. Le fichier enregistré utilise un suffixe de compteur pour éviter d'écraser les fichiers existants. L'extension de fichier est déterminée par le conteneur résolu. Les métadonnées du workflow (le prompt et les informations supplémentaires des nœuds) sont intégrées dans le fichier enregistré, sauf si l'enregistrement des métadonnées est désactivé au démarrage.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | La vidéo d'entrée, inchangée. | VIDEO |
| `ui` | Un aperçu du fichier vidéo enregistré, comprenant le chemin du fichier et les informations de sous-dossier pour l'affichage dans l'interface utilisateur. | PREVIEW_VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/fr.md)

---
**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`
