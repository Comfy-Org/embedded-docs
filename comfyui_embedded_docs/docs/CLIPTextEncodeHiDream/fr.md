> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeHiDream/fr.md)

Le nœud CLIPTextEncodeHiDream traite plusieurs entrées de texte en utilisant différents modèles de langage et les combine en une seule sortie de conditionnement. Il tokenise le texte provenant de quatre sources différentes (CLIP-L, CLIP-G, T5-XXL et LLaMA) et les encode en utilisant une approche d'encodage planifié. Cela permet un conditionnement de texte plus sophistiqué en exploitant simultanément plusieurs modèles de langage.

## Entrées

| Paramètre | Type de données | Type d'entrée | Par défaut | Plage | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Entrée requise | - | - | Le modèle CLIP utilisé pour la tokenisation et l'encodage |
| `clip_l` | STRING | Texte multiligne | - | - | Entrée de texte pour le traitement par le modèle CLIP-L |
| `clip_g` | STRING | Texte multiligne | - | - | Entrée de texte pour le traitement par le modèle CLIP-G |
| `t5xxl` | STRING | Texte multiligne | - | - | Entrée de texte pour le traitement par le modèle T5-XXL |
| `llama` | STRING | Texte multiligne | - | - | Entrée de texte pour le traitement par le modèle LLaMA |

**Note :** Toutes les entrées de texte prennent en charge les invites dynamiques et la saisie de texte multiligne. Le nœud nécessite que les quatre paramètres de texte soient fournis pour un fonctionnement correct, car chacun contribue à la sortie de conditionnement finale via le processus d'encodage planifié.

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | La sortie de conditionnement combinée provenant de toutes les entrées de texte traitées |