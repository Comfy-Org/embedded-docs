Le nœud TorchCompileModel applique la compilation PyTorch à un modèle pour optimiser ses performances. Il crée une copie du modèle d'entrée et l'enveloppe avec la fonctionnalité de compilation de PyTorch en utilisant le backend spécifié. Cela peut améliorer la vitesse d'exécution du modèle lors de l'inférence.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `modèle` | Le modèle à compiler et optimiser | MODEL | Oui | - |
| `backend` | Le backend de compilation PyTorch à utiliser pour l'optimisation (par défaut : "inductor") | STRING | Oui | "inductor"<br>"cudagraphs" |

## Sorties

| Nom de sortie | Description | Type de données |
| --- | --- | --- |
| `modèle` | Le modèle compilé avec la compilation PyTorch appliquée | MODEL |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/fr.md)

---
**Source fingerprint (SHA-256):** `923e71b528e6e53468916f74c2a02924bf51738f29e36638312c6da6357fcedb`
