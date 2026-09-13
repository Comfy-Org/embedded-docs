# MiniMax H3 Texte vers Vidéo

Ce nœud génère une vidéo à partir d'une invite textuelle en utilisant la famille de modèles MiniMax H3 : MiniMax H3, MiniMax H3 Max et MiniMax H3 Max Turbo. Vous sélectionnez le modèle, saisissez une invite textuelle et ajustez des paramètres tels que la résolution, le rapport d'aspect et la durée. Le nœud envoie la requête à l'API MiniMax, attend la fin de la tâche de génération et renvoie la vidéo résultante.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération de vidéo (par défaut : « MiniMax H3 »). La sélection d'un modèle affiche également les paramètres spécifiques au modèle décrits dans les sections ci-dessous. | DYNAMIC_COMBO | Oui | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques (par défaut : 42). | INT | Oui | 0 à 4294967295 |
| `watermark` | Indique s'il faut ajouter un filigrane AIGC à la vidéo (par défaut : false). Lorsqu'il est activé, seul le modèle « MiniMax H3 » est pris en charge. | BOOLEAN | Non | true<br>false |

### Entrées MiniMax H3

Ces paramètres apparaissent lorsque le modèle « MiniMax H3 » est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de vidéo. Doit contenir au moins un caractère non blanc. | STRING | Oui | Texte quelconque |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "768P"<br>"2K" |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : « 16:9 »). | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durée de la vidéo de sortie en secondes (4-15) (par défaut : 5). | INT | Oui | 4 à 15 |

### Entrées MiniMax H3 Max et MiniMax H3 Max Turbo

Ces paramètres sont partagés par les modèles « MiniMax H3 Max » et « MiniMax H3 Max Turbo » et apparaissent lorsque l'un de ces modèles est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle pour la génération de vidéo. Doit contenir au moins un caractère non blanc et peut comporter jusqu'à 50 000 caractères. | STRING | Oui | Jusqu'à 50 000 caractères |
| `resolution` | Résolution de la vidéo de sortie (par défaut : « 768P »). | COMBO | Oui | "480P"<br>"768P" |
| `ratio` | Rapport d'aspect de la vidéo de sortie (par défaut : « 16:9 »). | COMBO | Oui | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durée de la vidéo de sortie en secondes (5-15) (par défaut : 5). | INT | Oui | 5 à 15 |
| `prompt_expansion_mode` | Niveau d'effort consacré à la réécriture de l'invite avant la génération (par défaut : « balanced »). | COMBO | Oui | "balanced"<br>"quality" |

### Remarques

- Pour tous les modèles, l'invite doit contenir au moins un caractère non blanc.
- Le paramètre `watermark` n'est pris en charge que par « MiniMax H3 ». L'activer avec « MiniMax H3 Max » ou « MiniMax H3 Max Turbo » provoque une erreur.
- Les modèles « MiniMax H3 Max » et « MiniMax H3 Max Turbo » limitent l'invite à 50 000 caractères.
- Les limites de résolution et de durée dépendent du modèle sélectionné : « MiniMax H3 » prend en charge les résolutions « 768P » et « 2K » ainsi que les vidéos de 4 à 15 secondes, tandis que « MiniMax H3 Max » et « MiniMax H3 Max Turbo » prennent en charge les résolutions « 480P » et « 768P » ainsi que les vidéos de 5 à 15 secondes.
- Le prix estimé affiché pour ce nœud est calculé à partir du modèle, de la résolution et de la durée sélectionnés.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée à partir de l'invite textuelle fournie. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
