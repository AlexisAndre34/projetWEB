public class PokemonCasaniers extends PokemonSol{
    private int nbHeuresTele;
    public Pokemon(int name, int poids, int taille, int nbPattes, int nbHeuresTele);

    public void getNbHeuresTele();

    public void setNbHeuresTele(int nbHeuresTele){
        nbHeuresTele=nbHeuresTele;
    }
    public String toString(){
        return "je suis le pokemon " + name + " mon poids est de " + poids + ",ma vitesse est de " + vitesse + "km/h j'ai " + nbPattes + " pattes, ma taille est de " + taille + "m  je regarde la télé " + nbHeuresTele + "h par jour"
    }

}