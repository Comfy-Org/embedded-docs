# SenseNova Conditioning

Prépare le conditionnement SenseNova pour la génération d’images ou pour une sortie entrelacée de texte et d’images. Le sélecteur `task` définit le modèle de prompt et le comportement d’arrêt, et le nœud indique si le modèle souhaite une image, afin qu’une boucle sache quand exécuter l’échantillonneur.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `clip` | Modèle CLIP SenseNova. Connectez le chargeur CLIP qui alimente aussi CLIP Text Encode ; la sortie de l’encodeur va dans `conditioning`. Requis pour toutes les tâches, sauf lorsque le conditionnement entrant est déjà terminé. | CLIP | Non | - |
| `conditioning` | Conditionnement texte SenseNova provenant de CLIP Text Encode. | CONDITIONING | Oui | - |
| `negative` | Conditionnement négatif facultatif. Il est mis à jour et renvoyé pour les tâches `interleave` et `self-correction`. | CONDITIONING | Non | - |
| `task` | Tâche à exécuter. `"image"` encode le prompt pour un échantillonneur standard, `"image thinking"` permet au modèle de réfléchir avant de répondre, `"interleave"` produit du texte et des images en une seule passe, et `"self-correction"` permet au modèle de corriger sa propre sortie précédente. | DYNAMIC_COMBO | Oui | `"image"`<br>`"image thinking"`<br>`"interleave"`<br>`"self-correction"` |
| `max_tokens` | Nombre maximal de tokens générés pendant cet appel. Par défaut : 1024. | INT | Oui | 1 à 8192 |

### Entrées `interleave`

Ces entrées apparaissent lorsque `task` est défini sur `"interleave"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `thinking` | Permet au modèle de réfléchir avant de répondre. Par défaut : True. | BOOLEAN | Oui | True<br>False |
| `samples` | Sortie précédente de l’échantillonneur, connectée lors de la reprise après une demande d’image. | LATENT | Non | - |

### Entrées `self-correction`

Ces entrées apparaissent lorsque `task` est défini sur `"self-correction"`.

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `samples` | Sortie précédente de l’échantillonneur, connectée lors de la reprise après une demande d’image. | LATENT | Non | - |

**Contraintes et comportement :**

* L’entrée `clip` reçoit le modèle CLIP SenseNova lui-même, pas la sortie de CLIP Text Encode (qui est `CONDITIONING`). Le nœud renvoie une erreur si `clip` est absent ou n’est pas un CLIP SenseNova.
* `"image thinking"` nécessite exactement une entrée de conditionnement positive ; `"interleave"` et `"self-correction"` nécessitent une entrée positive et une entrée négative.
* Lorsque le modèle attend une image, connectez la sortie LATENT de l’échantillonneur précédent à `samples`. Passer des échantillons avant qu’une image ait été demandée constitue une erreur.
* Lorsque le conditionnement entrant est déjà terminé, le nœud le renvoie inchangé avec un `generated_text` vide et `image_requested` défini sur False.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | Conditionnement pour l’échantillonneur, étendu avec le texte généré par cet appel. | CONDITIONING |
| `generated_text` | Texte généré par cet appel. Utilisez SenseNova Interleave Decode pour le résultat complet. | STRING |
| `negative` | Conditionnement négatif mis à jour pour les tâches `interleave` et `self-correction`. | CONDITIONING |
| `image_requested` | True lorsque le modèle a demandé une image : exécutez l’échantillonneur, puis réinjectez la boucle dans ce nœud. | BOOLEAN |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SenseNovaConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `97fcdc26ccf80f48c5628f695a4ae8231b065b67414c93dec9bced6bb8d4c77c`
