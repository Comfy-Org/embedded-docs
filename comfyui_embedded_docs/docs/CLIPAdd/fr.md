> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/fr.md)

Le nœud CLIPAdd combine deux modèles CLIP en fusionnant leurs correctifs clés. Il crée une copie du premier modèle CLIP, puis ajoute la plupart des correctifs clés du second modèle, à l'exception des identifiants de position et des paramètres d'échelle logitique. Cela permet de mélanger les caractéristiques de différents modèles CLIP tout en préservant la structure du premier modèle.

## Entrées

| Paramètre | Type de données | Type d'entrée | Défaut | Plage | Description |
|-----------|-----------------|---------------|--------|-------|-------------|
| `clip1` | CLIP | Requis | - | - | Le modèle CLIP principal qui servira de base pour la fusion |
| `clip2` | CLIP | Requis | - | - | Le modèle CLIP secondaire qui fournit les correctifs supplémentaires à ajouter |

## Sorties

| Nom de sortie | Type de données | Description |
|---------------|-----------------|-------------|
| `CLIP` | CLIP | Renvoie un modèle CLIP fusionné combinant les caractéristiques des deux modèles d'entrée |

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
