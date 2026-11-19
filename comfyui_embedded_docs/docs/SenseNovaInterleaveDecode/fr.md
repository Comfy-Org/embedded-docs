# SenseNova Interleave Decode

Transformez l'historique d'entrelacement laissé par SenseNova Conditioning en texte, images et raisonnement utilisables. Exécutez-le à la fin de la boucle, avec l'option accumulate de End Loop désactivée, pour collecter en une seule passe tout ce que le modèle a produit.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP SenseNova utilisé pour décoder les tokens générés. | CLIP | Oui | - |
| `conditioning` | Conditionnement d'entrelacement provenant de SenseNova Conditioning. | CONDITIONING | Oui | - |
| `samples` | Dernier latent pixel du KSampler, nécessaire lorsque la boucle s'est terminée sur une demande d'image. | LATENT | Non | - |

**Contraintes et comportement :**

* Le conditionnement doit provenir de SenseNova Conditioning dans la tâche `interleave` ou `self-correction` ; toute autre valeur déclenche une erreur.
* Lorsque le modèle attend une image, connectez la sortie LATENT de l'échantillonneur à `samples`.
* Les images de référence connectées au début de l'exécution sont exclues de la sortie, et les nœuds consommateurs d'images sont ignorés lorsqu'aucune image n'a été générée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `text` | Texte décodé à partir de l'historique d'entrelacement, avec les marqueurs d'image remplacés par des lignes vides. | STRING |
| `images` | Les images que le modèle a générées pendant l'exécution. | IMAGE |
| `thinking` | Texte de raisonnement du modèle, lorsqu'il en a produit un. | STRING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaInterleaveDecode/fr.md)

---
**Source fingerprint (SHA-256):** `62c7ded50c1348e2242319209729a17d543d80e4d01ddf173cf8b77e4fd0be50`
