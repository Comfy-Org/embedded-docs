# Convertir l’espace colorimétrique de l’image

Le nœud ImageColorSpace convertit les images entre les espaces colorimétriques sRGB (Rec.709), Rec.709 linéaire, HDR (Rec.2020 HLG), HDR PQ (Rec.2020 PQ), HDR LogC3, ACEScg linéaire et HDR ACEScct. LogC3 utilise la courbe EI 800 avec les primaires Rec.709 et des codes bornés à [0, 1] ; ACEScg est un AP1 scène-linéaire à blanc D60, dont ACEScct est l'encodage logarithmique, tous deux adaptés à D65 par la transformation de Bradford. Lors d'une conversion vers une sortie SDR, ou de HDR PQ vers HDR, il applique un mappage tonal à la luminance excédentaire sur l'ensemble du lot et compresse les couleurs hors gamut ; les sorties linéaires, ACEScg et ACEScct, ainsi que les conversions linéaire vers HDR, préservent les valeurs étendues. Les sorties HLG et PQ écrêtent les canaux négatifs. Les conversions sont calculées en float32, et tout canal alpha est transmis sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à convertir. | IMAGE | Oui | Toute image valide. |
| `source` | Espace colorimétrique des pixels d'entrée. Par défaut : "sRGB". | COMBO | Oui | `"sRGB"`<br>`"HDR"`<br>`"HDR ACEScct"`<br>`"HDR LogC3"`<br>`"HDR PQ"`<br>`"linear"`<br>`"linear ACEScg"` |
| `destination` | Espace colorimétrique des pixels de sortie. Définissez le nœud de sauvegarde sur ce même espace colorimétrique. Convertissez LogC3 ou ACEScct en ACEScg linéaire avant d'enregistrer un EXR ACEScg, en linéaire avant d'enregistrer un EXR Rec.709, ou en sRGB/HDR/HDR PQ avant d'enregistrer une vidéo. Par défaut : "sRGB". | COMBO | Oui | `"sRGB"`<br>`"HDR"`<br>`"HDR ACEScct"`<br>`"HDR LogC3"`<br>`"HDR PQ"`<br>`"linear"`<br>`"linear ACEScg"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image convertie dans l'espace colorimétrique de destination spécifié. | IMAGE |

## Remarques

- La valeur linéaire 1.0 et ACEScg 1.0 utilisent le même blanc de référence de 203 nits que sRGB ; HLG utilise un affichage de référence de 1000 nits.
- Les sorties linéaires, ACEScg et ACEScct préservent les valeurs étendues ; les conversions linéaire vers HDR préservent les hautes lumières sans mappage tonal.
- La sortie SDR et la conversion PQ vers HLG appliquent un mappage tonal à la luminance excédentaire sur l'ensemble du lot (en partageant un même point blanc afin que l'exposition ne change pas d'une image à l'autre) et compressent les couleurs hors gamut. Les sorties HLG et PQ écrêtent les canaux négatifs.
- Les conversions sont calculées en float32 et renvoient l'appareil et le dtype intermédiaires.
- LogC3 et ACEScct sont des encodages log de caméra : convertissez-les en ACEScg linéaire (AP1) pour un EXR ACEScg, en linéaire (Rec.709) pour un EXR Rec.709, ou en sRGB/HDR/HDR PQ avant d'enregistrer une vidéo.
- L'alpha non prémultiplié (straight alpha) n'est pas transformé colorimétriquement ; seuls les canaux RGB sont convertis.
- Si `source` et `destination` sont identiques, aucune transformation colorimétrique n'est appliquée — l'image est uniquement déplacée vers l'appareil et le dtype intermédiaires.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/fr.md)

---
**Source fingerprint (SHA-256):** `cbb3452e6844985580d5b91c6b1cbfbd770307cda6c92aba8b21c9bdd45ae370`
