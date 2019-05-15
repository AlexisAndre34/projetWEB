public abstract class Pokemon {
    private String name;
    private int poids;
    public Pokemon(String name, int poids);
    public void getName();

    public void setName(String name){
        this.name=name
    }

    public void getPoids();

    public void SetPoids(int poids){
        poids=poids
    }


    abstract vitesse();
    

}

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

public class PokemonCroisiere extends PokemonMer{
    public double vitesse(){
        return (poids/25*nbNagoires)/2;
    }
}