# Tencent HY Image: Text to Image

Le nœud Tencent HY Image: Text to Image génère une image à partir d'une description textuelle avec le modèle Hunyuan Image de Tencent. Le prompt est envoyé à l'API, qui le réécrit et l'enrichit avant le rendu, et l'image finale est renvoyée sous forme de lot d'images.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `model` | Le modèle utilisé pour la génération. Le modèle sélectionné détermine quelles entrées supplémentaires sont affichées. | DYNAMIC_COMBO | Oui | `"hy-image-3.5-preview"` |

### Entrées hy-image-3.5-preview

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `prompt` | Décrit l'image à générer. Le modèle le réécrit et l'enrichit avant le rendu. Ne doit pas être vide (par défaut : vide). | STRING | Oui | Tout texte |
| `aspect_ratio` | Rapport d'aspect de la sortie. `"auto"` laisse le modèle choisir le ratio à partir du prompt et n'est pas disponible en 4K. Ignoré lorsque `resolution` vaut `"custom"`. | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (par défaut : `"auto"`) |
| `resolution` | Surface en pixels de l'image : 1K correspond à environ 1024x1024, 2K à environ 2048x2048 et 4K à environ 4096x4096. Tout ce qui dépasse 2K est rendu en 2K puis mis à l'échelle par le modèle. Défini sur `"custom"` pour utiliser `width` et `height` au lieu d'une surface prédéfinie. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (par défaut : `"2K"`) |
| `width` | Largeur de l'image en pixels. Utilisée uniquement lorsque `resolution` vaut `"custom"`. | INT | Oui | 256-8192, pas de 16 (par défaut : 2048) |
| `height` | Hauteur de l'image en pixels. Utilisée uniquement lorsque `resolution` vaut `"custom"`. | INT | Oui | 256-8192, pas de 16 (par défaut : 2048) |
| `seed` | Graine utilisée pour la génération. Les résultats varient toujours entre les exécutions avec la même graine. | INT | Oui | 0-2147483647 (par défaut : 42) |
| `watermark` | Indique s'il faut ajouter un filigrane généré par IA au résultat. Il s'agit d'un paramètre avancé. | BOOLEAN | Non | true<br>false (par défaut : false) |

`prompt` ne doit pas être vide. Avec la résolution `"custom"`, `width` et `height` doivent tous deux être des multiples de 16 et leur produit ne doit pas dépasser la limite de surface de 4096 x 4096 pixels (environ 16,7 mégapixels) ; n'importe quel rapport d'aspect fonctionne, bien qu'au-delà d'environ 6:1 le modèle commence à répéter le sujet. Le rapport d'aspect `"auto"` nécessite que le modèle choisisse une taille, il ne fonctionne donc que dans la limite de surface 2K : en 4K, choisissez un rapport d'aspect explicite ou utilisez `"custom"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L'image générée. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageTextToImageApi/fr.md)

---
**Source fingerprint (SHA-256):** `1d4e70d688c5aa4e79b81447da559e201078454077da34769f2a4f544fbba63f`
