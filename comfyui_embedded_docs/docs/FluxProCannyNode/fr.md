> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/fr.md)

Générer une image en utilisant une image de contrôle (canny). Ce nœud prend une image de contrôle et génère une nouvelle image basée sur l'invite fournie tout en suivant la structure des contours détectés dans l'image de contrôle.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `control_image` | IMAGE | Oui | - | L'image d'entrée utilisée pour le contrôle par détection de contours Canny |
| `prompt` | STRING | Non | - | Invite pour la génération d'image (par défaut : chaîne vide) |
| `prompt_upsampling` | BOOLEAN | Non | - | Indique s'il faut effectuer un suréchantillonnage sur l'invite. Si actif, modifie automatiquement l'invite pour une génération plus créative, mais les résultats sont non déterministes (la même graîne ne produira pas exactement le même résultat). (par défaut : Faux) |
| `canny_low_threshold` | FLOAT | Non | 0.01 - 0.99 | Seuil bas pour la détection de contours Canny ; ignoré si skip_processing est Vrai (par défaut : 0.1) |
| `canny_high_threshold` | FLOAT | Non | 0.01 - 0.99 | Seuil haut pour la détection de contours Canny ; ignoré si skip_processing est Vrai (par défaut : 0.4) |
| `skip_preprocessing` | BOOLEAN | Non | - | Indique s'il faut ignorer le prétraitement ; définir sur Vrai si control_image est déjà traitée en contours Canny, Faux s'il s'agit d'une image brute. (par défaut : Faux) |
| `guidance` | FLOAT | Non | 1 - 100 | Intensité de guidage pour le processus de génération d'image (par défaut : 30) |
| `steps` | INT | Non | 15 - 50 | Nombre d'étapes pour le processus de génération d'image (par défaut : 50) |
| `seed` | INT | Non | 0 - 18446744073709551615 | La graîne aléatoire utilisée pour créer le bruit. (par défaut : 0) |

**Note :** Lorsque `skip_preprocessing` est défini sur Vrai, les paramètres `canny_low_threshold` et `canny_high_threshold` sont ignorés car l'image de contrôle est supposée être déjà traitée comme une image de contours Canny.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `output_image` | IMAGE | L'image générée basée sur l'image de contrôle et l'invite |