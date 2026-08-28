# MiniMax H3 Texte vers Vidéo

Ce nœud génère une vidéo à partir d’une invite texte en utilisant le modèle MiniMax H3. Il envoie le texte ainsi que les paramètres vidéo tels que la résolution, le ratio et la durée à l’API MiniMax, attend la fin de la tâche de génération, puis retourne la vidéo résultante.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Modèle à utiliser pour la génération vidéo. (par défaut : « MiniMax H3 »). La sélection de ce modèle fournit également les options d’invite texte, de résolution, de ratio et de durée pour la vidéo générée (voir Entrées MiniMax H3 ci-dessous). | DYNAMIC_COMBO | Oui | `"MiniMax H3"` |
| `graine` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais pas nécessairement identiques. (par défaut : 42) | INT | Oui | 0 à 4294967295 |
| `filigrane` | Indique s’il faut ajouter un filigrane AIGC à la vidéo. (par défaut : false) | BOOLEAN | Non | true<br>false |

### Entrées MiniMax H3

Ces paramètres apparaissent lorsque le modèle « MiniMax H3 » est sélectionné.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite texte pour la génération vidéo. | STRING | Oui | Tout texte |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | « 768P »<br>« 2K » |
| `ratio` | Ratio de la vidéo de sortie. (par défaut : « 16:9 ») | COMBO | Oui | « 16:9 »<br>« 4:3 »<br>« 1:1 »<br>« 3:4 »<br>« 9:16 »<br>« 21:9 » |
| `duration` | Durée de la vidéo de sortie en secondes (4-15). (par défaut : 5) | INT | Oui | 4 à 15 |

Remarque : L’invite texte incluse dans l’option `model` doit contenir au moins un caractère non blanc. Le prix estimé affiché pour ce nœud est calculé à partir de la résolution sélectionnée et de la durée de la vidéo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `VIDEO` | La vidéo générée à partir de l’invite texte fournie. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `93f7c81ba4053da999d29392bce23f7fd809d21876ea489747d203201ed0377f`
