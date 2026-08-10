# MinimaxHailuo03TextToVideoNode

Ce nœud génère une vidéo à partir d'un prompt texte en utilisant le modèle MiniMax H3. Il envoie le texte ainsi que les paramètres vidéo tels que la résolution, la durée et le format d'image à l'API MiniMax, puis renvoie la vidéo résultante comme sortie.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------|----------|-------|
| `model` | Modèle à utiliser pour la génération vidéo. (défaut : "MiniMax H3"). Cette sélection inclut également le prompt texte, la résolution, la durée et le format d'image pour la vidéo générée. | COMBO | Oui | `"MiniMax H3"` |
| `seed` | Graine aléatoire. Une même requête avec la même graine donne des résultats similaires, mais pas garantis identiques. (défaut : 42) | INT | Oui | 0 à 4294967295 |
| `watermark` | Indique si un filigrane AIGC doit être ajouté à la vidéo. (défaut : false) | BOOLEAN | Non | true<br>false |

Remarque : Le prompt texte inclus dans l'option `model` doit contenir au moins un caractère non blanc. Le prix estimé affiché pour ce nœud est calculé à partir de la durée vidéo sélectionnée.

## Sorties

| Nom de sortie | Description | Type de données |
|-------------|-------------|-----------|
| `VIDEO` | La vidéo générée à partir du prompt texte fourni. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/fr.md)

---
**Source fingerprint (SHA-256):** `9478576dd02ed407a39c95c7227eb8e1482db8b77adc814691fbd807e4cc2893`
