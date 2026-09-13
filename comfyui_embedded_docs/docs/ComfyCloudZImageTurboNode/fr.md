# Comfy Cloud Z-Image Turbo Texte vers image [BÊTA]

Ce nœud génère une image à partir d’une invite textuelle à l’aide du modèle Z-Image Turbo, qui se termine en seulement 8 étapes. La génération s’exécute à distance sur les GPU de Comfy Cloud et est facturée en fonction de sa durée d’exécution, ce qui en fait l’une des options les plus rapides et les moins coûteuses ici pour itérer sur des idées d’images. Une fois la génération terminée, le nœud télécharge l’image finale pour l’utiliser dans votre workflow. Ce nœud fait partie de l’ensemble de nœuds Comfy Cloud, marqué BÊTA : des options peuvent être ajoutées ou supprimées, et un workflow peut être retiré.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle décrivant l’image à générer. Accepte une saisie multiligne et est rognée avant la soumission. Ne doit pas être vide après rognage. Par défaut : "" (vide). | STRING | Oui | 1 - 4096 caractères |
| `seed` | Graine aléatoire utilisée pour contrôler la reproductibilité de la génération. La modifier produit une variation différente. Inclut une option de contrôle après génération. Par défaut : 42. | INT | Non | 0 - 18446744073709551615 |
| `aspect_ratio` | Rapport d’aspect de l’image générée. Par défaut : "1:1". | COMBO | Non | "1:1"<br>"3:4"<br>"2:3"<br>"3:2"<br>"4:3"<br>"16:9"<br>"9:16"<br>"21:9" |
| `megapixels` | Budget total de pixels. 1.0 correspond à environ 1024x1024 pour un format carré. Par défaut : 1.0. | FLOAT | Non | 0.1 - 16.0<br>(pas de 0.1) |

Remarque : les valeurs des entrées sont validées avant que la génération ne soit soumise. Le `prompt` doit contenir entre 1 et 4 096 caractères après suppression des espaces superflus, `aspect_ratio` doit être l’une des options listées, et `megapixels` doit être saisi par incréments de 0.1.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `IMAGE` | L’image générée renvoyée sous forme de tenseur d’image, prête pour d’autres nœuds de traitement ou d’enregistrement d’image. | IMAGE |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/fr.md)

---
**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`
