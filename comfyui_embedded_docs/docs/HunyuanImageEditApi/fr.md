# Tencent HY Image: Edit

Le nœud Tencent HY Image: Edit modifie ou combine des images de référence à partir d’une instruction textuelle avec le modèle Hunyuan Image de Tencent. Connectez une à cinq images, décrivez la modification dans le prompt et faites référence aux images sous la forme `@Image1`, `@Image2`, etc. Le nœud téléverse les images de référence, envoie la requête à l’API et renvoie le résultat édité.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle utilisé pour l’édition. Le modèle sélectionné détermine quelles entrées supplémentaires sont affichées. | DYNAMIC_COMBO | Oui | `"hy-image-3.5-preview"` |

### Entrées hy-image-3.5-preview

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Les instructions d’édition. Prend en charge les références de style `@Image1` vers les images connectées. Ne doit pas être vide (valeur par défaut : vide). | STRING | Oui | N’importe quel texte |
| `aspect_ratio` | Rapport d’aspect de la sortie. `"auto"` suit le rapport d’aspect de la première image de référence et n’est pas disponible en 4K. Ignoré lorsque `resolution` est `"custom"`. | COMBO | Oui | `"auto"`<br>`"1:1"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"16:9"`<br>`"9:16"`<br>`"21:9"`<br>`"9:21"` (valeur par défaut : `"auto"`) |
| `resolution` | Surface en pixels de la sortie : 1K correspond à environ 1024x1024, 2K à environ 2048x2048 et 4K à environ 4096x4096. Tout ce qui dépasse 2K est rendu en 2K puis mis à l’échelle par le modèle. Définissez sur `"custom"` pour utiliser `width` et `height` au lieu d’une surface prédéfinie. | COMBO | Oui | `"1K"`<br>`"2K"`<br>`"4K"`<br>`"custom"` (valeur par défaut : `"2K"`) |
| `width` | Largeur de la sortie en pixels. Utilisée uniquement lorsque `resolution` est `"custom"`. | INT | Oui | 256-8192, pas de 16 (valeur par défaut : 2048) |
| `height` | Hauteur de la sortie en pixels. Utilisée uniquement lorsque `resolution` est `"custom"`. | INT | Oui | 256-8192, pas de 16 (valeur par défaut : 2048) |
| `seed` | Graine utilisée pour la génération. Les résultats varient encore entre les exécutions avec la même graine. | INT | Oui | 0-2147483647 (valeur par défaut : 42) |
| `reference_detail` | Niveau de détail des images de référence que le modèle voit : `"standard"` autorise jusqu’à 1024x1024 pixels par image, `"high"` jusqu’à 2048x2048 et préserve mieux les petits textes et les détails fins, mais prend plus de temps. Il s’agit d’un paramètre avancé. | COMBO | Non | `"standard"`<br>`"high"` (valeur par défaut : `"standard"`) |
| `watermark` | Indique s’il faut ajouter un filigrane généré par IA au résultat. Il s’agit d’un paramètre avancé. | BOOLEAN | Non | true<br>false (valeur par défaut : false) |

### Entrées de référence

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `images` | Les images de référence à éditer ou à combiner. Emplacement extensible : connectez 1 à 5 images (`image_1` à `image_5`). Faites-y référence dans le prompt sous la forme `@Image1` ... `@Image5`, numérotées dans l’ordre d’entrée ; une entrée par lot compte une fois par image. | IMAGE | Oui | 1-5 images |

`prompt` ne doit pas être vide, et une référence dans le prompt telle que `@Image3` déclenche une erreur lorsque seules 1 ou 2 images sont connectées. Au maximum, 5 images de référence peuvent être utilisées au total, en comptant séparément chaque image d’un lot. Avec la résolution `"custom"`, `width` et `height` doivent tous deux être des multiples de 16 et leur produit ne doit pas dépasser la limite de surface de 4096 x 4096 pixels (environ 16,7 mégapixels) ; n’importe quel rapport d’aspect fonctionne, bien qu’au-delà d’environ 6:1 le modèle commence à répéter le sujet. Le rapport d’aspect `"auto"` ne fonctionne que dans la limite de surface 2K, donc en 4K choisissez un rapport d’aspect explicite ou utilisez `"custom"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image éditée produite à partir des images de référence et du prompt. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageEditApi/fr.md)

---
**Source fingerprint (SHA-256):** `46c112347b51a2983521f87bbeb047289515f4073c48ba5d909fd3bae4597633`
