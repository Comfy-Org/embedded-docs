# Convert SDR to HDR

Le nœud **Convert SDR to HDR** étend les images sRGB à plage dynamique standard vers HDR Rec.2020 HLG. Il conserve l'aspect existant de l'image et mappe sa luminosité dans une plage plus large, le résultat doit donc être enregistré avec un espace colorimétrique HDR sélectionné. L'alpha est préservé tel quel.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | L'image ou les images SDR en sRGB à étendre vers HDR. | IMAGE | Oui | - |
| `algorithm` | Algorithme d'expansion HDR. La sélection d'un algorithme révèle ses paramètres (`target_luminance`). | DYNAMIC_COMBO | Oui | `"lottes"` |

### Entrées lottes

Ces paramètres apparaissent lorsque `algorithm` est défini sur `"lottes"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `target_luminance` | Cible de blanc crête en nits. 0 conserve le rendu calibré. Les images sombres ne sont pas normalisées sur ce pic. (par défaut : 650.0) | FLOAT | Oui | 0.0 à 10000.0 (incrément de 1.0) |

Chaque image du lot est convertie séparément : l'encodage sRGB est inversé en lumière linéaire, la luminosité est étendue à l'aide d'une courbe rationnelle de style Lottes mélangée à une courbe de gain logarithmique monotone calibrée, et le résultat est ré-encodé en Rec.2020 HLG. Comme la sortie est HDR, le nœud de sauvegarde doit utiliser l'espace colorimétrique `HDR` ; l'enregistrer en sRGB rend la luminosité incorrecte.

HLG suppose un écran de référence à 1000 nits, donc les valeurs de `target_luminance` inférieures à 1000 conservent cette référence et une valeur de `0` laisse le rendu calibré intact. Les images monocanal sont étendues à trois canaux avant la conversion, et le canal alpha est copié sans modification.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image ou les images HDR Rec.2020 HLG. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSDRToHDR/fr.md)

---
**Source fingerprint (SHA-256):** `51eb0beac3d48345a30ba66d80d95873384cf5155fc06c33353b6d1dc029658a`
