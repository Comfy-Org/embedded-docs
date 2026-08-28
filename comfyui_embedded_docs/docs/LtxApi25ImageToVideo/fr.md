# LTX 2.5 Image vers Vidéo

Ce nœud génère une vidéo de qualité professionnelle à partir d'une image de départ à l'aide d'un modèle LTX 2.5. Vous décrivez le contenu de la vidéo avec une invite textuelle, sélectionnez une variante de modèle, et ajustez la durée, la résolution, la fréquence d'images et la génération audio. Une image finale facultative peut être fournie pour définir la fin de la vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `image` | Première image à utiliser pour la vidéo. | IMAGE | Oui | Exactement une image |
| `modèle` | Groupe de paramètres du modèle. Sélectionne la variante de modèle LTX 2.5 à utiliser. | COMBO | Oui | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `durée` | Durée de la vidéo générée en secondes. | INT | Oui | Entier |
| `résolution` | Résolution de la vidéo générée. Les options disponibles peuvent dépendre du modèle sélectionné. | COMBO | Oui | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `fps` | Fréquence d'images de la vidéo générée. | INT | Oui | Entier (défaut : 25) |
| `générer_audio` | Indique s'il faut générer l'audio de la vidéo. | BOOLEAN | Oui | True<br>False (défaut : True) |
| `prompt` | Description textuelle du contenu vidéo à générer. Doit contenir entre 1 et 10 000 caractères. | STRING | Oui | 1 à 10 000 caractères |
| `seed` | Valeur de graine (seed) pour une génération reproductible. Utiliser la même graine avec les mêmes paramètres produit le même résultat. | INT | Oui | Entier (défaut : 42) |
| `last_frame` | Dernière image à utiliser pour la vidéo. | IMAGE | Non | Exactement une image |

**Remarque :** Une seule image est prise en charge pour `image`. Si `last_frame` est fourni, il doit également contenir exactement une image. Les options disponibles pour `model.resolution` peuvent varier en fonction de la variante `model` sélectionnée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée à partir de l'image de départ et des paramètres de génération fournis. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/fr.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
