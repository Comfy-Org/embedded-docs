Voici la traduction de la documentation du nœud Vidu Q3 Text-to-Video Generation :

Le nœud Vidu Q3 Text-to-Video Generation crée une vidéo à partir d'une description textuelle. Il utilise le modèle Vidu Q3 Pro ou Q3 Turbo pour générer un contenu vidéo basé sur votre invite, vous permettant de contrôler la durée, la résolution, le rapport hauteur/largeur de la vidéo et d'inclure ou non du son.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Modèle à utiliser pour la génération vidéo. La sélection d'un modèle révèle des paramètres de configuration supplémentaires pour le rapport hauteur/largeur, la résolution, la durée et le son. | COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` |
| `model.aspect_ratio` | Le rapport hauteur/largeur de la vidéo de sortie. Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. | COMBO | Oui* | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `model.resolution` | Résolution de la vidéo de sortie. Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. | COMBO | Oui* | `"720p"`<br>`"1080p"` |
| `model.duration` | Durée de la vidéo de sortie en secondes (par défaut : 5). Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. | INT | Oui* | 1 à 16 |
| `model.audio` | Lorsqu'il est activé, produit une vidéo avec du son (incluant dialogues et effets sonores) (par défaut : Faux). Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. | BOOLEAN | Oui* | Vrai/Faux |
| `invite` | Une description textuelle pour la génération vidéo, avec une longueur maximale de 2000 caractères. | STRING | Oui | N/A |
| `graine` | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). | INT | Non | 0 à 2147483647 |

*Remarque : Les paramètres `aspect_ratio`, `resolution`, `duration` et `audio` sont requis une fois qu'un `model` est sélectionné, car ils font partie de sa configuration.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `video` | Le fichier vidéo généré. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `a98b6c3093d659a5a4344c2c495063acf47a7922bf7d1fc851c3b8d8c0c87c5e`
