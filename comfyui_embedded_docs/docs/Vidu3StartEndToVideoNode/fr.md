Voici la traduction en français de la documentation du nœud ComfyUI, en respectant vos règles :

Ce nœud génère une vidéo par interpolation entre une image de début et une image de fin fournies, guidée par une invite textuelle. Il utilise le modèle Vidu Q3 pour créer une transition fluide entre les deux images, produisant une vidéo d'une durée et d'une résolution spécifiées.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à utiliser pour la génération vidéo. La sélection d'une option révèle des paramètres de configuration supplémentaires pour `resolution`, `duration` et `audio`. | COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.resolution` | Résolution de la vidéo de sortie. Ce paramètre est révélé après la sélection d'un `modèle`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `model.duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). Ce paramètre est révélé après la sélection d'un `modèle`. | INT | Oui | 1 à 16 |
| `model.audio` | Lorsqu'il est activé, produit une vidéo avec son (incluant dialogues et effets sonores) (par défaut : False). Ce paramètre est révélé après la sélection d'un `modèle`. | BOOLEAN | Oui | `True` / `False` |
| `image de début` | L'image de départ pour la séquence vidéo. | IMAGE | Oui | - |
| `image de fin` | L'image de fin pour la séquence vidéo. | IMAGE | Oui | - |
| `invite` | Une description textuelle guidant la génération vidéo (2000 caractères maximum). | STRING | Oui | - |
| `graine` | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). | INT | Non | 0 à 2147483647 |

**Remarque :** Les images `first_frame` et `end_frame` doivent avoir des rapports d'aspect similaires pour des résultats optimaux. Le rapport d'aspect des deux images doit être compris entre 80 % et 125 % l'un de l'autre (une proximité relative entre 0,8 et 1,25).

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `4a0a8d6657702d80278dc9239370683f408d7c051e91e8396939b7b81b87b4ed`
