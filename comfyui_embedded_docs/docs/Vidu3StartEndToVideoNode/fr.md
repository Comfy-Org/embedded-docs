# Génération vidéo Vidu Q3 à partir d'une image de début/fin

Ce nœud génère une vidéo en interpolant entre une image de départ et une image de fin fournies, guidé par un prompt textuel. Il utilise le modèle Vidu Q3 pour créer une transition fluide entre les deux images, produisant une vidéo d'une durée et d'une résolution spécifiées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération de vidéo. La sélection d'une option révèle des paramètres de configuration supplémentaires pour `resolution`, `duration` et `audio`. | DYNAMIC_COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `first_frame` | Image de départ de la séquence vidéo. | IMAGE | Oui | - |
| `end_frame` | Image de fin de la séquence vidéo. | IMAGE | Oui | - |
| `prompt` | Description du prompt (2000 caractères maximum). | STRING | Oui | - |
| `seed` | Valeur de graine pour contrôler le caractère aléatoire de la génération (par défaut : 1). | INT | Oui | 0 à 2147483647 |

### Entrées viduq3-pro et viduq3-turbo

Les paramètres suivants sont communs aux deux options de modèle (`viduq3-pro` et `viduq3-turbo`). Ils apparaissent après la sélection d'un modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `resolution` | Résolution de la vidéo de sortie. Ce paramètre apparaît après avoir sélectionné un `model`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). Ce paramètre apparaît après avoir sélectionné un `model`. | INT | Oui | 1 à 16 |
| `audio` | Lorsque activé, produit une vidéo avec le son (y compris le dialogue et les effets sonores) (par défaut : False). Ce paramètre apparaît après avoir sélectionné un `model`. | BOOLEAN | Oui | `True`<br>`False` |

**Remarque :** Les images `first_frame` et `end_frame` doivent avoir des ratios d'aspect similaires. Le ratio d'aspect des deux images doit être compris entre 80 % et 125 % l'une de l'autre (une proximité relative entre 0,8 et 1,25).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
