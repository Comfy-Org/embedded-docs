# PixVerse Image vers Vidéo

Génère une vidéo à partir d'une image fixe et d'un prompt textuel à l'aide de PixVerse. Le nœud téléverse l'image d'entrée, applique les paramètres de qualité, de durée et de mouvement sélectionnés, puis renvoie la vidéo résultante une fois la génération terminée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Image d'entrée à transformer en vidéo | IMAGE | Oui | - |
| `prompt` | Prompt pour la génération vidéo (par défaut : chaîne vide) | STRING | Oui | - |
| `qualité` | Réglage de la qualité vidéo (par défaut : res_540p) | COMBO | Oui | `res_540p`<br>`res_1080p` |
| `durée_secondes` | Durée de la vidéo générée en secondes | COMBO | Oui | `dur_2`<br>`dur_5`<br>`dur_10` |
| `mode_mouvement` | Style de mouvement appliqué à la génération vidéo | COMBO | Oui | `normal`<br>`fast`<br>`slow`<br>`zoom_in`<br>`zoom_out`<br>`pan_left`<br>`pan_right`<br>`pan_up`<br>`pan_down`<br>`tilt_up`<br>`tilt_down`<br>`roll_clockwise`<br>`roll_counterclockwise` |
| `graine` | Graine pour la génération vidéo (par défaut : 0) | INT | Oui | 0-2147483647 |
| `prompt_négatif` | Description textuelle facultative des éléments indésirables dans une image (par défaut : chaîne vide) | STRING | Non | - |
| `modèle_pixverse` | Modèle facultatif pour influencer le style de génération, créé par le nœud PixVerse Template | CUSTOM | Non | - |

**Remarque :** Lors de l'utilisation de la qualité 1080p, le mode de mouvement est automatiquement défini sur `normal` et la durée est limitée à 5 secondes. Pour les durées autres que 5 secondes, le mode de mouvement est également automatiquement défini sur `normal`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Vidéo générée à partir de l'image d'entrée et des paramètres | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`
