> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/fr.md)

Ce nœud génère une vidéo en interpolant entre une image de départ et une image de fin fournies, guidé par une description textuelle. Il utilise le modèle Vidu Q3 pour créer une transition fluide entre les deux images, produisant une vidéo d'une durée et d'une résolution spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` | Le modèle à utiliser pour la génération de vidéo. La sélection d'une option révèle des paramètres de configuration supplémentaires pour `resolution`, `duration` et `audio`. |
| `model.resolution` | COMBO | Oui | `"720p"`<br>`"1080p"` | Résolution de la vidéo en sortie. Ce paramètre est révélé après avoir sélectionné un `model`. |
| `model.duration` | INT | Oui | 1 à 16 | Durée de la vidéo en sortie en secondes (par défaut : 5). Ce paramètre est révélé après avoir sélectionné un `model`. |
| `model.audio` | BOOLEAN | Oui | `True` / `False` | Lorsqu'activé, produit une vidéo avec du son (incluant dialogues et effets sonores) (par défaut : False). Ce paramètre est révélé après avoir sélectionné un `model`. |
| `first_frame` | IMAGE | Oui | - | L'image de départ pour la séquence vidéo. |
| `end_frame` | IMAGE | Oui | - | L'image de fin pour la séquence vidéo. |
| `prompt` | STRING | Oui | - | Une description textuelle guidant la génération de la vidéo (maximum 2000 caractères). |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). |

**Note :** Les images `first_frame` et `end_frame` devraient avoir des ratios d'aspect similaires pour des résultats optimaux.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |
