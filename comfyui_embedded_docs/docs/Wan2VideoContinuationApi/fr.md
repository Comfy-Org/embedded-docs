# Wan 2.7 Continuation Vidéo

Le nœud Wan 2.7 Video Continuation génère un nouveau segment vidéo qui continue à partir de la fin d'un clip vidéo d'entrée. Il utilise le modèle Wan 2.7 pour synthétiser la continuation en fonction d'un prompt texte et peut éventuellement guider la fin vers une image cible spécifique.

## Entrées

### Entrées communes

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model` | Le modèle de génération vidéo à utiliser. | COMBO | Oui | `"wan2.7-i2v"` |
| `first_clip` | Vidéo d'entrée à partir de laquelle continuer. Durée : 2s-10s. Le rapport hauteur/largeur de sortie est dérivé de cette vidéo. | VIDEO | Oui | 2s à 10s |
| `last_frame` | Image de la dernière frame. La continuation effectuera une transition vers cette image. | IMAGE | Non | - |
| `seed` | Seed à utiliser pour la génération. (défaut : 0) | INT | Oui | 0 à 2147483647 |
| `prompt_extend` | Indique s'il faut améliorer le prompt avec l'assistance de l'IA. (défaut : True) | BOOLEAN | Oui | - |
| `watermark` | Indique s'il faut ajouter un filigrane généré par l'IA au résultat. (défaut : False) | BOOLEAN | Oui | - |

### Entrées wan2.7-i2v

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `model.prompt` | Prompt décrivant les éléments et les caractéristiques visuelles. Prend en charge l'anglais et le chinois. (défaut : chaîne vide) | STRING | Oui | - |
| `model.negative_prompt` | Prompt négatif décrivant ce qu'il faut éviter. (défaut : chaîne vide) | STRING | Oui | - |
| `model.resolution` | La résolution pour la vidéo de sortie. | COMBO | Oui | `"720P"`<br>`"1080P"` |
| `model.duration` | Durée totale de sortie en secondes. Le modèle génère une continuation pour remplir le temps restant après le clip d'entrée. (défaut : 5) | INT | Oui | 2 à 15 |

**Remarque :** La vidéo d'entrée `first_clip` doit avoir une durée comprise entre 2 et 10 secondes.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `output` | La continuation vidéo générée. | VIDEO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/fr.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`
