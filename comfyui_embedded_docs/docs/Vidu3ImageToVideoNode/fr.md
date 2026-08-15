# Génération d’image en vidéo Vidu Q3

Le nœud Vidu Q3 Image-to-Video Generation crée une séquence vidéo à partir d’une image d’entrée. Il utilise un modèle Vidu Q3 pour animer l’image, éventuellement guidé par un prompt texte, et génère un fichier vidéo.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour la génération vidéo. | DYNAMIC_COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `image` | Une image à utiliser comme image de départ de la vidéo générée. | IMAGE | Oui | - |
| `invite` | Un prompt texte facultatif pour la génération vidéo (2000 caractères maximum) (par défaut : vide). | STRING | Non | - |
| `graine` | Une valeur de seed pour contrôler le caractère aléatoire de la génération (par défaut : 1). | INT | Non | 0 à 2147483647 |

### viduq3-pro Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `résolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"720p"`<br>`"1080p"`<br>`"2K"` |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 1 à 16 |
| `audio` | Lorsque activé, génère une vidéo avec le son (y compris les dialogues et les effets sonores) (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |

### viduq3-turbo Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `résolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `durée` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 1 à 16 |
| `audio` | Lorsque activé, génère une vidéo avec le son (y compris les dialogues et les effets sonores) (par défaut : False). | BOOLEAN | Oui | `True`<br>`False` |

**Remarque :** L’`image` doit avoir un rapport hauteur/largeur compris entre 1:4 et 4:1 (du format portrait au paysage). Le `prompt` est facultatif mais ne peut pas dépasser 2000 caractères. Les options de résolution dépendent du modèle sélectionné : `"viduq3-pro"` prend en charge `"720p"`, `"1080p"` et `"2K"` ; `"viduq3-turbo"` prend en charge `"720p"` et `"1080p"`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3ImageToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `77500d1e19928128decc010540670e311cd8ec4fcad913412517f47f0e27e15f`
