Le nœud Pika Swaps remplace des objets ou des régions dans votre vidéo par une nouvelle image. Vous définissez les zones à remplacer à l'aide d'un masque, et le nœud effectue un échange transparent du contenu spécifié sur l'ensemble de la séquence vidéo.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `video` | La vidéo dans laquelle remplacer un objet. | VIDEO | Oui | - |
| `image` | L'image utilisée pour remplacer l'objet masqué dans la vidéo. | IMAGE | Oui | - |
| `mask` | Utilisez le masque pour définir les zones de la vidéo à remplacer. | MASK | Oui | - |
| `prompt_text` | Texte d'invite décrivant le remplacement souhaité. | STRING | Oui | - |
| `negative_prompt` | Texte d'invite décrivant ce qu'il faut éviter dans le remplacement. | STRING | Oui | - |
| `seed` | Valeur de graine aléatoire pour des résultats cohérents. | INT | Oui | 0 à 4294967295 |

**Remarque :** Ce nœud nécessite que tous les paramètres d'entrée soient fournis. Les paramètres `video`, `image` et `mask` fonctionnent ensemble pour définir l'opération de remplacement, où le masque spécifie les zones de la vidéo qui seront remplacées par l'image fournie.

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `output` | La vidéo traitée avec l'objet ou la région spécifié(e) remplacé(e). | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikaswaps/fr.md)

---
**Source fingerprint (SHA-256):** `007b7bc429fdada2fb8910392b056ae3a98d482cce9e280bdcd162ede497eb03`
