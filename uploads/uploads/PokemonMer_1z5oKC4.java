public class PokemonMer extends Pokemon {
    private int nbNagoires;
    public Pokemon(int name, int poids, int nbNagoires);

    public void getNbNagoires();

    public void setNbNagoires(int nbNagoires){
        nbNagoires=nbNagoires
    }

    public double vitesse(){
        return poids/25*nbNagoires;
    }
    public String toString(){
        return "je suis le pokemon " + name + " mon poids est de " + poids + ",ma vitesse est de " + vitesse + "km/h j'ai " + nbNagoires + " nagoires"
    }


}