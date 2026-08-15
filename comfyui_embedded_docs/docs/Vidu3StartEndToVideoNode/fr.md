# Génération vidéo Vidu Q3 à partir d'une image de début/fin

Ce nœud génère une vidéo en interpolant entre une image de début et une image de fin fournies, guidé par un prompt texte. Il utilise le modèle Vidu Q3 pour créer une transition fluide entre les deux images, produisant une vidéo d’une durée et d’une résolution spécifiées.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle à utiliser pour la génération vidéo. La sélection d’une option révèle des paramètres de configuration supplémentaires pour `resolution`, `duration` et `audio`. | DYNAMIC_COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `image de début` | L’image de départ de la séquence vidéo. | IMAGE | Oui | - |
| `image de fin` | L’image de fin de la séquence vidéo. | IMAGE | Oui | - |
| `invite` | Description du prompt (2000 caractères maximum). | STRING | Oui | - |
| `graine` | Une valeur de graine pour contrôler le caractère aléatoire de la génération (par défaut : 1). | INT | Non | De 0 à 2147483647 |

### Entrées de viduq3-pro et viduq3-turbo

Les paramètres suivants sont partagés par les deux options de modèle (`viduq3-pro` et `viduq3-turbo`). Ils sont révélés après la sélection d’un modèle.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `résolution` | Résolution de la vidéo de sortie. Ce paramètre est révélé après la sélection d’un `model`. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5). Ce paramètre est révélé après la sélection d’un `model`. | INT | Oui | De 1 à 16 |
| `audio` | Lorsqu’il est activé, génère une vidéo avec du son (y compris dialogues et effets sonores) (par défaut : False). Ce paramètre est révélé après la sélection d’un `model`. | BOOLEAN | Oui | `True`<br>`False` |

**Remarque :** Les images `first_frame` et `end_frame` doivent avoir des ratios d’aspect similaires pour des résultats optimaux. Le ratio d’aspect des deux images doit être compris entre 80 % et 125 % l’un de l’autre (une proximité relative entre 0,8 et 1,25).

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`
