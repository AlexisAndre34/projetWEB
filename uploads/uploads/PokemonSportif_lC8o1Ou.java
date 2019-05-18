public class PokemonSportif extends PokemonSol {
    private int fqCard;
    public Pokemon(int name, int poids, int taille, int nbPattes, int fqCard);

    public void getFqCard();

    public void setFqCard(int fqCard){
        fqCard=fqCard;
    }

    public String toString(){
        return "je suis le pokemon " + name + " mon poids est de " + poids + ",ma vitesse est de " + vitesse + "km/h j'ai " + nbPattes + " pattes, ma taille est de " + taille + "m ma fréquence cardiaque est de " + fqCard + "pulsations à la minute"
    }

}