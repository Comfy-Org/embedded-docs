# Sonilo Texte en Musique

Le nœud Sonilo Text to Music génère de la musique à partir d'une description textuelle en utilisant le modèle d'IA de Sonilo. Vous fournissez une invite décrivant la musique souhaitée, et le nœud envoie une requête au service Sonilo pour créer un fichier audio. Vous pouvez également spécifier la durée cible de la musique générée.

## Entrées

| Paramètre | Description | Type de données | Requis | Plage |
|-----------|-------------|-----------------|--------|-------|
| `prompt` | Invite textuelle décrivant la musique à générer. Doit contenir entre 1 et 1000 caractères. | STRING | Oui | 1 à 1000 caractères |
| `duration` | Durée cible en secondes. Maximum : 6 minutes. Défaut : 30. | INT | Non | 1 à 360 |
| `seed` | Graine pour la reproductibilité. Actuellement ignorée par le service Sonilo, mais conservée pour la cohérence du graphe. Défaut : 0. | INT | Non | 0 à 18446744073709551615 |

**Remarque :** L'entrée `seed` est fournie pour la cohérence du flux de travail, mais n'affecte actuellement pas la sortie du service Sonilo.

## Sorties

| Nom de sortie | Description | Type de données |
|---------------|-------------|-----------------|
| `audio` | La musique générée sous forme de fichier audio. | AUDIO |

> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/fr.md)

---
**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`
