# Rodin 3D Générer - Génération Lisse

Voici la traduction en français de la documentation du nœud Rodin 3D Smooth, en respectant vos règles :

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/en.md)

Le nœud Rodin 3D Smooth génère des actifs 3D en utilisant l'API Rodin, en traitant des images d'entrée et en les convertissant en modèles 3D lisses. Il prend plusieurs images en entrée et produit un fichier de modèle 3D téléchargeable. Le nœud gère l'ensemble du processus de génération, y compris la création de tâches, la vérification périodique de l'état et le téléchargement automatique des fichiers.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
| --- | --- | --- | --- | --- |
| `Images` | Images d'entrée à utiliser pour la génération du modèle 3D. Plusieurs images peuvent être fournies. | IMAGE | Oui | - |
| `Graine` | Valeur de graine aléatoire pour la cohérence de la génération. | INT | Oui | - |
| `Type de matériau` | Type de matériau à appliquer au modèle 3D. | STRING | Oui | - |
| `Nombre de polygones` | Nombre de polygones cible pour le modèle 3D généré. Détermine la qualité du maillage et le niveau de détail. | STRING | Oui | - |

## Sorties

| Nom de la sortie | Description | Type de données |
| --- | --- | --- |
| `GLB` | Chemin d'accès au fichier du modèle 3D téléchargé (uniquement pour la rétrocompatibilité). | STRING |
| `GLB` | Le modèle 3D généré au format GLB. | FILE3DGLB |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Smooth/fr.md)

---
**Source fingerprint (SHA-256):** `18783d4a3010234a3640d20c73cdd78e35a0eef7090bd433dba0fcc58e35ad3f`
