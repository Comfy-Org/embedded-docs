# Enregistrer le conditionnement

Ce nœud enregistre un seul conditionnement dans le dossier de sortie sous forme de fichier safetensors. Le fichier enregistré peut être déplacé vers le dossier models/embeddings puis chargé plus tard avec Load Conditioning, par exemple pour ignorer l’encodeur de texte. Le nœud transmet le conditionnement sans modification afin qu’il puisse encore être utilisé plus tard dans le workflow.

## Entrées

| Paramètre | Description | Type de données | Obligatoire | Plage |
|-----------|-------------|-----------------|-------------|-------|
| `conditioning` | Le conditionnement à enregistrer. Une seule entrée de conditionnement est prise en charge. | CONDITIONING | Oui | - |
| `filename_prefix` | Préfixe utilisé pour construire le nom du fichier de sortie. Le fichier est écrit dans le dossier de sortie avec un compteur numérique ajouté. Valeur par défaut : `conditioning/ComfyUI` | STRING | Oui | - |

**Remarques :**

- Si l’entrée `conditioning` contient plus d’une entrée (par exemple après avoir combiné des conditionnements), le nœud génère une erreur : « Save Conditioning ne prend en charge qu’une seule entrée de conditionnement ; enregistrez-la avant de combiner. »
- Les options de conditionnement qui sont des tenseurs, des listes/tuples de tenseurs, des booléens, des entiers, des nombres à virgule flottante ou des chaînes de caractères sont enregistrées avec le conditionnement. Les options qui sont `None` sont ignorées. Tout autre type d’option génère une erreur indiquant que l’option ne peut pas être enregistrée.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `conditioning` | Le même conditionnement que celui qui a été transmis, sans modification. | CONDITIONING |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/fr.md)

---
**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`
