> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/fr.md)

Générer une image à l'aide d'une image de contrôle (canny). Ce nœud prend une image de contrôle et génère une nouvelle image basée sur le prompt fourni, tout en suivant la structure des contours détectée dans l'image de contrôle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `control_image` | IMAGE | Oui | - | L'image d'entrée utilisée pour le contrôle par détection de contours Canny |
| `prompt` | STRING | Non | - | Prompt pour la génération de l'image (par défaut : chaîne vide) |
| `prompt_upsampling` | BOOLEAN | Non | - | Indique s'il faut effectuer un sur-échantillonnage du prompt. Si activé, modifie automatiquement le prompt pour une génération plus créative, mais les résultats sont non déterministes (une même graine ne produira pas exactement le même résultat). (par défaut : False) |
| `canny_low_threshold` | FLOAT | Non | 0,01 - 0,99 | Seuil bas pour la détection de contours Canny ; ignoré si `skip_preprocessing` est True (par défaut : 0,1) |
| `canny_high_threshold` | FLOAT | Non | 0,01 - 0,99 | Seuil haut pour la détection de contours Canny ; ignoré si `skip_preprocessing` est True (par défaut : 0,4) |
| `skip_preprocessing` | BOOLEAN | Non | - | Indique s'il faut ignorer le prétraitement ; définir sur True si `control_image` est déjà une image canny, False s'il s'agit d'une image brute. (par défaut : False) |
| `guidance` | FLOAT | Non | 1 - 100 | Force d'orientation pour le processus de génération d'image (par défaut : 30) |
| `steps` | INT | Non | 15 - 50 | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) |
| `seed` | INT | Non | 0 - 18446744073709551615 | La graine aléatoire utilisée pour créer le bruit. (par défaut : 0) |

**Remarque :** Lorsque `skip_preprocessing` est défini sur True, les paramètres `canny_low_threshold` et `canny_high_threshold` sont ignorés, car l'image de contrôle est supposée être déjà traitée comme une image de contours Canny. L'image `control_image` est alors utilisée directement comme image prétraitée.

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `output_image` | IMAGE | L'image générée à partir de l'image de contrôle et du prompt |

---
**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`
