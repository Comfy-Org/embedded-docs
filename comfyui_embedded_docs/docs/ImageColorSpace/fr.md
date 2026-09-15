# Convertir l’espace colorimétrique de l’image

Le nœud ImageColorSpace convertit les images entre les espaces colorimétriques sRGB (Rec.709), Rec.709 linéaire, HDR (Rec.2020 HLG) et HDR PQ (Rec.2020 PQ). Lors de la conversion vers une sortie SDR, ou de HDR PQ vers HDR, il effectue un mappage tonal de la luminance excédentaire sur l'ensemble du lot et compresse les couleurs hors gamut ; la sortie linéaire et les conversions linéaire vers HDR préservent les valeurs étendues sans mappage tonal. Les conversions sont calculées en float32, et tout canal alpha est transmis sans modification.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image d'entrée à convertir. | IMAGE | Oui | Toute image valide. |
| `source` | Espace colorimétrique des pixels d'entrée. Par défaut : "sRGB". | COMBO | Oui | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |
| `destination` | Espace colorimétrique des pixels de sortie. Définissez le nœud d'enregistrement sur ce même espace colorimétrique. Par défaut : "sRGB". | COMBO | Oui | `"sRGB"`<br>`"HDR"`<br>`"HDR PQ"`<br>`"linear"` |

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `image` | L'image convertie dans l'espace colorimétrique de destination spécifié. | IMAGE |

## Remarques

- Le linéaire 1,0 utilise le même blanc de référence de 203 nits que le sRGB ; le HLG utilise un affichage de référence de 1000 nits.
- La sortie linéaire et les conversions linéaire vers HDR préservent les valeurs étendues sans mappage tonal.
- La sortie SDR et la conversion PQ vers HLG effectuent un mappage tonal de la luminance excédentaire sur l'ensemble du lot (en partageant un point blanc afin que l'exposition ne change pas d'une image à l'autre) et compressent les couleurs hors gamut.
- Les conversions sont calculées en float32 et renvoient le périphérique et le dtype intermédiaires.
- L'alpha non prémultiplié n'est pas soumis à la transformation colorimétrique ; seuls les canaux RVB sont convertis.
- Si `source` et `destination` sont identiques, aucune transformation colorimétrique n'est appliquée — l'image est uniquement déplacée vers le périphérique et le dtype intermédiaires.

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorSpace/fr.md)

---
**Source fingerprint (SHA-256):** `04ae447a9f9805341e31755ad0fa56746ac0371fa2cb9bda95df3879c9dbead7`
