# Génération de vidéo à partir de texte Vidu Q3

Le nœud Vidu Q3 Text-to-Video Generation crée une vidéo à partir d'une description textuelle. Il utilise le modèle Vidu Q3 Pro ou Q3 Turbo pour générer du contenu vidéo en fonction de votre prompt, vous permettant de contrôler la durée, la résolution, le format d'image et la présence d'audio dans la vidéo.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `model` | Modèle à utiliser pour la génération vidéo. La sélection d'un modèle révèle des paramètres de configuration supplémentaires pour le format d'image, la résolution, la durée et l'audio. | DYNAMIC_COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `prompt` | Description textuelle pour la génération vidéo, avec une longueur maximale de 2000 caractères. | STRING | Oui | N/A |
| `seed` | Valeur de graine (seed) pour contrôler le caractère aléatoire de la génération (par défaut : 1). | INT | Oui | 0 à 2147483647 |

### Entrées de viduq3-pro et viduq3-turbo

Les paramètres de configuration suivants sont partagés par les modèles `viduq3-pro` et `viduq3-turbo`.

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Le ratio d'aspect de la vidéo de sortie. | COMBO | Oui | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | `"720p"`<br>`"1080p"` |
| `duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). | INT | Oui | 1 à 16 |
| `audio` | Lorsqu'il est activé, génère une vidéo avec du son (incluant dialogues et effets sonores) (par défaut : False). | BOOLEAN | Oui | True/False |

**Remarque :** Les paramètres `aspect_ratio`, `resolution`, `duration` et `audio` sont requis une fois qu'un `model` est sélectionné, car ils font partie de sa configuration. Le `prompt` ne doit pas être vide et ne peut pas dépasser 2000 caractères.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`
