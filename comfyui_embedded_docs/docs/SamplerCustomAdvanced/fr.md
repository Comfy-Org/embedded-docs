> Cette documentation a été générée par IA. Si vous trouvez des erreurs ou avez des suggestions d'amélioration, n'hésitez pas à contribuer ! [Modifier sur GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustomAdvanced/fr.md)

Le nœud SamplerCustomAdvanced effectue un échantillonnage avancé de l'espace latent en utilisant du bruit personnalisé, des configurations de guidage et d'échantillonnage. Il traite une image latente à travers un processus d'échantillonnage guidé avec une génération de bruit personnalisable et des plannings de sigma, produisant à la fois la sortie échantillonnée finale et une version débruitée lorsqu'elle est disponible.

## Entrées

| Paramètre | Type de données | Requis | Plage | Description |
|-----------|-----------|----------|-------|-------------|
| `bruit` | NOISE | Oui | - | Le générateur de bruit qui fournit le motif de bruit initial et la graine pour le processus d'échantillonnage |
| `guide` | GUIDER | Oui | - | Le modèle de guidage qui dirige le processus d'échantillonnage vers les sorties souhaitées |
| `échantillonneur` | SAMPLER | Oui | - | L'algorithme d'échantillonnage qui définit comment l'espace latent est parcouru pendant la génération |
| `sigmas` | SIGMAS | Oui | - | Le planning des sigma qui contrôle les niveaux de bruit tout au long des étapes d'échantillonnage |
| `image_latente` | LATENT | Oui | - | La représentation latente initiale qui sert de point de départ pour l'échantillonnage |

## Sorties

| Nom de sortie | Type de données | Description |
|-------------|-----------|-------------|
| `sortie_débruitée` | LATENT | La représentation latente échantillonnée finale après avoir terminé le processus d'échantillonnage |
| `denoised_output` | LATENT | Une version débruitée de la sortie lorsqu'elle est disponible, sinon retourne la même valeur que la sortie |
