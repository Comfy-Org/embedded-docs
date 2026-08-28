# ModelAttentionBackend

Ce nœud vous permet de choisir le backend d'attention qu'un modèle utilisera pour ses calculs d'attention. Il crée une copie du modèle et remplace la fonction d'attention par celle que vous sélectionnez, ce qui peut affecter les performances ou le comportement. Si le backend choisi n'est pas disponible, il revient automatiquement à l'attention PyTorch et enregistre un avertissement.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `modèle` | Le modèle auquel le backend d'attention sélectionné sera appliqué. | MODEL | Oui |  |
| `attention` | Le backend d'attention à utiliser (par défaut : « pytorch attention »). Si le backend sélectionné n'est pas disponible, l'attention PyTorch est utilisée comme solution de repli. | STRING | Oui | « pytorch attention »<br>« comfy kitchen attention » |

Remarque : L'option « comfy kitchen attention » n'est listée que lorsque le module d'attention int8 de comfy kitchen est disponible dans l'environnement actuel.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `MODEL` | Un clone du modèle d'entrée avec le backend d'attention sélectionné appliqué. | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/fr.md)

---
**Source fingerprint (SHA-256):** `4ba613cc0bf5b3e7f9effa895b98b3a3bd302e5d20e9d7e18d1633906c783244`
