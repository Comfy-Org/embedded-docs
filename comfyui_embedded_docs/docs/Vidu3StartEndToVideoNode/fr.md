> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/fr.md)

Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Ce nœud génère une vidéo par interpolation entre une image de début et une image de fin fournies, guidée par une invite textuelle. Il utilise le modèle Vidu Q3 pour créer une transition fluide entre les deux images, produisant une vidéo d'une durée et d'une résolution spécifiées.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `model` | COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` | Le modèle à utiliser pour la génération vidéo. La sélection d'une option révèle des paramètres de configuration supplémentaires pour `resolution`, `duration` et `audio`. |
| `model.resolution` | COMBO | Oui | `"720p"`<br>`"1080p"` | Résolution de la vidéo de sortie. Ce paramètre est révélé après la sélection d'un `model`. |
| `model.duration` | INT | Oui | 1 à 16 | Durée de la vidéo de sortie en secondes (par défaut : 5). Ce paramètre est révélé après la sélection d'un `model`. |
| `model.audio` | BOOLEAN | Oui | `True` / `False` | Lorsqu'il est activé, produit une vidéo avec son (incluant dialogues et effets sonores) (par défaut : False). Ce paramètre est révélé après la sélection d'un `model`. |
| `first_frame` | IMAGE | Oui | - | L'image de départ pour la séquence vidéo. |
| `end_frame` | IMAGE | Oui | - | L'image de fin pour la séquence vidéo. |
| `prompt` | STRING | Oui | - | Une description textuelle guidant la génération vidéo (2000 caractères maximum). |
| `seed` | INT | Non | 0 à 2147483647 | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). |

**Remarque :** Les images `first_frame` et `end_frame` doivent avoir des rapports d'aspect similaires pour des résultats optimaux. Le rapport d'aspect des deux images doit être compris entre 80 % et 125 % l'un de l'autre (une proximité relative entre 0,8 et 1,25).

## Sorties

| Nom de la sortie | Type de données | Description |
|------------------|-----------------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
