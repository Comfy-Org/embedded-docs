> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/fr.md)

Voici la traduction de la documentation du nœud Vidu Q3 Text-to-Video Generation :

Le nœud Vidu Q3 Text-to-Video Generation crée une vidéo à partir d'une description textuelle. Il utilise le modèle Vidu Q3 Pro ou Q3 Turbo pour générer un contenu vidéo basé sur votre invite, vous permettant de contrôler la durée, la résolution, le rapport hauteur/largeur de la vidéo et d'inclure ou non du son.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------------|--------|-------|-------------|
| `modèle` | COMBO | Oui | `"viduq3-pro"`<br>`"viduq3-turbo"` | Modèle à utiliser pour la génération vidéo. La sélection d'un modèle révèle des paramètres de configuration supplémentaires pour le rapport hauteur/largeur, la résolution, la durée et le son. |
| `model.aspect_ratio` | COMBO | Oui* | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` | Le rapport hauteur/largeur de la vidéo de sortie. Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. |
| `model.resolution` | COMBO | Oui* | `"720p"`<br>`"1080p"` | Résolution de la vidéo de sortie. Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. |
| `model.duration` | INT | Oui* | 1 à 16 | Durée de la vidéo de sortie en secondes (par défaut : 5). Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. |
| `model.audio` | BOOLEAN | Oui* | Vrai/Faux | Lorsqu'il est activé, produit une vidéo avec du son (incluant dialogues et effets sonores) (par défaut : Faux). Ce paramètre est révélé lorsqu'un `modèle` est sélectionné. |
| `invite` | STRING | Oui | N/A | Une description textuelle pour la génération vidéo, avec une longueur maximale de 2000 caractères. |
| `graine` | INT | Non | 0 à 2147483647 | Une valeur de graine pour contrôler l'aléatoire de la génération (par défaut : 1). |

*Remarque : Les paramètres `aspect_ratio`, `resolution`, `duration` et `audio` sont requis une fois qu'un `model` est sélectionné, car ils font partie de sa configuration.

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `video` | VIDEO | Le fichier vidéo généré. |

---
**Source fingerprint (SHA-256):** `a98b6c3093d659a5a4344c2c495063acf47a7922bf7d1fc851c3b8d8c0c87c5e`
