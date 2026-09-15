# MiniMax H3 Première-Dernière-Image vers Vidéo

Ce nœud génère une vidéo à partir d'une image de première frame et, en option, d'une image de dernière frame en utilisant les modèles MiniMax H3. Le sélecteur `model` modifie les paramètres de génération et les contraintes applicables, et le rapport d'aspect de la vidéo générée suit celui des images fournies.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Modèle à utiliser pour la génération vidéo. La sélection d'un modèle révèle ses paramètres spécifiques ci-dessous. | DYNAMIC_COMBO | Oui | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Image de la première frame de la vidéo. La vidéo générée suit le rapport d'aspect de cette image. | IMAGE | Oui | - |
| `last_frame` | Image de dernière frame optionnelle pour la vidéo. Lorsqu'elle est fournie, la vidéo est générée depuis la première frame vers cette dernière frame. | IMAGE | Non | - |
| `seed` | Graine aléatoire. La même requête avec la même graine donne des résultats similaires, mais non garantis identiques. Inclut une option « control after generate ». Défaut : 42. | INT | Oui | 0 à 4294967295 |
| `watermark` | Indique s'il faut ajouter un filigrane AIGC à la vidéo. Il s'agit d'un paramètre avancé. Pris en charge uniquement par le modèle `MiniMax H3`. Défaut : False. | BOOLEAN | Oui | True<br>False |

### Entrées MiniMax H3

Ces paramètres sont affichés lorsque `MiniMax H3` est sélectionné dans le sélecteur `model`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. Doit contenir au moins un caractère non blanc. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. | COMBO | Oui | "768P"<br>"2K" |
| `duration` | Durée de la vidéo de sortie en secondes. Défaut : 5. | INT | Oui | 4 à 15 |

### Entrées MiniMax H3 Max et MiniMax H3 Max Turbo

Ces paramètres sont partagés par `MiniMax H3 Max` et `MiniMax H3 Max Turbo`. La sélection de l'un ou l'autre de ces modèles révèle les mêmes paramètres.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Prompt textuel pour la génération vidéo. Ne doit pas être vide ou composé uniquement d'espaces, et est limité à 50 000 caractères. | STRING | Oui | Texte multiligne |
| `resolution` | Résolution de la vidéo de sortie. Défaut : 768P. | COMBO | Oui | "480P"<br>"768P" |
| `duration` | Durée de la vidéo de sortie en secondes. Défaut : 5. | INT | Oui | 5 à 15 |
| `prompt_expansion_mode` | Niveau d'effort consacré à la réécriture du prompt avant la génération. Défaut : balanced. | COMBO | Oui | "balanced"<br>"quality" |

**Notes sur les contraintes :**

- Le prompt doit contenir du texte : les prompts vides ou composés uniquement d'espaces sont rejetés.
- Toute image de frame fournie doit mesurer au moins 256 pixels de large et 256 pixels de haut, avec un rapport d'aspect largeur-hauteur compris entre 0,4 et 2,5 (environ 2:5 à 5:2). Cette exigence s'applique à `first_frame` et, lorsqu'elle est fournie, à `last_frame`.
- Lorsque `last_frame` est omis, la vidéo est générée à partir de la première frame uniquement.
- La vidéo de sortie suit le rapport d'aspect des images fournies.
- `watermark` n'est pris en charge que par `MiniMax H3`. L'activer avec `MiniMax H3 Max` ou `MiniMax H3 Max Turbo` déclenche une erreur.
- La durée varie de 4 à 15 secondes pour `MiniMax H3` et de 5 à 15 secondes pour `MiniMax H3 Max` et `MiniMax H3 Max Turbo`.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `video` | La vidéo générée, créée à partir de la première frame et de la dernière frame optionnelle en utilisant le modèle MiniMax H3 sélectionné. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/fr.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
