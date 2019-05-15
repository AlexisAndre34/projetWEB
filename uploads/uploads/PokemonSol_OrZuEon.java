public abstract class PokemonSol extends Pokemon {
    private double taille;
    private int nbPattes;
    public Pokemon(int name, int poids, int taille, int nbPattes);

    public void getTaille();

    public void setTaille(double taille){
        taille=taille;
    }

    public void getNbPattes();

    public void setNbPattes(int nbPattes){
        nbPattes=nbPattes;
    }

    abstract String toString();

    public double vitesse(){
        return nbPattes*taille*3;
    }
}